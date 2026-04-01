# Human Eval Rubric: AI Output Quality

> Scores the system's outputs at each approval gate.
> Used BY the Product Owner to evaluate whether the AI's work is actually good —
> not just formatted correctly, but substantively valuable and trustworthy.
> Applies the same 1-5 weighted scoring as system rubrics.
> Version: 1.0

---

## When to Use This

Score the system's output **at each gate before approving**. Not every dimension applies at every gate — use the gate-specific sections below.

| Gate | What You're Scoring | Dimensions to Use |
|------|--------------------|--------------------|
| Gate 1: Proceed? | Research output | 1, 2, 3, 4, 5, 6 |
| Gate 2: Build? | Design output | 1, 2, 3, 4, 7, 8 |
| Gate 3: Approach? | Architecture output | 1, 2, 3, 4, 9, 10 |
| Gate 4: Ship? | QA + Security + Validate + Perf reports | 1, 2, 3, 4, 11, 12 |

Dimensions 1-4 are **universal** (apply at every gate). Dimensions 5-12 are **gate-specific**.

---

## Universal Dimensions (Every Gate)

### 1. Substance vs. Filler (weight: 2.0)

Does the output contain real, actionable insight — or is it padded with generic statements anyone could write without context?

| Score | Anchor |
|-------|--------|
| 1 | Entirely generic. Could apply to any project. No project-specific analysis. |
| 2 | Mostly generic with a few project-specific details sprinkled in. |
| 3 | Mix of generic and specific. Key recommendations are grounded in the actual project. |
| 4 | Predominantly specific. Recommendations reference actual files, user segments, or constraints unique to this project. |
| 5 | Every statement is grounded in specifics. No filler. Could not be copy-pasted to another project without heavy editing. |

### 2. Honesty & Uncertainty (weight: 2.0)

Does the output clearly distinguish what it knows from what it assumes? Does it flag gaps instead of filling them with confident-sounding guesses?

| Score | Anchor |
|-------|--------|
| 1 | Presents assumptions as facts. No uncertainty flagged. Fabricates data or sources. |
| 2 | Mostly confident tone. Assumptions exist but aren't labeled. May cite frameworks without applying them. |
| 3 | Some assumptions labeled. Key unknowns acknowledged. Mostly honest but occasionally overconfident. |
| 4 | Clear distinction between facts and assumptions. Unknowns flagged with impact assessment. Recommendations qualified appropriately. |
| 5 | Every claim is sourced or labeled as an assumption. Unknowns have explicit "what I'd need to verify" notes. Zero fabrication. Comfortable saying "I don't know." |

### 3. Actionability (weight: 1.5)

Can you act on this output immediately, or do you need to ask follow-up questions to understand what it's actually recommending?

| Score | Anchor |
|-------|--------|
| 1 | Vague observations with no clear recommendation. "Consider doing X" without specifics. |
| 2 | Recommendations exist but lack specifics (no file paths, no concrete steps, no priority). |
| 3 | Clear recommendations with some specifics. You could act on most of them without follow-up. |
| 4 | Concrete, prioritized recommendations. Includes specific files, components, or steps. Trade-offs stated. |
| 5 | Every recommendation is immediately actionable with zero ambiguity. Includes priority, effort estimate, trade-offs, and what to do if the recommendation is rejected. |

### 4. Correctness (weight: 2.0)

Based on what you know about your product, users, and market — is the output actually right? Does it match reality?

| Score | Anchor |
|-------|--------|
| 1 | Fundamentally wrong. Misunderstands the problem, the user, or the technical constraints. |
| 2 | Partially wrong. Gets the broad strokes but makes incorrect assumptions about key details. |
| 3 | Mostly correct. Minor inaccuracies that wouldn't derail the project but should be corrected. |
| 4 | Correct on all major points. Any inaccuracies are in edge cases or low-impact areas. |
| 5 | Fully correct. Matches your understanding of the problem, users, and constraints. Surfaces things you hadn't considered that turn out to be right. |

---

## Gate 1: Research Output

### 5. Evidence Quality (weight: 1.5)

Does the research cite real evidence, or is it pattern-matching from training data presented as research?

| Score | Anchor |
|-------|--------|
| 1 | No evidence. Claims are unsupported assertions. "Users want X" with no basis. |
| 2 | Generic evidence. "Studies show..." without specific citations. Competitors mentioned but not analyzed. |
| 3 | Some real evidence. Competitor analysis with specific features/pricing. Market sizing with stated methodology. |
| 4 | Strong evidence. Sources cited with dates. Evidence tiers labeled (T1-T4). Gaps in evidence explicitly flagged. |
| 5 | Rigorous evidence. Primary sources where available. Every claim traceable. Conflicting evidence presented fairly. Clear distinction between T1 (interviews) and T4 (inference). |

### 6. Problem Understanding (weight: 1.5)

Does the research demonstrate genuine understanding of the problem and user, or surface-level restatement of what you already told it?

| Score | Anchor |
|-------|--------|
| 1 | Restates the problem brief back to you with no new insight. |
| 2 | Adds some context but nothing you didn't already know. User stories are generic. |
| 3 | Identifies non-obvious aspects of the problem. User stories reflect specific user contexts. JTBD job statements are present. |
| 4 | Deepens your understanding. Identifies user segments you hadn't considered. Maps the job (8 steps). Kano classification of features is plausible. |
| 5 | Changes how you think about the problem. Surfaces constraints, competing behaviors, or market dynamics that reshape your approach. Evidence-backed insights you could not have generated yourself. |

---

## Gate 2: Design Output

### 7. Design Completeness (weight: 1.5)

Does the design cover all states and scenarios, or just the happy path screenshot?

| Score | Anchor |
|-------|--------|
| 1 | Only the happy path. One state shown. No error, empty, loading, or offline treatment. |
| 2 | Happy path + 1-2 additional states. Missing several critical states. |
| 3 | Most states covered (empty, loading, populated, error). Offline and edge cases may be thin. |
| 4 | All 7 states addressed (empty, loading, populated, error, offline, edge, first-use). Micro-interactions defined. |
| 5 | All states with transitions between them mapped. Edge cases are specific to this feature, not generic. Accessibility annotations included. Behavioral economics principles applied and cited. |

### 8. Design Taste (weight: 1.5)

This is the subjective dimension only you can score. Does the design feel right for your product and users?

| Score | Anchor |
|-------|--------|
| 1 | Feels wrong. Doesn't match the product's personality or users' expectations. |
| 2 | Functional but generic. Could be any app. No distinctive character. |
| 3 | Solid design that fits the product. Nothing jarring, but nothing delightful either. |
| 4 | Feels right. Matches the product's personality. You'd be comfortable showing it to users. |
| 5 | Feels better than what you imagined. Has a moment of delight. You're excited to build it. Passes the benchmark ("would this feel at home next to iMessage or ChatGPT?"). |

---

## Gate 3: Architecture Output

### 9. Technical Soundness (weight: 1.5)

Does the architecture make sound technical decisions, or does it over-engineer, under-engineer, or follow patterns blindly?

| Score | Anchor |
|-------|--------|
| 1 | Fundamentally flawed. Will not scale, has circular dependencies, or violates basic principles. |
| 2 | Works but fragile. Tightly coupled. Missing error handling strategy. Patterns chosen without justification. |
| 3 | Solid fundamentals. Architecture pattern justified. Separation of concerns is clean. Error types defined. |
| 4 | Well-designed. Caching strategy with TTLs. Testing pyramid specified. Security layers defined. Trade-offs between alternatives explicitly stated. |
| 5 | Elegant. Minimal complexity for the requirements. Every decision has a "why not the alternative" justification. Failure modes mapped. Could hand this to a senior engineer and they'd agree with every choice. |

### 10. Proportionality (weight: 1.0)

Is the architecture appropriately sized for the problem, or is it over-engineered for an MVP / under-engineered for a critical system?

| Score | Anchor |
|-------|--------|
| 1 | Massive over-engineering (microservices for a todo app) or dangerous under-engineering (no auth on a payment system). |
| 2 | Noticeably mismatched to the problem scope. Adds abstractions that won't be needed for years, or skips protections that are needed now. |
| 3 | Roughly proportional. Minor over/under-engineering in specific areas. |
| 4 | Well-matched. Complexity is justified by requirements. Nothing speculative, nothing missing. |
| 5 | Perfectly calibrated. You couldn't remove anything without losing capability or add anything without adding waste. Matches the current pipeline mode (EXPLORE/BUILD/SCALE). |

---

## Gate 4: Validation Reports

### 11. Coverage (weight: 1.5)

Do the QA, Security, Validate, and Perf reports actually cover what matters, or do they test the easy things and skip the hard ones?

| Score | Anchor |
|-------|--------|
| 1 | Reports are shallow. Happy path only. Major attack surfaces, edge cases, or performance scenarios untested. |
| 2 | Some coverage of non-happy paths, but the hard scenarios (offline, race conditions, prompt injection, memory leaks) are missing. |
| 3 | Good coverage of common scenarios. Most OWASP checks present. Accessibility basics covered. Performance budgets checked. |
| 4 | Thorough coverage. Edge cases specific to this feature tested. STRIDE threat model applied. WCAG 2.2 checks present. Cost analysis for AI features included. |
| 5 | Exhaustive and creative. Tests scenarios you hadn't thought of. Security audit finds non-obvious attack vectors. QA catches state transition bugs. Performance identifies hidden cost drivers. |

### 12. Verdict Trustworthiness (weight: 1.0)

Do you trust the PASS/BLOCK verdicts? Would a false PASS here put users at risk?

| Score | Anchor |
|-------|--------|
| 1 | Verdicts feel arbitrary. PASS given despite obvious issues. No confidence in the assessment. |
| 2 | Verdicts are directionally correct but reasoning is thin. You'd want to verify independently. |
| 3 | Verdicts are reasonable and well-reasoned. Minor concerns about completeness. |
| 4 | Verdicts are well-supported with evidence. BLOCK verdicts include specific remediation steps. You'd act on these without second-guessing. |
| 5 | Verdicts are rigorous. PASS verdicts explicitly state what was verified. BLOCK verdicts are precise (not just "needs work" but "file X, line Y, because Z"). You'd ship based on a PASS with full confidence. |

---

## Grading

### Per-Gate Scoring

**Gate 1** (dims 1-6): `Max = 5 * (2+2+1.5+2+1.5+1.5) = 52.5`
**Gate 2** (dims 1-4, 7-8): `Max = 5 * (2+2+1.5+2+1.5+1.5) = 52.5`
**Gate 3** (dims 1-4, 9-10): `Max = 5 * (2+2+1.5+2+1.5+1) = 50`
**Gate 4** (dims 1-4, 11-12): `Max = 5 * (2+2+1.5+2+1.5+1) = 50`

```
Percentage = weighted_total / gate_max * 100

>= 80%: STRONG  — Output is genuinely valuable. Approve with confidence.
60-79%: ADEQUATE — Output is usable but has gaps. Approve with noted concerns, or request a re-run on weak dimensions.
40-59%: WEAK    — Output needs significant improvement. Do not approve. Send back with specific feedback.
< 40%:  FAIL    — Output is not trustworthy. Re-run the skill with clearer inputs, or flag a systemic issue.
```

### What To Do With Scores

| Score | Action |
|-------|--------|
| STRONG | Approve the gate. Note what worked well (helps calibrate future sessions). |
| ADEQUATE | Approve if deadline-pressured. Otherwise, tell the system which dimensions scored low and why — it will re-run. |
| WEAK | Do not approve. Provide specific feedback: "Evidence quality was a 2 because [X]. I need [Y] before proceeding." |
| FAIL | Stop and diagnose. Is the problem brief unclear? Is the system missing context? Is this the wrong tool for the job? |

### Tracking Over Time

Keep a simple log (even just a note) of your gate scores per feature:

```
Feature: [name]
Gate 1: 78% (ADEQUATE) — evidence was T3/T4 heavy, pushed for real user data
Gate 2: 85% (STRONG)
Gate 3: 72% (ADEQUATE) — over-engineered caching for MVP, asked to simplify
Gate 4: 88% (STRONG)
```

Patterns to watch:
- **Consistently low on dimension 2 (Honesty)**: The system is overconfident. Add "flag all assumptions explicitly" to your prompts.
- **Consistently low on dimension 4 (Correctness)**: The system lacks context. Provide more domain knowledge or create domain files.
- **One gate always weaker**: That skill may need tuning or the inputs to that phase are insufficient.
- **Scores trending down over a session**: Context fatigue. Consider starting a fresh session.
