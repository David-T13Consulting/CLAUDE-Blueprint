---
description: Compute and display the 4 multi-agent success metrics — Collaboration Accuracy, Redundancy Rate, Eval Pass Rate, and Human Intervention % — from the event log. Run any time to get a health snapshot. Optionally filter by feature name.
---

Read `.claude/metrics/log.md` and compute the 4 metrics below. If `$ARGUMENTS` is provided, filter to rows where `feature` matches. Then display the dashboard.

## Computation Rules

### 1. Collaboration Accuracy
`= handoff_success / (handoff_success + handoff_failure)`

- Count rows where `metric=collaboration, event=handoff_success`
- Count rows where `metric=collaboration, event=handoff_failure`
- If denominator = 0: display "No handoffs recorded yet"
- Target: ≥90%. Below 80% = investigate which gates are failing.

### 2. Redundancy Rate
`= rework / agent_run`

- Count rows where `metric=redundancy, event=rework`
- Count rows where `metric=redundancy, event=agent_run`
- If denominator = 0: display "No agent runs recorded yet"
- Target: ≤15%. Above 25% = agents are producing outputs that need too much rework; check research and design quality upstream.

### 3. Eval Pass Rate
`= eval_pass / (eval_pass + eval_fail)`

- Count rows where `metric=eval, event=eval_pass`
- Count rows where `metric=eval, event=eval_fail`
- Also count `eval_regression` as a warning (not in pass/fail denominator)
- If denominator = 0: display "No evals recorded yet — spawn eval-judge after each skill"
- Target: ≥80%. Below 60% = outputs consistently weak; check agent instructions.

### 4. Human Intervention %
`= (gate_overridden + veto_overridden) / (gate_approved + gate_overridden + veto_upheld + veto_overridden)`

- Count all four intervention event types
- Overrides (gate_overridden + veto_overridden) = numerator
- All decisions = denominator
- If denominator = 0: display "No gate decisions recorded yet"
- Target: ≤20%. Above 40% = agents are not meeting quality bar, forcing constant human correction.

---

## Required Output Format

```
+--------------------------------------------------+
|        MULTI-AGENT METRICS DASHBOARD             |
+--------------------------------------------------+

Filter: [feature name or "all features"]
Period: [date range from log or "all time"]
Total events: [N]

┌─────────────────────────────────────────────────┐
│ Collaboration Accuracy          [X%]  [●/○/○]   │
│ handoff_success: N | handoff_failure: N          │
│ Target: ≥90%  Status: ON_TARGET / AT_RISK / FAIL │
├─────────────────────────────────────────────────┤
│ Redundancy Rate                 [X%]  [●/○/○]   │
│ rework: N | agent_run: N                         │
│ Target: ≤15%  Status: ON_TARGET / AT_RISK / FAIL │
├─────────────────────────────────────────────────┤
│ Eval Pass Rate                  [X%]  [●/○/○]   │
│ eval_pass: N | eval_fail: N | regression: N      │
│ Target: ≥80%  Status: ON_TARGET / AT_RISK / FAIL │
├─────────────────────────────────────────────────┤
│ Human Intervention %            [X%]  [●/○/○]   │
│ overrides: N | proper approvals: N               │
│ Target: ≤20%  Status: ON_TARGET / AT_RISK / FAIL │
└─────────────────────────────────────────────────┘

REGRESSIONS: [list eval_regression events or "none"]

DIAGNOSIS:
[For each metric not ON_TARGET, one sentence on likely cause and what to check]

RAW LOG TAIL (last 10 events):
[last 10 rows from log.md]
```

Status indicator:
- ON_TARGET: metric is within target range — `●`
- AT_RISK: within 10% of threshold — `◑`
- FAIL: outside target threshold — `○`

After displaying, check if any metric is FAIL and surface: "⚠️ [metric] is below target. Likely cause: [diagnosis]. Consider: [action]."
