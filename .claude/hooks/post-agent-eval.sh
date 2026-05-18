#!/usr/bin/env bash
# PostToolUse hook: detect # CONTRACT: in Agent output and prompt eval-judge scoring
# Receives hook payload via stdin as JSON

INPUT=$(cat)

# Check if the agent response contains a CONTRACT block
if echo "$INPUT" | grep -q '"# CONTRACT:'; then
  # Extract the contract type name
  CONTRACT_TYPE=$(echo "$INPUT" | grep -o '"# CONTRACT: [^\\]*' | head -1 | sed 's/"# CONTRACT: //')
  echo "[POST-AGENT EVAL] Subagent produced # CONTRACT: ${CONTRACT_TYPE}. Spawn eval-judge: Agent(subagent_type='eval-judge', prompt='Score the ${CONTRACT_TYPE} output above. Rubric: .claude/evals/rubrics/. Baseline dir: .claude/evals/baselines/.')"
elif echo "$INPUT" | grep -q '# CONTRACT:'; then
  CONTRACT_TYPE=$(echo "$INPUT" | grep "# CONTRACT:" | head -1 | sed 's/.*# CONTRACT: //' | tr -d '"')
  echo "[POST-AGENT EVAL] Subagent produced # CONTRACT: ${CONTRACT_TYPE}. Spawn eval-judge: Agent(subagent_type='eval-judge', prompt='Score the ${CONTRACT_TYPE} output above. Rubric: .claude/evals/rubrics/. Baseline dir: .claude/evals/baselines/.')"
fi

exit 0
