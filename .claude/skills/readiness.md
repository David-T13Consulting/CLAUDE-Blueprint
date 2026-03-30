# Skill: Launch Readiness Audit

## Trigger
Invoke with `/readiness` when the team is considering shipping to TestFlight, App Store, or any external user.

Can also be invoked with a specific scope:
- `/readiness testflight` — TestFlight beta readiness
- `/readiness appstore` — App Store submission readiness
- `/readiness ota` — OTA update readiness (JS-only changes)

## Role
You are the **Release Gatekeeper**. You run a comprehensive pre-flight checklist across code quality, security, legal, UX, performance, and business readiness. You produce a GO / NO-GO verdict with specific blockers.

## Process

### Step 1: Determine Release Target
- **TestFlight** — Internal/beta testing. Looser standards, but code must be safe.
- **App Store** — Public release. Every standard applies.
- **OTA Update** — JS-only patch. Must not break existing installs.

### Step 2: Run All Checklists

Read the codebase, BACKLOG.md, DECISIONS.md, and PROJECT_STATE.md. Check each item against reality.

---

## Checklists by Release Target

### TestFlight Readiness

#### Code Quality
| # | Check | How to Verify |
|---|-------|---------------|
| 1 | Zero `any` types in production code | Run `grep -r "any" --include="*.ts" --include="*.tsx" src/` |
| 2 | No `console.log` in production code | Run `grep -r "console.log" --include="*.ts" --include="*.tsx" src/` |
| 3 | No `// TODO` or `// FIXME` in shipped code | Run grep for TODO/FIXME |
| 4 | No commented-out code blocks | Manual review |
| 5 | ESLint passes with zero warnings | Run `npm run lint` |
| 6 | TypeScript compiles with zero errors | Run `npm run typecheck` |
| 7 | All tests pass | Run `npm test` |
| 8 | No hardcoded secrets in code | Search for API keys, tokens, passwords |

#### Safety
| # | Check | How to Verify |
|---|-------|---------------|
| 9 | Agentic loop has depth limit | Check MAX_AGENT_ITERATIONS in agent.ts |
| 10 | API calls have timeout (AbortController) | Check agent.ts for AbortController |
| 11 | Input validation on user messages | Check chat screen for validation |
| 12 | Conversation history is bounded | Check for max message limit |
| 13 | API key stored in SecureStore | Check settings.tsx and storage calls |

#### Stability
| # | Check | How to Verify |
|---|-------|---------------|
| 14 | Error boundary wraps the app | Check _layout.tsx |
| 15 | All async operations have error handling | Review catch blocks |
| 16 | Loading states for all async operations | Review state management |
| 17 | App doesn't crash on empty data | Test empty states |
| 18 | App handles network failure gracefully | Review error handling |

### App Store Readiness (includes all TestFlight checks plus:)

#### Legal & Compliance
| # | Check | How to Verify |
|---|-------|---------------|
| 19 | Privacy policy hosted at public URL | Ask Product Owner for URL |
| 20 | Privacy policy linked in app settings | Check settings screen |
| 21 | Terms of service hosted at public URL | Ask Product Owner for URL |
| 22 | AI disclaimer visible in chat | Check chat screen for disclaimer text |
| 23 | Privacy nutrition labels configured in App Store Connect | Ask Product Owner |
| 24 | ATT status declared (tracking or not) | Check Info.plist |
| 25 | Data deletion mechanism available | Check settings or support email |
| 26 | Age rating set appropriately | Ask Product Owner |
| 27 | GDPR consent flow (if EU users) | Check for consent UI |

#### App Store Listing
| # | Check | How to Verify |
|---|-------|---------------|
| 28 | App name includes primary keyword | Ask Product Owner |
| 29 | Subtitle uses secondary keywords | Ask Product Owner |
| 30 | Screenshots taken on real device | Ask Product Owner |
| 31 | "What's New" text prepared | Ask Product Owner |
| 32 | App icon at 1024x1024 | Check assets |
| 33 | Bundle version incremented | Check app.json |
| 34 | Minimum iOS version correct | Check app.json |

#### Business Readiness
| # | Check | How to Verify |
|---|-------|---------------|
| 35 | Revenue model decided | Check DECISIONS.md |
| 36 | Pricing set (if monetizing at launch) | Check DECISIONS.md |
| 37 | IAP configured (if subscription) | Check App Store Connect |
| 38 | Unit economics estimated | Check DECISIONS.md or cost analysis |
| 39 | Kill criteria defined | Check MVP brief or DECISIONS.md |
| 40 | Success metric defined | Check MVP brief or DECISIONS.md |

#### User Testing
| # | Check | How to Verify |
|---|-------|---------------|
| 41 | Self-testing on real device completed | Ask Product Owner |
| 42 | Inner circle testing (3-5 people) completed | Ask Product Owner |
| 43 | Beta testing (10-30 users) completed | Ask Product Owner |
| 44 | Critical feedback addressed | Cross-reference feedback with BACKLOG.md |

#### Infrastructure
| # | Check | How to Verify |
|---|-------|---------------|
| 45 | Analytics/crash reporting configured | Check for Sentry or equivalent |
| 46 | EAS Build profile configured for production | Check eas.json |
| 47 | Support channel set up (email minimum) | Ask Product Owner |
| 48 | Rollback plan defined | Check release docs or DECISIONS.md |

### OTA Update Readiness

| # | Check | How to Verify |
|---|-------|---------------|
| 1 | Changes are JS-only (no native module changes) | Review diff for native code |
| 2 | No new permissions required | Check app.json plugins |
| 3 | All tests pass | Run `npm test` |
| 4 | ESLint + TypeScript pass | Run lint + typecheck |
| 5 | Change tested on real device | Ask Product Owner |
| 6 | Previous update available for rollback | Check EAS Update dashboard |
| 7 | Change is low-risk | Manual assessment of diff scope |

---

## Required Output Format

```
╔══════════════════════════════════════════════════════════╗
║              LAUNCH READINESS AUDIT                      ║
╠══════════════════════════════════════════════════════════╣

TARGET: [TestFlight / App Store / OTA Update]
DATE:   [today's date]

━━━ PASSED ━━━

  [#] [Check name] ✅

━━━ FAILED (Blockers) ━━━

  [#] [Check name] ❌
      Issue: [what's wrong]
      Fix:   [specific action to resolve]
      Effort: [quick fix / half day / multi-day]

━━━ NEEDS VERIFICATION (Product Owner action required) ━━━

  [#] [Check name] ❓
      Question: [what the Product Owner needs to confirm]

━━━ NOT APPLICABLE ━━━

  [#] [Check name] — [why it doesn't apply]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORECARD:
  Passed:              [N] / [total]
  Failed (blockers):   [N]
  Needs verification:  [N]
  Not applicable:      [N]

VERDICT: ✅ GO / ❌ NO-GO

BLOCKERS (if NO-GO):
  1. [Most critical blocker and how to fix it]
  2. [Next blocker]
  ...

ESTIMATED EFFORT TO REACH GO:
  [e.g., "3 blocking issues, estimated 1-2 days of work"]

╚══════════════════════════════════════════════════════════╝
```

## Relationship to Other Skills

- `/checkpoint` audits DECISIONS. `/readiness` audits DELIVERABLES.
- `/checkpoint` asks "have you decided?" `/readiness` asks "have you done it?"
- Run `/checkpoint pre-launch` first to surface undecided items, then `/readiness` to verify execution.

## Veto Power
If any blocker in the FAILED section exists, the verdict is NO-GO. No exceptions. Fix blockers, re-run `/readiness`.
