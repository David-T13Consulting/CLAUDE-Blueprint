# AI Concepts Knowledge Layer

> Not to be confused: `eval-harness.md` is the measurement harness; `agent-harness.md` is the runtime harness.

## Table of contents

### Measuring Quality
- [Evals](./evals.md)
- [Golden Dataset](./golden-dataset.md)
- [Rubric](./rubric.md)
- [LLM as a Judge](./llm-as-a-judge.md)
- [Eval Harness](./eval-harness.md)

### Keeping It Safe
- [Guardrails](./guardrails.md)
- [Human in the Loop](./human-in-the-loop.md)
- [Red Teaming](./red-teaming.md)

### Running It Live
- [Observability](./observability.md)
- [Governance](./governance.md)

### Agent Runtime
- [Agent Harness](./agent-harness.md)

## Dependency map

- `llm-as-a-judge` → `rubric`
- `red-teaming` → `guardrails`, `evals`
- `governance` → `human-in-the-loop`
- `observability` → `evals`, `guardrails`
- `evals` → `eval-harness`
- `golden-dataset` → `evals`
- `guardrails` → `human-in-the-loop`
- `eval-harness` → `golden-dataset`, `llm-as-a-judge`
- `agent-harness` → `agents`
