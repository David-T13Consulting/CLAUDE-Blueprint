# Eval Rubric: QA Output

> Scores `/qa` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Test Coverage Breadth (weight: 2.0)

Does the test plan follow the testing pyramid with appropriate distribution?

| Score | Anchor |
|-------|--------|
| 1 | Only happy path tested |
| 2 | Happy path + a few edge cases, no pyramid awareness |
| 3 | Testing pyramid followed: unit (70%), integration (20%), E2E (10%) with all categories covered |
| 4 | Full pyramid + accessibility tests (jest-axe) + security edge cases + state transition tests |
| 5 | Comprehensive coverage including race conditions, flaky test prevention, and exploratory testing notes |

### 2. Bug Quality (weight: 2.0)

Are bugs specific, reproducible, and actionable with root cause analysis?

| Score | Anchor |
|-------|--------|
| 1 | No bugs found (suspicious) or bugs are vague |
| 2 | Bugs described but missing file/line references or severity |
| 3 | Bugs with description, severity (CRITICAL/HIGH/MEDIUM/LOW), and file:line reference |
| 4 | Bugs with reproduction steps, expected vs actual behavior, and root cause analysis |
| 5 | Bugs with root cause, suggested fix with code, and regression test recommendation |

### 3. Test Code Quality (weight: 1.5)

Are written tests meaningful, properly structured, and maintainable?

| Score | Anchor |
|-------|--------|
| 1 | No tests written |
| 2 | Trivial tests (existence checks only) or poor naming |
| 3 | Meaningful assertions following AAA pattern (Arrange-Act-Assert) with descriptive names |
| 4 | Tests use MSW for HTTP mocking, cover multiple scenarios, proper setup/teardown |
| 5 | Tests are maintainable, use boundary mocking only, include jest-axe accessibility checks, zero flakiness |

### 4. Accessibility Testing (weight: 1.0)

Were accessibility checks performed on new components?

| Score | Anchor |
|-------|--------|
| 1 | No accessibility testing |
| 2 | Mentioned but not executed |
| 3 | jest-axe run on new components, VoiceOver labels verified |
| 4 | jest-axe + touch target sizes measured + contrast ratios checked |
| 5 | Full accessibility test suite: axe violations, labels, targets, Dynamic Type, reduced motion |

### 5. Regression Verification (weight: 1.5)

Was the existing test suite run with failures properly analyzed?

| Score | Anchor |
|-------|--------|
| 1 | No regression check |
| 2 | Mentioned but not actually run |
| 3 | Run with results reported (pass count, fail count) |
| 4 | Run with any failures traced to specific changes (real regression vs. test maintenance) |
| 5 | Run, analyzed, flaky tests identified and quarantined, regressions traced with remediation |

### 6. Verdict Justification (weight: 1.0)

Is the PASS/BLOCK verdict well-justified with clear criteria?

| Score | Anchor |
|-------|--------|
| 1 | Verdict without reasoning |
| 2 | Brief reasoning ("looks good") |
| 3 | Verdict tied to specific test results and bug severity |
| 4 | Verdict with risk assessment, coverage analysis, and confidence level |
| 5 | Verdict with clear pass criteria, accepted risks documented, and testing debt identified |

## Grading

```
Max possible = 5 * (2+2+1.5+1+1.5+1) = 45
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
