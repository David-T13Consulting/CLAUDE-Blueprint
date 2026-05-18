# Metrics Event Log

> Append-only. One row per event. Never edit existing rows.
> Written by: gate commands (after each gate decision), eval-judge (after each score), main agent (after rework).
> Read by: `/metrics` command for aggregation.

## Column Definitions

| Column | Values | Meaning |
|--------|--------|---------|
| `date` | ISO date | When the event occurred |
| `feature` | string | Feature or task name |
| `metric` | see below | Which of the 4 metrics this event feeds |
| `event` | see below | The specific event type |
| `value` | string | Event payload |
| `notes` | string or `—` | Free text context |

### Valid `metric` values
- `collaboration` — feeds Collaboration Accuracy
- `eval` — feeds Eval Pass Rate
- `intervention` — feeds Human Intervention %
- `redundancy` — feeds Redundancy Rate

### Valid `event` values

**collaboration:**
- `handoff_success` — gate approved, next phase accepted the contract
- `handoff_failure` — subagent VETOed or gate rejected; work sent back

**eval:**
- `eval_pass` — eval-judge scored STRONG or ADEQUATE (≥60%)
- `eval_fail` — eval-judge scored WEAK or FAIL (<60%)
- `eval_regression` — score dropped >10pts from baseline

**intervention:**
- `gate_approved` — Product Owner gave proper gate approval
- `gate_overridden` — Product Owner skipped gate ("just do it", "skip this", etc.)
- `veto_upheld` — Product Owner accepted agent VETO and stopped/reworked
- `veto_overridden` — Product Owner overrode an agent VETO and proceeded anyway

**redundancy:**
- `rework` — user gave "change X" feedback; agent re-ran a phase already completed
- `agent_run` — an agent phase completed (denominator for redundancy rate)

---

## Event Log

| date | feature | metric | event | value | notes |
|------|---------|--------|-------|-------|-------|
