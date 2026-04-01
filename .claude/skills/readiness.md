# Skill: Launch Readiness Audit

## Trigger
Invoke with `/readiness` when the team is considering shipping to beta, production, or any external user.

Can also be invoked with a specific scope:
- `/readiness beta` — Beta/staging readiness
- `/readiness production` — Full production release readiness
- `/readiness hotfix` — Hotfix/patch readiness (minimal changes)

## Role
You are the **Release Gatekeeper**. You run a comprehensive pre-flight checklist across code quality, security, legal, UX, performance, and business readiness. You produce a GO / NO-GO verdict with specific blockers.

## Release Engineering Knowledge Base

### Semantic Versioning (SemVer 2.0.0)
Version format: **MAJOR.MINOR.PATCH**
- **MAJOR** (1.0.0 → 2.0.0): Breaking changes — incompatible API or behavior changes
- **MINOR** (1.0.0 → 1.1.0): New features, backward compatible
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, backward compatible
- **Pre-release**: 1.0.0-beta.1, 1.0.0-rc.1

**Rules:**
- First public release: 1.0.0 (not 0.x — that signals instability)
- Every release increments exactly one segment
- If MAJOR or MINOR increments, reset the segments to the right (1.2.3 → 2.0.0)

### Deployment Strategies

| Strategy | Risk Level | Rollback Speed | When to Use |
|----------|-----------|---------------|-------------|
| **Blue-Green** | Low | Instant (switch traffic) | Production releases with zero-downtime requirement |
| **Canary** | Low | Fast (shift traffic back) | When you want to validate with real users before full rollout |
| **Rolling** | Medium | Medium (redeploy old version) | Standard server-side deployments |
| **Feature flags** | Lowest | Instant (toggle off) | Any feature that might need quick disable. Preferred for new features. |
| **Big bang** | Highest | Slow (full redeploy) | Avoid. Only for v1.0.0 with no existing users. |

**For mobile apps:**
- **Staged rollout** (10% → 25% → 50% → 100%) via App Store / Play Store
- **OTA updates** (Expo Updates, CodePush) for JS-only changes — instant, no store review
- **TestFlight / Internal testing track** for beta builds

### Observability Requirements (pre-launch minimum)

| Signal | Tool Options | Must Have Before Launch? |
|--------|-------------|------------------------|
| **Error tracking** | Sentry, Bugsnag, Crashlytics | YES — non-negotiable |
| **Analytics** | Mixpanel, PostHog, Amplitude, Firebase Analytics | YES — can't measure success without it |
| **Performance monitoring** | Sentry Performance, New Relic, Datadog | Recommended for production, optional for beta |
| **Log aggregation** | Structured console (dev), LogRocket (prod) | YES for production |
| **Uptime monitoring** | Pingdom, UptimeRobot, Better Uptime | YES for any backend/API |

### Data Retention & Privacy Policies

| Data Type | Retention | Deletion | Encryption |
|-----------|----------|----------|------------|
| **User content** (conversations, inputs) | User-controlled (delete on request) | Hard delete within 30 days of request | At rest (AES-256) |
| **Analytics events** | 12 months | Auto-purge after retention period | In transit (TLS) |
| **Crash reports** | 90 days | Auto-purge | In transit (TLS) |
| **Auth tokens** | Session-scoped or 30 days max | On logout or expiry | Keychain/SecureStore |
| **API keys** | Until rotated | On rotation | Keychain/SecureStore |
| **Logs** | 30 days (dev), 90 days (prod) | Auto-purge | In transit (TLS) |

## Process

### Step 1: Determine Release Target
- **Beta** — Internal/beta testing. Looser standards, but code must be safe.
- **Production** — Public release. Every standard applies.
- **Hotfix** — Targeted patch. Must not break existing functionality.

### Step 2: Run All Checklists

Read the codebase, BACKLOG.md, DECISIONS.md, and PROJECT_STATE.md. Check each item against reality.

---

## Checklists by Release Target

### Beta Readiness

#### Code Quality
| # | Check | How to Verify |
|---|-------|---------------|
| 1 | No `any` types (if TypeScript) or equivalent type issues | Search source code |
| 2 | No debug logging in production code | Search for `console.log`, `print()`, `debugger` |
| 3 | No `// TODO` or `// FIXME` in shipped code | Grep for TODO/FIXME |
| 4 | No commented-out code blocks | Manual review |
| 5 | Linter passes with zero warnings | Run lint command |
| 6 | Type checker passes with zero errors | Run typecheck command |
| 7 | All tests pass | Run test suite |
| 8 | No hardcoded secrets in code | Search for API keys, tokens, passwords |

#### Safety
| # | Check | How to Verify |
|---|-------|---------------|
| 9 | Recursive/agentic loops are depth-limited | Check for max iteration constants |
| 10 | API calls have timeouts | Check for AbortController or timeout config |
| 11 | User input is validated | Check input handling code |
| 12 | Data storage is bounded (no unbounded growth) | Review storage/history management |
| 13 | Secrets stored securely (not in code, not in logs) | Review credential handling |

#### Stability
| # | Check | How to Verify |
|---|-------|---------------|
| 14 | Error boundary / global error handler exists | Check app entry point |
| 15 | All async operations have error handling | Review catch blocks |
| 16 | Loading states for all async operations | Review state management |
| 17 | App handles empty/null data gracefully | Test empty states |
| 18 | App handles network failure gracefully | Review error handling |

### Production Readiness (includes all Beta checks plus:)

#### Legal & Compliance
| # | Check | How to Verify |
|---|-------|---------------|
| 19 | Privacy policy hosted at public URL | Ask Product Owner for URL |
| 20 | Privacy policy linked in app/service | Check settings or footer |
| 21 | Terms of service hosted at public URL | Ask Product Owner for URL |
| 22 | AI disclaimer visible to users | Check UI for disclaimer text |
| 23 | Data collection disclosures accurate on all platforms | Ask Product Owner |
| 24 | Data deletion mechanism available | Check settings or support channel |
| 25 | Age rating set appropriately | Ask Product Owner |
| 26 | GDPR consent flow (if EU users) | Check for consent UI |

#### Platform Listing (adapt to your platform)

> **Mobile (App Store / Play Store)**:
> Screenshots, app description, keywords, version, icon, store-specific disclosures
>
> **Web**: Landing page, meta tags, OG images, sitemap, analytics
>
> **API**: Documentation, versioning, status page, rate limit docs

| # | Check | How to Verify |
|---|-------|---------------|
| 27 | Public listing / landing page complete | Ask Product Owner |
| 28 | Screenshots or demo materials ready | Ask Product Owner |
| 29 | Description / marketing copy finalized | Ask Product Owner |
| 30 | Version number incremented | Check config files |

#### Business Readiness
| # | Check | How to Verify |
|---|-------|---------------|
| 31 | Revenue model decided | Check DECISIONS.md |
| 32 | Pricing set (if monetizing at launch) | Check DECISIONS.md |
| 33 | Payment infrastructure configured (if applicable) | Check payment provider setup |
| 34 | Unit economics estimated | Check DECISIONS.md or cost analysis |
| 35 | Kill criteria defined | Check MVP brief or DECISIONS.md |
| 36 | Success metric defined | Check MVP brief or DECISIONS.md |

#### User Testing
| # | Check | How to Verify |
|---|-------|---------------|
| 37 | Self-testing on real device/environment completed | Ask Product Owner |
| 38 | Inner circle testing (3-5 people) completed | Ask Product Owner |
| 39 | Beta testing (10-30 users) completed | Ask Product Owner |
| 40 | Critical feedback addressed | Cross-reference feedback with BACKLOG.md |

#### Infrastructure
| # | Check | How to Verify |
|---|-------|---------------|
| 41 | Analytics/crash reporting configured | Check for monitoring integration |
| 42 | Production build/deploy pipeline configured | Check CI/CD config |
| 43 | Support channel set up (email minimum) | Ask Product Owner |
| 44 | Rollback plan defined | Check release docs or DECISIONS.md |

### Hotfix Readiness

| # | Check | How to Verify |
|---|-------|---------------|
| 1 | Changes are minimal and targeted | Review diff scope |
| 2 | No new dependencies or permissions introduced | Review dependency/config changes |
| 3 | All tests pass | Run test suite |
| 4 | Linter + type checker pass | Run lint + typecheck |
| 5 | Change tested in staging/preview | Ask Product Owner |
| 6 | Previous version available for rollback | Check deployment history |
| 7 | Change is low-risk | Manual assessment of diff scope |

---

## Required Output Format

```
╔══════════════════════════════════════════════════════════╗
║              LAUNCH READINESS AUDIT                      ║
╠══════════════════════════════════════════════════════════╣

TARGET: [Beta / Production / Hotfix]
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
