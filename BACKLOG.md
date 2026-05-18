# Backlog

> **Prioritized list of all work to be done.**
> Items are ordered by priority within each category. Top = do first.
> Updated: 2026-04-01

---

## Critical — Must fix before any user sees this app

*(Empty)*

## High — Required for a shippable v1

| ID | Item | Category |
|----|------|----------|
| B-001 | Build `/retrospective` skill — automates extracting universal vs. project-specific learnings from CONVENTIONS.md, DECISIONS.md, and eval baselines at project end or monthly | Blueprint Learning |
| B-002 | Build `/sync-blueprint` skill — diffs a fork against the latest blueprint version, recommends which changes to apply, handles conflicts in App Config section | Blueprint Learning |

## Medium — Important but not blocking launch

| ID | Item | Category |
|----|------|----------|
| B-003 | Add retrospective trigger to session protocol — after 3+ projects or monthly, prompt the user to review UPSTREAM_CANDIDATES.md | Blueprint Learning |
| B-004 | Build eval baseline aggregation across forks — when the same rubric is scored across multiple projects, identify systemic weak dimensions that indicate a skill needs improvement | Blueprint Learning |
| B-005 | Add "forked from blueprint v1.x.x" tracking to PROJECT_STATE.md template so forks know their origin version | Blueprint Learning |
| B-006 | Create a blueprint diff tool that generates a human-readable summary of what changed between two blueprint versions (for CHANGELOG consumption) | Blueprint Learning |

## Low — Nice to have, do when time allows

| ID | Item | Category |
|----|------|----------|
| B-007 | Build a "blueprint health score" that aggregates human eval rubric scores across gates and projects to identify systemic quality trends | Blueprint Learning |
| B-008 | Explore automating downstream sync — when blueprint bumps a version, notify active forks and generate merge-ready patches for non-conflicting changes | Blueprint Learning |

## Follow-ups from v2.0.0 Migration

| ID | Item | Category | Priority |
|----|------|----------|----------|
| T-42a | Wire eval-judge automation in PostToolUse hook — currently a stub `echo` reminder; needs proper shell script that detects `# CONTRACT:` in agent output and triggers scoring | Hooks | Medium |
| T-80 | Create `SUS/usability-metrics` methodology skill — extracted from ux-validator, currently inline only | Skills | Low |
| T-81 | Create `interaction-laws` methodology skill — Fitts, Hick, Miller, Jakob, Doherty extracted from designer | Skills | Low |
| T-82 | Create `perf-budgets` methodology skill — Core Web Vitals and performance budget table extracted from perf-engineer | Skills | Low |

## Completed

| ID | Item | Completed |
|----|------|-----------|
| ✅ | L4 agentic architecture (orchestrator, eval-judge, task routing) | 2026-04-01 |
| ✅ | Upgrade all 23 files to 4/5 domain expertise | 2026-04-01 |
| ✅ | Human eval rubric for Product Owner gate reviews | 2026-04-01 |
| ✅ | Blueprint versioning (v1.0.0) + CHANGELOG + UPSTREAM_CANDIDATES template | 2026-04-01 |
| ✅ | v2.0.0 migration: 8 role subagents, 10 auto-loading skills, 10 slash commands, 4 hooks, engineer_output contract | 2026-05-18 |
