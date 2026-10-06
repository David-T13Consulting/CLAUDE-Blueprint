# Agent Harness Artifacts

This directory contains the runtime scaffolding for inspecting and validating `.claude/agents` definitions.

## Purpose

The agent harness artifacts are designed to:

- document the runtime role of `.claude/agents/*.md` files
- provide a CLI to validate agent metadata and expected tool permissions
- keep the agent runtime layer aligned with the blueprint's guardrails and observability concepts

## Files

- `agent_harness/harness.py` — runtime validator and inspection tool for agent definitions
- `agent_harness/README.md` — documentation for the agent harness artifacts

## Quick Start

Inspect the agent definitions in `.claude/agents`:

```bash
python3 agent_harness/harness.py --list
```

Validate agent metadata and tool permissions:

```bash
python3 agent_harness/harness.py --validate
```

## Notes

The harness is intentionally lightweight and does not execute agents.
It is meant to increase confidence that the agent definitions are consistent and that agent metadata is compliant with the blueprint expectations.
