# Architecture — Job Posting Crawler

> **Status**: Draft for Gate 3 review (Product Owner)
> **Depends on**: `docs/VISION.md`
> **Date**: 2026-07-31

---

## Decisions taken (and what they cost)

| Decision | Choice | Why | What it costs |
|----------|--------|-----|---------------|
| **Runtime** | GitHub Actions scheduled workflow | Free, no server, lives with the code, secrets already managed | Cron can drift 5-15 min under load; secrets live in GitHub |
| **Language** | TypeScript (strict, Node 22) | CLAUDE.md standards are TS-specific (zero-`any` policy, typed error taxonomy) | None material |
| **State** | `data/seen.json`, committed back by the workflow | No database to run; git history doubles as a free audit log | Repo grows slowly; concurrent runs would conflict (mitigated below) |
| **Matching** | Deterministic rules → Claude on survivors | ~90% of volume rejected at zero token cost | Rules can reject an oddly-titled good role — mitigated by keeping rules loose |
| **Model** | `claude-haiku-4-5`, `claude-sonnet-5` via config | See "Model choice" below | Haiku is less nuanced on ambiguous seniority |
| **Delivery** | Email via Resend HTTP API | No SMTP session handling; free tier covers a daily send | Third-party dependency; swappable behind one interface |

---

## Model choice — a deliberate deviation, flagged

The Claude API guidance default is Opus 5. **I am recommending `claude-haiku-4-5` instead**, and want that visible rather than buried:

- The project's own `CLAUDE.md` mandates model tiering under Monetization: *"Use Haiku for simple tasks (classification, formatting), Sonnet for conversations, Opus only when depth is critical."* Scoring a job posting against a fixed profile and emitting a score plus one sentence is classification with a short rationale.
- Cost at realistic volume, ~5 LLM-scored survivors/day at ~1.2K input / 200 output tokens each:

| Model | Input $/MTok | Output $/MTok | ≈ Cost/day | ≈ Cost/month |
|-------|-------------:|--------------:|-----------:|-------------:|
| `claude-haiku-4-5` | $1 | $5 | $0.011 | **$0.33** |
| `claude-sonnet-5` | $3 (intro $2) | $15 (intro $10) | $0.033 | $0.99 |

Both are far inside the "few cents a day" the PO approved. The real argument for Haiku is not cost, it's that this task doesn't need more.

**The model is a config value, not a hardcoded constant.** If the digest shows poor seniority judgement in week 1, flip `MATCH_MODEL` to `claude-sonnet-5` — one env var, no code change. I'd rather ship Haiku and upgrade on evidence than pay for depth we haven't shown we need.

Requests use adaptive thinking with `effort: "low"` (a scoped classification task), structured outputs to guarantee a parseable score, and prompt caching on the profile block — the profile is identical across every scoring call in a run, so it caches after the first.

---

## System shape

```
GitHub Actions cron (weekdays, ~07:00 PO-local)
   │
   ▼
┌──────────────────────────────────────────────────────────┐
│ 1. LOAD CONFIG                                           │
│    companies.yaml  ·  profile.yaml  ·  data/seen.json    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 2. FETCH  (parallel, bounded concurrency, per-adapter)    │
│    greenhouse │ lever │ ashby │ …  │ html (fallback)      │
│    Each adapter: source-specific JSON → Posting[]         │
│    One adapter failing never fails the run                │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 3. DIFF                                                   │
│    Drop every posting whose stable ID is already in seen  │
│    → only genuinely new postings continue                 │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 4. RULE FILTER   (free, deterministic, ~90% rejected)     │
│    title include/exclude · seniority · location/remote    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 5. LLM SCORE   (Claude, only on survivors)                │
│    profile + posting → { score 0-100, reason, flags }     │
│    Structured output · prompt-cached profile · bounded    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 6. DIGEST                                                 │
│    score ≥ threshold → render email → send                │
│    nothing above threshold → send nothing                 │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 7. PERSIST                                                │
│    Record every posting seen this run (matched or not)    │
│    Commit data/seen.json back to the branch               │
└──────────────────────────────────────────────────────────┘
```

**The ordering is the whole design.** Diff before filter, filter before LLM. Every stage is cheaper than the one after it, so the expensive stage sees the smallest possible input. Reversing any two of these multiplies cost without improving results.

---

## Data model

```typescript
/** A job posting as normalized from any source. */
interface Posting {
  readonly id: string;          // `${companyId}:${sourceId}` — stable, the dedup key
  readonly companyId: string;
  readonly companyName: string;
  readonly title: string;
  readonly location: string | null;
  readonly url: string;
  readonly description: string | null;  // truncated to MAX_DESCRIPTION_CHARS
  readonly postedAt: string | null;     // ISO 8601; absent on some sources
  readonly source: AdapterKind;
  readonly firstSeenAt: string;         // ISO 8601, set by us — always present
}

/** Result of scoring one posting against the profile. */
interface MatchResult {
  readonly score: number;               // 0-100
  readonly reason: string;              // one sentence, shown in the email
  readonly matched: readonly string[];  // profile criteria this posting hits
  readonly concerns: readonly string[]; // caveats worth surfacing
}

type ScoredPosting = Posting & { readonly match: MatchResult };
```

**On `postedAt`**: Greenhouse gives `updated_at`, Lever gives a millisecond `createdAt`, Ashby varies, and HTML scraping usually gives nothing. It is therefore **display-only and nullable** — never load-bearing. Recency is determined by `firstSeenAt`, which we control and which is always present. Trusting a source's timestamp for dedup would be the easiest way to silently miss roles.

### Adapter contract

```typescript
interface CompanyAdapter {
  readonly kind: AdapterKind;
  /** Returns every currently-open posting. Throws AdapterError on failure. */
  fetchPostings(company: CompanyConfig): Promise<readonly Posting[]>;
}
```

One interface, one implementation per ATS. Adding a company is a YAML entry; adding an ATS is one file implementing this interface. Nothing else in the system changes.

### Config, in the PO's hands

```yaml
# config/companies.yaml
companies:
  - id: acme
    name: Acme Corp
    adapter: greenhouse
    slug: acme                  # the ATS board token
  - id: globex
    name: Globex
    adapter: lever
    slug: globex
```

```yaml
# config/profile.yaml  — the PO owns this file; digest quality lives or dies here
titles:
  include: ["engineering manager", "staff engineer", "principal engineer"]
  exclude: ["intern", "junior", "sales", "recruiter"]
seniority: { min: senior, max: director }
locations:
  remote: true
  cities: ["Brussels", "Antwerp"]
  countries: ["BE", "NL"]
keywords:
  strong: ["platform", "developer experience", "distributed systems"]
  dealbreakers: ["on-call 24/7", "relocation required"]
threshold: 65                   # only postings scoring ≥ this reach the inbox
```

The profile is plain YAML on purpose. The PO will tune this repeatedly in week 1, and that must not require touching code.

---

## Failure modes and how each is handled

| Failure | Handling | Rationale |
|---------|----------|-----------|
| One company's site is down | Caught per-adapter, logged, run continues | 30 companies must not be held hostage by one |
| ATS changes its response shape | Zod-validated at the adapter boundary; that company is skipped with a loud log line | Fail visibly on one company rather than corrupting the digest |
| Claude API down / rate-limited | Typed retry with exponential backoff; on exhaustion the posting is surfaced **unscored and flagged** | Better a slightly noisy digest than a silently dropped role |
| Anthropic spend runs away | Hard cap on LLM calls per run; excess deferred to tomorrow | Bounded cost is non-negotiable |
| `seen.json` lost or corrupted | Next run treats everything as new → one large digest, then normal | Degrades to noisy, never to silent |
| Two runs overlap | `concurrency` group in the workflow cancels the older run | Prevents a commit race on `seen.json` |
| `seen.json` grows unbounded | Entries pruned after `SEEN_RETENTION_DAYS` (default 180) | CLAUDE.md: memory must be bounded |
| Email send fails | Retried; on final failure the workflow **fails loudly** | A silent notifier is worse than no notifier |

**The unifying rule: every failure mode degrades toward noise, never toward silence.** A missed role is invisible and therefore unfixable; an extra role in the digest costs three seconds. Given that asymmetry, every ambiguous case resolves toward surfacing.

---

## Security

Scoped honestly to what a personal, single-user, no-inbound-surface tool actually needs — not a ceremonial OWASP pass.

| Concern | Handling |
|---------|----------|
| **Secrets** | `ANTHROPIC_API_KEY`, `RESEND_API_KEY`, `DIGEST_TO_EMAIL` as GitHub Actions secrets. Never logged, never in error text, never committed. `.env.example` documents names only. |
| **Prompt injection** | Job descriptions are attacker-influenceable text (anyone can post a job). Descriptions are truncated, wrapped in explicit delimiters, and the scorer uses structured outputs — so a malicious description can at worst produce a wrong score, never new instructions or tool calls. The scorer has no tools and no side effects. |
| **Output safety** | The digest is HTML email. All posting-derived text is HTML-escaped; URLs are validated `https://` before becoming an `href`. |
| **Network** | HTTPS enforced; per-request timeout via `AbortSignal`; bounded concurrency so we're a polite client. |
| **Dependency surface** | Deliberately tiny: `zod`, `@anthropic-ai/sdk`, `yaml`. Exact pinned versions. `npm audit` in CI. |
| **Data at rest** | `seen.json` holds public job postings only — no personal data. `profile.yaml` holds PO preferences and is the one file worth thinking about before making the repo public. |

---

## Files to be created

```
.github/workflows/crawl.yml       Scheduled workflow + commit-back + concurrency guard
.github/workflows/ci.yml          lint · typecheck · test · audit
config/companies.yaml             Target companies (PO-owned)
config/profile.yaml               Match criteria (PO-owned)
data/seen.json                    Dedup state (machine-owned, committed)
src/types.ts                      Posting, MatchResult, config types + Zod schemas
src/config.ts                     Load + validate YAML, fail fast on bad config
src/adapters/index.ts             Adapter registry
src/adapters/greenhouse.ts        Greenhouse board API
src/adapters/lever.ts             Lever postings API
src/adapters/ashby.ts             Ashby posting API
src/adapters/html.ts              Generic CSS-selector fallback
src/crawler.ts                    Orchestrates fetch across companies
src/dedupe.ts                     seen.json read/write, diff, retention pruning
src/matcher/rules.ts              Deterministic pre-filter
src/matcher/llm.ts                Claude scoring, caching, retry, spend cap
src/digest/render.ts              HTML + plaintext email rendering
src/digest/send.ts                Resend transport behind a Notifier interface
src/errors.ts                     Typed error taxonomy
src/logger.ts                     Structured logging, secret redaction
src/index.ts                      Entry point
```

Every file under 200 lines per CLAUDE.md. Tests co-located as `*.test.ts`.

---

## Implementation order

Sequenced so the riskiest assumption dies first and something useful exists early.

1. **Connectivity spike** — hit Greenhouse, Lever, Ashby live; confirm field names against real responses. *This is the only task that can invalidate the design; it goes first.*
2. Project scaffolding — package.json, tsconfig (strict), ESLint, Prettier, Vitest, CI workflow.
3. Types + Zod schemas + config loading.
4. Greenhouse adapter + tests (the most common ATS — proves the interface).
5. Dedup store with retention pruning + tests.
6. Rule filter + tests.
7. **First runnable milestone: crawl → diff → filter → console output.** No LLM, no email. Verifiable end to end.
8. LLM scorer with structured outputs, caching, retry, spend cap + tests.
9. Digest rendering (HTML + plaintext) + escaping tests.
10. Resend transport + a `--dry-run` flag that prints instead of sending.
11. Lever + Ashby adapters.
12. HTML fallback adapter.
13. Scheduled workflow with commit-back and concurrency guard.
14. Setup helper — resolve a company name to its ATS + slug, so adding companies isn't manual archaeology.

Steps 1-7 are the spine. If the timebox runs out mid-list, everything through 7 still has standalone value and the remainder is a clean continuation.

---

## What I'd flag before you approve

1. **The connectivity spike is a real gate, not a formality.** I verified endpoint shapes from vendor docs because this sandbox can't reach those hosts. High confidence, not certainty.
2. **Digest quality is bounded by `profile.yaml`, not by this architecture.** The most likely week-1 outcome is a mediocre digest caused by a thin profile, and the fix is tuning that file. Budget time for two or three tuning passes.
3. **Company coverage is uneven by construction.** ATS-backed companies will work reliably. Companies with bespoke career pages need the HTML fallback and will break when they redesign. Worth knowing which of your targets fall in the tail — the setup helper in step 14 will tell us.
4. **GitHub Actions cron drifts.** "07:00" means "usually between 07:00 and 07:15". Fine for a morning digest; flagging it so it isn't a surprise.
