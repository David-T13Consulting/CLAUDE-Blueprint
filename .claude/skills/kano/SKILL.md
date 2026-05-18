---
name: kano
description: Use when prioritizing features, scoping an MVP, or classifying what users expect vs. what delights them. Provides the Kano Model framework with classification rules and MVP scoping guidance.
---

# Kano Model for Feature Prioritization

Source: Kano, Seraku, Takahashi, Tsuji — "Attractive Quality and Must-Be Quality" (Journal of the Japanese Society for Quality Control, 1984).

## Core Principle

Not all features deliver satisfaction equally. Some features hurt when absent (but don't impress when present). Others delight when present (but aren't missed when absent). Kano classifies features by the relationship between their presence and user satisfaction.

## The 5 Categories

| Category | Absent | Present | Strategy |
|----------|--------|---------|----------|
| **Must-have** (Basic) | Extreme dissatisfaction | Neutral (expected, unnoticed) | Ship first. Non-negotiable. |
| **Performance** (Linear) | Proportional dissatisfaction | Proportional satisfaction | More = better. Compete here. |
| **Excitement** (Delighter) | Neutral (unnoticed) | Delight and surprise | Differentiates. Don't announce — let users discover. |
| **Indifferent** | Neutral | Neutral | Cut from v1. Users don't care. |
| **Reverse** | Some users prefer absence | Subset is actively unhappy | Avoid or make optional. |

### Must-Have (Basic Quality)

Users expect these. When absent: rage, app store 1-stars, churn. When present: "of course it has this."

Examples:
- App doesn't crash
- Can undo a destructive action
- Data isn't lost between sessions

**Rule:** You cannot delight users on Performance or Excitement features until Must-haves are covered. Fix these first — always.

### Performance (Linear Quality)

More is more. Users notice and appreciate improvements. Competition often happens here.

Examples:
- Faster search results
- More plant species in the database
- More accurate weather forecasts

**Rule:** When you need to differentiate on an established feature, invest in Performance quality. Every incremental improvement counts.

### Excitement (Attractive Quality)

Users don't ask for these. They don't know they want them. But when present: delight, word-of-mouth, sharing. The "wow" moment.

Examples:
- AI identifies a plant disease from a photo
- App celebrates a plant's anniversary with the user
- Weekly summary shows plants saved vs. last month

**Rules:**
- Don't announce Excitement features — let users discover them
- One well-executed Excitement feature > five mediocre ones
- Excitement features decay: they become Must-haves or Indifferent over time as users get used to them (the Kano saturation effect)

### Indifferent

Users don't care either way. Building these is waste.

Examples:
- Customizable app icon color
- Sorting direction preference
- "About us" page details

**Rule:** Ruthlessly eliminate Indifferent features from v1. Time spent on Indifferent is time stolen from Must-haves.

### Reverse

A feature that satisfies some users while actively upsetting others. Usually a philosophical design choice.

Examples:
- Gamification mechanics (some users love streaks; others find them infantilizing)
- Push notification frequency (some want daily; others want opt-out entirely)
- Social sharing features (some want them; others are private)

**Rule:** If a feature is Reverse for a significant user segment, either make it optional or eliminate it.

## How to Classify a Feature

### Method 1: Functional-Dysfunctional Survey (Kano Questionnaire)

For each feature, ask two questions:
1. **Functional:** "How would you feel if this feature WAS present?"
2. **Dysfunctional:** "How would you feel if this feature was NOT present?"

Options: "I like it" / "I expect it" / "I'm neutral" / "I can tolerate it" / "I dislike it"

Use the evaluation matrix to map answer pairs to categories.

### Method 2: Inference from Evidence (without a survey)

When you don't have survey data, classify using evidence:

| Evidence | Category |
|----------|----------|
| App store 1-star reviews mention its absence | Must-have |
| Competitor feature with explicit user praise in reviews | Performance |
| Viral moment when a product does something unexpected | Excitement |
| Feature exists in many apps but no one mentions it | Indifferent |
| Feature exists but users in reviews ask for it to be optional | Reverse |

Always label evidence tier (T1-T4 from JTBD framework).

## MVP Scoping Rule

```
MVP = All Must-haves
    + Top 1-2 Performance features (your competitive differentiator)
    + 1 Excitement feature (your delight moment)
    - All Indifferent features
    - Reverse features (or make optional)
```

### Example MVP Decision

```
FEATURE CLASSIFICATION: [Product Name]

Must-have (required for v1):
  - User can add a plant with name and photo
  - App remembers watering schedule
  - Notifications fire on time

Performance (ship the best one):
  - Plant database size [CHOSE THIS — 10,000+ species at launch]
  - Watering schedule accuracy
  - Photo recognition accuracy

Excitement (ship one):
  - AI plant doctor (identify disease from photo) [CHOSE THIS]
  - Plant family tree visualization
  - Community plant sharing

Indifferent (cut):
  - Dark mode customization
  - Widget color themes
  - Sorting preferences

Reverse (optional or cut):
  - Gamification streaks [make optional — 40% of users dislike them]
```

## Kano Over Time (Saturation Effect)

Features migrate categories:

```
Excitement → Performance → Must-have

Example: Mobile banking app
1995: "View balance on phone" = Excitement (wow!)
2005: "Mobile balance" = Performance (better than competitor = better)
2015: "Mobile balance" = Must-have (no one downloads an app without this)
```

**Implication:** Yesterday's differentiator is tomorrow's table stakes. Continuously add new Excitement features to stay ahead.

## Integration with Other Frameworks

**With JTBD:** Kano classifies features; JTBD explains why. A Must-have feature exists because it's essential to executing the functional job. An Excitement feature may address a latent emotional or social job the user didn't articulate.

**With MVP Brief:** Kano classification IS the scoping framework. The "Out of Scope (v1)" section of the MVP Brief should map directly to Indifferent and Reverse features.

**With Backlog:** Label every backlog item with its Kano category. Must-haves get priority queued. Excitement features get scheduled strategically. Indifferent features get removed.
