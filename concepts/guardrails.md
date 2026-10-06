---
title: "Guardrails"
category: "keeping it safe"
requires: []
related:
  - "red-teaming"
  - "human-in-the-loop"
  - "observability"
---

What it is
----------
Guardrails are live filters and policies that screen AI input and output for unsafe, disallowed, or low-confidence content.

Problem it solves
-----------------
They solve the risk of harmful or incorrect model behavior reaching users in production.

How it works
-------------
Guardrails apply rules before and after an AI call. They block or sanitize unsafe outputs and escalate ambiguous cases for review.

Depends on / feeds
------------------
- `./red-teaming.md`
- `./human-in-the-loop.md`
- `./observability.md`

Preview
-------
```text
guardrail check:
- input: user query
- output: model response
- rule: no personally identifiable info
- result: blocked
- action: escalate to human review
```
