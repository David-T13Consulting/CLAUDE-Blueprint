# Project State

> **This file is the single source of truth for where the project stands RIGHT NOW.**
> Read this first at the start of every session. Update it at every milestone.
> Last updated: 2026-07-31

---

## Current Status

| Field | Value |
|-------|-------|
| **Phase** | Job Posting Crawler — awaiting Product Owner review of vision + architecture + mockup |
| **Pipeline Mode** | BUILD |
| **Active Work** | Job Posting Crawler (L4-ORCHESTRATED), branch `claude/job-posting-crawler-dura0o` |
| **Blocked On** | PO review of `docs/VISION.md`, `docs/ARCHITECTURE.md`, `docs/digest-mockup.html`. Then PRD → PO approval → build. |
| **Next Action** | PO reviews the three docs; answers the 4 open questions in VISION.md (company list, match criteria, delivery address/time, weekday-only) |

## Active Feature — Job Posting Crawler

Daily crawl of self-curated company career sites (via public ATS APIs), matched
against a PO-authored profile, delivered as one morning email digest.

**Confirmed by PO**: GitHub Actions cron runtime · email digest delivery ·
rules-first matching with Claude scoring only the survivors.

**Deferred to review**: the 4 open questions listed in `docs/VISION.md`.

**Known risk**: ATS endpoint shapes were verified against vendor documentation,
not live calls — this sandbox's network policy blocks those hosts. Implementation
task 1 is a connectivity spike that closes this.

## What Exists

- CLAUDE.md blueprint v1.0.0 (with L4 adaptive task routing)
- Agent skills (10) in `.claude/skills/` — all at 4/5 domain expertise
- Custom subagents (5) in `.claude/agents/` — all at 4/5 domain expertise
- Eval rubrics (9) in `.claude/evals/rubrics/` — 8 system + 1 human eval, all at 4/5
- Structured I/O contracts in `.claude/contracts/schemas.md`
- Blueprint learning infrastructure: CHANGELOG.md, UPSTREAM_CANDIDATES.md template
- Memory files (this file + BACKLOG, DECISIONS, CONVENTIONS)

- Job Posting Crawler review docs: `docs/VISION.md`, `docs/ARCHITECTURE.md`, `docs/digest-mockup.html`

## Session Log

- **2026-07-31**: Started Job Posting Crawler as the first real fork of the blueprint. Classified L4. PO chose GitHub Actions + email digest + rules-then-LLM matching. Produced vision, architecture, and email mockup for review. No code written yet — awaiting gate approval.

- **2026-04-01**: Built L4 agentic architecture (orchestrator, eval-judge, task routing)
- **2026-04-01**: Upgraded all 23 skill/agent/rubric files to 4/5 domain expertise
- **2026-04-01**: Added human eval rubric for Product Owner gate reviews
- **2026-04-01**: Added blueprint versioning (v1.0.0), CHANGELOG, UPSTREAM_CANDIDATES, learning loop backlog (B-001 through B-008)
