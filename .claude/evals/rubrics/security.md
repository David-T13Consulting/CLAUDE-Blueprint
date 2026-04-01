# Eval Rubric: Security Output

> Scores `/security` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Threat Modeling (weight: 2.0)

Is a systematic threat model applied (STRIDE or equivalent), not ad hoc checks?

| Score | Anchor |
|-------|--------|
| 1 | No systematic threat modeling |
| 2 | Ad hoc security checks without framework |
| 3 | STRIDE applied to primary components with threats identified |
| 4 | STRIDE per component with specific threat scenarios and mitigations |
| 5 | Full STRIDE model with threat-to-mitigation mapping, residual risk documented |

### 2. OWASP Coverage (weight: 2.0)

Are OWASP categories (Mobile 2024 and/or LLM 2025) systematically checked?

| Score | Anchor |
|-------|--------|
| 1 | No OWASP reference |
| 2 | OWASP mentioned but only 2-3 categories checked |
| 3 | OWASP Mobile M1-M10 systematically checked with pass/fail per category |
| 4 | Full OWASP Mobile M1-M10 + LLM Top 10 (if AI features) with evidence per category |
| 5 | Full OWASP coverage with CWE mapping, specific code references, and remediation for each finding |

### 3. Finding Specificity (weight: 2.0)

Are findings specific with file:line references, CVSS scoring, and concrete fix instructions?

| Score | Anchor |
|-------|--------|
| 1 | Generic warnings ("should validate input") |
| 2 | Findings mention files but no line numbers or severity justification |
| 3 | Findings with file:line, CWE ID, and severity level (CRITICAL/HIGH/MEDIUM/LOW) |
| 4 | Findings with CVSS 4.0-aligned scoring, CWE ID, impact assessment, and specific fix with code example |
| 5 | Findings with CVSS vector, PoC scenario, impact, fix, verification steps, and regression test suggestion |

### 4. LLM/AI Threat Assessment (weight: 1.5)

For apps with AI features: are LLM-specific threats assessed?

| Score | Anchor |
|-------|--------|
| 1 | Not assessed (for AI apps) or N/A correctly noted (no AI) |
| 2 | "AI seems secure" — no specific analysis |
| 3 | Prompt injection and system prompt leakage specifically tested |
| 4 | LLM01-LLM10 assessed: prompt injection, output handling, excessive agency, unbounded consumption |
| 5 | Full LLM threat audit with specific test cases, cost abuse scenarios, and defense-in-depth mitigations |

*Note: For non-AI apps, score this dimension as N/A (excluded from calculation).*

### 5. Supply Chain & Secrets Audit (weight: 1.5)

Were dependencies and secrets actually scanned, not just mentioned?

| Score | Anchor |
|-------|--------|
| 1 | Not checked |
| 2 | Mentioned but not actually executed |
| 3 | `npm audit` run with results reported; basic secrets pattern search performed |
| 4 | Audit + pinning check + unnecessary dep analysis + secrets scan with specific patterns |
| 5 | Full supply chain review: transitive deps, license compliance, integrity verification, plus git history secrets scan |

### 6. Severity Calibration (weight: 1.0)

Are severity levels accurately assigned using a consistent framework?

| Score | Anchor |
|-------|--------|
| 1 | All findings same severity (uncalibrated) |
| 2 | Two levels used without clear criteria |
| 3 | Four levels used with reasonable assignment based on exploitability |
| 4 | CVSS 4.0-aligned scoring with attack vector, complexity, and impact considered |
| 5 | Full CVSS vector string per finding with base, threat, and environmental considerations |

## Grading

For apps with AI features (6 dimensions):
```
Max possible = 5 * (2+2+2+1.5+1.5+1) = 50
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```

For non-AI apps (5 dimensions, LLM dimension excluded):
```
Max possible = 5 * (2+2+2+1.5+1) = 42.5
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
