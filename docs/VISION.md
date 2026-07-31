# Product Vision — Job Posting Crawler

> **Status**: Draft for Gate 1/2 review (Product Owner)
> **Pipeline mode**: BUILD · **Task level**: L4-ORCHESTRATED
> **Date**: 2026-07-31

---

## Problem Brief

```
WHO has this problem?
  Senior professionals running a targeted job search — people who know the
  ~20-40 specific companies they'd actually join, rather than browsing a
  general job board.

WHAT is the problem?
  Companies post roles on their own career sites hours-to-weeks before those
  roles reach LinkedIn, and a meaningful share never reach LinkedIn at all.
  Openings get missed entirely, or are seen after the strong applicants are
  already in the pipeline.

HOW do they cope today?
  Manually checking 20-40 career pages — which realistically means checking
  three of them, sporadically, and only when actively frustrated with the
  search. LinkedIn/Indeed alerts cover the subset that gets syndicated, with
  heavy noise from recruiters and irrelevant titles.

WHY does this matter?
  Application timing is one of the few levers a candidate actually controls.
  Being in the first cohort of applicants materially changes the odds. The
  cost of the status quo is missed opportunities that were never even seen —
  an invisible failure, which is why it goes unaddressed.

HAVE YOU TALKED TO REAL PEOPLE?
  [ ] Yes — spoke to [N] potential users
  [x] No — this is the Product Owner's own stated problem (n=1, the PO).
      Treated as validated for a personal-use tool; NOT validated as a
      multi-user product. See "Scope boundary" below.
```

**Scope boundary**: This is scoped as a **personal tool for the Product Owner**, not a product for other users. That materially changes what we build — no auth, no multi-tenancy, no billing, no privacy policy, no App Store. If the PO later wants this to serve other people, that is a different product and needs real user validation first (Problem Validation Scorecard + User Testing stages 2-3).

---

## Problem Validation Scorecard

Scored for the personal-tool scope. **The Product Owner should re-score this themselves** — per CLAUDE.md, market intuition beats pattern matching, and self-scoring by the system is the weakest form of validation.

| Criterion | Assessment | Score |
|-----------|-----------|:-----:|
| **Pain** | Missed openings are invisible, so pain is real but under-felt day to day | 6 |
| **Frequency** | Daily during an active search; near-zero when not searching | 7 |
| **Alternatives** | LinkedIn alerts exist but miss non-syndicated roles and are noisy; manual checking doesn't survive contact with a busy week | 8 |
| **Willingness to pay** | N/A for personal use — the relevant cost is build time, not money | — |
| **Feasibility** | High. Most companies use one of ~8 ATS platforms with public JSON endpoints | 9 |
| **Market size** | N/A at personal scope | — |
| **Average (scored criteria)** | | **7.5** |

**Verdict: Green light** for the personal-tool scope. The feasibility score is the important one — this problem is unusually tractable because the ATS ecosystem is concentrated.

---

## MVP Brief

```
MVP BRIEF: Morning Job Digest
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET USER:
  The Product Owner, running a targeted search across a self-curated list of
  companies.

PROBLEM:
  New roles at target companies appear on career sites before (or instead of)
  LinkedIn, and get missed.

CORE VALUE:
  One email each morning listing genuinely relevant new openings posted at my
  target companies since yesterday — with enough context to decide "apply or
  ignore" without opening the link.

  That is the ONE thing. Not a dashboard. Not application tracking. Not a CRM.

SUCCESS METRIC:
  At least one opening surfaced in the first 30 days that I would not
  otherwise have seen and that I actually apply to.

  Supporting: false-positive rate under ~30% (i.e. at least 7 of 10 surfaced
  roles are ones I agree are worth a look). Measured by the PO marking a
  handful of digests.

OUT OF SCOPE (v1):
  - Web dashboard / UI of any kind (email is the entire interface)
  - Application tracking, status, or reminders
  - Auto-apply, cover letters, résumé tailoring
  - Multi-user, accounts, auth, billing
  - Companies that require login, CAPTCHA, or JS execution to view jobs
  - Salary inference, company research, Glassdoor-style enrichment
  - Mobile app, push notifications, Slack
  - Historical analytics / trend charts

SHIP DATE:
  Timeboxed to one working session for the crawl+match+email core.
  Whatever isn't ready at that point is cut, not extended.

KILL CRITERIA:
  - If after 3 weeks the digest has surfaced zero roles the PO considered
    applying to, the matching is wrong or the company list is wrong — stop
    and fix one of those before writing more code.
  - If more than half of daily digests are empty AND the PO knows roles were
    posted, the adapters are broken — fix or drop those companies.
  - If maintaining adapters against site changes exceeds ~30 min/month,
    narrow the company list to ATS-backed companies only.
```

---

## Why this is tractable: the ATS concentration insight

The core technical bet is that **we do not need to scrape arbitrary websites**. The large majority of companies that run a real hiring process use a hosted applicant tracking system, and the major ATS platforms expose their public job boards as unauthenticated JSON.

Verified endpoint patterns (from vendor documentation — see Sources):

| ATS | Public endpoint pattern | Auth |
|-----|------------------------|------|
| Greenhouse | `boards-api.greenhouse.io/v1/boards/{token}/jobs` | none |
| Lever | `api.lever.co/v0/postings/{company}?mode=json` | none |
| Ashby | `api.ashbyhq.com/posting-api/job-board/{slug}` | none |

That means for most target companies the "crawler" is a JSON fetch and a diff — not brittle HTML scraping. HTML scraping exists only as a fallback for the tail.

> **Honest caveat I could not close**: this sandbox's network policy blocks outbound requests to these hosts, so I verified the endpoint shapes against vendor documentation rather than by calling them live. The first implementation task is a connectivity spike that hits all three for real and confirms field names before the adapter interfaces are frozen. If a shape differs, the adapter layer absorbs it — but I'd rather find that out in task 1 than at integration.

---

## What the daily experience looks like

1. Crawl runs on a schedule each weekday morning.
2. Each company adapter returns the current list of open postings.
3. Anything whose ID we've already seen is dropped — only genuinely new postings continue.
4. Cheap deterministic rules (title keywords, seniority, location, hard exclusions) reject the obvious misses. This is where ~90% of volume dies, at zero token cost.
5. Survivors are scored by Claude against a profile file the PO writes, producing a 0-100 fit score and a one-sentence reason.
6. Anything above the score threshold goes into one email. Nothing above threshold means **no email** — silence is a feature; a daily "0 new roles" email trains you to ignore the sender.

---

## Success metrics & review cadence

| Metric | Target | How measured |
|--------|--------|--------------|
| **Primary — Useful surface rate** | ≥1 applied-to role in 30 days | PO judgement |
| Precision | ≥70% of surfaced roles judged worth a look | PO marks a sample of digests |
| Coverage | 0 known-missed roles at ATS-backed companies | PO spot-checks a career page occasionally |
| Cost | < $1/month in API spend | Logged per run |
| Reliability | ≥95% of scheduled runs complete | Workflow run history |

**Review cadence**: daily glance for week 1 (is it broken?), then a single honest check at week 3 against the kill criteria.

---

## Open questions for the Product Owner

These do not block the architecture, but they block a *good* first digest. Answers wanted before or at PRD approval:

1. **Which companies?** The system needs the initial list. Names are enough — resolving each to its ATS slug is our job, and the setup tooling will do it semi-automatically.
2. **What's a match?** The profile file needs your actual criteria: target titles/role families, seniority band, locations and remote policy, must-have and dealbreaker keywords. The quality of the digest is bounded almost entirely by this file, not by the code.
3. **Delivery address and send time?** Which inbox, and what local time counts as "morning".
4. **Weekdays only, or every day?** Recommendation: weekdays — companies rarely post on weekends, and a weekend email is noise.

---

## Sources

- [Greenhouse Job Board API docs](https://developers.greenhouse.io/job-board) · [field reference](https://github.com/grnhse/greenhouse-api-docs/blob/master/source/includes/job-board/_jobs.md)
- [Lever Postings API README](https://github.com/lever/postings-api/blob/master/README.md)
- [Ashby Public Job Posting API](https://developers.ashbyhq.com/docs/public-job-posting-api)
- [ATS platforms with public job posting APIs](https://cavuno.com/blog/ats-platforms-public-job-posting-apis)
