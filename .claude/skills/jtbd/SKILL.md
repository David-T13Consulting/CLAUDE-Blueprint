---
name: jtbd
description: Use when analyzing user motivation, writing user stories, or distinguishing the "job" from the solution. Provides the Jobs-to-Be-Done framework and 8-step job map. Referenced by researcher and designer subagents.
---

# Jobs-to-Be-Done (JTBD) Framework

Source: Christensen, Hall, Dillon, Duncan — "Know Your Customers' 'Jobs to Be Done'" (HBR, 2016). Ulwick — *Jobs to Be Done: Theory to Practice* (2016).

## Core Principle

Users don't buy products — they hire them to do a job. The job is stable; the solution is not. Focus on the job to find durable insight.

**Wrong question:** "What do users want?"
**Right question:** "What job are they trying to get done when they encounter this problem?"

## Core Job Statement Format

```
When [situation/trigger],
I want to [motivation/functional goal],
So I can [desired outcome].
```

**Example:**
```
When I'm planning what to plant next season,
I want to know which vegetables grow well in my climate and schedule,
So I can avoid wasting money on plants that fail.
```

Rules:
- Situation is specific (not "when I'm gardening" — too broad)
- Motivation is functional (not emotional — that's a related job)
- Outcome is measurable or observable

## Functional vs. Emotional vs. Social Jobs

Every core job has three dimensions. All matter:

| Dimension | Question | Example |
|-----------|----------|---------|
| **Functional** | What task is getting done? | Track which plants to water |
| **Emotional** | How do they want to feel? | Confident, not anxious about killing plants |
| **Social** | How do they want to be perceived? | Like a competent gardener |

Design primarily for the functional job. Delight through the emotional and social dimensions.

## The 8-Step Job Map

Map how the user accomplishes the job today. For each step, identify the current solution and opportunity level.

| Step | Question | What to Capture |
|------|----------|----------------|
| **1. Define** | How does the user determine what they need? | Inputs, mental models, success criteria |
| **2. Locate** | How do they find the resources/information needed? | Search behavior, trusted sources |
| **3. Prepare** | What setup is required before the core action? | Configuration, prerequisites, context |
| **4. Confirm** | How do they verify they're ready to proceed? | Checkpoints, second opinions |
| **5. Execute** | How do they perform the core action? | The actual task being done |
| **6. Monitor** | How do they track progress or status? | Feedback loops, indicators |
| **7. Modify** | How do they adjust when something goes wrong? | Error recovery, course correction |
| **8. Conclude** | How do they know the job is done? | Completion signal, satisfaction check |

### Job Map Template

```
JOB: [Core job statement]

Step 1 — Define
  Current: [how user defines what they need today]
  Pain:    [what's broken about this]
  Opportunity: [HIGH / MEDIUM / LOW]

Step 2 — Locate
  Current: [how user finds resources today]
  Pain:    [what's broken about this]
  Opportunity: [HIGH / MEDIUM / LOW]

[... repeat for steps 3-8]

HIGHEST OPPORTUNITY STEPS: [list the 2-3 steps with the most pain]
```

## Outcome-Driven Innovation (Ulwick)

For each step in the job map, identify desired outcomes using this format:

```
[Direction] + [metric/object] + [context]
```

Examples:
- "Minimize the time it takes to identify which plants to water today"
- "Reduce the likelihood of accidentally overwatering drought-tolerant plants"
- "Increase the accuracy of harvest timing predictions"

Then score each outcome on a 2×2 matrix:

| | Low Importance | High Importance |
|---|---|---|
| **Satisfied** | Over-served (ignore) | Table stakes (must have) |
| **Unsatisfied** | Ignore | **Opportunity (build this)** |

High importance + low satisfaction = the opportunity space. This is where innovation wins.

## JTBD vs. Traditional Personas

| Personas | JTBD |
|----------|------|
| "Sarah, 35, busy mom" | "When I can't remember my last watering, I want to know instantly so I don't stress" |
| Based on demographics | Based on situations and motivations |
| Encourages stereotyping | Encourages context-thinking |
| Describes the user | Describes the behavior |
| Gets stale | Stays relevant as long as the job exists |

Use JTBD when you want to understand *why* users behave as they do. Use personas only as a communication shorthand after JTBD analysis is done.

## Writing JTBD-Informed User Stories

Upgrade the standard user story format:

**Standard (weak):**
```
As a user, I want to see my plants, so I can water them.
```

**JTBD-informed (strong):**
```
As a home gardener who struggles to remember watering schedules,
When I open the app in the morning before leaving for work,
I want to immediately see which plants need attention today,
So that I can take action in under 2 minutes and not worry about it all day.

Acceptance criteria:
  - Today's care list is visible without any navigation on app open
  - List updates in real time when I mark a plant as watered
  - Empty state ("All done for today!") is just as clear as a populated list
  - Works offline (I may not have WiFi in my garden)
```

## Evidence Standards

JTBD findings must be labeled by evidence tier:

| Tier | Source | Label |
|------|--------|-------|
| T1 — Primary | User interviews, contextual inquiry | "Observed in N user interviews" |
| T2 — Secondary | Published research, validated surveys | "Source: [citation]" |
| T3 — Proxy | App store reviews, forum posts | "Inferred from [N] reviews on [platform]" |
| T4 — Inference | Pattern-matched from training data | "Inference — validate before committing" |

T4 JTBD analysis is a hypothesis. Never present it as validated insight.
