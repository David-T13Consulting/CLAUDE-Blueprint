---
title: "Eval Harness"
category: "measuring quality"
requires:
  - "evals"
related:
  - "llm-as-a-judge"
  - "golden-dataset"
---

What it is
----------
An eval harness is the runtime that executes evaluations end-to-end. It feeds cases to a scorer, handles retries and parsing, and emits a consolidated report.

Problem it solves
-----------------
It solves the need to run many evaluation cases consistently and safely, including scoring, baseline comparison, and result aggregation.

How it works
-------------
The harness loads test cases from a dataset, chooses the scorer (exact-match or LLM judge), runs each case, gathers scores, and writes a summary report.

Depends on / feeds
------------------
- `./evals.md`
- `./golden-dataset.md`
- `./llm-as-a-judge.md`

Preview
-------
```text
Eval harness run:
- cases: 12
- scorer: LLM-as-a-judge
- passed: 9
- weighted_score: 82.3%
- regression: no
```
