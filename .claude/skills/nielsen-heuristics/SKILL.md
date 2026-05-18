---
name: nielsen-heuristics
description: Use when evaluating a design or implemented UI for usability. Provides Nielsen's 10 Usability Heuristics with design implications, validation questions, and a structured audit template. Referenced by designer and ux-validator subagents.
---

# Nielsen's 10 Usability Heuristics

Source: Nielsen, J. — "10 Usability Heuristics for User Interface Design" (NN/g, 1994, updated 2020/2024). The most widely-cited usability framework in UX. Apply as a checklist on every design and again on every implemented feature.

## The 10 Heuristics

### H1: Visibility of System Status

**Principle:** Always keep users informed about what's happening through appropriate feedback within a reasonable time.

**Design implication:** Every async operation needs a loading state. Every state change needs a visible signal. Never leave users guessing.

**Validation question:** Does the user always know what's happening? Are there any dead states (action taken, no feedback given)?

**Implementation checklist:**
- [ ] Loading spinner or skeleton visible during API calls
- [ ] Progress indicator for operations >1 second
- [ ] Success confirmation when action completes
- [ ] Error state visible when something fails
- [ ] No silent failures (UI updates only on success — not on error)

**Doherty Threshold integration:**
- <400ms: No indicator needed (feels instant)
- 400ms–1s: Subtle visual feedback (opacity change, pulse)
- 1–10s: Spinner or skeleton screen
- >10s: Progress bar with estimated time

---

### H2: Match Between System and the Real World

**Principle:** Use words, phrases, and concepts familiar to the user, not system-oriented jargon. Follow real-world conventions.

**Design implication:** Every label, button, message, and error is written in the user's language. UI metaphors match real-world objects users already understand.

**Validation question:** Does every label, button, and message use language the target user would naturally say? Are any developer terms or system concepts exposed?

**Implementation checklist:**
- [ ] All labels reviewed against user research vocabulary
- [ ] Error messages use plain language (not "Error 500: Internal Server Error")
- [ ] Dates, currencies, units in user's local format
- [ ] Metaphors match the domain (e.g., "garden" not "data set")
- [ ] No technical jargon visible to users (ID strings, API terms, status codes)

---

### H3: User Control and Freedom

**Principle:** Support undo and redo. Users will make mistakes — give them clearly marked "emergency exits."

**Design implication:** Every destructive action has an undo. Every modal has a close. Every multi-step flow has a back. Users can always recover from mistakes without punishment.

**Validation question:** Can the user undo, cancel, or go back from every state? Is any dead-end reachable?

**Implementation checklist:**
- [ ] Undo available after destructive actions (delete, clear, submit)
- [ ] Cancel button in every modal and sheet
- [ ] Back navigation on every sub-screen
- [ ] Multi-step flows: can exit at any step without losing everything
- [ ] Confirmation dialog before irreversible actions (not just "Are you sure?" — explain consequences)

---

### H4: Consistency and Standards

**Principle:** Users shouldn't have to wonder whether different words, situations, or actions mean the same thing. Follow platform conventions.

**Design implication:** The same action always looks and behaves the same way across the app. Platform conventions are followed so users can transfer knowledge from other apps.

**Validation question:** Does this feature match the rest of the app? Are any interaction patterns surprising or inconsistent with platform conventions?

**Implementation checklist:**
- [ ] Same action = same UI element everywhere (delete always red, save always blue)
- [ ] Gestures consistent (swipe-to-dismiss works the same everywhere)
- [ ] Platform conventions followed (iOS: back swipe, bottom tab bar; Android: back button)
- [ ] Design tokens applied (same colors, spacing, fonts as rest of app)
- [ ] Icons: same family, same weight, same size grid

---

### H5: Error Prevention

**Principle:** Even better than good error messages is a careful design which prevents a problem from occurring in the first place.

**Design implication:** Constrain inputs. Confirm before destruction. Validate before submission. Prevent errors rather than handle them.

**Validation question:** Are dangerous actions guarded? Are inputs constrained to valid values? Can users enter data that causes errors?

**Implementation checklist:**
- [ ] Confirmation for destructive actions (with explicit description of what will be lost)
- [ ] Input constraints applied (max length, valid formats, type enforcement)
- [ ] Form validation on change, not just on submit
- [ ] "Send" disabled until required fields are filled
- [ ] Auto-correct / auto-format applied where helpful (phone number formatting, date parsing)

---

### H6: Recognition Rather Than Recall

**Principle:** Minimize the user's memory load. Make objects, actions, and options visible. The user should not have to remember information from one part of the interface to another.

**Design implication:** Show options — don't hide them. Recent items, suggestions, and visible navigation reduce memory demand.

**Validation question:** Can the user navigate without memorizing? Are all available actions visible (or one tap away)?

**Implementation checklist:**
- [ ] Navigation items visible (not buried in hamburger menus)
- [ ] Recent items surfaced (search history, recent conversations)
- [ ] Suggested actions visible at relevant moments
- [ ] Labels on all icons (recognition > recall)
- [ ] Multi-step flows: previous answers visible during later steps
- [ ] Hick's Law: no more than 5-7 visible options without grouping

---

### H7: Flexibility and Efficiency of Use

**Principle:** Accelerators — unseen by novice users — may speed up interaction for expert users. Allow users to tailor frequent actions.

**Design implication:** Core tasks have shortcuts. Power users can move faster without the system burdening novices.

**Validation question:** Are there shortcuts or accelerators for users who repeat the same actions frequently?

**Implementation checklist:**
- [ ] Swipe actions for frequent operations (swipe to complete, swipe to delete)
- [ ] Long-press context menus for power actions
- [ ] Keyboard shortcuts documented (if web or tablet)
- [ ] Batch operations available for repeated tasks
- [ ] Smart defaults based on usage patterns (remembers last state)

---

### H8: Aesthetic and Minimalist Design

**Principle:** Dialogues should not contain irrelevant or rarely needed information. Every extra unit of information competes with relevant information and diminishes its relative visibility.

**Design implication:** Remove anything that doesn't serve the user's current goal. Whitespace is not empty — it's breathing room that aids comprehension.

**Validation question:** Is anything on screen that doesn't need to be? Would removing any element hurt usability?

**Implementation checklist:**
- [ ] Every element on screen serves the user's current goal
- [ ] Generous whitespace (minimum 16pt margins, 8pt between elements)
- [ ] No decorative elements that add noise (unnecessary borders, dividers, backgrounds)
- [ ] Typography hierarchy does the heavy lifting (not color or decoration)
- [ ] Max 2-3 colors on screen at once
- [ ] Primary action visually dominant; secondary actions recede

---

### H9: Help Users Recognize, Diagnose, and Recover from Errors

**Principle:** Error messages should be expressed in plain language, precisely indicate the problem, and constructively suggest a solution.

**Design implication:** Plain language, specific problem, actionable next step. Never show system errors to users. Never say "Error 500."

**Validation question:** Are error messages specific, constructive, and actionable? Would a non-technical user know what to do?

**Error message format:**
```
BAD:  "Error 500: Internal Server Error"
BAD:  "An error occurred."
OK:   "Something went wrong. Try again."
GOOD: "We couldn't save your changes. Check your connection and tap Retry."
GREAT: "Your session timed out. [Sign in again →] to pick up where you left off."
```

**Implementation checklist:**
- [ ] No raw API error messages exposed to users
- [ ] Every error has a specific cause (not generic "something went wrong")
- [ ] Every error has a constructive action (retry, go back, contact support)
- [ ] Recovery action is tap-able (not "type the command again")
- [ ] Success state as clear as error state

---

### H10: Help and Documentation

**Principle:** Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation. It should be easy to search, focused on the user's task, and list concrete steps.

**Design implication:** The best UI needs no docs. But complex features need contextual help. Help is searchable, task-oriented, and shows up where the user has the question.

**Validation question:** If the feature is complex, is contextual help available at the right moment? Is any help text actually needed (and if so, why is the UI requiring it)?

**Implementation checklist:**
- [ ] If a tooltip is needed, ask: "Can the UI be redesigned to not need this?"
- [ ] Onboarding: show, don't tell (interactive tutorial > text carousel)
- [ ] Contextual help appears at the moment of confusion, not before
- [ ] Help text is scannable (not paragraphs)
- [ ] Empty states include guidance ("Tap + to add your first plant")

---

## Audit Template

Use this in both `/design` (pre-build) and `/validate` (post-build):

```
HEURISTIC AUDIT: [Feature Name]

| # | Heuristic | Status | Evidence | Action Required |
|---|-----------|--------|----------|-----------------|
| H1 | Visibility of system status | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H2 | Match system ↔ real world | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H3 | User control and freedom | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H4 | Consistency and standards | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H5 | Error prevention | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H6 | Recognition over recall | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H7 | Flexibility and efficiency | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H8 | Aesthetic minimalism | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H9 | Error recovery | PASS/FAIL | [specific finding] | [fix if FAIL] |
| H10 | Help and documentation | PASS/FAIL | [specific finding] | [fix if FAIL] |

VIOLATIONS: [N]
RESOLVED: [N]
UNRESOLVED: [N — list each with priority]
```

**Rule:** Any FAIL must be resolved or explicitly accepted (with rationale) before the design is approved. No unresolved violations at Gate 2 or Gate 4.

## Severity Rating for Violations

| Severity | Criteria | Example |
|----------|----------|---------|
| **Critical** | Blocks user from completing core task | No error recovery, no loading state on primary action |
| **High** | Significantly impairs usability | Jargon in error messages, no undo for destructive action |
| **Medium** | Creates friction, workaround exists | Minor inconsistency, suboptimal loading pattern |
| **Low** | Slight polish opportunity | Minor aesthetic deviation, optional help text |
