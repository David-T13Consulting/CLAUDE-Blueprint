# Decision Log

> **Every significant decision gets recorded here with context and rationale.**
> Future sessions read this file to avoid re-debating settled questions.
> Format: most recent first.

---

## D-008: v2.0.0 Migration Complete — Smoke Tests Passed
**Date**: 2026-05-18
**Decision**: v2.0.0 architecture migration is complete. All 7 phases executed. Smoke tests passed: 31/31 files have valid frontmatter, all role agents have CONTRACT blocks, all commands reference correct subagents.
**What shipped**:
- 10 auto-loading methodology skills (JTBD, Kano, Nielsen, Testing Pyramid, OWASP Mobile, OWASP LLM, STRIDE, CVSS, route, memory-protocol)
- 8 role subagents with model right-sizing and tool whitelists
- 10 slash commands routing to subagents
- 4 hooks (SessionStart, PreToolUse, PostToolUse, Stop)
- `engineer_output` contract added to schemas.md
- Orchestrator updated to reference new agent roster with parallel spawn pattern
**Pending**: T-42a (eval-judge automation hook), T-80/T-81/T-82 (additional methodology skills)
**Status**: Active

---

## D-007: No Backwards Compatibility for v2.0.0 Architecture Migration
**Date**: 2026-05-18
**Decision**: Clean break. This is a blueprint repo with no live forks consuming it. Old `.claude/skills/*.md` flat files are deleted, not symlinked or kept.
**Rationale**: Backwards-compat shims add complexity and become permanent. No forks are affected. Future forks will fork from v2.0.0 onward.
**Status**: Active

---

## D-006: Subagent Naming Convention
**Date**: 2026-05-18
**Decision**: Subagents use role nouns (`researcher`, `designer`, `architect`, `engineer`, `qa`, `security`, `ux-validator`, `perf-engineer`). Slash commands keep verb form (`/research`, `/design`, etc.).
**Rationale**: Subagents are team members (nouns); slash commands are instructions (verbs). Separates the "who" from the "do it".
**Status**: Active

---

## D-005: Model Right-Sizing Per Subagent
**Date**: 2026-05-18
**Decision**: orchestrator/researcher/architect/security → opus (deep reasoning). engineer/designer/qa/ux-validator/perf-engineer → sonnet (implementation). eval-judge/codebase-explorer → haiku (deterministic, fast).
**Rationale**: Cost/capability fit. Haiku for deterministic tasks, Opus for tasks requiring judgment and synthesis, Sonnet as the production default.
**Status**: Active

---

## D-004: QA and Security Duplication Resolution
**Date**: 2026-05-18
**Decision**: Collapse `skills/qa.md` + `agents/qa-runner.md` into a single `agents/qa.md`. Same for security (`skills/security.md` + `agents/security-reviewer.md` → `agents/security.md`). Old files deleted in Phase 6.
**Rationale**: Two definitions of the same role diverge over time and create confusion about which is authoritative. One subagent per role, with full depth inside it.
**Status**: Active

---

## D-003: Primitives — What Goes Where
**Date**: 2026-05-18
**Decision**: Roles → `.claude/agents/` (subagents with frontmatter, tool whitelist, model). Methodology → `.claude/skills/<name>/SKILL.md` (auto-loading capability packs). User triggers → `.claude/commands/` (slash commands, thin wrappers). Enforcement → `.claude/settings.json` hooks.
**Rationale**: Claude Code (May 2026) has four distinct primitives — Skill / Subagent / Slash Command / Hook — that serve different purposes. Using Skills for role-playing (the v1 pattern) means one agent context has no tool isolation, no model assignment, no parallelism, and no auto-load. Using proper primitives enables all four.
**Status**: Active

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
