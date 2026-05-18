---
name: interaction-laws
description: Use when specifying interaction design, sizing touch targets, limiting choices, or evaluating cognitive load. Provides Fitts's Law, Hick's Law, Miller's Law, Jakob's Law, Doherty Threshold, Postel's Law, and Peak-End Rule with design rules and quantitative constraints. Referenced by designer and ux-validator subagents.
---

# Interaction Design Laws

These laws are not guidelines — they are quantitative models of human behavior. Apply them to produce measurable interaction decisions, not subjective ones.

## Fitts's Law — Target Sizing and Placement

**Source:** Fitts, P.M. (1954). "The information capacity of the human motor system." Journal of Experimental Psychology, 47(6), 381–391.

**Formula:** `T = a + b × log₂(D/W + 1)`

- T = time to acquire a target
- D = distance from starting point to target center
- W = width of the target
- a, b = empirically determined constants

**Plain language:** Movement time increases with distance and decreases with target size. Far + small = slow and error-prone. Close + large = fast and accurate.

**Design rules:**
- **Primary actions:** Large targets (minimum 44×44pt per Apple HIG, 48×48dp per Material 3), positioned in the thumb zone (bottom-center on mobile)
- **Destructive actions:** Small targets, positioned away from primary actions (top-right, secondary menu)
- **Edges and corners:** Infinite effective width — a button flush against a screen edge is easier to tap than one floating in the middle
- **Minimum touch target:** 44×44pt (Apple HIG), 48×48dp (Material 3), 24×24 CSS px (WCAG 2.5.8 minimum)

**When to apply:**
- Specifying button sizes for primary vs. secondary actions
- Positioning actions relative to the thumb zone
- Evaluating whether a target is too small or too far

**Audit question:** Are destructive actions (delete, clear, send irreversible message) smaller and farther from the thumb than primary actions?

---

## Hick's Law — Choice Reduction

**Source:** Hick, W.E. (1952). "On the rate of gain of information." Quarterly Journal of Experimental Psychology, 4(1), 11–26.

**Formula:** `T = b × log₂(n + 1)`

- T = decision time
- n = number of choices
- b = empirically determined constant

**Plain language:** Every additional choice increases decision time logarithmically. Doubling choices doesn't double decision time — but presenting 10 options is meaningfully slower than presenting 3.

**Design rules:**
- **Maximum visible options without grouping/search:** 5–7 (Miller's Law intersection)
- **Navigation menus:** Maximum 5 items at the same level
- **Progressive disclosure:** Show the 3 most common options; put the rest behind "More" or "Advanced"
- **Onboarding:** Present one decision at a time, not all at once
- **Settings screens:** Group related settings; don't present 40 toggles on one screen

**When to apply:**
- Designing navigation structures
- Specifying dropdown or picker contents
- Evaluating whether a screen has too many simultaneous choices

**Audit question:** Can a first-time user immediately identify the primary action, or are they faced with 5+ equally weighted options?

---

## Miller's Law — Working Memory Chunking

**Source:** Miller, G.A. (1956). "The magical number seven, plus or minus two." Psychological Review, 63(2), 81–97.

**Plain language:** Working memory holds approximately 7 ± 2 chunks of information at once. Beyond this, cognitive load increases and recall drops.

**Design rules:**
- **Maximum items per group:** 5–7 (err toward 3–5 for mobile)
- **Navigation sections:** Chunk into groups of 3–5 items with a clear label
- **Ungrouped lists:** Break any list >7 items into sections
- **Progressive disclosure:** Use hierarchy — show summary, reveal details on demand
- **Form fields:** Don't present >5 fields without a visual group break

**When to apply:**
- Designing list screens with many items
- Specifying navigation depth and grouping
- Evaluating whether a screen has too much information density

**Audit question:** Does any single screen require the user to track more than 7 pieces of information simultaneously?

---

## Jakob's Law — Convention Over Innovation

**Source:** Nielsen, J. (2000). "End of Web Design." Nielsen Norman Group. Also: Yablonski, J. — Laws of UX (2020).

**Plain language:** Users spend most of their time on other apps. They build mental models from those apps. If your UI breaks their existing mental model, they have to learn a new one — and most won't bother.

**Design rules:**
- **Navigation:** Use the platform's established patterns (iOS: tab bar at bottom, back swipe, large title; Android: bottom nav or navigation rail, back button)
- **Common actions:** Trash icon = delete, heart/star = favorite, share icon = share — don't invent new icons for established concepts
- **Input patterns:** Text fields, date pickers, toggles — use platform components, not custom ones
- **Gestures:** Swipe-to-dismiss, pull-to-refresh, long-press context menu — these work because users have learned them elsewhere

**When NOT to apply:**
- Your app's core value proposition is a novel interaction model (e.g., swipe-based dating apps)
- The convention is wrong for your use case (but verify this with user testing before departing)

**Innovation budget:** Spend your one departure from convention on the thing that makes your app unique. Use conventions for everything else.

**Audit question:** Does a user who uses iMessage and Apple Notes daily already know how to navigate this feature without learning anything new?

---

## Doherty Threshold — Response Time Perception

**Source:** Doherty, W.J. & Thadani, A.J. (1982). "The economic value of rapid response time." IBM Systems Journal.

**The threshold:** 400ms. Below this, users perceive the system as responding instantly. Above this, they notice the delay.

**Design rules by response time:**

| Response Time | User Perception | Design Action |
|--------------|-----------------|---------------|
| <100ms | Instantaneous | No indicator needed (tap feedback only) |
| 100–400ms | Fast, barely noticeable | Subtle visual state change (opacity, scale) |
| 400ms–1s | Noticeably slow | Spinner, subtle loading indicator |
| 1–10s | Long wait | Skeleton screen or progress bar |
| >10s | Very long, user may abandon | Progress bar + estimated time remaining |

**Optimistic UI:** For operations that almost always succeed, update the UI immediately and roll back if the server returns an error. This keeps perceived performance below 400ms even for network calls.

**AI / LLM specifics:**
- Show thinking indicator immediately on message send (the LLM takes 1–10s)
- Stream tokens as they arrive — first token visible within 1s feels responsive even if completion takes 10s
- Never show a blank screen while waiting for an AI response

**Audit question:** For every async operation in the feature, what does the user see between 0ms and 400ms after initiating the action?

---

## Postel's Law — Liberal Input, Conservative Output

**Source:** Postel, J. (1980). RFC 761 — Transmission Control Protocol. Yablonski, J. — Laws of UX (2020).

**Plain language:** Be liberal in what you accept from users; be strict and consistent in what you produce.

**Design rules:**
- **Input:** Accept multiple formats for the same data (dates: "Jan 5", "1/5/26", "2026-01-05" → all valid), auto-format on input (phone numbers, credit cards)
- **Output:** Always display in a single consistent format (Jan 5, 2026)
- **Don't punish users** for using the wrong format — accept their intent and correct silently
- **Do validate intent** — "banana" as a date is still invalid; Postel's Law is not "accept anything"

**Audit question:** For each user input field, could the same valid data be entered in more than one format? If yes, do we accept all reasonable formats?

---

## Peak-End Rule — Memory of Experiences

**Source:** Kahneman, D., Fredrickson, B.L., Schreiber, C.A., & Redelmeier, D.A. (1993). "When more pain is preferred to less." Psychological Science, 4(6), 401–405.

**Plain language:** People judge an experience primarily by how it felt at its most intense moment (the peak) and how it ended — not by averaging the entire experience.

**Design rules:**
- **Design a peak:** Every feature needs one moment of genuine delight (animation, clever copy, visual reward, unexpected helpfulness). This disproportionately shapes how users remember the feature.
- **Design a good ending:** Completion states matter more than progress states. "All done!" beats "No more items."
- **Reduce pain peaks:** If there's an error or failure, make the recovery as smooth as possible — the failure peak will be remembered.
- **The mundane middle:** The loading spinner and empty states are less important than you think — they don't shape the memory.

**Delight moment examples:**
- Confetti animation on first task completed
- Personalized "Good morning, [name]" on daily open
- Plant celebrates its birthday in a garden app
- "You've saved 12 minutes this week" summary on Friday

**Audit question:** What is the single most memorable moment in this feature, and is it a moment of delight or frustration?

---

## Quick Reference Card

```
User has too many choices?         → Hick's Law: reduce to ≤5-7, use progressive disclosure
Target too hard to tap?            → Fitts's Law: increase size, move closer to thumb zone
Screen feels overwhelming?         → Miller's Law: chunk into groups of ≤5, add visual hierarchy
UI feels unfamiliar?               → Jakob's Law: use platform conventions; innovate on value only
Action feels slow?                 → Doherty Threshold: show feedback <400ms; use optimistic UI
Users can't enter their data?      → Postel's Law: accept multiple formats, auto-correct
Feature memorable for wrong reason? → Peak-End Rule: add a delight moment; smooth the failure recovery
```
