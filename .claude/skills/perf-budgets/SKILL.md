---
name: perf-budgets
description: Use when setting performance budgets, auditing render performance, analyzing memory usage, reviewing network efficiency, or calculating AI/LLM costs. Provides Core Web Vitals thresholds, a performance budget table, re-render prevention checklist, animation performance guide, memory leak detection patterns, network optimization patterns, and AI model cost tiering. Referenced by perf-engineer subagent.
---

# Performance Budgets & Engineering Reference

These are non-negotiable thresholds and systematic checklists for production-grade performance. Numbers come from real-world benchmarks — not internal intuition.

---

## Performance Budgets

| Metric | Budget | Measurement Tool |
|--------|--------|-----------------|
| JS bundle size | <200KB gzipped (initial) | expo-atlas, webpack-bundle-analyzer |
| Time to Interactive (TTI) | <3s on 3G, <1.5s on 4G | Lighthouse, WebPageTest |
| First Contentful Paint (FCP) | <1.8s | Lighthouse |
| Largest Contentful Paint (LCP) | <2.5s | Lighthouse |
| Cumulative Layout Shift (CLS) | <0.1 | Lighthouse |
| Interaction to Next Paint (INP) | <200ms | Lighthouse |
| Frame rate | 60fps (16.67ms/frame budget) | React DevTools Profiler |
| API response (p95) | <2s | Custom instrumentation |
| API response (p99) | <5s | Custom instrumentation |
| Memory growth | <50MB after 30min active use | Xcode Instruments, Android Profiler |
| Cold start | <2s to interactive | Platform profiling tools |
| AI response: first token | <1s (streaming) | Custom instrumentation |

**Veto rule:** Any budget violated by >2× is an automatic BLOCK. Optimization is required before shipping.

---

## Core Web Vitals — What They Measure

**Source:** Google Web Vitals initiative, 2020–present. These are the metrics Google uses to assess page experience quality.

| Vital | Measures | Good | Needs Improvement | Poor |
|-------|---------|------|-----------------|------|
| **LCP** (Largest Contentful Paint) | Loading performance | <2.5s | 2.5–4s | >4s |
| **INP** (Interaction to Next Paint) | Responsiveness | <200ms | 200–500ms | >500ms |
| **CLS** (Cumulative Layout Shift) | Visual stability | <0.1 | 0.1–0.25 | >0.25 |
| **FCP** (First Contentful Paint) | Perceived load start | <1.8s | 1.8–3s | >3s |
| **TTI** (Time to Interactive) | Full interactivity | <3.8s | 3.8–7.3s | >7.3s |

**CLS formula:** `CLS = impact fraction × distance fraction` per layout shift event, summed over the page lifetime.

**INP replaces FID (First Input Delay):** INP measures the worst-case interaction delay across the entire session, not just the first interaction.

---

## Re-Render Prevention Checklist

| Pattern | Problem | Solution | When to Apply |
|---------|---------|----------|---------------|
| Unstable object/array references | New reference on every render triggers child re-renders | `useMemo` / `useCallback` | When passed as props to memoized children |
| Context over-subscription | Entire subtree re-renders on any context change | Split contexts by update frequency; use selectors | Context with >3 consumers and frequent updates |
| Uncontrolled re-renders | Parent cascades unnecessarily to all children | `React.memo` on pure components | Components that render >2× without prop changes |
| Expensive inline derivations | Heavy computation on every render | `useMemo` with correct deps | Computations >1ms — measure before adding |
| List rendering: ScrollView + map | Renders all items even off-screen | `FlatList`/`FlashList` with `keyExtractor` | Any list >20 items |

**Rule:** Don't add `useMemo`/`useCallback` by default — they add memory and complexity. Measure first, memoize second. Profile in React DevTools Profiler to find actual re-render hot spots.

---

## Animation Performance

| Approach | Thread | FPS Risk | Use When |
|----------|--------|----------|----------|
| `Animated` (JS-driven, no native driver) | JS thread | HIGH | Avoid for interactive animations |
| `Animated` with `useNativeDriver: true` | UI thread | LOW | Opacity, transform (no layout props) |
| `react-native-reanimated` worklets | UI thread | LOWEST | Complex, gesture-driven, layout-independent |
| CSS transitions (web) | Compositor | LOW | Opacity, transform, filter — not layout |

**Hard rule:** Any animation touching layout properties (width, height, top, left, margin, padding) MUST use Reanimated worklets. JS-driven layout animations will drop frames.

**Frame budget math:**
- 60fps = 16.67ms per frame
- 120fps = 8.33ms per frame (ProMotion)
- JS work >8ms in a frame causes jank at 60fps; >4ms causes jank at 120fps

---

## Memory Leak Detection

| Source | Leak Pattern | Prevention |
|--------|-------------|------------|
| Event listeners | `addEventListener` without `removeEventListener` | Clean up in `useEffect` return function |
| Timers | `setInterval`/`setTimeout` not cleared | Store ref with `useRef`, clear on unmount |
| Subscriptions | WebSocket, Observable, EventEmitter not closed | Unsubscribe/close in cleanup |
| Promises | Resolves after component unmounts, updates state | AbortController; check `isMounted` flag |

### Bounded Data Structures

Unbounded growth is a guaranteed memory leak over time. Every dynamic data structure must have a cap and eviction policy.

| Data Type | Bound | Eviction Strategy |
|-----------|-------|------------------|
| Conversation messages | Max 100 in memory | Remove oldest |
| API response cache | Max 50MB | LRU eviction |
| Image cache | Max 100MB | LRU with TTL (7 days) |
| Search history | Max 50 items | Remove oldest |
| Undo history | Max 20 steps | Remove oldest |

**Testing for leaks:** Take a heap snapshot before and after 30 minutes of active use. Growth >50MB indicates a leak. Use Xcode Instruments (iOS) or Android Profiler (Android) for native heap analysis.

---

## Network Efficiency Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Duplicate requests | Same data fetched by multiple components | Shared data layer, React Query deduplication |
| Waterfall requests | Sequential calls that could run in parallel | `Promise.all` / `Promise.allSettled` |
| Over-fetching | More data returned than displayed | Pagination, field selection, GraphQL |
| No caching | Fetching unchanged data on every mount | HTTP caching (ETag, Cache-Control) |
| No retry | Transient failures treated as permanent failures | Exponential backoff: 1s → 2s → 4s (max 3 retries) |
| No timeout | Hung requests hold resources indefinitely | AbortController — 30s default, 60s for AI calls |

**Retry formula:**
```
delay = base_delay × 2^(attempt − 1) + jitter
jitter = random(0, base_delay × 0.1)

Attempt 1: wait 1s (+jitter)
Attempt 2: wait 2s (+jitter)
Attempt 3: wait 4s (+jitter)
Give up after attempt 3 → show error to user
```

---

## AI/LLM Cost Optimization

### Model Tiering

Right-size the model to the task. The cost difference between Haiku and Opus is 10–50×.

| Task Type | Model | Output Token Budget |
|-----------|-------|-------------------|
| Classification, formatting, simple extraction | Haiku | 256–512 |
| Conversation, analysis, code generation | Sonnet | 1024–2048 |
| Complex reasoning, architecture, critical decisions | Opus | 2048–4096 |

**Rule:** Default to Sonnet. Downgrade to Haiku for simple tasks, upgrade to Opus only when depth is demonstrably required.

### Cost Calculation Template

```
COST PER INTERACTION:
  Input tokens:  ~[N] × $[rate]/1M tokens = $[X]
  Output tokens: ~[N] × $[rate]/1M tokens = $[X]
  Total per call:                          = $[X]

COST PER USER PER DAY:
  [N] interactions/day × $[X]/interaction = $[X]

COST PER USER PER MONTH:
  $[X]/day × 30 days                      = $[X]

UNIT ECONOMICS:
  Revenue/user/month:   $[X]
  Cost/user/month:      $[X]
  Margin:               $[X]  ← must be positive
```

**Kill criterion:** If `cost/user/month > revenue/user/month`, the feature cannot ship until the margin is positive. Scaling a negative-margin feature accelerates losses.

### Context Window Management

Sending the full conversation history on every call is the #1 avoidable cost driver.

- Don't send full history — summarize older messages, keep recent 5–10 in full
- Sliding window: last N messages + system prompt + compressed summary of earlier messages
- Reserve 25% of context window for the response
- Use the API's token counting endpoint or `tiktoken` to track usage before it overruns
- Cache frequently reused prefixes (system prompts, static context) using prompt caching

### Streaming

Always stream responses when displaying to users. Streaming doesn't reduce cost, but it dramatically improves perceived performance — first token visible within 1s feels fast even if full completion takes 10s. Never show a blank screen while waiting for a full AI response.

---

## Bundle Size Analysis

For each new dependency added, classify before shipping:

| Question | Action |
|----------|--------|
| Is it used in the critical path? | If no, lazy-load it |
| Does it tree-shake? | Check with bundle analyzer |
| Is a lighter alternative available? | e.g., `date-fns` instead of `moment` |
| Can the function be implemented inline? | For utilities <10 lines, skip the dependency |

**Budget enforcement:** Any single dependency >50KB gzipped requires explicit justification. Any dependency that pushes total bundle over 200KB requires either replacing an existing dependency or lazy-loading.

---

## Startup Impact Assessment

For every feature added to the app:

1. Does it add to the critical initialization path?
2. Can it be lazy-loaded after the first meaningful paint?
3. Does it add global event listeners or background work on startup?
4. Does it register services, fonts, or assets that block rendering?

**Rule:** Features should not add to the critical startup path without justification. Lazy-load everything that isn't needed for the first frame.

---

## Quick Reference Card

```
Animation dropping frames?         → Move to useNativeDriver or Reanimated worklets
List rendering slowly?             → Replace ScrollView+map with FlatList/FlashList
Memory growing unboundedly?        → Add bounds + eviction to data structures; check cleanup on unmount
Network calls duplicating?         → Add shared data layer with deduplication
AI cost too high?                  → Downgrade model tier; reduce context; summarize history
Bundle >200KB?                     → Lazy-load non-critical paths; audit and replace heavy deps
First paint too slow?              → Defer non-critical initialization; lazy-load routes
Any budget violated >2×?           → BLOCK — mandatory fix before shipping
```
