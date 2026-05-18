---
name: route
description: Use at the start of any new task to classify complexity (L1-L4) and select the correct pipeline, agents, and gates. Triggers automatically on incoming work before any agent activates.
---

# Task Complexity Router

Classify every incoming task before any work begins. Announce the classification. The user can override at any time.

## Classification Signals

| Signal | Weight |
|--------|--------|
| File scope (how many files?) | Low |
| New interfaces required? | Medium |
| Design decisions needed? | High |
| Architectural impact? | High |
| Cross-cutting concerns? | High |
| User-facing behavior change? | Medium |
| Ambiguity / decomposition needed? | High |
| Risk level (data loss, security, revenue)? | High |
| Irreversibility? | Medium |

**Scoring heuristic:**
- 0-1 High signals → L1 or L2
- 2-3 High signals → L3
- 4+ High signals or explicit decomposition need → L4
- Any single "Risk: High" bumps minimum to L2

## Complexity Levels

### L1 — TRIVIAL
Single-file change, well-defined, no design decisions, no user-facing behavior change.
**Examples:** fix typo, rename variable, update constant, delete dead code, answer question.
**Pipeline:** Engineer only. No gates. No reports. No eval.

### L2 — STANDARD
1-3 file changes, clear requirements, existing patterns to follow, localized impact.
**Examples:** bug fix, small refactor, add validation, UI tweak, add a test.
**Pipeline:** Engineer + relevant validator(s). Gate 4 only (lightweight: 2-3 line summary).
**Eval:** On request only.

### L3 — COMPLEX
New user-facing feature, multiple components, new data models, API integration, architectural decisions.
**Examples:** new feature, major refactor, new screen, API integration, state management change.
**Pipeline:** Full — researcher → designer → architect → engineer → qa + security + ux-validator + perf-engineer (parallel). All 4 human gates.
**Eval:** Automatic after each subagent completes.

### L4 — ORCHESTRATED
Epic-scale, multiple independent features, system-wide change, 3+ independent subtasks.
**Examples:** "Build the MVP", "Redesign settings", "Add offline support across the app".
**Pipeline:** Orchestrator decomposes → L2/L3 subtasks → merge. Gates O-1 (decomp) + O-2 (merge).
**Eval:** Every subtask output.

## User Overrides

| User says | Effect |
|-----------|--------|
| "Just do it" / "Quick fix" / "Don't overthink" | Force L1 |
| "Full pipeline" / "Do this properly" | Force L3 |
| "Decompose this" / "Break this down" | Force L4 |

## Pipeline Mode Interaction

| Mode | L1 | L2 | L3 | L4 |
|------|----|----|----|----|
| EXPLORE | As-is | Skip security/perf | Designer + Engineer only | Not available |
| BUILD | As-is | As-is | Full pipeline | Full orchestration |
| SCALE | As-is | As-is + perf | Full pipeline + cost | Full + cost analysis |

## Announcement Format

Always announce before starting work:

```
[L{N}-{LEVEL}] {rationale}. Pipeline: {agents}. Gates: {gates}.
```

Examples:
- `[L1-TRIVIAL] Single-file typo fix. Pipeline: Engineer. Gates: none.`
- `[L2-STANDARD] Bug fix in auth service. Pipeline: Engineer → QA. Gates: Gate 4 (lightweight).`
- `[L3-COMPLEX] New chat history feature. Pipeline: Full sequence. Gates: all 4.`
- `[L4-ORCHESTRATED] MVP build — decomposing into subtasks. Gates: O-1 + O-2.`

## Classification Rules

1. When in doubt, go ONE level up — over-process is cheaper than under-process
2. L1 is the default for trivial work — don't spin up subagents to rename a variable
3. If classification changes mid-task (discovered more complexity), STOP and reclassify
4. The user always has final authority

## Structured Output (when invoked explicitly as /route)

```yaml
# CONTRACT: route_output
task: "[task description]"
level: "L1" | "L2" | "L3" | "L4"
rationale: "[why this level]"
signals:
  file_count: 1
  new_interfaces: false
  design_decisions: false
  architectural_impact: false
  cross_cutting: false
pipeline:
  agents: ["engineer"]
  gates: []
  parallel_groups: []
subtasks: null
```
