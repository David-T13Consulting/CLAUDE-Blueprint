# Eval Artifacts

This directory contains the runnable evaluation system for the CLAUDE blueprint.

## Purpose

The eval artifacts let you:

- run curated golden dataset cases
- score outputs using exact-match and judge-based evaluation
- capture summary metrics for quality and regressions
- inspect safety-focused red-team cases

## Files

- `evals/harness.py` — top-level harness for evaluation runs
- `evals/judge/scorer.py` — judge runner with optional Anthropic integration
- `evals/data/golden_dataset.json` — curated reference cases
- `evals/redteam/cases.json` — adversarial prompt cases
- `evals/SYSTEM-PROFILE.md` — system profile for the eval layer

## Quick Start

Run the golden dataset with exact matching:

```bash
python3 evals/harness.py --run --judge exact
```

Run with the LLM judge if you have the Anthropic API key configured:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python3 evals/harness.py --run --judge llm
```

Inspect the available cases:

```bash
python3 evals/harness.py --list
```

Run and save a JSON summary report:

```bash
python3 evals/harness.py --run --judge exact --output eval-report.json
```

Validate the red-team case file schema:

```bash
python3 evals/harness.py --validate-redteam
```

## Notes

- If `ANTHROPIC_API_KEY` is not set, `--judge llm` will still run, but it will log that LLM scoring is unavailable and default to stub output.
- The harness is intentionally self-contained and uses only Python standard library features.
