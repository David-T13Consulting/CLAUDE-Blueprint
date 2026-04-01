# Eval Rubric: Performance Output

> Scores `/perf` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Profiling Rigor (weight: 2.0)

Are specific profiling tools used and named, with quantitative measurements?

| Score | Anchor |
|-------|--------|
| 1 | No profiling tools mentioned |
| 2 | Vague analysis ("seems fast") without tools or measurements |
| 3 | Profiling tools named (React DevTools, Hermes, Flipper, Lighthouse) with component-level analysis |
| 4 | Tools used with specific measurements: re-render counts, frame timing, component render duration |
| 5 | Full profiling with before/after measurements, flame graphs referenced, and optimization recommendations per bottleneck |

### 2. Performance Budgets (weight: 2.0)

Are quantitative performance budgets defined and checked?

| Score | Anchor |
|-------|--------|
| 1 | No performance budgets |
| 2 | Vague goals ("should be fast") |
| 3 | Key budgets defined: JS bundle <200KB, TTI <3s, 60fps target, API p95 <2s |
| 4 | All budgets checked with pass/fail: bundle, TTI, FCP, LCP, CLS, INP, frame rate, memory, API latency, cold start |
| 5 | Budgets with actual measurements, trend comparison, and platform-specific targets (Core Web Vitals) |

### 3. Memory Analysis (weight: 1.5)

Are memory bounds, cleanup, and leak potential genuinely evaluated?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "No leaks found" — no evidence shown |
| 3 | Bounded structures verified, cleanup on unmount checked, memory growth estimated |
| 4 | Specific leak risks identified per pattern (timers, subscriptions, closures), with prevention strategy |
| 5 | Memory growth profile measured (initial → 30min), LRU eviction verified, worst-case scenarios modeled |

### 4. Network Efficiency (weight: 1.5)

Are redundant calls, caching, retry logic, and timeout handling verified?

| Score | Anchor |
|-------|--------|
| 1 | Not analyzed |
| 2 | Basic check on API call existence |
| 3 | Duplicate detection, caching strategy per data type, and timeout verified |
| 4 | Full network audit: dedup, caching with TTL, exponential backoff retry, waterfall vs parallel analysis |
| 5 | Network optimization with offline handling, request prioritization, and bandwidth estimation |

### 5. Cost Analysis (weight: 2.0)

For AI features: are token costs calculated with model tiering and optimization plan?

| Score | Anchor |
|-------|--------|
| 1 | Not analyzed (for AI features) or N/A correctly noted |
| 2 | "Costs seem reasonable" — no numbers |
| 3 | Tokens per interaction estimated, cost per user per day/month calculated |
| 4 | Full cost template: input/output tokens, cost per interaction, per user per day/month, margin vs revenue |
| 5 | Cost analysis with model tiering strategy (Haiku/Sonnet/Opus), context window management, caching opportunities, and sensitivity analysis |

*Note: For non-AI apps, score this dimension as N/A (excluded from calculation).*

### 6. Bundle & Startup Impact (weight: 1.0)

Is the feature's size and startup impact quantified and optimized?

| Score | Anchor |
|-------|--------|
| 1 | Not mentioned |
| 2 | "Added some dependencies" |
| 3 | New deps listed with gzipped sizes, bundle impact quantified |
| 4 | Bundle analysis with lighter alternatives considered, tree-shaking verified, lazy loading applied |
| 5 | Full bundle audit: composition analysis (Expo Atlas/webpack), startup path impact, code splitting, deferred initialization |

## Grading

For AI apps (6 dimensions):
```
Max possible = 5 * (2+2+1.5+1.5+2+1) = 50
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```

For non-AI apps (5 dimensions, cost excluded):
```
Max possible = 5 * (2+2+1.5+1.5+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
