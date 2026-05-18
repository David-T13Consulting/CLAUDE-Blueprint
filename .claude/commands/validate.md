---
description: Run UX Validation on an implemented feature. Audits first-time experience, WCAG 2.2 AA accessibility, feedback completeness, emotional tone, cognitive load, consistency, and benchmark. Produces a verdict. One of four parallel validators feeding Gate 4.
---

Spawn the `ux-validator` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name to validate.

**Prerequisite check:** Before spawning, verify the feature is implemented (code exists). If not, do NOT spawn — tell the user: "UX validation requires an implementation. Build the feature first."

The subagent will produce a full UX Validation Report including:
- Usability metrics (estimated task completion rate, taps to value, SUS score)
- First-time experience assessment (intuitive without instructions?)
- WCAG 2.2 AA compliance checklist (all criteria: PASS/FAIL/N-A)
- Feedback completeness audit (every action → feedback chain)
- Emotional tone review (human language, error message quality, delight moment)
- Cognitive load assessment (Hick's Law violations, recall burdens, extraneous load sources)
- Consistency check (design system compliance)
- Benchmark comparison (vs. iMessage / Apple Notes / ChatGPT app)
- Think-aloud protocol and 3-5 test tasks for Product Owner to run with real users
- Issues list (severity: critical/high/medium/low per UX dimension)
- DELIGHTFUL / USABLE_NEEDS_POLISH / REDESIGN verdict
- Structured `# CONTRACT: validate_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim.

**Veto rule:** If the first-time experience test fails (user cannot figure it out without instructions) or WCAG 2.2 AA fails on primary screens, the verdict is REDESIGN — the feature goes back to the Engineer (and possibly Designer) before Gate 4.

If verdict is DELIGHTFUL or USABLE_NEEDS_POLISH: note any remaining issues and suggest the other Gate 4 validators if not already run.
