---
title: "Agent Harness"
category: "agent runtime"
requires: []
related:
  - "eval-harness"
  - "governance"
---

What it is
----------
Not to be confused with `eval-harness.md`: an agent harness is the runtime scaffolding around an agent, including tool routing, memory, and the control loop that decides next actions.

Problem it solves
-----------------
It solves the need to orchestrate multi-step agent behavior safely and consistently, keeping the agent from wandering off task.

How it works
-------------
An agent harness receives the task, tracks memory and tools, decides the next action, and either executes a tool or returns a response. In this repo, the actual agent harnesses are represented by `.claude/agents/*.md` definitions.

Depends on / feeds
------------------
- `./guardrails.md`
- `./observability.md`
- `../.claude/agents/orchestrator.md`
- `../.claude/agents/eval-judge.md`

Preview
-------
```text
agent harness:
- task: create concept docs
- tools: Read, Write, Grep, Glob
- memory: recent repo state, branch context
- next action: create /concepts/ files
```
