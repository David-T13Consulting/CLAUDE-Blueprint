---
description: Audit which decisions need to be made right now based on the project's current lifecycle phase (VALIDATION/DESIGN/BUILD/PRE-LAUNCH/POST-LAUNCH). Surfaces OVERDUE, BLOCKED, and UPCOMING decisions. Does not spawn a subagent — runs in main context.
---

Run the Decision Checkpoint Audit directly in this context. Do NOT spawn a subagent.

Read `PROJECT_STATE.md`, `BACKLOG.md`, and `DECISIONS.md` to determine the current project phase and which decisions are pending.

**Arguments:** `$ARGUMENTS` may specify a phase (validation, design, build, pre-launch, post-launch) or be empty (auto-detect phase from PROJECT_STATE.md).

**Phase detection:**
- No validated problem yet → VALIDATION
- Research done, no design → DESIGN
- Design approved, building → BUILD
- Features complete, not shipped → PRE-LAUNCH
- App is live → POST-LAUNCH

**For each decision in the relevant phase, classify as:**
- **DECIDED** — Already logged in DECISIONS.md or resolved in the codebase
- **BLOCKED** — Needs a decision NOW before work can continue
- **UPCOMING** — Not urgent yet but approaching (next 1-2 milestones)
- **OVERDUE** — Should have been decided by now based on project progress

**Decision tables by phase:**

VALIDATION: V-01 (problem statement), V-02 (scorecard ≥7), V-03 (target user), V-04 (pipeline mode), V-05 (core value), V-06 (out of scope), V-07 (kill criteria), V-08 (success metric)

DESIGN: D-01 (interaction model), D-02 (all states inventoried), D-03 (benchmark passes), D-04 (a11y requirements), D-05 (animation specs), D-06 (component reuse)

BUILD: B-01 (data model), B-02 (API contracts), B-03 (error handling strategy), B-04 (state management), B-05 (deps justified), B-06 (critical backlog empty), B-07 (test strategy), B-08 (agentic loop safety)

PRE-LAUNCH: P-01 (revenue model), P-02 (pricing), P-03 (unit economics positive), P-04 (privacy policy URL), P-05 (ToS URL), P-06 (AI disclaimer), P-07 (developer account), P-08 (listing complete), P-09 (self-testing done), P-10 (inner circle testing), P-11 (beta testing), P-12 (analytics configured), P-13 (GDPR consent), P-14 (privacy labels), P-15 (support channel), P-16 (GTM channels), P-17 (launch date set)

POST-LAUNCH: L-01 (activation rate), L-02 (day-7 retention), L-03 (kill criteria met?), L-04 (API costs within budget), L-05 (1-star patterns), L-06 (top user request), L-07 (SCALE mode?), L-08 (OTA vs full release)

**Output format:**

```
╔══════════════════════════════════════════════════════════╗
║              DECISION CHECKPOINT AUDIT                   ║
╠══════════════════════════════════════════════════════════╣

CURRENT PHASE: [phase]
DETECTED FROM: [source]

━━━ OVERDUE ━━━
  [ID]: [decision] — [why overdue] — [action]

━━━ BLOCKED ━━━
  [ID]: [decision] — [what's waiting] — [2-3 options] — [recommendation]

━━━ UPCOMING ━━━
  [ID]: [decision] — [when it becomes blocking]

━━━ DECIDED ━━━
  [ID]: [decision] — [date] — [summary]

SUMMARY: Overdue: N | Blocked: N | Upcoming: N | Decided: N

NEXT ACTION: [single most important decision to make now]
╚══════════════════════════════════════════════════════════╝
```

Only surface what's relevant NOW. Don't dump every possible decision. After the audit, if no decisions are overdue or blocked, confirm: "All decisions for the current phase are resolved. Continue working."
