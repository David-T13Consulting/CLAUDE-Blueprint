---
title: "Evals"
category: "measuring quality"
requires:
  - "golden-dataset"
  - "rubric"
  - "eval-harness"
related:
  - "observability"
  - "red-teaming"
---

What it is
----------
Evals are the scorecards that measure AI outputs against explicit quality criteria. They turn subjective review into repeatable, weighted scoring.

Problem it solves
-----------------
They solve the problem of trusting AI work by making quality visible, comparable, and auditable over time.

How it works
-------------
An eval runs a skill output through either exact-match scoring or an LLM judge, applies a rubric, and produces a weighted grade. It stores baselines and flags regressions when the score drops.

Depends on / feeds
------------------
- `./golden-dataset.md`
- `./rubric.md`
- `./eval-harness.md`
- `../.claude/evals/README.md`
- `../.claude/evals/rubrics/human-eval.md`

Preview
-------
```text
EVAL SCORECARD
━━━━━━━━━━━━━━

SKILL: research
DATE: 2026-08-05

SCORES:
  1. Substance vs. Filler (weight 2.0): 4/5 — Specific examples referenced from CLAUDE.md
  2. Honesty & Uncertainty (weight 2.0): 5/5 — Explicit assumptions and open questions listed

WEIGHTED SCORE: 85% → STRONG
BASELINE COMPARISON: First evaluation — baseline established
RECOMMENDATIONS:
  - Link the new concept docs to existing agent and rubric files.
```
