# Eval Rubric: Research Output

> Scores `/research` outputs against quality dimensions.
> Used by the eval judge agent (`.claude/agents/eval-judge.md`).

## Dimensions

### 1. Problem Clarity (weight: 2.0)

Does the problem statement identify a specific user, a specific pain, and a specific context?

| Score | Anchor |
|-------|--------|
| 1 | No clear problem stated or completely generic |
| 2 | Problem mentioned but vague ("users want better X") |
| 3 | Problem identifies a user and a pain point |
| 4 | Problem identifies user, pain, context, and current workaround |
| 5 | Problem is specific, falsifiable, and backed by evidence |

### 2. Scorecard Rigor (weight: 2.0)

Are validation scores justified with evidence, or just arbitrary numbers?

| Score | Anchor |
|-------|--------|
| 1 | Scores with no justification at all |
| 2 | Scores with vague rationale ("seems like a 7") |
| 3 | Scores with brief rationale per dimension |
| 4 | Scores backed by competitive data or user evidence |
| 5 | Each score backed by specific data points, research, or market evidence |

### 3. Competitive Analysis Depth (weight: 1.0)

Does it identify real competitors with real strengths and weaknesses?

| Score | Anchor |
|-------|--------|
| 1 | No competitors mentioned |
| 2 | Competitors listed but no analysis |
| 3 | Competitors analyzed at surface level |
| 4 | Specific feature gaps and opportunities identified |
| 5 | Deep competitive map with differentiation strategy |

### 4. User Stories Quality (weight: 1.0)

Are user stories specific, testable, and tied to the problem?

| Score | Anchor |
|-------|--------|
| 1 | Missing or generic ("As a user, I want to use the app") |
| 2 | Present but could apply to any product |
| 3 | Specific to this problem with clear outcomes |
| 4 | Include acceptance criteria and edge cases |
| 5 | Cover primary and secondary personas with prioritization |

### 5. Failure Mode Coverage (weight: 1.0)

Are failure modes realistic, specific, and actionable?

| Score | Anchor |
|-------|--------|
| 1 | Missing entirely |
| 2 | Generic failure modes ("user might not like it") |
| 3 | Specific failures identified for the core flow |
| 4 | Failures cover UX, technical, and business dimensions |
| 5 | Failures are prioritized with mitigation strategies |

### 6. Actionability (weight: 1.0)

Could someone act on this report immediately?

| Score | Anchor |
|-------|--------|
| 1 | Too vague to inform any decision |
| 2 | Directionally useful but missing key details |
| 3 | Clear recommendation with reasoning |
| 4 | Recommendation with specific next steps |
| 5 | Full decision framework — clear go/no-go with criteria |

## Grading

```
Weighted total = sum(score * weight)
Max possible = sum(5 * weight) = 5 * (2+2+1+1+1+1) = 40
Percentage = weighted_total / 40 * 100

>= 80%: STRONG
60-79%: ADEQUATE
40-59%: WEAK
< 40%:  FAIL
```
