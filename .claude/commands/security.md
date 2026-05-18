---
description: Run a security audit on a feature or the full app. Applies STRIDE threat modeling, OWASP Mobile Top 10 (2024), OWASP LLM Top 10 (2025), and CVSS 4.0 scoring. Produces a PASS or BLOCK verdict. One of four parallel validators feeding Gate 4.
---

Spawn the `security` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name or "full app" for a full-application audit.

The subagent will produce a full Security Audit Report including:
- Threat model per component using STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation)
- OWASP Mobile Top 10 (2024) coverage (M1-M10: PASS/FAIL/N-A per category)
- OWASP Top 10 for LLM Applications (2025) coverage (LLM01-LLM10, if AI features present)
- Findings sorted by severity (Critical/High/Medium/Low) with CVSS 4.0 scores and CWE references
- Specific fix for each finding with code example
- Dependency audit (npm audit results, pinned versions check)
- Secrets scan (hardcoded credentials, storage compliance)
- PASS or BLOCK verdict (BLOCK if any Critical or High finding)
- Structured `# CONTRACT: security_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim.

**Veto rule:** If ANY critical or high vulnerability is found, the verdict is BLOCK — no exceptions. The finding must be fixed by the Engineer and security re-run before Gate 4 can be presented.

If verdict is PASS: note the findings summary and suggest the other Gate 4 validators if not already run:
```
/qa [feature]
/validate [feature]
/perf [feature]
```
Or run `/ship [feature]` to execute all four in parallel automatically.
