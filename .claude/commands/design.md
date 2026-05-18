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
> Design is complete. Does this match your vision? Choose your next step:
>
> **Agentic path** (stay in this flow):
> - ✅ Build it → run `/architect [feature name]`
> - 🔄 Change [X] → specify what needs redesigning; the designer re-runs with feedback
> - ❌ Scrap and redesign → start over from design (or back to research)
>
> **Visual path** (refine in Claude Design first):
> - 🎨 Take to Claude Design → open `claude.ai/design`, paste this spec as the starting prompt, refine into a visual prototype, then return with the Claude Design URL or handoff bundle. The designer will update the `design_output` contract with `claude_design_handoff_url`, and the architect will consume the visual prototype as the authoritative source instead of the ASCII spec.
>
> Both paths converge at `/architect`. The visual path is recommended when the feature is UI-heavy, novel, or needs stakeholder buy-in before engineering invests effort.

Do NOT proceed to `/architect` without explicit Product Owner approval.

**After the Product Owner responds, log to `.claude/metrics/log.md`** (append one or more rows):

- Approved (either path): `| [date] | [feature] | collaboration | handoff_success | gate_2_approved | — |` and `| [date] | [feature] | intervention | gate_approved | gate_2 | — |`
- "Change X" (rework): `| [date] | [feature] | collaboration | handoff_failure | gate_2_rework | [what changed] |` and `| [date] | [feature] | redundancy | rework | design_rerun | [reason] |`
- "Just do it" / skip: `| [date] | [feature] | intervention | gate_overridden | gate_2 | [reason] |`
- VETO accepted: `| [date] | [feature] | collaboration | handoff_failure | gate_2_veto | [veto reason] |`
- VETO overridden by PO: `| [date] | [feature] | intervention | veto_overridden | designer_veto | [reason] |`

Also log the agent run itself: `| [date] | [feature] | redundancy | agent_run | designer | — |`
