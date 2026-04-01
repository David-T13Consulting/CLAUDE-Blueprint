# Eval Rubric: Research Output

> Scores `/research` outputs against quality dimensions.
> Used by the eval judge agent (`.claude/agents/eval-judge.md`).
> Version: 2.0

## Dimensions

### 1. Problem Clarity (weight: 2.0)

Does the problem statement identify a specific user, a specific pain, and a specific context?

| Score | Anchor |
|-------|--------|
| 1 | No clear problem stated or completely generic |
| 2 | Problem mentioned but vague ("users want better X") |
| 3 | Problem identifies a user and a pain point with context |
| 4 | Problem identifies user, pain, context, current workaround, and emotional state |
| 5 | Problem is specific, falsifiable, backed by cited evidence, with JTBD job statement |

### 2. Scorecard Rigor (weight: 2.0)

Are validation scores justified with evidence, not just arbitrary numbers?

| Score | Anchor |
|-------|--------|
| 1 | Scores with no justification at all |
| 2 | Scores with vague rationale ("seems like a 7") |
| 3 | Scores with brief rationale and evidence tier labeled per dimension |
| 4 | Scores backed by competitive data or user evidence, each with explicit evidence tier (T1-T4) |
| 5 | Each score backed by specific data points with source citations, evidence tiers, and confidence bounds |

### 3. Market Sizing (weight: 1.5)

Is the market opportunity quantified with TAM/SAM/SOM or equivalent methodology?

| Score | Anchor |
|-------|--------|
| 1 | No market sizing |
| 2 | Vague ("big market" / "lots of users") |
| 3 | TAM/SAM/SOM framework applied with estimates and assumptions stated |
| 4 | Bottom-up estimation with specific data sources and conversion assumptions |
| 5 | Multiple sizing methodologies cross-validated, assumptions sensitivity-tested |

### 4. Competitive Analysis Depth (weight: 1.0)

Does it identify real competitors with real strengths, weaknesses, and gap analysis?

| Score | Anchor |
|-------|--------|
| 1 | No competitors mentioned |
| 2 | Competitors listed but no analysis |
| 3 | 3+ competitors analyzed with specific strengths/weaknesses and ratings |
| 4 | Gap analysis identifies unserved needs from 1-2 star reviews and user complaints |
| 5 | Deep competitive map with differentiation strategy, pricing comparison, and market positioning |

### 5. User Analysis Quality (weight: 1.5)

Is user analysis grounded in JTBD or equivalent named framework, not generic personas?

| Score | Anchor |
|-------|--------|
| 1 | Missing or generic ("As a user, I want to use the app") |
| 2 | Basic demographic persona without behavioral insight |
| 3 | JTBD job statement with functional steps identified |
| 4 | Full job map (define → locate → execute → conclude) with pain points per step |
| 5 | Multi-persona JTBD with Kano classification of features and Outcome-Driven Innovation lens |

### 6. Failure Modes & Risk (weight: 1.0)

Are failure modes mapped across UX, technical, and business dimensions with severity?

| Score | Anchor |
|-------|--------|
| 1 | Missing entirely |
| 2 | Generic failure modes ("user might not like it") |
| 3 | Specific failures across UX, technical, and business with probability/impact |
| 4 | Failures prioritized with mitigation strategies per dimension |
| 5 | Risk matrix with probability × impact scoring, mitigations, and monitoring plan |

### 7. Problem-Solution Fit Assessment (weight: 1.0)

Is the maturity level (problem exists → solution resonates → users will pay) honestly assessed?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | Assumed fit without evidence |
| 3 | Three levels assessed with YES/NO/PARTIAL and evidence |
| 4 | Assessment includes specific evidence gaps and validation plan |
| 5 | Fit assessment with staged validation roadmap and kill criteria per level |

## Grading

```
Weighted total = sum(score * weight)
Max possible = 5 * (2+2+1.5+1+1.5+1+1) = 50
Percentage = weighted_total / 50 * 100

>= 80%: STRONG
60-79%: ADEQUATE
40-59%: WEAK
< 40%:  FAIL
```
