# Eval Rubric: Architecture Output

> Scores `/architect` outputs against quality dimensions.

## Dimensions

### 1. Data Model Correctness (weight: 2.0)

Are types fully defined, correctly typed, and covering all entities?

| Score | Anchor |
|-------|--------|
| 1 | No data model or uses `any` |
| 2 | Basic types but incomplete or loosely typed |
| 3 | All entities typed with required fields |
| 4 | Full type definitions with optionals, enums, and relationships |
| 5 | Discriminated unions, type guards, and validation schemas |

### 2. Service Design (weight: 1.5)

Are service boundaries clean with clear inputs, outputs, and responsibilities?

| Score | Anchor |
|-------|--------|
| 1 | No service layer defined |
| 2 | Services mentioned but contracts unclear |
| 3 | Services with defined inputs and outputs |
| 4 | Clean separation of concerns with error contracts |
| 5 | Services with dependency injection points and testability |

### 3. Integration Quality (weight: 2.0)

Does the plan integrate cleanly with existing code without destabilizing it?

| Score | Anchor |
|-------|--------|
| 1 | Ignores existing architecture entirely |
| 2 | Acknowledges existing code but plan conflicts |
| 3 | Integrates with existing patterns |
| 4 | Extends existing patterns with clear modification plan |
| 5 | Enhances architecture while maintaining backward compatibility |

### 4. Risk Assessment (weight: 1.5)

Are technical risks identified with concrete mitigations?

| Score | Anchor |
|-------|--------|
| 1 | No risks mentioned |
| 2 | Generic risks ("might be slow") |
| 3 | Specific risks with severity levels |
| 4 | Risks with concrete mitigation strategies |
| 5 | Risks categorized with fallback plans and monitoring |

### 5. Implementation Order (weight: 1.0)

Is the build order logical and dependency-aware?

| Score | Anchor |
|-------|--------|
| 1 | No order specified |
| 2 | List of files without ordering rationale |
| 3 | Dependency-ordered with brief rationale |
| 4 | Phased approach with testable checkpoints |
| 5 | Incremental delivery plan — each step produces working code |

## Grading

```
Max possible = 5 * (2+1.5+2+1.5+1) = 40
>= 80%: STRONG | 60-79%: ADEQUATE | 40-59%: WEAK | < 40%: FAIL
```
