---
description: Run Software Architecture planning on a designed feature. Defines data models, service interfaces, state management, file plan, and implementation order. Requires design to exist first. Stops at Gate 3 for Product Owner approval before implementation begins.
---

Spawn the `architect` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name to architect.

**Prerequisite check:** Before spawning, verify a Design Specification exists for this feature (in the conversation or referenced in PROJECT_STATE.md). If no design exists, do NOT spawn — tell the user: "Run `/design [feature]` first. Architecture without a design is building the wrong thing correctly."

The subagent will produce a full Architecture Plan including:
- Data model (entities, relationships, types)
- Service interfaces and API contracts between components
- State management approach (local vs. shared vs. persisted)
- Data flow diagram (Input → Processing → Storage → Output)
- Caching strategy per data source
- File plan (what to create/modify, in what order)
- Implementation order (dependency graph)
- Failure modes at the system level (API down, race conditions, storage full)
- Integration points with existing architecture
- Technical risks and mitigations
- Structured `# CONTRACT: architecture_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim, then stop and present:

> **GATE 3: APPROACH?**
> Architecture is planned. Does this technical approach make sense?
> - ✅ Go → begin implementation (Engineer activates)
> - 🔄 Adjust [X] → specify what needs rethinking; the architect re-runs with feedback
> - ❌ Different approach → restart architecture with new constraints

Do NOT begin implementation without explicit Product Owner approval.

**After the Product Owner responds, log to `.claude/metrics/log.md`** (append one or more rows):

- Approved: `| [date] | [feature] | collaboration | handoff_success | gate_3_approved | — |` and `| [date] | [feature] | intervention | gate_approved | gate_3 | — |`
- "Adjust X" (rework): `| [date] | [feature] | collaboration | handoff_failure | gate_3_rework | [what changed] |` and `| [date] | [feature] | redundancy | rework | architect_rerun | [reason] |`
- "Just do it" / skip: `| [date] | [feature] | intervention | gate_overridden | gate_3 | [reason] |`
- VETO accepted: `| [date] | [feature] | collaboration | handoff_failure | gate_3_veto | [veto reason] |`
- VETO overridden: `| [date] | [feature] | intervention | veto_overridden | architect_veto | [reason] |`

Also log the agent run: `| [date] | [feature] | redundancy | agent_run | architect | — |`
