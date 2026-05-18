---
description: Run UX Research on a problem. Validates the problem, sizes the market, profiles the user (JTBD), maps competitors, and produces a Kano feature classification. Stops at Gate 1 for Product Owner approval before proceeding to design.
---

Spawn the `researcher` subagent via the Agent tool. Pass `$ARGUMENTS` as the problem statement to investigate.

The subagent will produce a full UX Research Report including:
- Problem Validation Scorecard (1-10 per dimension, average, GREEN LIGHT / EXPLORE ONLY / PARK IT)
- Market sizing (TAM/SAM/SOM)
- Target user analysis using Jobs-to-Be-Done framework
- Competitive landscape with gap analysis
- Feature classification using Kano Model
- User stories (3-5, JTBD-informed format)
- Failure mode and risk matrix
- Problem-Solution Fit assessment
- Structured `# CONTRACT: research_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim, then stop and present:

> **GATE 1: PROCEED?**
> Research is complete. Should we proceed to design, rethink the problem, or kill it?
> - ✅ Proceed → run `/design [feature name]`
> - 🔄 Rethink → clarify what needs re-researching
> - ❌ Kill it → log the decision in DECISIONS.md and stop

Do NOT proceed to `/design` without explicit Product Owner approval.
