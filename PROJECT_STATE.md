# Project State

> **This file is the single source of truth for where the project stands RIGHT NOW.**
> Read this first at the start of every session. Update it at every milestone.
> Last updated: 2026-05-18

---

## Current Status

| Field | Value |
|-------|-------|
| **Phase** | Blueprint v2.0.0 — migration from flat skills to proper Claude Code primitives complete |
| **Pipeline Mode** | N/A (this is the blueprint itself, not a project fork) |
| **Active Work** | Phase 7 smoke tests (T-70, T-71) |
| **Blocked On** | Nothing |
| **Next Action** | Run T-71 frontmatter linter smoke test, then fork for a real project |

## What Exists

### Role Subagents (`.claude/agents/`) — 11 files
- `researcher.md` — UX Research (opus, 20 turns) → `research_output`
- `designer.md` — Product Design (sonnet, 20 turns) → `design_output`
- `architect.md` — Software Architecture (opus, 25 turns) → `architecture_output`
- `engineer.md` — Implementation (sonnet, 40 turns) → `engineer_output`
- `qa.md` — QA Engineering (sonnet, 25 turns) → `qa_output`
- `security.md` — Security Audit (opus, 20 turns) → `security_output`
- `ux-validator.md` — UX Validation (sonnet, 15 turns) → `validate_output`
- `perf-engineer.md` — Performance Engineering (sonnet, 20 turns) → `perf_output`
- `orchestrator.md` — L4 Task Orchestrator (opus, 50 turns)
- `eval-judge.md` — Quality Evaluator (haiku, 10 turns)
- `codebase-explorer.md` — Read-only Codebase Mapping (sonnet)

### Auto-Loading Skills (`.claude/skills/<name>/SKILL.md`) — 10 files
- `route/` — L1-L4 task classification
- `memory-protocol/` — Session start + memory update rules
- `jtbd/` — Jobs-to-Be-Done framework + 8-step job map
- `kano/` — Kano Model for feature prioritization
- `nielsen-heuristics/` — Nielsen's 10 Usability Heuristics
- `testing-pyramid/` — 70/20/10 unit/integration/E2E framework
- `owasp-mobile/` — OWASP Mobile Top 10 (2024)
- `owasp-llm/` — OWASP Top 10 for LLM Applications (2025)
- `stride/` — STRIDE threat modeling
- `cvss/` — CVSS 4.0 severity scoring

### Slash Commands (`.claude/commands/`) — 10 files
- `research.md` → researcher → Gate 1
- `design.md` → designer → Gate 2
- `architect.md` → architect → Gate 3
- `qa.md` → qa → feeds Gate 4
- `security.md` → security → feeds Gate 4
- `validate.md` → ux-validator → feeds Gate 4
- `perf.md` → perf-engineer → Gate 4
- `ship.md` → 4 parallel validators → Gate 4 merged report
- `checkpoint.md` → main context decision audit
- `readiness.md` → main context pre-flight audit

### Hooks (`.claude/settings.json`)
- SessionStart: memory file reminder
- PreToolUse on Bash(git commit): lint + typecheck gate
- PostToolUse on Agent: eval-judge reminder (T-42a stub)
- Stop: untracked files check

### Eval Infrastructure
- Rubrics (9) in `.claude/evals/rubrics/`
- Contracts (8 schemas) in `.claude/contracts/schemas.md`
- Baselines in `.claude/evals/baselines/`

## Session Log

- **2026-04-01**: Built L4 agentic architecture (orchestrator, eval-judge, task routing)
- **2026-04-01**: Upgraded all 23 skill/agent/rubric files to 4/5 domain expertise
- **2026-04-01**: Added human eval rubric for Product Owner gate reviews
- **2026-04-01**: Added blueprint versioning (v1.0.0), CHANGELOG, UPSTREAM_CANDIDATES, learning loop backlog (B-001 through B-008)
- **2026-05-18**: Architecture review — identified conflation of Claude Code primitives (Skills/Subagents/Commands/Hooks)
- **2026-05-18**: Migration to v2.0.0 — full execution: 8 role subagents, 10 auto-loading skills, 10 slash commands, 4 hooks, engineer_output contract, orchestrator updated
