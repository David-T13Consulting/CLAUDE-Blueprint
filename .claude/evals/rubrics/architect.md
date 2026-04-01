# Eval Rubric: Architecture Output

> Scores `/architect` outputs against quality dimensions.
> Version: 2.0

## Dimensions

### 1. Data Model Correctness (weight: 2.0)

Are types fully defined, strictly typed, and validated at boundaries?

| Score | Anchor |
|-------|--------|
| 1 | No data model or uses `any` |
| 2 | Basic types but incomplete or loosely typed |
| 3 | All entities typed with required fields and proper TypeScript annotations |
| 4 | Discriminated unions, branded types, and Zod schemas for external data validation |
| 5 | Full type system with runtime validation, type guards, validation schemas, and error types per domain |

### 2. Service & API Design (weight: 1.5)

Are service boundaries clean with typed contracts, and do API designs follow standards?

| Score | Anchor |
|-------|--------|
| 1 | No service layer defined |
| 2 | Services mentioned but contracts unclear |
| 3 | Services with typed inputs, outputs, and named error types |
| 4 | Clean separation of concerns with RFC 7807 error format, typed error hierarchy, and testability |
| 5 | Full API contract spec: REST conventions, versioning, pagination, rate limiting, and dependency injection |

### 3. Architecture Pattern (weight: 1.5)

Is a named architecture pattern chosen and consistently applied?

| Score | Anchor |
|-------|--------|
| 1 | No architecture pattern identified |
| 2 | Pattern implied but not named or enforced |
| 3 | Named pattern (MVVM, Clean Architecture, etc.) with rationale and layer map |
| 4 | Pattern with SOLID compliance verified, anti-patterns identified, and layer boundaries enforced |
| 5 | Pattern with ADR (Architecture Decision Record), trade-off analysis, and migration path from current state |

### 4. Security & Observability Architecture (weight: 1.5)

Are security and observability planned at the architecture level?

| Score | Anchor |
|-------|--------|
| 1 | No security or observability consideration |
| 2 | Mentioned but vague ("we'll add logging") |
| 3 | Security layers defined (transport, storage, auth, input boundary) |
| 4 | Security layers + observability plan (logs, metrics, traces, errors) with specific tools |
| 5 | Full security architecture with encryption standards, secrets management, plus observability with alerting thresholds |

### 5. Testing & Caching Strategy (weight: 1.0)

Is the testing pyramid specified with coverage targets, and is caching strategy defined?

| Score | Anchor |
|-------|--------|
| 1 | No testing or caching plan |
| 2 | "We'll write tests" or "we'll cache things" |
| 3 | Testing pyramid defined (70/20/10) with what to test at each level; caching strategy per data type |
| 4 | Testing plan with mock strategy (MSW), specific tools, and coverage targets; caching with TTL, max size, and invalidation |
| 5 | Testing plan with state management decision tree, boundary-based mocking, and cache eviction strategy with performance budgets |

### 6. Risk Assessment Quality (weight: 1.5)

Are technical risks categorized with concrete mitigations and monitoring?

| Score | Anchor |
|-------|--------|
| 1 | No risks mentioned |
| 2 | Generic risks ("might be slow") |
| 3 | Specific risks with category, severity, and probability |
| 4 | Risks with concrete mitigation strategies and monitoring approach |
| 5 | Risk matrix with fallback plans, rollback strategy, and verifiable checkpoints per implementation step |

## Grading

```
Max possible = 5 * (2+1.5+1.5+1.5+1+1.5) = 45
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
