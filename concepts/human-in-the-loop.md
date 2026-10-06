---
title: "Human in the Loop"
category: "keeping it safe"
requires: []
related:
  - "governance"
  - "observability"
---

What it is
----------
Human in the loop is a process where a person reviews, approves, or corrects AI outputs before they are released or acted on.

Problem it solves
-----------------
It solves the need for human judgment on risky, high-stakes, or low-confidence decisions that the AI should not handle autonomously.

How it works
-------------
Low-confidence or policy-blocked cases are routed to a reviewer who validates the result, edits it, or rejects it. The decision is then logged for audit and governance.

Depends on / feeds
------------------
- `./governance.md`
- `./observability.md`
- `./guardrails.md`

Preview
-------
```text
review request:
- case_id: 202
- reason: low confidence on compliance check
- reviewer: product owner
- decision: approve with edits
```
