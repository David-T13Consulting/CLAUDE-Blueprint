# Decision Log

> **Every significant decision gets recorded here with context and rationale.**
> Future sessions read this file to avoid re-debating settled questions.
> Format: most recent first.

---

## D-005: Model Tiering — Haiku 4.5 for Job Matching
**Date**: 2026-07-31
**Decision**: Job-posting scoring uses `claude-haiku-4-5` by default, with `claude-sonnet-5` available via a `MATCH_MODEL` env var. Model is configuration, never a hardcoded constant.
**Rationale**: Scoring a posting against a fixed profile and emitting a score plus one sentence is classification with a short rationale — the exact case CLAUDE.md's Monetization section assigns to Haiku. Cost at ~5 scored survivors/day: ~$0.33/mo on Haiku vs ~$0.99/mo on Sonnet 5. Cost is not the deciding factor (both are trivial); the argument is that the task doesn't need more depth. Upgrade on evidence of poor seniority judgement, not preemptively.
**Note**: This deviates from the Claude API skill's default-to-Opus guidance. The project's own CLAUDE.md model-tiering rule takes precedence, and the deviation is flagged explicitly in ARCHITECTURE.md rather than made silently.
**Status**: Active — pending Gate 3 approval

---

## D-004: Degrade Toward Noise, Never Toward Silence
**Date**: 2026-07-31
**Decision**: Every failure mode in the crawler resolves toward surfacing more, not less. LLM scoring unavailable → send unscored and flagged. `seen.json` lost → one oversized digest. Adapter fails → named in the footer. Email send fails → workflow fails loudly.
**Rationale**: The failure costs are wildly asymmetric. A missed job posting is invisible to the user and therefore permanently unfixable — they never learn it existed. An extra row in the digest costs three seconds of reading. Given that asymmetry, every ambiguous case should resolve toward noise. The one exception is the quiet day: when nothing scores above threshold, no email is sent at all, because a daily "0 new roles" message trains the user to ignore the sender.
**Status**: Active

---

## D-003: Job Crawler Targets ATS APIs, Not General Web Scraping
**Date**: 2026-07-31
**Decision**: The crawler is built on per-ATS adapters hitting public unauthenticated JSON endpoints (Greenhouse, Lever, Ashby, and similar), with generic HTML scraping as a fallback for the tail only.
**Rationale**: The ATS market is concentrated enough that most companies running a real hiring process expose their job board as JSON. This turns "crawl 34 career sites" from brittle HTML parsing into a fetch-and-diff against a stable contract. It is the single decision that makes the project tractable in a one-session timebox.
**Verification gap**: Endpoint shapes were confirmed from vendor documentation, not live requests — this sandbox's network policy blocks those hosts. Implementation task 1 is a connectivity spike against all three before the adapter interface is frozen. The adapter layer localizes the blast radius if a shape differs.
**Status**: Active — pending Gate 3 approval

---

## D-002: Blueprint Learning Loop Architecture
**Date**: 2026-04-01
**Decision**: Implemented blueprint versioning (SemVer 1.0.0), CHANGELOG.md, and UPSTREAM_CANDIDATES.md template. Future improvements (retrospective skill, sync skill, baseline aggregation) tracked in BACKLOG.md as B-001 through B-008.
**Rationale**: Each fork is currently an island — learnings die in the fork. The blueprint needs a feedback loop: per-project learnings → classify universal vs. project-specific → upstream universal ones → all future forks inherit improvements. Built the "now" pieces (versioning, changelog, upstream template). Deferred automation (skills, triggers) until after 2-3 real projects provide data on what's actually needed.
**Key design choice**: Manual-first. Don't automate the learning loop until patterns are clear from real usage. Over-engineering a learning system before having learnings is ironic.
**Status**: Active — v1.0.0 shipped, automation deferred to B-001/B-002

---

## D-001: Add Human Eval Rubric for Gate Reviews
**Date**: 2026-04-01
**Decision**: Created `.claude/evals/rubrics/human-eval.md` — a rubric the Product Owner uses to score AI outputs at each gate (1-5 per dimension, weighted, same format as system rubrics).
**Rationale**: The 8 existing rubrics only score system outputs. Nothing scored whether the system's work was actually *good* from the human's perspective. Without this, gate approvals are subjective and uncalibrated — "looks good" means different things at different times.
**Dimensions**: 4 universal (Substance, Honesty, Actionability, Correctness) + 2 per gate (Evidence/Problem for G1, Completeness/Taste for G2, Soundness/Proportionality for G3, Coverage/Trustworthiness for G4).
**Status**: Active
