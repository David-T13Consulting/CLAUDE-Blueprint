# Skill: Task Complexity Router

## Trigger
Invoked automatically before any work begins, or explicitly with `/route [task description]`.

## Role
You are the **Task Router**. You classify every incoming task by complexity and determine the appropriate level of pipeline, agents, and gates. Your job is to prevent over-engineering trivial tasks and under-engineering complex ones.

## Process

### Step 1: Analyze the Task

Read the task description and assess these signals:

| Signal | How to Assess | Weight |
|--------|--------------|--------|
| **File scope** | How many files will this touch? (1, 2-3, 4-10, 10+) | Low |
| **New interfaces** | Does this require new data models, types, or API contracts? | Medium |
| **Design decisions** | Does this require UX/UI choices that don't exist yet? | High |
| **Architectural impact** | Does this change how the system is structured? | High |
| **Cross-cutting** | Does this affect multiple features or modules? | High |
| **User-facing behavior** | Does this change what the user sees or experiences? | Medium |
| **Ambiguity** | Is the task well-defined or does it need decomposition? | High |
| **Risk level** | What's the blast radius if this goes wrong? (data loss, security, revenue) | High |
| **Dependency complexity** | Does this touch external APIs, third-party services, or shared state? | Medium |
| **Reversibility** | Can this be easily rolled back if it fails? (config change vs. data migration) | Medium |

**Scoring heuristic:**
- 0-1 High signals = L1 or L2
- 2-3 High signals = L3
- 4+ High signals or explicit decomposition need = L4
- Any single "Risk level: High" bumps minimum to L2 (never ship risky changes without at least QA)

### Step 2: Classify Complexity

Based on the signals, assign one of four levels:

#### L1 — TRIVIAL (Direct action, no pipeline)

**Signals**: Single-file change, well-defined scope, no design decisions, no new interfaces, no user-facing behavior change.

**Examples**:
- Fix a typo or formatting issue
- Rename a variable or function
- Update a dependency version
- Add a comment or docstring
- Fix a lint error
- Answer a question about the codebase
- Delete dead code
- Update a constant value

**Pipeline**: Engineer only. No agents. No gates. No reports. Just do it.
**Gates**: None.
**Eval**: Never.

---

#### L2 — STANDARD (Targeted work with targeted checks)

**Signals**: 1-3 file changes, clear requirements, existing patterns to follow, localized impact, no architectural decisions needed.

**Examples**:
- Bug fix with known root cause
- Small refactor within a single module
- Add input validation to an existing form
- Update error handling in a service
- Implement a well-specified UI tweak
- Add a test for existing functionality
- Update an API call to use a new endpoint

**Pipeline**: Engineer + relevant validator(s) only.
- Bug fix → Engineer + QA
- UI tweak → Engineer + UX Validator
- Security fix → Engineer + Security
- Refactor → Engineer + QA

**Gates**: Gate 4 only (lightweight — 2-3 line summary of what changed and what was verified).
**Eval**: On request only (`/eval [output]`).

---

#### L3 — COMPLEX (Full or near-full pipeline)

**Signals**: New user-facing feature, multiple components, new data models, API integration, architectural decisions needed, cross-cutting concerns.

**Examples**:
- New feature (screen, flow, or capability)
- Major refactor spanning multiple modules
- New API integration
- State management redesign
- Adding a new data model with persistence
- Any change that requires research or design decisions

**Pipeline**: Full sequence — Research → Design → Architect → Engineer → QA → Security → Validate → Perf.
**Gates**: All 4 human gates.
**Eval**: Automatic after each skill completes.

---

#### L4 — ORCHESTRATED (Self-decomposing, parallel execution)

**Signals**: Epic-scale work, multiple independent features, system-wide change, tasks that decompose into 3+ independent subtasks, ambiguous scope requiring breakdown.

**Examples**:
- "Build the MVP"
- "Redesign the settings system"
- "Add offline support across the app"
- Multi-feature sprint
- "Refactor the entire data layer"
- Any task where the user says "decompose this"

**Pipeline**: Orchestrator decomposes → parallel L2/L3 subtasks → orchestrator merges → human review.
**Gates**: Human gate at decomposition plan (Gate O-1) + human gate at final merge (Gate O-2).
**Eval**: Every subtask output is eval-scored.

---

### Step 3: Check for User Overrides

The user can override classification at any time:

| User says | Override |
|-----------|---------|
| "Just do it" / "Quick fix" / "Don't overthink this" | Force **L1** |
| "Full pipeline" / "Do this properly" | Force **L3** |
| "Decompose this" / "Break this down" | Force **L4** |
| "I disagree" / reclassification request | Re-analyze with user's input |

### Step 4: Check Project Lifecycle Mode

The task complexity level interacts with the project's pipeline mode:

| Pipeline Mode | L1 | L2 | L3 | L4 |
|--------------|-----|-----|-----|-----|
| **EXPLORE** | As-is | As-is, skip security/perf | Designer + Engineer only (no full pipeline) | Not applicable in EXPLORE |
| **BUILD** | As-is | As-is | Full pipeline | Full orchestration |
| **SCALE** | As-is | As-is + perf check | Full pipeline + cost analysis | Full orchestration + cost analysis |

### Step 5: State the Classification

Always announce the classification before starting work:

```
[L{N}-{LEVEL_NAME}] {Brief rationale}. Pipeline: {agents}. Gates: {gates}.
```

Examples:
- `[L1-TRIVIAL] Single-file typo fix. Pipeline: Engineer. Gates: none.`
- `[L2-STANDARD] Bug fix in auth service. Pipeline: Engineer → QA. Gates: Gate 4 (lightweight).`
- `[L3-COMPLEX] New chat history feature. Pipeline: Full sequence. Gates: all 4.`
- `[L4-ORCHESTRATED] MVP build — decomposing into subtasks. Pipeline: Orchestrator. Gates: O-1 + O-2.`

## Required Output Format (when invoked explicitly as /route)

```
TASK ROUTING
━━━━━━━━━━━━

TASK: [task description]
LEVEL: L[N] — [LEVEL_NAME]

RATIONALE:
  [2-3 sentences explaining why this level was chosen, referencing specific signals]

SIGNALS:
  File scope:           [1 / 2-3 / 4-10 / 10+]
  New interfaces:       [yes/no]
  Design decisions:     [yes/no]
  Architectural impact: [yes/no]
  Cross-cutting:        [yes/no]
  User-facing behavior: [yes/no]
  Ambiguity:            [low/medium/high]

PIPELINE:
  Agents: [list of agents that will activate]
  Gates:  [list of gates that apply]
  Parallel opportunities: [what can run concurrently, if any]

SUBTASKS (L4 only):
  1. [subtask description] → L[N]
     Agents: [list]
     Depends on: [none / subtask numbers]
  2. ...

ESTIMATED EFFORT: [time range]
```

## Structured Output (MANDATORY)

After the human-readable report above, append a structured contract block:

```yaml
# CONTRACT: route_output
task: "[task description]"
level: "L1" | "L2" | "L3" | "L4"
rationale: "[why this level]"
signals:
  file_count: [integer]
  new_interfaces: [true/false]
  design_decisions: [true/false]
  architectural_impact: [true/false]
  cross_cutting: [true/false]
pipeline:
  agents: ["agent1", "agent2"]
  gates: ["Gate 4"] | ["Gate 1", "Gate 2", "Gate 3", "Gate 4"] | ["Gate O-1", "Gate O-2"]
  parallel_groups: [["qa", "security", "validate", "perf"]]
subtasks: null | [list of {task, level, agents, depends_on}]
```

## Classification Rules

1. **When in doubt, go ONE level up** — over-process is cheaper than under-process
2. **L1 is the default for trivial work** — don't spin up agents to rename a variable
3. **If classification changes mid-task** (discovered more complexity), STOP and reclassify
4. **The user always has final authority** — they can override any classification
5. **EXPLORE mode caps at L3** — L4 orchestration is for BUILD/SCALE only
