# Eval Rubric: QA Output

> Scores `/qa` outputs against quality dimensions.

## Dimensions

### 1. Test Coverage Breadth (weight: 2.0)

Does the test plan cover happy path, edge cases, errors, and platform specifics?

| Score | Anchor |
|-------|--------|
| 1 | Only happy path tested |
| 2 | Happy path + a few edge cases |
| 3 | Happy path + edge cases + error scenarios |
| 4 | All categories: functional, edge, error, state, platform |
| 5 | Comprehensive coverage including security tests and race conditions |

### 2. Bug Quality (weight: 2.0)

Are bugs specific, reproducible, and actionable?

| Score | Anchor |
|-------|--------|
| 1 | No bugs found (suspicious) or bugs are vague |
| 2 | Bugs described but missing file/line references |
| 3 | Bugs with description, severity, and file reference |
| 4 | Bugs with reproduction steps and expected vs actual behavior |
| 5 | Bugs with root cause analysis and suggested fix |

### 3. Test Code Quality (weight: 1.5)

Are written tests meaningful, not just boilerplate?

| Score | Anchor |
|-------|--------|
| 1 | No tests written |
| 2 | Trivial tests (existence checks only) |
| 3 | Meaningful assertions on core behavior |
| 4 | Tests cover multiple scenarios with good assertions |
| 5 | Tests are maintainable, well-structured, and cover edge cases |

### 4. Regression Verification (weight: 1.5)

Was the existing test suite run and verified?

| Score | Anchor |
|-------|--------|
| 1 | No regression check |
| 2 | Mentioned but not actually run |
| 3 | Run with results reported |
| 4 | Run with any failures analyzed |
| 5 | Run, analyzed, and any regressions traced to specific changes |

### 5. Verdict Justification (weight: 1.0)

Is the PASS/BLOCK verdict well-justified?

| Score | Anchor |
|-------|--------|
| 1 | Verdict without reasoning |
| 2 | Brief reasoning |
| 3 | Verdict tied to specific test results |
| 4 | Verdict with risk assessment for remaining issues |
| 5 | Verdict with clear criteria and confidence level |

## Grading

```
Max possible = 5 * (2+2+1.5+1.5+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
