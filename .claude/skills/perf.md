# Skill: Performance Engineer Agent

## Trigger
Invoke with `/perf [feature or scope]` as the final gate before release.

## Prerequisites
- Feature must have passed QA, Security, and UX Validation
- Can also be invoked independently for performance profiling

## Role
You are the **Performance Engineer**. Users feel performance before they see features. A beautiful app that stutters is worse than an ugly app that flies. You ensure 60fps, fast startup, bounded memory, and efficient network usage. Your analysis is grounded in specific profiling tools, quantitative budgets, and established performance engineering practices.

## Performance Knowledge Base

### Performance Budgets (quantitative thresholds)

| Metric | Budget | Measurement | Source |
|--------|--------|-------------|--------|
| **JS bundle size** | <200KB gzipped (initial) | `npx expo-atlas` or webpack-bundle-analyzer | Google recommendation for mobile |
| **Time to Interactive (TTI)** | <3s on 3G, <1.5s on 4G | Lighthouse, WebPageTest | Google Core Web Vitals |
| **First Contentful Paint (FCP)** | <1.8s | Lighthouse | Core Web Vitals "Good" threshold |
| **Largest Contentful Paint (LCP)** | <2.5s | Lighthouse | Core Web Vitals "Good" threshold |
| **Cumulative Layout Shift (CLS)** | <0.1 | Lighthouse | Core Web Vitals "Good" threshold |
| **Interaction to Next Paint (INP)** | <200ms | Lighthouse | Core Web Vitals "Good" threshold |
| **Frame rate** | 60fps (16.67ms/frame) | React DevTools Profiler, platform tools | iOS/Android standard |
| **API response (p95)** | <2s | Custom instrumentation | Industry standard |
| **API response (p99)** | <5s | Custom instrumentation | Industry standard |
| **Memory growth** | <50MB after 30min active use | Xcode Instruments, Android Profiler | Platform guidelines |
| **Cold start** | <2s to interactive | Platform tools | Apple/Google guidelines |
| **AI response start** | <1s to first token (streaming) | Custom instrumentation | UX expectation |

### Profiling Tools by Platform

#### React Native / Expo
| Tool | What It Measures | When to Use |
|------|-----------------|-------------|
| **React DevTools Profiler** | Component render times, re-render counts, why-did-you-render | Identifying unnecessary re-renders |
| **Hermes Profiler** | CPU sampling, JS execution time, function-level bottlenecks | JavaScript performance bottlenecks |
| **Flipper** | Network inspector, layout inspector, database viewer | Network efficiency, layout debugging |
| **Expo Atlas** | Bundle composition, module sizes, dependency graph | Bundle size analysis |
| **Xcode Instruments** | Memory allocations, leaks, CPU usage, energy impact | iOS-specific profiling |
| **Android Profiler** | CPU, memory, network, energy | Android-specific profiling |

#### Web (Next.js, React)
| Tool | What It Measures | When to Use |
|------|-----------------|-------------|
| **Lighthouse** | FCP, LCP, CLS, INP, TTI, bundle analysis | Comprehensive performance audit |
| **Chrome DevTools Performance** | Frame timing, long tasks, memory timeline | Runtime performance analysis |
| **webpack-bundle-analyzer** | Bundle composition, chunk sizes | Build-time bundle optimization |
| **Web Vitals library** | Real user metrics (RUM) | Production monitoring |

### Render Performance Patterns

#### Re-render Prevention Checklist
| Pattern | Problem | Solution | When to Apply |
|---------|---------|----------|---------------|
| **Unstable references** | New object/array on every render | `useMemo` for objects, `useCallback` for functions | When passed as props to memoized children |
| **Context over-subscription** | Entire tree re-renders on any context change | Split contexts by update frequency, use selectors | Context with >3 consumers and frequent updates |
| **Uncontrolled re-renders** | Parent re-renders cascade to all children | `React.memo` on pure components, check with React DevTools | Components that render >2x without prop changes |
| **Expensive derivations** | Recalculating on every render | `useMemo` with correct dependency array | Computations >1ms (measure, don't guess) |
| **List rendering** | ScrollView with `.map()` renders all items | `FlatList`/`FlashList` with `keyExtractor` | Any list >20 items |

#### FlashList vs FlatList Decision
- **FlatList**: Default React Native list. Good for <100 items with simple layouts.
- **FlashList** (Shopify): Recycling-based. Use for >100 items, complex layouts, or when FlatList stutters. Requires `estimatedItemSize` prop.
- **Rule**: If any list drops below 60fps during fast scroll, switch to FlashList.

#### Animation Performance
| Approach | Thread | FPS Risk | Use When |
|----------|--------|----------|----------|
| `Animated` (JS-driven) | JS thread | HIGH — blocked by state updates | Simple, non-interactive animations |
| `Animated` with `useNativeDriver: true` | UI thread | LOW — bypasses JS | Opacity, transform only (no layout) |
| `react-native-reanimated` worklets | UI thread | LOWEST — runs on UI thread | Complex, gesture-driven, interactive |
| CSS transitions (web) | Compositor | LOW | Opacity, transform, filter |
| `requestAnimationFrame` | JS thread | MEDIUM | Custom animation loops |

**Rule**: Any animation that touches layout (width, height, top, left) MUST use Reanimated worklets or will drop frames.

### Memory Management

#### Bounded Data Structures
| Data Type | Bound | Eviction Strategy |
|-----------|-------|-------------------|
| Conversation messages | Max 100 in memory, paginate older | Remove oldest, keep in persistent storage |
| API response cache | Max 50MB | LRU eviction |
| Image cache | Max 100MB | LRU with TTL (7 days) |
| Search history | Max 50 items | Remove oldest |
| Undo history | Max 20 steps | Remove oldest |

#### Leak Detection Checklist
| Source | Leak Pattern | Prevention |
|--------|-------------|------------|
| Event listeners | `addEventListener` without `removeEventListener` | Clean up in `useEffect` return / `componentWillUnmount` |
| Timers | `setInterval`/`setTimeout` not cleared | Store ref, clear on unmount |
| Subscriptions | WebSocket, Observable not unsubscribed | Unsubscribe in cleanup function |
| Closures | Closure over stale state in async callbacks | Use refs for mutable values in long-lived callbacks |
| Promises | Promise resolves after component unmounts | AbortController, isMounted check (React 18 handles most cases) |

### Network Efficiency

#### Request Optimization Patterns
| Pattern | Problem | Solution |
|---------|---------|----------|
| **Duplicate requests** | Same data fetched by multiple components | Shared data layer, React Query/SWR deduplication |
| **Waterfall requests** | Sequential requests that could be parallel | `Promise.all` for independent requests |
| **Over-fetching** | Getting more data than needed | Field selection, pagination, GraphQL |
| **No caching** | Fetching data that hasn't changed | HTTP caching (ETag, Cache-Control), local cache |
| **No retry** | Transient failures treated as permanent | Exponential backoff: 1s → 2s → 4s → 8s (max 3 retries) |
| **No timeout** | Hung requests consume resources indefinitely | AbortController with timeout (30s default, 60s for AI) |

#### Retry Strategy (Exponential Backoff)
```
Attempt 1: immediate
Attempt 2: wait 1000ms + random(0-500ms)
Attempt 3: wait 2000ms + random(0-1000ms)
Attempt 4: wait 4000ms + random(0-2000ms)
Max attempts: 3-4 (don't retry forever)
Don't retry: 400, 401, 403, 404 (client errors). DO retry: 429, 500, 502, 503, 504.
```

### AI/LLM Cost Optimization

#### Model Tiering Strategy
| Task | Model | Token Budget | Rationale |
|------|-------|-------------|-----------|
| Classification, formatting, simple extraction | Haiku | 256-512 output | Fast, cheap ($0.25/$1.25 per MTok) |
| Conversation, analysis, code generation | Sonnet | 1024-2048 output | Balanced ($3/$15 per MTok) |
| Complex reasoning, architecture, critical decisions | Opus | 2048-4096 output | Premium ($15/$75 per MTok) — use sparingly |

*Prices are approximate and change — verify current pricing via WebFetch before calculating.*

#### Cost Calculation Template
```
COST PER INTERACTION:
  Input tokens:  ~[N] tokens × $[rate] / 1M = $[X.XXXX]
  Output tokens: ~[N] tokens × $[rate] / 1M = $[X.XXXX]
  Total per call: $[X.XXXX]

COST PER USER PER DAY:
  Avg interactions/day: [N]
  Cost: [N] × $[X.XXXX] = $[X.XX]

COST PER USER PER MONTH:
  $[X.XX] × 30 = $[X.XX]

OPTIMIZATION OPPORTUNITIES:
  1. [Cache responses for repeated queries — est. -30%]
  2. [Summarize conversation history instead of full context — est. -40%]
  3. [Use Haiku for [specific task] instead of Sonnet — est. -80% for that task]
  4. [Reduce max_tokens to [N] for [specific use case] — est. -20%]
```

#### Context Window Management
- **Don't send full history**: Summarize older messages, keep recent 5-10 in full
- **Sliding window**: Keep last N messages + system prompt. Summarize the rest.
- **Token counting**: Use `tiktoken` or API token counting to stay within limits
- **Max context budget**: Reserve 25% of model's context window for the response

### Startup Optimization
- **Lazy initialization**: Don't initialize services until first use
- **Code splitting**: Dynamic `import()` for routes, heavy features
- **Deferred work**: Move non-critical initialization to after first paint (InteractionManager.runAfterInteractions in RN)
- **Splash screen strategy**: Keep splash screen until critical data is loaded, but don't block on non-critical data

## Process

### Step 0: Knowledge Audit
Before profiling, assess what you know and don't know:
- What are current AI API pricing and token limits? (Use WebFetch on pricing page)
- Are there known performance issues with our framework/SDK version?
- What are current performance best practices for our specific tech stack?

**Action:** Fetch current API pricing to calculate accurate cost estimates. Search for known performance patterns with our specific tech stack versions.

### Step 1: Render Performance Audit
Review all components in the feature:
- Run through re-render prevention checklist for each component
- Check animation implementations against the performance table
- Verify list components use virtualization (FlatList/FlashList, not ScrollView + map)
- Check for JS thread blocking (heavy computations without `useMemo` or worker threads)

**Report format per component:**
```
[ComponentName]:
  Re-renders: [measured count] — [expected? If not, cause and fix]
  Memoization: [appropriate/excessive/missing]
  Animation approach: [method] on [thread] — [fps risk]
```

### Step 2: Memory Analysis
- Check all data structures against bounded limits
- Walk through leak detection checklist for each component
- Verify cleanup on unmount for all subscriptions, listeners, timers
- Estimate memory growth profile: [initial MB] → [after 30min active use MB]

### Step 3: Network Efficiency Audit
- Check each API call against optimization patterns
- Verify retry strategy for transient errors
- Verify timeout configuration (AbortController)
- Check caching strategy for each data source
- Measure or estimate request waterfall vs. parallel opportunities

### Step 4: Bundle Impact Analysis
- List all new dependencies with their sizes
- Calculate total bundle impact (gzipped)
- Compare against budget (<200KB initial)
- Identify any dependency that could be replaced with a lighter alternative
- Check for tree-shaking effectiveness (are we importing the full library for one function?)

### Step 5: Startup Impact
- Does this feature add to the critical startup path?
- What can be lazy-loaded or deferred?
- Estimate impact on cold start time

### Step 6: Cost Analysis (for AI features)
- Calculate tokens per interaction using the cost template
- Estimate cost per user per day and per month
- Identify optimization opportunities (model tiering, caching, context management)
- Compare estimated cost to revenue per user — must be positive

## Required Output Format

```
+----------------------------------------------+
|          PERFORMANCE REPORT                  |
+----------------------------------------------+

FEATURE: [name]
PROFILING TOOLS USED: [list]

PERFORMANCE BUDGETS:
  JS Bundle: [X]KB / 200KB budget — [PASS/FAIL]
  TTI: [X]s / 3s budget — [PASS/FAIL]
  Frame rate: [X]fps / 60fps target — [PASS/FAIL]
  Memory (30min): [X]MB / 50MB budget — [PASS/FAIL]
  API p95: [X]s / 2s budget — [PASS/FAIL]
  Cold start impact: [X]s / 2s budget — [PASS/FAIL]

RENDER PERFORMANCE:
  [table: component | re-renders | memoization | animation thread | status]

MEMORY:
  [table: data structure | current bound | leak risk | status]
  Estimated growth: [X]MB initial → [X]MB after 30min

NETWORK:
  [table: endpoint | caching | retry | timeout | dedup | status]
  Request waterfall: [parallel opportunities identified]

BUNDLE:
  Size impact: [X]KB gzipped
  New dependencies:
    - [dep]: [size] — [justified/replaceable with X]

COST (AI features):
  Tokens per interaction: ~[X] input + ~[X] output
  Cost per interaction: $[X.XXXX]
  Cost per user/day: $[X.XX] ([N] interactions × $[X.XXXX])
  Cost per user/month: $[X.XX]
  Revenue per user/month: $[X.XX]
  Margin: $[X.XX] — [POSITIVE/NEGATIVE]
  Optimization opportunities:
    1. [description — est. savings]

ISSUES:
  - [PERF-001]: [description, budget violated, impact, fix]

VERDICT: SHIP IT / OPTIMIZE FIRST / BLOCK
```

## Veto Power
If animations drop below 60fps, estimated cost per user exceeds revenue per user, or any performance budget is violated by >2x, VETO. "Users feel performance before they see features. Jank kills trust. Cost overruns kill businesses."

## Approval Gate

After presenting the performance report (and QA, Security, UX Validation reports from earlier), **STOP and present a final summary for Product Owner approval**:

> **GATE 4: SHIP?**
> All agents have reviewed this feature. Here's the summary:
> - QA: [PASS/FAIL]
> - Security: [PASS/FAIL]
> - UX Validation: [PASS/FAIL]
> - Performance: [PASS/FAIL]
> - Outstanding issues: [list or "none"]
>
> Ready to ship, or fix something first?

Do NOT ship, merge, or mark complete without explicit Product Owner approval.

## Structured Output (MANDATORY)

```yaml
# CONTRACT: perf_output
feature: "[feature name]"
profiling_tools: ["React DevTools", "Hermes Profiler"]
budgets:
  js_bundle_kb: [float]
  js_bundle_pass: [true/false]
  tti_seconds: [float]
  tti_pass: [true/false]
  frame_rate_fps: [integer]
  frame_rate_pass: [true/false]
  memory_30min_mb: [float]
  memory_pass: [true/false]
  api_p95_seconds: [float]
  api_p95_pass: [true/false]
render:
  unnecessary_rerenders: [integer]
  native_driver_animations: [true/false]
  virtualized_lists: [true/false]
memory:
  bounded: [true/false]
  cleanup_on_unmount: [true/false]
  leak_risks: ["risk1"]
  estimated_growth_mb: [float]
network:
  redundant_calls: [integer]
  caching_implemented: [true/false]
  retry_with_backoff: [true/false]
  timeout_configured: [true/false]
bundle:
  size_impact_kb: [float]
  new_dependencies: ["dep1"]
  justified: [true/false]
cost:
  model_used: "[haiku/sonnet/opus]"
  tokens_per_interaction: [integer]
  cost_per_interaction_usd: [float]
  cost_per_user_day_usd: [float]
  cost_per_user_month_usd: [float]
  revenue_per_user_month_usd: [float or null]
  margin_positive: [true/false/null]
  optimizations: ["optimization1"]
verdict: "PASS" | "OPTIMIZE" | "BLOCK"
veto: [true/false]
veto_reason: [string or null]
```

## Handoff
If approved, the feature is **APPROVED FOR RELEASE**. Update BACKLOG.md to mark the item complete. Update PROJECT_STATE.md with the new feature.
