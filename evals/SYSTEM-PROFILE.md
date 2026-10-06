# Evaluation System Profile

## Overview

This repository is a blueprint for AI-assisted development. The `evals/` directory contains a runnable evaluation system that connects the repository's concept-level docs, structured I/O contracts, and agent definitions into a concrete measurement pipeline.

This system is intentionally lightweight and platform-agnostic. It can run in any Python 3.9+ environment with no external dependencies, and it falls back safely when the Anthropic API key is not configured.

## Scope

- `evals/harness.py` — evaluation orchestration runtime for golden dataset cases
- `evals/judge/scorer.py` — LLM judge runner and stubbed fallback
- `evals/data/golden_dataset.json` — curated reference cases grounded in this blueprint
- `evals/redteam/cases.json` — adversarial prompts for safety validation
- `evals/README.md` — usage documentation for the eval artifacts
- `agent_harness/harness.py` — runtime scaffolding for `.claude/agents/*.md`
- `agent_harness/README.md` — agent harness concept and CLI guidance

## Purpose

The evaluation system exists to:

- validate open-ended agent outputs against project-specific quality criteria
- measure consistency with the repository's structured contract schema
- provide a reproducible harness for golden dataset tests and judge-based scoring
- document the attack surface and safe runtime behavior for AI evaluation

## Grounding in this repo

This profile is grounded in the repository's actual artifacts:

- `.claude/contracts/schemas.md` — machine-readable contract definitions
- `.claude/evals/rubrics/` — quality dimensions for judge scoring
- `.claude/agents/` — agent definitions and tool permissions
- `concepts/` docs — design intent for evals, agent harness, guardrails, and governance

## Technical architecture

### Runtime

The eval runtime is Python-based and uses only the standard library. It supports two scoring modes:

1. `exact-match`
   - Compares model output to a canonical expected answer.
   - Useful for deterministic verification of reference cases.

2. `llm-judge`
   - Delegates scoring to an LLM using `.claude/evals/rubrics/`.
   - Uses the Anthropic API when `ANTHROPIC_API_KEY` is configured.
   - Falls back to a stub with an explicit message if the key is missing.

### Data

- `evals/data/golden_dataset.json` contains curated cases keyed to the blueprint.
- `evals/redteam/cases.json` captures adversarial and safety-oriented cases.

### Observability

The harness emits a JSON-friendly summary report that includes:

- total cases run
- pass / fail counts
- categories covered
- scoring mode used
- any runtime warnings or API fallback messages

## Security and sensitive data

- No API keys are stored in source control.
- `ANTHROPIC_API_KEY` is read only from the environment.
- The runtime does not persist user input or model responses beyond the current run.
- The harness avoids external dependencies to minimize supply chain risk.

## Risk tier

This is a design-time evaluation system for a blueprint repository.

- Risk level: **moderate**
- Primary concerns:
  - model output quality when using open-ended scoring
  - prompt injection and hallucination in judge-based evaluation
  - accidental exposure of private API keys if misconfigured

## How to use

1. Read `evals/README.md` for commands and workflow.
2. Run `python3 evals/harness.py --run --judge exact` to verify the golden dataset.
3. Run `python3 evals/harness.py --run --judge llm` if `ANTHROPIC_API_KEY` is configured.
4. Use `agent_harness/harness.py --validate` to inspect `.claude/agents` definitions.

## Notes

This profile is intentionally focused on artifact-level reproducibility, not on a deployed AI product. It provides the scaffolding necessary to move from concept to runnable evaluation without introducing project-specific runtime dependencies.
