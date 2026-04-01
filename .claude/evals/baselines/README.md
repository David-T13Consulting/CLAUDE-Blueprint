# Eval Baselines

This directory stores eval score baselines — one file per skill per evaluation run.

## File Format

```yaml
skill: "research"
date: "2026-04-01"
weighted_score_percent: 78.5
grade: "ADEQUATE"
dimensions:
  - name: "Problem Clarity"
    score: 4
    weight: 2.0
  - name: "Scorecard Rigor"
    score: 3
    weight: 2.0
  # ...
```

## Naming Convention

`[skill]-[YYYY-MM-DD].yaml`

Example: `research-2026-04-01.yaml`

## How It Works

- **First run**: No baseline exists. The eval judge creates the first baseline file.
- **Subsequent runs**: The judge reads the most recent baseline for the skill and compares.
- **Regression**: If the current score is 10+ points below the baseline, a regression is flagged.
- **Baseline updates**: Every eval run creates a new baseline file (doesn't overwrite old ones).

## Maintenance

- Old baselines accumulate over time. They're small (YAML) and cheap to keep.
- To reset a baseline (e.g., after a major restructuring), delete the most recent file for that skill.
- Never edit baseline files manually — they're machine-generated.
