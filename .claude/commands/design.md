---
description: Run Product Design on a validated feature. Defines the interaction model, screen flow, states, component specs, heuristic audit, and behavioral design. Requires research to exist first. Stops at Gate 2 for Product Owner approval before proceeding to architecture.
---

Spawn the `designer` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name to design.

**Prerequisite check:** Before spawning, verify a UX Research report exists for this feature (in the conversation or referenced in PROJECT_STATE.md). If no research exists, do NOT spawn — tell the user: "Run `/research [problem]` first. Design without validated research is waste."

The subagent will produce a full Design Specification including:
- Core interaction model and taps-to-value count
- Information architecture (tree structure)
- Screen flow diagram (including error/back flows)
- Every screen with ASCII layout mockup
- All states per screen (empty, loading, populated, error, offline, edge cases)
- New component specs (layout, visual treatment, interaction behavior, animation, accessibility)
- Nielsen's 10 Heuristics audit (all 10 checked against the design)
- Behavioral design notes (defaults, Peak-End rule, social proof)
- Benchmark verdict (does it feel at home next to iMessage / ChatGPT?)
- Structured `# CONTRACT: design_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim, then stop and present:

> **GATE 2: BUILD?**
> Design is complete. Does this match your vision?
> - ✅ Build it → run `/architect [feature name]`
> - 🔄 Change [X] → specify what needs redesigning; the designer re-runs with feedback
> - ❌ Scrap and redesign → start over from design (or back to research)

Do NOT proceed to `/architect` without explicit Product Owner approval.
