# Structured I/O Contracts

> **This file defines the machine-parseable output schemas for all skills and agents.**
> Every skill report MUST include a `CONTRACT` YAML block at the end.
> The orchestrator and eval judge consume ONLY the contract block — not the human-readable report above it.

---

## How Contracts Work

1. Every skill produces its normal human-readable report (unchanged)
2. At the very end, it appends a fenced YAML block starting with `# CONTRACT: [type]`
3. The orchestrator parses the `verdict` and `veto` fields to make routing decisions
4. The eval judge parses all fields to score output quality against rubrics
5. Contract blocks are YAML — no prose, no markdown, just structured data

**Format:**
```yaml
# CONTRACT: [skill]_output
field: value
nested:
  field: value
verdict: "ENUM_VALUE"
veto: false
veto_reason: null
```

---

## Contract Schemas

### route_output

Produced by: `/route [task]`
Consumed by: Main agent (routing decisions), orchestrator (L4 decomposition)

```yaml
# CONTRACT: route_output
task: string                          # Original task description
level: "L1" | "L2" | "L3" | "L4"     # Complexity classification
rationale: string                     # Why this level was chosen
signals:                              # What triggered this classification
  file_count: integer                 # Estimated files affected
  new_interfaces: boolean             # Requires new data models or APIs
  design_decisions: boolean           # Requires UX/UI decisions
  architectural_impact: boolean       # Changes system structure
  cross_cutting: boolean              # Affects multiple features/modules
pipeline:
  agents: list[string]                # Which agents activate
  gates: list[string]                 # Which gates apply
  parallel_groups: list[list[string]] # What can run concurrently
subtasks: null | list                 # L4 only: decomposed subtasks
  - task: string
    level: "L2" | "L3"               # Never L4 (no recursion)
    agents: list[string]
    depends_on: list[integer] | null  # Indices of prerequisite subtasks
```

---

### research_output

Produced by: `/research [problem]`
Consumed by: Gate 1 decision, `/design` prerequisite check, eval judge

```yaml
# CONTRACT: research_output
problem: string                       # One-sentence problem statement
target_user: string                   # Who has this problem
validation_scores:
  pain: 1-10
  frequency: 1-10
  alternatives: 1-10
  willingness_to_pay: 1-10
  feasibility: 1-10
  market_size: 1-10
  average: float                      # Calculated average
decision: "GREEN_LIGHT" | "EXPLORE_ONLY" | "PARK_IT"
user_stories:
  - string                            # "As a [user], I want [X], so that [Y]"
failure_modes:
  - string                            # What could go wrong
competitive_gaps:
  - string                            # What competitors miss
verdict: "PROCEED" | "EXPLORE_FIRST" | "DO_NOT_BUILD"
veto: boolean
veto_reason: string | null
```

---

### design_output

Produced by: `/design [feature]`
Consumed by: Gate 2 decision, `/architect` prerequisite check, eval judge

```yaml
# CONTRACT: design_output
feature: string                       # Feature name
research_ref: string                  # Problem statement from research
core_interaction: string              # One-sentence interaction model
screens:
  - name: string
    states:                           # All UI states for this screen
      - "empty" | "loading" | "populated" | "error" | "offline"
    components: list[string]          # Components used
    new_components: list[string]      # Components that need to be created
interactions:
  - trigger: string                   # What the user does
    action: string                    # What happens
    feedback: string                  # What the user sees/feels
accessibility:
  voiceover_labels: boolean
  touch_targets_44pt: boolean
  dynamic_type: boolean
  contrast_compliant: boolean
benchmark_pass: boolean               # Feels native next to iMessage/ChatGPT/Notes
verdict: "APPROVED" | "NEEDS_POLISH" | "REDESIGN"
veto: boolean
veto_reason: string | null
```

---

### architecture_output

Produced by: `/architect [feature]`
Consumed by: Gate 3 decision, engineer implementation, eval judge

```yaml
# CONTRACT: architecture_output
feature: string
design_ref: string                    # Design spec reference
data_model:
  - name: string                      # Type/interface name
    fields:
      - name: string
        type: string
        required: boolean
services:
  new:
    - name: string
      purpose: string
      inputs: list[string]
      outputs: list[string]
  modified:
    - name: string
      change: string
state_management:
  local: list[string]                 # Component-local state
  shared: list[string]                # App-wide state
  persisted: list[string]             # Stored on device/server
file_plan:
  create:
    - path: string
      purpose: string
  modify:
    - path: string
      change: string
implementation_order: list[string]    # Ordered steps
risks:
  - risk: string
    severity: "high" | "medium" | "low"
    mitigation: string
verdict: "APPROVED" | "PHASED_APPROACH" | "REDESIGN"
veto: boolean
veto_reason: string | null
```

---

### qa_output

Produced by: `/qa [feature]`
Consumed by: Post-implementation gate, orchestrator, eval judge

```yaml
# CONTRACT: qa_output
feature: string
files_reviewed: list[string]
tests:
  passed: integer
  failed: integer
  skipped: integer
  coverage_percent: float | null
bugs:
  - id: string                        # BUG-001, BUG-002, etc.
    description: string
    severity: "critical" | "high" | "medium" | "low"
    file: string
    line: integer | null
tests_written:
  - file: string
    test_count: integer
    assertion_count: integer
regression_pass: boolean              # Existing tests still pass
verdict: "PASS" | "BLOCK"
veto: boolean
veto_reason: string | null
```

---

### security_output

Produced by: `/security [scope]`
Consumed by: Post-QA gate, orchestrator, eval judge

```yaml
# CONTRACT: security_output
scope: string                         # What was audited
files_reviewed: list[string]
findings:
  - id: string                        # VULN-001, VULN-002, etc.
    severity: "critical" | "high" | "medium" | "low"
    category: string                  # OWASP category or custom
    description: string
    file: string
    line: integer | null
    fix: string                       # Recommended remediation
counts:
  critical: integer
  high: integer
  medium: integer
  low: integer
dependency_audit:
  vulnerabilities: integer
  outdated: integer
verdict: "PASS" | "BLOCK"
veto: boolean
veto_reason: string | null
```

---

### validate_output

Produced by: `/validate [feature]`
Consumed by: Post-security gate, orchestrator, eval judge

```yaml
# CONTRACT: validate_output
feature: string
checks:
  first_time_experience: boolean      # Can a new user succeed without help?
  accessibility:
    voiceover_labels: boolean
    touch_targets: boolean
    contrast_ratios: boolean
    dynamic_type: boolean
    reduce_motion: boolean
  feedback_completeness:
    tap_feedback: boolean
    loading_states: boolean
    error_states: boolean
    success_states: boolean
  emotional_tone: boolean             # Calm, confident, trustworthy
  consistency: boolean                # Matches rest of app
  benchmark: boolean                  # Feels native next to top apps
issues:
  - id: string                        # UX-001, UX-002, etc.
    description: string
    severity: "critical" | "high" | "medium" | "low"
    recommendation: string
delight_factor: string | null         # One moment that makes users smile
verdict: "DELIGHTFUL" | "USABLE_NEEDS_POLISH" | "REDESIGN"
veto: boolean
veto_reason: string | null
```

---

### perf_output

Produced by: `/perf [feature]`
Consumed by: Gate 4 decision, orchestrator, eval judge

```yaml
# CONTRACT: perf_output
feature: string
render:
  fps_target_met: boolean             # 60fps animations
  unnecessary_rerenders: boolean      # Found wasted renders
  native_driver: boolean              # Animations on native thread
memory:
  bounded: boolean                    # No unbounded growth
  cleanup_on_unmount: boolean         # Subscriptions/listeners cleaned
  leak_potential: list[string]        # Identified leak risks
network:
  redundant_calls: boolean            # Found duplicate API calls
  caching_implemented: boolean
  timeout_handling: boolean
bundle:
  size_impact_kb: float | null
  new_dependencies: list[string]
  justified: boolean                  # All deps necessary
cost:
  tokens_per_interaction: integer | null
  estimated_cost_per_user_day: float | null
  optimizations: list[string]         # Cost reduction opportunities
verdict: "PASS" | "OPTIMIZE" | "BLOCK"
veto: boolean
veto_reason: string | null
```

---

### orchestrator_output

Produced by: Orchestrator agent (L4 tasks)
Consumed by: Main agent (final gate), eval judge

```yaml
# CONTRACT: orchestrator_output
task: string                          # Original L4 task
subtasks:
  - id: integer
    task: string
    level: "L2" | "L3"
    status: "passed" | "blocked" | "skipped"
    verdict: string                   # From the subtask's own contract
    issues: list[string]              # Blocking issues if any
totals:
  subtasks_total: integer
  passed: integer
  blocked: integer
  skipped: integer
eval_scores:                          # From eval judge runs
  - skill: string
    score_percent: float
    grade: "STRONG" | "ADEQUATE" | "WEAK" | "FAIL"
    regression: boolean
blocking_issues: list[string]         # Aggregated across all subtasks
verdict: "ALL_CLEAR" | "PARTIAL_BLOCK" | "FULL_BLOCK"
gate_recommendation: "AUTO_PASS" | "HUMAN_REVIEW"
```

---

### eval_output

Produced by: Eval judge agent
Consumed by: Orchestrator, main agent, baseline system

```yaml
# CONTRACT: eval_output
skill: string                         # Which skill was evaluated
date: string                          # ISO date
scores:
  - dimension: string                 # Rubric dimension name
    score: 1-5                        # Rating
    weight: float                     # Dimension weight (1.0 or 2.0)
    justification: string             # Why this score
weighted_score_percent: float         # Weighted total / max possible
grade: "STRONG" | "ADEQUATE" | "WEAK" | "FAIL"
baseline:
  previous_score: float | null        # null if no baseline exists
  delta: float | null                 # Current - previous
  regression_detected: boolean        # True if delta < -10
recommendations: list[string]         # How to improve weak dimensions
```
