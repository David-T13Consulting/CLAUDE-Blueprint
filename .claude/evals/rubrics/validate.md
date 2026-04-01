# Eval Rubric: UX Validation Output

> Scores `/validate` outputs against quality dimensions.

## Dimensions

### 1. First-Time Experience Analysis (weight: 2.0)

Is the first-use experience genuinely evaluated from a naive user's perspective?

| Score | Anchor |
|-------|--------|
| 1 | Not evaluated |
| 2 | "Looks intuitive" — no real analysis |
| 3 | Entry point clarity and taps-to-value measured |
| 4 | Full first-use walkthrough with hesitation points identified |
| 5 | First-use analysis with comparison to onboarding best practices |

### 2. Accessibility Rigor (weight: 2.0)

Are accessibility checks specific and verifiable, not just checkboxes?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "Should be accessible" — no specifics |
| 3 | VoiceOver labels and touch targets checked |
| 4 | Labels, targets, contrast ratios, Dynamic Type, reduce motion |
| 5 | Specific a11y issues with exact elements and fix instructions |

### 3. Feedback Completeness (weight: 1.5)

Is every user action verified to have appropriate feedback?

| Score | Anchor |
|-------|--------|
| 1 | Not checked |
| 2 | "Loading states present" — no detail |
| 3 | Tap feedback, loading, error, and success states verified |
| 4 | All states verified with specific observations per action |
| 5 | Feedback verified + suggestions for enhancement (haptics, animations) |

### 4. Emotional Tone (weight: 1.0)

Is the copy and tone genuinely evaluated for humanity and empathy?

| Score | Anchor |
|-------|--------|
| 1 | Not evaluated |
| 2 | "Tone seems fine" |
| 3 | Error messages and key copy reviewed for tone |
| 4 | Full copy review with specific improvement suggestions |
| 5 | Delight moments identified or recommended with specific examples |

### 5. Consistency Check (weight: 1.5)

Is the feature verified against existing app patterns?

| Score | Anchor |
|-------|--------|
| 1 | Not checked |
| 2 | "Looks consistent" — no specifics |
| 3 | Color, spacing, and typography verified against design system |
| 4 | Full pattern verification including icons, animations, and interactions |
| 5 | Inconsistencies cataloged with specific file:line references |

## Grading

```
Max possible = 5 * (2+2+1.5+1+1.5) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
