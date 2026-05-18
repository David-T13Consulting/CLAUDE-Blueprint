---
name: sus-usability-metrics
description: Use when evaluating usability, estimating SUS scores, assessing cognitive load, or benchmarking feature quality against quantitative thresholds. Provides SUS scoring guide, usability benchmarks (Task Completion Rate, Time on Task, Error Rate, Taps to Value), Sweller's Cognitive Load Theory, Norman's 3 Levels of Emotional Design, and A/B testing readiness checklist. Referenced by ux-validator subagent.
---

# Usability Metrics & SUS Reference

These are quantitative frameworks for measuring and communicating usability. Apply them to produce defensible verdicts, not subjective opinions.

---

## Usability Benchmarks

| Metric | Good | Acceptable | Poor |
|--------|------|-----------|------|
| Task Completion Rate | >90% | 70–90% | <70% |
| Time on Task | <30s | 30–60s | >60s |
| Error Rate | <5% | 5–15% | >15% |
| Taps to Value | ≤3 | 4–5 | >5 |
| SUS Score | >80 | 68–80 | <68 |

**When to apply:** Use these thresholds in validation reports to classify features as GOOD/ACCEPTABLE/POOR on each dimension. A feature with any POOR metric needs a fix before shipping.

---

## System Usability Scale (SUS)

**Source:** Brooke, J. (1996). "SUS: A quick and dirty usability scale." In P. Jordan, B. Thomas, B. Weerdmeester, & I. McClelland (Eds.), *Usability evaluation in industry* (pp. 189–194).

SUS is a 10-question questionnaire scored 0–100. Use it for comparative benchmarking across versions or against competitors. Each item is scored 1–5; the formula normalizes to a 0–100 scale.

### Grade Scale

| Score | Grade | Percentile | Adjective |
|-------|-------|-----------|-----------|
| >80.3 | A | Top 10% | Excellent |
| 68–80.3 | B–C | Above average | Good |
| 51–67 | D | Below average | OK — usability issues exist |
| <51 | F | Bottom 25% | Poor — significant problems |

**Threshold:** 68 is the industry-accepted average. Below 68 = product has meaningful usability problems that reduce adoption.

### SUS Questions (for reference)

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

**Scoring:** Odd questions (1,3,5,7,9): score − 1. Even questions (2,4,6,8,10): 5 − score. Sum all 10, multiply by 2.5.

### Estimating SUS Without a Study

When real users aren't available, estimate by auditing against the 10 heuristics and usability benchmarks:

- 1 heuristic violation → −5 points
- Task completion <90% → −10 points
- Taps to value >3 → −5 points
- No onboarding/empty state → −5 points
- Inconsistency with rest of app → −5 points

Start at 80, apply deductions. Label the result "estimated" in the report.

---

## Sweller's Cognitive Load Theory

**Source:** Sweller, J. (1988). "Cognitive load during problem solving: Effects on learning." *Cognitive Science*, 12(2), 257–285.

Cognitive load is the mental effort required to use a system. Three types:

| Type | Definition | Design Action |
|------|-----------|--------------|
| **Intrinsic** | Complexity inherent to the task | Can't eliminate, only scaffold |
| **Extraneous** | Load caused by poor design | Eliminate — this is the designer's job |
| **Germane** | Load that builds useful mental models | Support and encourage |

**Target:** Minimize extraneous load. If the user is thinking about the interface rather than their goal, extraneous load is too high.

### Extraneous Load Red Flags

Each flag indicates a design problem that adds extraneous cognitive load:

- User must read >2 lines of text to take an action
- >3 simultaneous options without grouping
- Icons without labels (requires learning)
- Different interaction patterns for similar actions (inconsistency)
- Information needed from a previous screen (recall burden)
- Jargon or technical language in UI text
- Dense screen without visual hierarchy
- Error messages that don't tell the user what to do next

**When to apply:** Walk through the feature step by step. Count red flags. >2 red flags = cognitive load audit needed. Report each flag as a named issue (COGNITIVE-001, etc.) with a specific fix.

---

## Norman's 3 Levels of Emotional Design

**Source:** Norman, D.A. (2004). *Emotional Design: Why We Love (or Hate) Everyday Things*. Basic Books.

Users evaluate products on three emotional levels simultaneously. All three must pass for a product to be remembered fondly.

| Level | What It Measures | Validation Method |
|-------|-----------------|-----------------|
| **Visceral** | Immediate sensory reaction — does it look/feel appealing? | Show the screen for 5 seconds. What's the first impression? |
| **Behavioral** | Effectiveness and usability — does it do what the user wants? | Can the user complete the task efficiently without frustration? |
| **Reflective** | Long-term meaning and identity — does the user feel proud using it? | Would the user show this to a friend? Do they feel competent? |

**Design implication:** A product can be functionally correct (behavioral pass) but fail viscerally (ugly, cold) or reflectively (embarrassing to use). All three levels shape word-of-mouth and retention.

**Delight requirement:** Every feature must have at least one moment that triggers positive visceral or reflective response. No delight = memorable for the wrong reasons (Peak-End Rule: see `interaction-laws` skill).

---

## A/B Testing Readiness Checklist

Before running an A/B test on a UX change, verify these conditions. Testing a change that fails this checklist produces unreliable results.

| Condition | Check | Why It Matters |
|-----------|-------|---------------|
| **Sample size** | Calculate minimum N before starting | Underpowered tests produce false negatives |
| **Single variable** | Only one element differs between A and B | Multiple changes = can't attribute the result |
| **Success metric pre-defined** | Metric chosen before seeing data | Post-hoc metric selection = p-hacking |
| **Duration pre-defined** | Test runs for full weeks (eliminates day-of-week bias) | Stopping early when "good" = peeking bias |
| **No contamination** | Users don't switch between A and B | Mixed exposure = corrupted results |
| **Statistical significance** | p < 0.05 (95% confidence) before deciding | Don't ship based on noise |
| **Practical significance** | Effect size matters, not just significance | A 0.1% improvement isn't worth shipping |

### Minimum Sample Size Formula

```
n = (Z² × p × (1−p)) / E²

Z = 1.96 (95% confidence)
p = baseline conversion rate (estimate)
E = minimum detectable effect (e.g., 0.05 = 5%)
```

For most mobile features: minimum 1,000 users per variant, minimum 7 days.

### When NOT to A/B Test

- Feature is so clearly broken that any change is better
- Sample size would require >3 months to reach
- The change is a bug fix, not a design choice
- The ethical cost of exposing half your users to a broken experience is too high

---

## Think-Aloud Protocol Template

Use this to structure real-user testing sessions. Give to the Product Owner for manual testing.

```
TASK: [exact task to complete — one sentence, no hints]
START POINT: [screen or state to begin from]
SAY ALOUD: "I'm looking at... I think I should... I'm confused about..."

RECORD:
  Time to first action: ___s
  Hesitation points: [where the user paused]
  Wrong turns: [where the user tapped the wrong thing]
  Emotional reactions: [frustration, surprise, delight]
  Completion: yes / no / partial

TESTER DEBRIEF (after task):
  "What was confusing?"
  "What did you expect to happen?"
  "Would you use this feature again?"
```

**Rules:**
- Don't explain the feature before the task
- Don't guide during the task — silence and observe
- Note behavior, not just stated opinion (people say "it's fine" to be polite)

---

## Quick Reference Card

```
User struggling to understand what to do?  → Extraneous cognitive load (Sweller)
Feature looks bad on first glance?         → Visceral level failure (Norman)
Feature works but doesn't delight?         → Missing reflective + germane design (Norman)
SUS estimated below 68?                    → Meaningful usability problems — fix before shipping
Want to test a design change?              → Check A/B testing readiness checklist first
Task completion rate below 90%?            → Redesign the entry point and primary action
More than 5 taps to core value?            → Simplify the flow
```
