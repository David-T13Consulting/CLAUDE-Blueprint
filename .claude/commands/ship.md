---
description: Run all four Gate 4 validators in parallel (QA, Security, UX Validation, Performance), collect their reports, and present a merged Gate 4 summary for the Product Owner's final ship decision.
---

You are running the **Gate 4 parallel validation** for `$ARGUMENTS`. This spawns four subagents simultaneously and merges their results into a single Gate 4 report.

**Prerequisite check:** Before spawning, verify:
1. The feature is implemented (code exists)
2. Gate 3 (Architecture) was approved
3. The feature has not already gone through Gate 4

If prerequisites are not met, state what's missing and stop.

**Step 1: Spawn all four validators in parallel**

Send a single message with four Agent tool calls targeting the same feature:
- `qa` subagent — QA testing and bug report
- `security` subagent — Security audit (STRIDE, OWASP Mobile, OWASP LLM, CVSS)
- `ux-validator` subagent — UX Validation (accessibility, feedback, emotional tone, benchmark)
- `perf-engineer` subagent — Performance audit (budgets, render, memory, network, cost)

Pass `$ARGUMENTS` as the feature scope to all four.

**Step 2: Collect all four contract blocks**

Wait for all four subagents to complete. Parse the `# CONTRACT:` YAML block from each.

**Step 3: Check for vetoes and blocks**

Before presenting:
- QA BLOCK? → List all critical/high bugs
- Security BLOCK? → List all critical/high vulnerabilities
- UX REDESIGN? → List accessibility failures and first-time experience failures
- Performance BLOCK? → List budget violations

**Step 4: Present the merged Gate 4 report**

```
╔══════════════════════════════════════════════════════════╗
║                    GATE 4: SHIP?                         ║
╠══════════════════════════════════════════════════════════╣

FEATURE: [name]
DATE: [today]

VALIDATION RESULTS:

  QA:          [PASS / BLOCK]
    Bugs:      [N critical, N high, N medium, N low]
    Coverage:  [X%]
    Key issue: [top bug if any, or "none"]

  Security:    [PASS / BLOCK]
    Findings:  [N critical, N high, N medium, N low]
    Key issue: [top vulnerability if any, or "none"]

  UX:          [DELIGHTFUL / USABLE_NEEDS_POLISH / REDESIGN]
    A11y:      [PASS / FAIL — N violations]
    Key issue: [top UX finding if any, or "none"]

  Performance: [SHIP IT / OPTIMIZE FIRST / BLOCK]
    Budgets:   [all pass / N fail]
    Cost:      [$X/user/month — positive margin / negative margin]
    Key issue: [top perf finding if any, or "none"]

OUTSTANDING ISSUES REQUIRING ACTION BEFORE SHIP:
  [List any blocking issues, or "None — all validators passed"]

OVERALL VERDICT: ✅ SHIP IT / ❌ NOT READY (fix [X] first)
╚══════════════════════════════════════════════════════════╝

Ready to ship, or fix something first?
```

**Step 5: Wait for Product Owner decision**

Do NOT ship, merge, or mark complete without explicit Product Owner approval.

If approved:
- Update `BACKLOG.md` to mark the feature complete (✅)
- Update `PROJECT_STATE.md` with the new feature in "What Exists"
- Log the Gate 4 approval in `DECISIONS.md`
- Commit: `chore: update project memory — Gate 4 approved, [feature] shipped`

**Log all events to `.claude/metrics/log.md`** (append after Product Owner decision):

For each of the 4 validators, log its agent run and eval result:
```
| [date] | [feature] | redundancy | agent_run | qa | — |
| [date] | [feature] | redundancy | agent_run | security | — |
| [date] | [feature] | redundancy | agent_run | ux-validator | — |
| [date] | [feature] | redundancy | agent_run | perf-engineer | — |
```

For the gate decision:
- All pass → `| [date] | [feature] | collaboration | handoff_success | gate_4_approved | — |` and `| [date] | [feature] | intervention | gate_approved | gate_4 | — |`
- Fix X first (rework) → `| [date] | [feature] | collaboration | handoff_failure | gate_4_rework | [what's blocking] |` and `| [date] | [feature] | redundancy | rework | [agent]_rerun | [reason] |`
- Any BLOCK overridden → `| [date] | [feature] | intervention | veto_overridden | gate_4_[qa/security/ux/perf] | [reason] |`

For each validator verdict, log eval pass/fail:
- PASS / DELIGHTFUL / SHIP IT → `| [date] | [feature] | eval | eval_pass | [qa/security/ux/perf] | [score if known] |`
- BLOCK / REDESIGN → `| [date] | [feature] | eval | eval_fail | [qa/security/ux/perf] | [top issue] |`
