---
title: "LLM as a Judge"
category: "measuring quality"
requires:
  - "rubric"
related:
  - "evals"
  - "eval-harness"
---

What it is
----------
LLM-as-a-judge is the pattern of using a language model to score other language model outputs. It replaces or supplements exact-match scoring for open-ended tasks.

Problem it solves
-----------------
It solves the problem of evaluating subjective or creative outputs where exact answers don’t exist and human judges are expensive.

How it works
-------------
The judge prompt loads the rubric and the model output, then returns graded scores and justifications. In this repo, `.claude/agents/eval-judge.md` is the real judge agent.

Depends on / feeds
------------------
- `./rubric.md`
- `./eval-harness.md`
- `../.claude/agents/eval-judge.md`

Preview
-------
```text
Judge prompt summary:
- skill: research
- rubric: Substance, Honesty, Actionability, Correctness
- output: [contract + human report]

Result:
- Substance: 4/5 — specific project details cited.
- Correctness: 5/5 — aligned with CLAUDE.md requirements.
```
