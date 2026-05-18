#!/usr/bin/env bash
# Stop hook: remind Claude to update memory files after gate decisions
# Fires when Claude's turn ends

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
  exit 0
fi

# Check for untracked or modified files
UNTRACKED=$(git -C "$REPO_ROOT" status --porcelain 2>/dev/null | grep '^??' | wc -l | tr -d ' ')
MODIFIED=$(git -C "$REPO_ROOT" status --porcelain 2>/dev/null | grep -v '^??' | wc -l | tr -d ' ')

if [ "$UNTRACKED" -gt 0 ] || [ "$MODIFIED" -gt 0 ]; then
  echo "[~/.claude/stop-hook-git-check.sh]: There are untracked files in the repository. Please commit and push these changes to the remote branch."
fi
