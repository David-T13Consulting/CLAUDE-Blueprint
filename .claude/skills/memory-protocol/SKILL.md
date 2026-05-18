---
name: memory-protocol
description: Use at the start of every session and after gate decisions. Provides the mandatory file read list, continuous memory update rules, and commit cadence for keeping project context alive across sessions.
---

# Memory Protocol

## Session Start (MANDATORY — before ANY work)

Read these files in order:
1. `CLAUDE.md` — standards and operating system
2. `PROJECT_STATE.md` — where the project stands right now
3. `CONVENTIONS.md` — how the user likes to work
4. `BACKLOG.md` — what needs to be done
5. `DECISIONS.md` (skim recent) — context on settled questions

Then state: *"I've read the project state. [1-sentence summary]. What are we working on?"*

Do NOT ask questions already answered in these files.

## Continuous Update Triggers (act IMMEDIATELY, not later)

| Trigger | Action | File |
|---------|--------|------|
| Decision made | Log it now | `DECISIONS.md` |
| Gate approved or rejected | Update status now | `PROJECT_STATE.md` |
| Backlog item completed | Mark ✅ now | `BACKLOG.md` |
| New work identified | Add it now | `BACKLOG.md` |
| Feature finished / milestone reached | Full update + commit now | `PROJECT_STATE.md` + changed files |
| User corrects behavior / states preference | Log it now | `CONVENTIONS.md` |
| User says "done", "goodnight", "that's it" | Final sweep + commit | All memory files |

**The rule: if the session died RIGHT NOW, would the next session know what happened?** If no — you're behind.

## Commit Cadence

Don't commit after every line. Commit at:
- After every approval gate
- After completing a feature or major task
- After a batch of 2-3 decisions
- When the user signals they're done
- Before starting a long implementation

Commit format: `chore: update project memory — [brief context]`

## Memory File Reference

| File | Purpose | Read at start? | Update when? |
|------|---------|:--------------:|:------------:|
| `CLAUDE.md` | Standards, agents, processes | ✅ Always | Only if standards change |
| `PROJECT_STATE.md` | Current project status | ✅ Always | At every milestone, gate, or status change |
| `BACKLOG.md` | Prioritized work items | ✅ Always | When items added, completed, or reprioritized |
| `DECISIONS.md` | Decision log with rationale | ✅ Skim recent | Immediately when a decision is made |
| `CONVENTIONS.md` | User preferences & style | ✅ Always | Immediately when a new preference is observed |
