---
title: "Observability"
category: "running it live"
requires: []
related:
  - "evals"
  - "guardrails"
  - "human-in-the-loop"
---

What it is
----------
Observability is the system for logging, tracing, and detecting drift in AI behavior and production usage.

Problem it solves
-----------------
It solves the problem of visibility: without observability, you cannot tell whether the model is failing, drifting, or being misused.

How it works
-------------
Observability captures request/response logs, confidence signals, and alerts on anomalies. Low-confidence or suspicious cases are forwarded to human review and evaluation workflows.

Depends on / feeds
------------------
- `./evals.md`
- `./guardrails.md`
- `./human-in-the-loop.md`

Preview
-------
```text
trace event:
- user_id: anon-123
- model: claude-3.5
- confidence: 0.42
- issue: unexpected tone shift
- action: route to review queue
```
