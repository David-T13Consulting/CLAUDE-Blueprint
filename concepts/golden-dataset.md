---
title: "Golden Dataset"
category: "measuring quality"
requires: []
related:
  - "evals"
  - "observability"
---

What it is
----------
A golden dataset is a curated set of reference examples with known correct outputs. It is used for closed-ended evaluation where exact answers are expected.

Problem it solves
-----------------
It solves the need for deterministic verification when AI behavior should match a specific, known correct result.

How it works
-------------
Each case in the golden dataset contains an input, an expected output, and metadata for the evaluation harness. The eval system runs these cases and compares model answers against the answer key.

Depends on / feeds
------------------
- `./evals.md`
- `./eval-harness.md`
- `./observability.md`

Preview
-------
```yaml
- id: "101"
  input: "Summarize the product strategy in one sentence."
  expected_output: "A blueprint for AI product development with built-in decision gates, quality evals, and safety checks."
  category: "product strategy"
```
