# Eval Framework

> **This framework scores agent/skill outputs against rubrics to ensure quality at scale.**
> It detects regressions, establishes baselines, and provides actionable improvement recommendations.

---

## How It Works

1. A skill produces output (e.g., `/research`, `/qa`, `/security`)
2. The eval judge agent (`.claude/agents/eval-judge.md`) is spawned
3. The judge loads the matching rubric from `.claude/evals/rubrics/[skill].md`
4. Each dimension is scored 1-5 with weights
5. A weighted percentage is calculated and graded
6. The score is compared to the baseline (if one exists)
7. Regressions (>10 point drop) are flagged

## When Evals Run

| Task Level | Eval Behavior |
|-----------|--------------|
| **L1 (Trivial)** | Never — no overhead for trivial tasks |
| **L2 (Standard)** | On request only — invoke with `/eval [skill output]` |
| **L3 (Complex)** | Automatic — after each skill completes, before the next gate |
| **L4 (Orchestrated)** | Every subtask — orchestrator runs eval on all skill outputs |

## Grading Scale

| Grade | Percentage | Meaning |
|-------|-----------|---------|
| **STRONG** | >= 80% | Output is thorough, well-reasoned, and actionable |
| **ADEQUATE** | 60-79% | Output meets the minimum bar but has room for improvement |
| **WEAK** | 40-59% | Output has significant gaps — consider re-running the skill |
| **FAIL** | < 40% | Output is not usable — must be re-done |

## Dimension Scoring (1-5)

| Score | Meaning |
|-------|---------|
| 1 | Missing or unusable |
| 2 | Present but superficial |
| 3 | Adequate — meets minimum bar |
| 4 | Good — thorough and insightful |
| 5 | Excellent — would impress a domain expert |

## Regression Detection

- On each eval run, the score is saved to `.claude/evals/baselines/[skill]-[date].yaml`
- On subsequent runs, the judge compares to the most recent baseline
- If the score drops by **10+ percentage points**, a regression is flagged
- Regressions are **flags, not blocks** — the human decides whether to act

## Cold Start

On a fresh project, there are no baselines. The first eval for each skill establishes the baseline. Regression detection activates from the second run onward.

## Directory Structure

```
.claude/evals/
  README.md               ← This file
  rubrics/
    research.md           ← Scoring rubric for /research
    design.md             ← Scoring rubric for /design
    architect.md          ← Scoring rubric for /architect
    qa.md                 ← Scoring rubric for /qa
    security.md           ← Scoring rubric for /security
    validate.md           ← Scoring rubric for /validate
    perf.md               ← Scoring rubric for /perf
    route.md              ← Scoring rubric for /route
  baselines/
    README.md             ← Baseline system docs
    [skill]-[date].yaml   ← Auto-generated baseline files
```

## How to Invoke

The eval judge runs automatically for L3+ tasks. For manual invocation:

1. Run a skill (e.g., `/research [problem]`)
2. Ask: "Evaluate this research output" or use the orchestrator
3. The eval judge produces a scorecard with grades and recommendations

The orchestrator automatically invokes the eval judge for L4 subtask outputs.
