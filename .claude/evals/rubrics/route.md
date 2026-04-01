# Eval Rubric: Route Output

> Scores `/route` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Classification Accuracy (weight: 2.0)

Is the complexity level appropriate for the task?

| Score | Anchor |
|-------|--------|
| 1 | Wildly wrong (L1 for a new feature, L4 for a typo fix) |
| 2 | Off by one level with weak justification |
| 3 | Correct level with adequate reasoning citing 3+ signals |
| 4 | Correct level with signal-by-signal analysis including weights |
| 5 | Correct level with nuanced handling of ambiguous signals, risk-weighting, and edge case reasoning |

### 2. Signal Analysis (weight: 1.5)

Are the complexity signals thoroughly evaluated with the scoring heuristic?

| Score | Anchor |
|-------|--------|
| 1 | No signal analysis |
| 2 | 1-2 signals mentioned |
| 3 | All core signals evaluated (file scope, interfaces, design, architecture, cross-cutting, ambiguity) |
| 4 | All signals + risk level, dependency complexity, reversibility — with weights applied |
| 5 | Signals evaluated with specific evidence, High-signal count used for level determination, edge cases reasoned |

### 3. Pipeline Selection (weight: 1.5)

Are the right agents and gates selected for this level?

| Score | Anchor |
|-------|--------|
| 1 | No pipeline specified |
| 2 | Generic pipeline (just "full" or "minimal") |
| 3 | Correct agents listed for the complexity level with gates identified |
| 4 | Agents + gates + parallel opportunities identified + pipeline mode interaction (EXPLORE/BUILD/SCALE) |
| 5 | Optimal agent selection with rationale for each, parallel groups maximized, and override awareness |

### 4. Decomposition Quality (L4 only) (weight: 2.0)

For L4 tasks: are subtasks well-scoped, independent, and correctly leveled?

| Score | Anchor |
|-------|--------|
| 1 | No decomposition for an L4 task |
| 2 | Subtasks listed but overlapping or poorly scoped |
| 3 | Independent subtasks with correct L2/L3 levels and no L4 recursion |
| 4 | Clear dependency graph with parallel groups identified, testable deliverables per subtask |
| 5 | Optimal decomposition with minimal dependencies, max parallelism, rollback plan, and effort estimates per subtask |

*Note: For L1-L3 tasks, score this dimension as N/A (excluded from calculation).*

### 5. Effort Estimation (weight: 1.0)

Is the time estimate reasonable and calibrated?

| Score | Anchor |
|-------|--------|
| 1 | No estimate |
| 2 | Unrealistic estimate (1 hour for a full feature, 1 week for a typo fix) |
| 3 | Reasonable range provided (e.g., "2-4 hours") |
| 4 | Range with assumptions stated and risk factors identified |
| 5 | Range calibrated to task signals, pipeline mode, and project velocity with confidence level |

## Grading

For L1-L3 tasks (4 dimensions):
```
Max possible = 5 * (2+1.5+1.5+1) = 30
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```

For L4 tasks (5 dimensions):
```
Max possible = 5 * (2+1.5+1.5+2+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
