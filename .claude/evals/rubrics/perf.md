# Eval Rubric: Performance Output

> Scores `/perf` outputs against quality dimensions.

## Dimensions

### 1. Render Analysis Depth (weight: 2.0)

Are re-renders, animation performance, and virtualization actually analyzed?

| Score | Anchor |
|-------|--------|
| 1 | Not analyzed |
| 2 | "Seems fine" — no specific analysis |
| 3 | Key components checked for unnecessary re-renders |
| 4 | Re-renders traced with specific culprits identified |
| 5 | Full render audit with fix suggestions and before/after comparison |

### 2. Memory Analysis (weight: 1.5)

Are memory bounds, cleanup, and leak potential genuinely evaluated?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "No leaks found" — no evidence shown |
| 3 | Bounded structures and cleanup on unmount verified |
| 4 | Specific leak risks identified with affected components |
| 5 | Memory growth patterns analyzed with worst-case scenarios |

### 3. Network Efficiency (weight: 1.5)

Are redundant calls, caching, and timeout handling verified?

| Score | Anchor |
|-------|--------|
| 1 | Not analyzed |
| 2 | Basic check on API call existence |
| 3 | Duplicate detection and caching strategy reviewed |
| 4 | Full network profile with optimization recommendations |
| 5 | Network strategy with offline handling and cost optimization |

### 4. Cost Analysis (weight: 2.0)

For AI features: are token costs calculated with optimization opportunities?

| Score | Anchor |
|-------|--------|
| 1 | Not analyzed (for AI features) or N/A correctly noted |
| 2 | "Costs seem reasonable" — no numbers |
| 3 | Tokens per interaction estimated |
| 4 | Cost per user per day/month calculated with assumptions stated |
| 5 | Full unit economics with optimization plan and model tiering strategy |

### 5. Bundle Impact (weight: 1.0)

Is the feature's size impact quantified and justified?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "Added some dependencies" |
| 3 | New deps listed with sizes |
| 4 | Bundle impact quantified with justification per dependency |
| 5 | Bundle analysis with lighter alternatives considered |

## Grading

```
Max possible = 5 * (2+1.5+1.5+2+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
