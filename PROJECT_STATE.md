# Project State

> **This file is the single source of truth for where the project stands RIGHT NOW.**
> Read this first at the start of every session. Update it at every milestone.
> Last updated: [DATE]

---

## Current Status

| Field | Value |
|-------|-------|
| **Phase** | Blueprint v1.0.0 complete — ready to fork for real projects |
| **Pipeline Mode** | N/A (this is the blueprint itself, not a project fork) |
| **Active Work** | None |
| **Blocked On** | Nothing |
| **Next Action** | Fork this repo for a real project and start building |

## What Exists

- CLAUDE.md blueprint v1.0.0 (with L4 adaptive task routing)
- Agent skills (10) in `.claude/skills/` — all at 4/5 domain expertise
- Custom subagents (5) in `.claude/agents/` — all at 4/5 domain expertise
- Eval rubrics (9) in `.claude/evals/rubrics/` — 8 system + 1 human eval, all at 4/5
- Structured I/O contracts in `.claude/contracts/schemas.md`
- Blueprint learning infrastructure: CHANGELOG.md, UPSTREAM_CANDIDATES.md template
- Memory files (this file + BACKLOG, DECISIONS, CONVENTIONS)

## Session Log

- **2026-04-01**: Built L4 agentic architecture (orchestrator, eval-judge, task routing)
- **2026-04-01**: Upgraded all 23 skill/agent/rubric files to 4/5 domain expertise
- **2026-04-01**: Added human eval rubric for Product Owner gate reviews
- **2026-04-01**: Added blueprint versioning (v1.0.0), CHANGELOG, UPSTREAM_CANDIDATES, learning loop backlog (B-001 through B-008)
- **2026-08-05**: Implemented runnable eval harness and agent harness scaffold, added golden dataset and red-team validation flow
