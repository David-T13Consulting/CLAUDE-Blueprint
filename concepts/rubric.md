---
title: "Rubric"
category: "measuring quality"
requires: []
related:
  - "evals"
  - "llm-as-a-judge"
---

What it is
----------
A rubric is the scoring guide that defines quality criteria and anchors for open-ended AI work. It is the reference used by both human evaluators and automated judges.

Problem it solves
-----------------
It solves the ambiguity in assessing creative or reasoning-heavy outputs by making evaluation criteria explicit and consistent.

How it works
-------------
A rubric contains dimensions, weights, and score anchors. The judge agent loads the rubric from real repo paths and uses it to convert narrative output into numeric scores.

Depends on / feeds
------------------
- `./evals.md`
- `./llm-as-a-judge.md`
- `../.claude/evals/rubrics/human-eval.md`
- `../.claude/evals/rubrics/research.md`
- `../.claude/evals/rubrics/architect.md`

Preview
-------
```text
1. Substance vs. Filler (weight 2.0)
   5: Every statement is grounded in specifics.
   3: Mix of generic and specific.
   1: Entirely generic.
```
