# Eval Rubric: UX Validation Output

> Scores `/validate` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. First-Time Experience Analysis (weight: 2.0)

Is the first-use experience genuinely evaluated with quantitative metrics?

| Score | Anchor |
|-------|--------|
| 1 | Not evaluated |
| 2 | "Looks intuitive" — no real analysis |
| 3 | Entry point clarity, first-action clarity, and taps-to-value measured |
| 4 | Full first-use walkthrough with hesitation points, task completion rate estimate, and SUS score |
| 5 | First-use analysis with benchmark comparison, think-aloud protocol provided, and cognitive load assessment |

### 2. Accessibility Rigor (weight: 2.0)

Are WCAG 2.2 AA checks specific and verifiable, not just checkboxes?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "Should be accessible" — no specifics |
| 3 | VoiceOver labels, touch targets (44pt), and contrast ratios (4.5:1) checked |
| 4 | Full WCAG 2.2 AA checklist: labels, targets, contrast, Dynamic Type, reduce motion, focus visibility, target size, dragging alternatives |
| 5 | Specific a11y issues with exact elements, measurements, fix instructions, and WCAG success criteria references |

### 3. Feedback Completeness (weight: 1.5)

Is every user action verified to have appropriate feedback with timing?

| Score | Anchor |
|-------|--------|
| 1 | Not checked |
| 2 | "Loading states present" — no detail |
| 3 | Tap feedback, loading, error, and success states verified with present/absent status |
| 4 | All states verified with timing (Doherty Threshold: <400ms, <1s, <10s), specific observations per action |
| 5 | Feedback verified + gaps identified + enhancement suggestions (haptics, animations, micro-interactions) |

### 4. Cognitive Load Assessment (weight: 1.5)

Is cognitive load evaluated using established frameworks?

| Score | Anchor |
|-------|--------|
| 1 | Not evaluated |
| 2 | "Seems simple enough" — no framework |
| 3 | Hick's Law violations identified (too many choices) and recall burdens flagged |
| 4 | Intrinsic, extraneous, and germane load assessed; specific screens with excessive load identified |
| 5 | Full cognitive load analysis with Sweller's framework, specific reduction recommendations, and before/after comparison |

### 5. Emotional Tone & Delight (weight: 1.0)

Is the copy and tone genuinely evaluated for humanity and Peak-End Rule?

| Score | Anchor |
|-------|--------|
| 1 | Not evaluated |
| 2 | "Tone seems fine" |
| 3 | Error messages and key copy reviewed for tone (human vs. robotic) |
| 4 | Full copy review with specific improvements, delight moment identified or recommended |
| 5 | Don Norman's 3 levels (visceral, behavioral, reflective) evaluated, Peak-End delight designed |

### 6. Consistency & Benchmarking (weight: 1.0)

Is the feature verified against existing app patterns and benchmark apps?

| Score | Anchor |
|-------|--------|
| 1 | Not checked |
| 2 | "Looks consistent" — no specifics |
| 3 | Color, spacing, typography, and icons verified against design system |
| 4 | Full pattern verification + benchmark comparison vs. reference apps (ChatGPT, iMessage, etc.) |
| 5 | Comparative benchmark table with scores, A/B testing readiness verified, testing materials provided |

## Grading

```
Max possible = 5 * (2+2+1.5+1.5+1+1) = 45
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
