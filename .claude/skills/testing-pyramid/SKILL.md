---
name: testing-pyramid
description: Use when planning a test strategy, writing tests, or auditing test coverage. Provides the Testing Pyramid framework with unit/integration/E2E ratios, mock strategy, flaky test prevention, and coverage interpretation. Referenced by the qa subagent.
---

# Testing Pyramid Framework

Source: Cohn, M. — *Succeeding with Agile* (2009). Fowler, M. — "TestPyramid" (martinfowler.com, 2012). Google Testing Blog — "Just Say No to More End-to-End Tests" (2015).

## Core Principle

Most tests should be small, fast, and isolated. A few should be large, slow, and end-to-end. Inverting this ratio produces a slow, brittle, expensive test suite.

## The Pyramid

```
         /  E2E  \          10% — Critical user journeys only
        / Integr. \         20% — Service interactions, contracts
       /   Unit    \        70% — Pure logic, hooks, utilities
      ──────────────
```

**Anti-pattern: The Ice Cream Cone**

```
       /  Unit  \           (almost none)
      / Integr. \           (a few)
     /    E2E    \          (hundreds — slow, expensive, flaky)
    ──────────────
```

If your test suite takes >5 minutes, you have an inverted pyramid. Slow CI is a code smell.

## Level by Level

### Unit Tests (70%)

**What to test:** Pure functions, validators, formatters, reducers, hook logic, state transitions, business rules, type guards.

**What NOT to test:** React component rendering, API calls, file I/O, database queries, platform APIs.

**Speed target:** <5ms per test. Thousands of unit tests should complete in seconds.

**Key characteristic:** Zero external dependencies. No network. No file system. No clock. Deterministic.

```typescript
// GOOD unit test — pure logic, no mocks needed
describe('validateUserInput', () => {
  it('should reject empty strings', () => {
    expect(() => validateUserInput('')).toThrow('Message cannot be empty');
  });

  it('should reject strings over 4000 characters', () => {
    expect(() => validateUserInput('a'.repeat(4001))).toThrow('Message too long');
  });

  it('should return trimmed valid input', () => {
    expect(validateUserInput('  hello  ')).toBe('hello');
  });
});
```

### Integration Tests (20%)

**What to test:** Service ↔ API contracts, Hook ↔ Service composition, Component ↔ Hook interaction, error handling at boundaries.

**What NOT to test:** Internal implementation details, CSS styling, presentation logic.

**Speed target:** <100ms per test. Integration tests should complete in under a minute.

**Key characteristic:** Mock at the boundary, not inside your own code. Use MSW (Mock Service Worker) for HTTP — it intercepts at the network layer, not the service layer.

```typescript
// GOOD integration test — mocks network boundary, not internal service
import { setupServer } from 'msw/node';
import { rest } from 'msw';

const server = setupServer(
  rest.post('/api/chat', (req, res, ctx) => {
    return res(ctx.json({ content: 'Hello!' }));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

it('should display agent response after message send', async () => {
  const { getByRole, findByText } = render(<ChatScreen />);
  await userEvent.type(getByRole('textbox'), 'What is 2+2?');
  await userEvent.click(getByRole('button', { name: 'Send' }));
  expect(await findByText('Hello!')).toBeInTheDocument();
});
```

### E2E Tests (10%)

**What to test:** 3-5 critical user journeys end-to-end, on real or emulated device.

**What NOT to test:** Every permutation, edge cases (those belong in unit/integration), cosmetic behavior.

**Speed target:** <30s per test. Total E2E suite <10 minutes.

**Key characteristic:** Real app, real browser or device, real network (or realistic stub). Catches integration regressions that lower levels miss.

**Critical journey selection criteria:**
1. If this breaks, the app is dead (core value prop)
2. Happens on every user session
3. Involves multiple systems working together (auth + API + storage)
4. Has caused a production incident before

## Mock Strategy

**Rule: Mock at boundaries, not within your own code.**

| Boundary | Mock Technique | Tool |
|----------|---------------|------|
| HTTP/Network | Intercept at network level | **MSW (Mock Service Worker)** — preferred |
| Time | Fake timers | `jest.useFakeTimers()` |
| Storage | In-memory implementation | Custom mock matching the interface |
| Platform APIs | Module-level mock | `jest.mock('react-native/...')` |
| Randomness | Seed or mock | `jest.spyOn(Math, 'random').mockReturnValue(0.5)` |

**Anti-patterns — never do this:**
- Mocking your own service layer in integration tests (you're testing the mock, not the service)
- Mocking implementation details (`jest.spyOn(component, '_internalMethod')`)
- Using `jest.mock` on the module under test itself
- Global test state that leaks between tests

## Flaky Test Prevention

A test that fails 1 in 10 runs is a flaky test. Quarantine it (`.skip` with a TODO), fix the root cause, re-enable. Never leave flaky tests running — they erode trust in the entire suite.

| Source | Prevention | Detection |
|--------|-----------|-----------|
| **Timing-dependent** | Fake timers, `waitFor`, no `setTimeout` in tests | Passes/fails inconsistently across runs |
| **Order-dependent** | Each test sets up and tears down its own state | Fails only when run after a specific other test |
| **Environment-dependent** | Mock all external deps (network, storage, time) | Passes locally, fails in CI |
| **Race conditions** | `act()`, `waitFor()`, proper async patterns | Fails intermittently under load |
| **Shared mutable state** | `beforeEach` reset, no global variable modification | Fails in parallel execution |

## Test Naming Convention

```typescript
describe('[ModuleName]', () => {
  describe('[methodName or behavior group]', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange — set up test state
      // Act — perform the action
      // Assert — verify the result
    });
  });
});
```

**Good names:**
- `should return empty array when no messages exist`
- `should throw ValidationError when input exceeds 4000 characters`
- `should retry 3 times with exponential backoff when network fails`

**Bad names:**
- `test1`
- `works correctly`
- `handles error`
- `should work`

## Coverage Interpretation

Coverage is a floor, not a ceiling. High coverage with meaningless assertions is worse than moderate coverage with high-signal tests.

| Coverage % | Meaning | Action |
|-----------|---------|--------|
| >90% | Likely over-testing implementation details | Review for tests that test the wrong thing |
| 70-90% | Healthy range for production code | Maintain; focus on meaningful gaps |
| 50-70% | Acceptable early-stage; risky for production | Prioritize critical path coverage |
| <50% | High regression risk | Stop features. Write tests first. |

**What coverage does NOT tell you:**
- Whether tests are meaningful (100% coverage with `expect(true).toBe(true)` is useless)
- Whether edge cases are covered (coverage counts lines, not scenarios)
- Whether error paths are tested (most uncovered code is error handling)

**Rule:** Coverage on new code must be ≥70% before shipping. Error handling paths must be tested explicitly — they're the most important code and the least covered.

## Edge Case Taxonomy

Every feature needs tests in these categories (distributed across unit/integration levels):

| Category | Examples |
|----------|---------|
| **Boundary values** | max-1, max, max+1 character limits; 0, 1, N items in a list |
| **Empty states** | Empty string, null, undefined, empty array, empty object |
| **First use** | No prior data, no preferences set, fresh install state |
| **Maximum load** | Longest allowed string, most items in a list, max concurrent requests |
| **Rapid repetition** | Double-tap submit, rapid state changes, concurrent mutations |
| **Interrupted actions** | Background app mid-save, network drop mid-request, kill app mid-save |
| **Error scenarios** | Network failure, 400/401/403/429/500 responses, timeout, malformed response |
| **State transitions** | Empty → Loading → Success; Loading → Error → Retry → Success |

## Accessibility Testing

Automated a11y testing catches ~30-40% of accessibility issues. Manual testing catches the rest.

```typescript
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

it('has no accessibility violations', async () => {
  const { container } = render(<ChatBubble message="Hello" />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

| Check | Tool | Level |
|-------|------|-------|
| Color contrast | axe-core, Lighthouse | Automated |
| Missing ARIA labels | axe-core, jest-axe | Automated |
| Touch target size | Custom lint rule | Semi-automated |
| Keyboard navigation | Manual | Manual |
| Screen reader (VoiceOver/TalkBack) | Manual on device | Manual — critical paths |
| Dynamic Type | iOS Accessibility Inspector | Manual |
| Reduced Motion | `prefers-reduced-motion: reduce` | Semi-automated |

**Rule:** All new components must pass `jest-axe` before shipping. VoiceOver manual testing required for primary screens.
