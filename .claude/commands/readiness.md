---
description: Run a pre-flight readiness audit before shipping to beta, production, or as a hotfix. Checks code quality, safety, stability, legal/compliance, user testing, business readiness, and infrastructure. Produces a GO / NO-GO verdict with specific blockers.
---

Run the Launch Readiness Audit directly in this context. Do NOT spawn a subagent.

Read the codebase, `BACKLOG.md`, `DECISIONS.md`, and `PROJECT_STATE.md` to check each item against reality.

**Arguments:** `$ARGUMENTS` specifies the release target:
- `beta` — Beta/staging readiness (code quality + safety + stability)
- `production` — Full production release (all checks including legal, listing, business, user testing)
- `hotfix` — Targeted patch (minimal checklist: diff scope, no new deps, tests pass, rollback plan)
- (empty) — Default to `production`

**Beta checklist (run for all targets):**

Code Quality: no `any` types, no debug logging, no TODO/FIXME, no commented code, linter passes, typecheck passes, all tests pass, no hardcoded secrets

Safety: agentic loops are depth-limited, API calls have timeouts, user input is validated, storage is bounded, secrets in Keychain/SecureStore

Stability: error boundary exists, all async ops have error handling, loading states present, empty/null data handled, network failure handled gracefully

**Production checklist (add to beta):**

Legal: privacy policy at public URL, ToS at public URL, AI disclaimer visible, data deletion mechanism exists, GDPR consent flow (if EU users)

Platform listing: listing/landing page complete, screenshots ready, copy finalized, version incremented

Business: revenue model decided, pricing set, unit economics estimated, kill criteria defined, success metric defined

User testing: self-testing on real device done, inner circle testing (3-5 people), beta testing (10-30 users), critical feedback addressed

Infrastructure: analytics + crash reporting configured, production build pipeline configured, support channel exists, rollback plan defined

**Hotfix checklist:**

Changes are minimal and targeted; no new dependencies/permissions; all tests pass; linter + typecheck pass; tested in staging; previous version available for rollback; change is low-risk

**Output format:**

```
╔══════════════════════════════════════════════════════════╗
║              LAUNCH READINESS AUDIT                      ║
╠══════════════════════════════════════════════════════════╣

TARGET: [Beta / Production / Hotfix]
DATE: [today's date]

━━━ PASSED ━━━   [N checks ✅]

━━━ FAILED (Blockers) ━━━
  [#] [Check name] ❌
      Issue: [what's wrong]
      Fix: [specific action]
      Effort: [quick fix / half day / multi-day]

━━━ NEEDS VERIFICATION (Product Owner action required) ━━━
  [#] [Check name] ❓
      Question: [what to confirm]

━━━ NOT APPLICABLE ━━━
  [#] [Check name] — [why]

SCORECARD: Passed: N/total | Failed: N | Needs verification: N | N/A: N

VERDICT: ✅ GO / ❌ NO-GO

BLOCKERS (if NO-GO):
  1. [Most critical blocker and how to fix it]

ESTIMATED EFFORT TO REACH GO: [e.g., "2 blockers, ~1 day of work"]
╚══════════════════════════════════════════════════════════╝
```

**Veto rule:** If ANY blocker in the FAILED section exists, verdict is NO-GO. No exceptions. Fix blockers and re-run `/readiness`.

**Relationship to `/checkpoint`:** `/checkpoint` asks "have you decided?" `/readiness` asks "have you done it?" Run `/checkpoint [phase]` first to surface undecided items, then `/readiness` to verify execution.
