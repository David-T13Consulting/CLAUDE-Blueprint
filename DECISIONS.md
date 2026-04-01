# Decision Log

> **Every significant decision gets recorded here with context and rationale.**
> Future sessions read this file to avoid re-debating settled questions.
> Format: most recent first.

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
