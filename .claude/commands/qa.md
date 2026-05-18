---
description: Run QA testing on an implemented feature. Creates a test plan (unit/integration/E2E), writes tests, checks edge cases, runs regression, and audits accessibility. Produces a PASS or BLOCK verdict. One of four parallel validators feeding Gate 4.
---

Spawn the `qa` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name or scope to test.

**Prerequisite check:** Before spawning, verify the feature is implemented (code exists). If not, do NOT spawn — tell the user: "QA requires an implementation. Build the feature first."

The subagent will produce a full QA Report including:
- Test plan (unit/integration/E2E counts, planned vs. written)
- Actual test code for critical paths
- Bug report for each issue found (severity: CRITICAL/HIGH/MEDIUM/LOW per bug severity framework)
- Accessibility audit (jest-axe violations, VoiceOver labels, touch targets)
- Regression results (do existing tests still pass?)
- Coverage report (%, gaps identified)
- Exploratory notes (ad-hoc findings, code smells, race conditions)
- PASS or BLOCK verdict
- Structured `# CONTRACT: qa_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim.

If verdict is BLOCK: note the blocking bugs and wait for the user to direct next steps (fix with Engineer, then re-run QA).

If verdict is PASS: suggest running the other Gate 4 validators in parallel:
```
/security [feature]
/validate [feature]
/perf [feature]
```
Or run `/ship [feature]` to execute all four in parallel automatically.
