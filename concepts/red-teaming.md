---
title: "Red Teaming"
category: "keeping it safe"
requires: []
related:
  - "guardrails"
  - "evals"
---

What it is
----------
Red teaming is the practice of attacking your own AI system with adversarial inputs to expose vulnerabilities.

Problem it solves
-----------------
It solves the blind spots in safety controls by finding failure modes that normal testing misses.

How it works
-------------
Teams or tools generate malicious prompts, edge-case scenarios, and policy evasion attempts, then record the failures so guardrails and evals can be improved.

Depends on / feeds
------------------
- `./guardrails.md`
- `./evals.md`
- `./observability.md`

Preview
-------
```text
red-team case:
- attack: prompt injection via system instructions
- result: model bypassed safety filter
- fix: tighten guardrail rule and add eval case
```
