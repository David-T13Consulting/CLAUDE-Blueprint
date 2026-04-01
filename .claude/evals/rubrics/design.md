# Eval Rubric: Design Output

> Scores `/design` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Flow Completeness (weight: 2.0)

Does the design cover the full user journey, not just the happy path?

| Score | Anchor |
|-------|--------|
| 1 | Only happy path shown |
| 2 | Happy path + one alternate state |
| 3 | All major states defined (empty, loading, populated, error, offline) |
| 4 | All states + edge cases + transitions + back-flows (error → retry, cancel → return) |
| 5 | Complete journey map including entry, core, exit, re-entry, and information architecture |

### 2. Heuristic Compliance (weight: 2.0)

Are Nielsen's 10 heuristics explicitly checked and addressed?

| Score | Anchor |
|-------|--------|
| 1 | No heuristic analysis |
| 2 | Vague reference to "usability" without specific heuristics |
| 3 | 5+ heuristics checked with pass/fail status |
| 4 | All 10 heuristics checked with specific evidence per screen |
| 5 | Full heuristic audit table with all 10 PASS, plus behavioral design principles identified |

### 3. Interaction Design Specificity (weight: 1.5)

Are interactions grounded in design laws (Fitts's, Hick's, Miller's) with quantitative specs?

| Score | Anchor |
|-------|--------|
| 1 | No interaction details |
| 2 | Basic tap actions described without timing or sizing |
| 3 | Trigger, action, feedback defined with animation durations and easing |
| 4 | Interactions cite Fitts's Law (target sizes), Hick's Law (choice reduction), with timing specs |
| 5 | Full interaction spec with gesture handling, edge behaviors, reduced-motion alternatives, and Doherty Threshold compliance |

### 4. Accessibility Specification (weight: 2.0)

Are WCAG 2.2 AA requirements explicitly checked, not just mentioned?

| Score | Anchor |
|-------|--------|
| 1 | No accessibility mentioned |
| 2 | "Should be accessible" — no specifics |
| 3 | VoiceOver labels, touch targets (44pt), and contrast ratios specified |
| 4 | Labels, targets, contrast, Dynamic Type, reduce motion, focus visibility, target size (WCAG 2.5.8) |
| 5 | Full WCAG 2.2 AA checklist with specific label text, contrast measurements, and testing instructions per component |

### 5. Visual Design Quality (weight: 1.0)

Does the design follow platform conventions and design system tokens?

| Score | Anchor |
|-------|--------|
| 1 | No visual specification |
| 2 | Generic descriptions ("looks good") |
| 3 | Colors, typography, and spacing reference DESIGN_SYSTEM.md |
| 4 | Platform-specific guidelines followed (iOS HIG/Material), 4pt/8pt grid, modular type scale |
| 5 | Liquid Glass effects, semantic colors, SF Symbols, platform-native feel verified against benchmark apps |

### 6. Behavioral Design (weight: 1.0)

Are behavioral economics principles consciously applied with ethical boundaries?

| Score | Anchor |
|-------|--------|
| 1 | No behavioral design awareness |
| 2 | Implicit behavior patterns without naming |
| 3 | 1-2 principles named and applied (default bias, social proof) |
| 4 | 3+ principles applied with ethical boundary checks, dark patterns flagged and removed |
| 5 | Comprehensive behavioral audit: defaults, anchoring, Peak-End Rule, completion bias — all with citations and ethical limits |

## Grading

```
Max possible = 5 * (2+2+1.5+2+1+1) = 47.5
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
