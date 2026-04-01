# Eval Rubric: Design Output

> Scores `/design` outputs against quality dimensions.

## Dimensions

### 1. Flow Completeness (weight: 2.0)

Does the design cover the full user journey, not just the happy path?

| Score | Anchor |
|-------|--------|
| 1 | Only happy path shown |
| 2 | Happy path + one alternate state |
| 3 | All major states defined (empty, loading, populated, error) |
| 4 | All states + edge cases + transitions between them |
| 5 | Complete journey map including entry, core, exit, and re-entry |

### 2. State Coverage (weight: 2.0)

Are all UI states for every screen explicitly defined?

| Score | Anchor |
|-------|--------|
| 1 | States not mentioned |
| 2 | Only "populated" state described |
| 3 | Empty, loading, populated, and error states defined |
| 4 | All states + offline + edge cases (max data, first use) |
| 5 | Every state has specific visual treatment, copy, and behavior |

### 3. Interaction Design (weight: 1.5)

Are interactions specific enough to implement without guessing?

| Score | Anchor |
|-------|--------|
| 1 | No interaction details |
| 2 | Basic tap actions described |
| 3 | Trigger, action, and feedback defined for core interactions |
| 4 | Micro-interactions, animations, and timing specified |
| 5 | Full interaction spec with gesture handling, edge behaviors |

### 4. Accessibility Specification (weight: 1.5)

Are accessibility requirements explicitly defined, not just mentioned?

| Score | Anchor |
|-------|--------|
| 1 | No accessibility mentioned |
| 2 | "Should be accessible" — no specifics |
| 3 | Screen reader labels and touch targets specified |
| 4 | Labels, targets, contrast, Dynamic Type, and reduce motion |
| 5 | Full a11y spec with specific label text and testing instructions |

### 5. Benchmark Alignment (weight: 1.0)

Does the design feel native and modern, matching top-tier apps?

| Score | Anchor |
|-------|--------|
| 1 | Looks like a prototype or wireframe |
| 2 | Functional but generic |
| 3 | Clean and usable |
| 4 | Feels polished and intentional |
| 5 | Would feel at home next to iMessage/ChatGPT/Apple Notes |

## Grading

```
Max possible = 5 * (2+2+1.5+1.5+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
