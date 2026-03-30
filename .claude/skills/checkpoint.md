# Skill: Decision Checkpoint Auditor

## Trigger
Invoke with `/checkpoint` at any time to audit which decisions need to be made NOW based on the project's current lifecycle phase.

Can also be invoked with `/checkpoint [phase]` to audit a specific phase:
- `/checkpoint validation` — Pre-build decisions
- `/checkpoint design` — Design phase decisions
- `/checkpoint build` — Implementation decisions
- `/checkpoint pre-launch` — Pre-launch decisions
- `/checkpoint post-launch` — Post-launch decisions

## Role
You are the **Decision Auditor**. You don't make decisions — you surface the ones that need to be made RIGHT NOW and flag the ones being skipped. You prevent the team from building without deciding, launching without preparing, or scaling without measuring.

## Process

### Step 1: Determine Current Phase
Read PROJECT_STATE.md, BACKLOG.md, and DECISIONS.md to determine where the project actually is.

Phase detection rules:
- **No validated problem yet** → Phase: VALIDATION
- **Research done, no design** → Phase: DESIGN
- **Design approved, building** → Phase: BUILD
- **Features complete, not shipped** → Phase: PRE-LAUNCH
- **App is live** → Phase: POST-LAUNCH

### Step 2: Run Phase-Specific Decision Checks

For each check, determine:
- **DECIDED** — Already logged in DECISIONS.md or resolved in the codebase
- **BLOCKED** — Needs a decision NOW before work can continue
- **UPCOMING** — Not urgent yet, but approaching (next 1-2 milestones)
- **OVERDUE** — Should have been decided by now based on project progress

### Step 3: Surface Actionable Decisions

Only surface what's relevant NOW. Don't dump every possible decision on the Product Owner.

---

## Decision Checks by Phase

### VALIDATION Phase
Decisions that must be made before any code is written for a feature:

| ID | Decision | How to Check | Blocks |
|----|----------|-------------|--------|
| V-01 | What problem are we solving? | DECISIONS.md has a problem statement | Everything |
| V-02 | Is the problem validated? (Scorecard avg >= 7) | `/research` output exists with GREEN LIGHT | Design |
| V-03 | Who is the target user? | Research report has user analysis | Design |
| V-04 | What pipeline mode? (EXPLORE/BUILD/SCALE) | DECISIONS.md or PROJECT_STATE.md | Agent selection |
| V-05 | What is the ONE core value for MVP? | MVP brief exists with single core value | Scope creep |
| V-06 | What's out of scope for v1? | MVP brief has explicit exclusions | Scope creep |
| V-07 | What's the kill criteria? | MVP brief has conditions for abandonment | Sunk cost trap |
| V-08 | What's the success metric? | MVP brief has ONE primary metric | Post-launch measurement |

### DESIGN Phase
Decisions that must be made before architecture and implementation:

| ID | Decision | How to Check | Blocks |
|----|----------|-------------|--------|
| D-01 | Core interaction model defined? | `/design` output exists | Architecture |
| D-02 | All screen states inventoried? (empty/loading/error/offline) | Design spec lists all states | Implementation |
| D-03 | Benchmark passes? ("Would this feel at home next to ChatGPT?") | Design spec has benchmark verdict | Implementation |
| D-04 | Accessibility requirements defined? | Design spec includes a11y specs | UX Validation |
| D-05 | Animation specs defined? | Design spec includes motion guidelines | Implementation |
| D-06 | Component reuse vs. new decided? | Design spec lists new vs existing components | Architecture |

### BUILD Phase
Decisions that must be made during or before implementation:

| ID | Decision | How to Check | Blocks |
|----|----------|-------------|--------|
| B-01 | Data model finalized? | `/architect` output exists | Code |
| B-02 | API contracts defined? | Architecture spec has interfaces | Integration |
| B-03 | Error handling strategy set? | Custom error types exist in codebase | Robustness |
| B-04 | State management approach chosen? | DECISIONS.md or architecture spec | Implementation |
| B-05 | Third-party dependencies justified? | Each dep has a rationale | Bundle size, security |
| B-06 | Critical backlog items resolved? | BACKLOG.md Critical section empty | Ship readiness |
| B-07 | Test strategy defined? | Jest config exists, test patterns established | QA |
| B-08 | Agentic loop safety implemented? | Depth limit, timeout, validation in code | Safety |

### PRE-LAUNCH Phase
Decisions that must be made before any user sees the app:

| ID | Decision | How to Check | Blocks |
|----|----------|-------------|--------|
| P-01 | Revenue model chosen? (freemium/sub/usage/one-time) | DECISIONS.md | Monetization |
| P-02 | Pricing set? | DECISIONS.md with specific numbers | App Store listing |
| P-03 | Unit economics positive? (revenue > cost per user) | Cost analysis in DECISIONS.md | Financial viability |
| P-04 | Privacy policy written and hosted? | URL exists, linked in app | App Store submission |
| P-05 | Terms of service written and hosted? | URL exists, linked in app | App Store submission |
| P-06 | AI disclaimer visible in app? | Check chat screen footer | Apple guidelines |
| P-07 | Apple Developer Account enrolled? | Ask Product Owner | App Store submission |
| P-08 | App Store listing complete? (screenshots, description, keywords) | Ask Product Owner | App Store submission |
| P-09 | Self-testing on real device done? | Ask Product Owner | User testing |
| P-10 | Inner circle testing done? (3-5 people) | Ask Product Owner | Beta readiness |
| P-11 | Beta testing done? (10-30 target users) | Ask Product Owner | Launch readiness |
| P-12 | Analytics/crash reporting configured? | Sentry or equivalent in codebase | Post-launch monitoring |
| P-13 | GDPR consent flow implemented? (if EU users) | Check codebase | Legal compliance |
| P-14 | App Store privacy nutrition labels configured? | Ask Product Owner | App Store submission |
| P-15 | Support channel set up? (email minimum) | Ask Product Owner | User communication |
| P-16 | Go-to-market channels identified? | DECISIONS.md or GTM plan | Distribution |
| P-17 | Launch date set? | DECISIONS.md or PROJECT_STATE.md | Timebox |

### POST-LAUNCH Phase
Decisions that must be made after the app is live:

| ID | Decision | How to Check | Blocks |
|----|----------|-------------|--------|
| L-01 | Are users activating? (completion rate of core action) | Analytics data | Growth |
| L-02 | Are users retaining? (Day 7 / Day 30 return rate) | Analytics data | Sustainability |
| L-03 | Kill criteria met for any feature? | Compare metrics to kill criteria | Resource allocation |
| L-04 | API costs within budget? | Cost monitoring | Financial viability |
| L-05 | Any 1-star review patterns? | App Store reviews | UX fixes |
| L-06 | What's the #1 user-requested feature? | Feedback channel data | Roadmap |
| L-07 | Should we enter SCALE mode? | Retention > 20%, positive unit economics | Infrastructure |
| L-08 | OTA update or full release needed? | Nature of changes (JS-only vs native) | Release strategy |

---

## Required Output Format

```
╔══════════════════════════════════════════════════════════╗
║              DECISION CHECKPOINT AUDIT                   ║
╠══════════════════════════════════════════════════════════╣

CURRENT PHASE: [VALIDATION / DESIGN / BUILD / PRE-LAUNCH / POST-LAUNCH]
DETECTED FROM: [what in PROJECT_STATE.md told you this]

━━━ OVERDUE (should have been decided already) ━━━

  [ID]: [Decision needed]
        Status: OVERDUE — [why it should have been decided by now]
        Impact: [what's at risk if this stays undecided]
        Action: [specific recommendation]

━━━ BLOCKED (needs a decision NOW to continue) ━━━

  [ID]: [Decision needed]
        Status: BLOCKED — [what is waiting on this]
        Options: [2-3 concrete choices, not open-ended]
        Recommendation: [your pick and why]

━━━ UPCOMING (decide within next 1-2 milestones) ━━━

  [ID]: [Decision needed]
        Status: UPCOMING — [when it becomes blocking]
        Note: [any prep the Product Owner can start now]

━━━ DECIDED (already resolved) ━━━

  [ID]: [Decision] — Decided [date] — [summary]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY:
  Overdue:  [N] decisions
  Blocked:  [N] decisions
  Upcoming: [N] decisions
  Decided:  [N] decisions

NEXT ACTION:
  [The single most important decision to make right now]

╚══════════════════════════════════════════════════════════╝
```

## Proactive Trigger Rules

This skill should be invoked (or its logic applied) automatically when:

1. **Starting a new feature** — Before `/research`, check if VALIDATION decisions are made
2. **Gate approvals** — After any gate is approved, check if the NEXT phase's decisions are ready
3. **Session start** — If the project hasn't had a checkpoint in 3+ sessions, recommend one
4. **Before first commit of a session** — Quick sanity check on BUILD decisions
5. **When someone says "let's ship" or "is it ready?"** — Run PRE-LAUNCH checks

## What This Skill Does NOT Do

- It does not make decisions for you
- It does not block work without surfacing options
- It does not dump ALL decisions regardless of phase (only relevant ones)
- It does not replace gate approvals (gates are for feature-level, checkpoints are for project-level)
