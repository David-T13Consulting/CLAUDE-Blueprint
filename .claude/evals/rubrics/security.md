# Eval Rubric: Security Output

> Scores `/security` outputs against quality dimensions.

## Dimensions

### 1. Attack Surface Coverage (weight: 2.0)

Are all entry points identified and analyzed?

| Score | Anchor |
|-------|--------|
| 1 | No attack surface analysis |
| 2 | Only obvious entry points (user input) |
| 3 | User input + API responses + storage |
| 4 | All entry points including deep links, notifications, file system |
| 5 | Full attack surface map with risk levels per entry point |

### 2. Finding Specificity (weight: 2.0)

Are findings specific with file:line references and concrete fix instructions?

| Score | Anchor |
|-------|--------|
| 1 | Generic warnings ("should validate input") |
| 2 | Findings mention files but no line numbers |
| 3 | Findings with file:line and description |
| 4 | Findings with file:line, impact assessment, and fix |
| 5 | Findings with PoC scenario, impact, fix, and verification steps |

### 3. OWASP Alignment (weight: 1.5)

Are findings mapped to known vulnerability categories?

| Score | Anchor |
|-------|--------|
| 1 | No categorization |
| 2 | Ad-hoc categories |
| 3 | OWASP categories referenced |
| 4 | Full OWASP Mobile Top 10 coverage attempted |
| 5 | OWASP coverage + AI/LLM-specific threats (prompt injection, data exfil) |

### 4. Dependency Audit (weight: 1.5)

Were dependencies actually checked for known vulnerabilities?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | Mentioned but not run |
| 3 | `npm audit` results reported |
| 4 | Audit + pinning check + unnecessary dep analysis |
| 5 | Full supply chain review including transitive dependencies |

### 5. Severity Calibration (weight: 1.0)

Are severity levels accurately assigned, not inflated or deflated?

| Score | Anchor |
|-------|--------|
| 1 | All findings same severity (uncalibrated) |
| 2 | Two levels used without clear criteria |
| 3 | Four levels used with reasonable assignment |
| 4 | Severity tied to exploitability and impact |
| 5 | CVSS-aligned scoring with exploitation complexity considered |

## Grading

```
Max possible = 5 * (2+2+1.5+1.5+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
