# Migration Plan — Multi-Agent Architecture Upgrade

> **Audience:** Sonnet, executing this plan after Opus has scoped it.
> **Branch:** `claude/review-agent-architecture-Cz07o`
> **Pipeline mode:** BUILD · **Complexity:** L4 (orchestrated) · **Gates:** O-1 (decomposition) + O-2 (merged result)
> **Goal:** Convert the current "one main Claude wearing many hats" into a real multi-agent team using May-2026 Claude Code primitives (Skills, Subagents, Slash Commands, Hooks) used correctly.

---

## 0 · Why this plan exists

A review of `.claude/` found the four primitives — **Skill / Subagent / Slash Command / Hook** — are conflated. Today's `.claude/skills/*.md` files are actually slash-command prompt templates the main agent role-plays through. Real Skills (auto-loading capability bundles with frontmatter), per-role Subagents, registered slash commands, and deterministic hooks are mostly missing.

Target architecture:
- **Subagents = the team members** (one per pipeline role)
- **Skills = the textbooks they pull from** (methodology, reusable)
- **Slash commands = how the Product Owner addresses the team**
- **Hooks = office rules nobody can skip**

---

## 1 · Decisions to lock in before any file changes (Phase 0)

| ID | Decision | Resolution |
|---|---|---|
| D-A | What goes where | Roles → `.claude/agents/`. Methodology → `.claude/skills/<name>/SKILL.md`. User triggers → `.claude/commands/`. Enforcement → `.claude/settings.json` hooks. |
| D-B | QA/Security duplication | Collapse `skills/qa.md` + `agents/qa-runner.md` into a single `agents/qa.md`. Same for security. Old files deleted in Phase 6. |
| D-C | Model assignments | See table in §3. Right-size: Haiku for cheap/deterministic, Opus for deep reasoning, Sonnet default. |
| D-D | Naming | Subagents use role nouns (`researcher`, `designer`), not action verbs (`research`, `validate`). Slash commands keep verb form (`/research`). |
| D-E | Backwards compat | None. This is a blueprint repo with no live forks consuming it. Clean break. |

**Sonnet: log all five decisions in `DECISIONS.md` as D-003 through D-007 before touching code.**

---

## 2 · Target directory structure (the picture to aim for)

```
.claude/
├── settings.json                    NEW — hooks + project permissions
├── commands/                        NEW directory
│   ├── research.md       /research [problem]
│   ├── design.md         /design [feature]
│   ├── architect.md      /architect [feature]
│   ├── qa.md             /qa [feature]
│   ├── security.md       /security [scope]
│   ├── validate.md       /validate [feature]
│   ├── perf.md           /perf [feature]
│   ├── checkpoint.md     /checkpoint [phase]
│   ├── readiness.md      /readiness [scope]
│   └── ship.md           /ship [feature]   (composite: fan out QA+Sec+UX+Perf)
├── agents/                          EXPANDED
│   ├── orchestrator.md              KEEP (updated in Phase 5)
│   ├── eval-judge.md                KEEP (move to haiku)
│   ├── codebase-explorer.md         KEEP
│   ├── researcher.md                NEW
│   ├── designer.md                  NEW
│   ├── architect.md                 NEW
│   ├── engineer.md                  NEW
│   ├── qa.md                        NEW (merges skills/qa.md + agents/qa-runner.md)
│   ├── security.md                  NEW (merges skills/security.md + agents/security-reviewer.md)
│   ├── ux-validator.md              NEW
│   └── perf-engineer.md             NEW
├── skills/                          RESHAPED — directory per skill
│   ├── route/SKILL.md               NEW (auto-loads on new tasks)
│   ├── memory-protocol/SKILL.md     NEW (auto-loads at session start)
│   ├── jtbd/SKILL.md                NEW
│   ├── kano/SKILL.md                NEW
│   ├── nielsen-heuristics/SKILL.md  NEW
│   ├── testing-pyramid/SKILL.md     NEW
│   ├── owasp-mobile/SKILL.md        NEW
│   ├── owasp-llm/SKILL.md           NEW
│   ├── stride/SKILL.md              NEW
│   └── cvss/SKILL.md                NEW
├── contracts/schemas.md             KEEP (unchanged)
└── evals/                           KEEP (unchanged)
```

Old `.claude/skills/*.md` (10 flat files) are **deleted in Phase 6**, not before. Keep them as reference until then.

---

## 3 · Model & tool assignments (reference table)

| Subagent | Model | Tools | maxTurns | Rationale |
|---|---|---|---|---|
| `orchestrator` | opus | Bash, Read, Grep, Glob, Write, Edit | 50 | Deep reasoning for decomposition |
| `eval-judge` | haiku | Read, Grep, Glob, Write (baselines only) | 10 | Deterministic scoring against rubric |
| `codebase-explorer` | haiku | Read, Grep, Glob | 30 | Fast search |
| `researcher` | opus | Read, Grep, Glob, WebSearch, WebFetch | 20 | Market analysis, JTBD synthesis |
| `designer` | sonnet | Read, Grep, Glob, WebFetch | 20 | Heuristic application, flow design |
| `architect` | opus | Read, Grep, Glob, WebSearch | 25 | Pattern selection, trade-off reasoning |
| `engineer` | sonnet | Read, Edit, Write, Bash, Grep, Glob | 40 | Implementation |
| `qa` | sonnet | Read, Grep, Glob, Bash, Edit | 25 | Runs tests, writes tests |
| `security` | opus | Read, Grep, Glob, WebSearch | 20 | Threat modeling, CVSS reasoning |
| `ux-validator` | sonnet | Read, Grep, Glob, WebFetch | 15 | Heuristic-driven review |
| `perf-engineer` | sonnet | Read, Grep, Glob, Bash | 20 | Profiling, budget enforcement |

---

## 4 · Subtask cards (the actual work)

Each card is **one atomic subtask** Sonnet executes. Cards within a Phase are sequential unless explicitly marked `[parallel-safe]`. Cards across Phase 1 and Phase 2 are independent — Phase 2 can start once Phase 0 is done.

### Phase 0 — Setup

**T-00 Log decisions** — Append D-003 through D-007 to `DECISIONS.md` covering items in §1. Single commit: `chore: log architecture migration decisions`.

**T-01 Create empty directory skeleton** — `mkdir -p .claude/commands .claude/skills/route` so writes don't fail later. No commit; bundled with T-02.

**T-02 Stub `.claude/settings.json`** — Create with empty `hooks: {}` and a minimal `permissions` allowlist (read of project files, Bash for git/npm). Commit: `chore: scaffold .claude/settings.json`.

### Phase 1 — Role subagents (the team) [cards parallel-safe with each other and with Phase 2]

**Source rule:** for each role subagent, ingest the matching `.claude/skills/<role>.md` (current flat file) **wholesale into the subagent's system prompt body**, then strip pure-methodology sections (those move to Phase 2 Skills and get referenced by name).

**T-10 `.claude/agents/researcher.md`**
- Frontmatter per §3 table (opus, 20 turns, Read/Grep/Glob/WebSearch/WebFetch).
- Source: `.claude/skills/research.md`.
- Strip into Phase 2 skills: JTBD, Kano, evidence tier table only if it grows.
- Output contract: `research_output` (already defined in `contracts/schemas.md` — do not edit).
- Veto power preserved. Approval-gate language preserved (Gate 1).

**T-11 `.claude/agents/designer.md`**
- Frontmatter per §3 (sonnet, 20 turns).
- Source: `.claude/skills/design.md`.
- Strip into Phase 2 skills: Nielsen heuristics, Fitts/Hick references.
- Output contract: `design_output`.

**T-12 `.claude/agents/architect.md`**
- Frontmatter per §3 (opus, 25 turns).
- Source: `.claude/skills/architect.md`.
- Strip into Phase 2 skills: SOLID, architectural pattern table.
- Output contract: `architect_output`.

**T-13 `.claude/agents/engineer.md`** *(NEW — no skill source today)*
- Frontmatter per §3 (sonnet, 40 turns).
- Body: distil the "Engineer agent" checklist from CLAUDE.md §"Agent Roles" #4. Add explicit handoff requirements: must read research + design + architect contracts, must produce `engineer_output` contract (add to `schemas.md` if absent — see T-50).
- Veto: production-readiness violations.

**T-14 `.claude/agents/qa.md`** (merges `skills/qa.md` + `agents/qa-runner.md`)
- Frontmatter per §3 (sonnet, 25 turns).
- Source: union of `skills/qa.md` (strategy/severity/mock strategy/output format) and `agents/qa-runner.md` (test execution patterns, flaky test detection).
- Strip into Phase 2 skills: Testing Pyramid.
- Output contract: `qa_output`.
- Delete-targets noted (Phase 6): `skills/qa.md`, `agents/qa-runner.md`.

**T-15 `.claude/agents/security.md`** (merges `skills/security.md` + `agents/security-reviewer.md`)
- Frontmatter per §3 (opus, 20 turns).
- Source: union of `skills/security.md` (frameworks/severity) and `agents/security-reviewer.md` (audit output format).
- Strip into Phase 2 skills: OWASP Mobile, OWASP LLM, STRIDE, CVSS.
- Output contract: `security_output`.
- Delete-targets noted: `skills/security.md`, `agents/security-reviewer.md`.

**T-16 `.claude/agents/ux-validator.md`**
- Frontmatter per §3 (sonnet, 15 turns).
- Source: `.claude/skills/validate.md`.
- Strip into Phase 2 skills: SUS, usability metrics.
- Output contract: `validate_output`.

**T-17 `.claude/agents/perf-engineer.md`**
- Frontmatter per §3 (sonnet, 20 turns).
- Source: `.claude/skills/perf.md`.
- Strip into Phase 2 skills: Performance budgets (Core Web Vitals table).
- Output contract: `perf_output`.

**Verification after Phase 1:** each new agent file has valid YAML frontmatter (`name`, `description`, `tools`, `model`, `maxTurns`), references the correct contract type, and preserves veto language. Commit: `feat(agents): add 8 role subagents (researcher, designer, architect, engineer, qa, security, ux-validator, perf-engineer)`.

### Phase 2 — Methodology Skills (the textbooks)

Each Skill is a directory: `.claude/skills/<name>/SKILL.md`. Frontmatter format:

```yaml
---
name: <kebab-name>
description: Use when <specific trigger condition>. Provides <what it gives the agent>.
---
```

The `description` is the auto-load trigger — write it so a model evaluating "should I load this?" can answer crisply. Bad: "About JTBD". Good: "Use when analyzing user motivation or writing user stories. Provides the Jobs-to-Be-Done framework and job map template."

**T-20 `route/SKILL.md`** — Auto-classify new tasks L1-L4. `description: Use at the start of any new task to classify complexity (L1-L4) and select the pipeline. Triggers automatically on incoming work.` Body: classification rules from current `skills/route.md` (keep the signals table, level definitions, override commands).

**T-21 `memory-protocol/SKILL.md`** — `description: Use at the start of a session and after gate decisions. Provides the read-on-start file list and continuous memory update rules.` Body: distil "Session Protocol — Memory & Continuity" section of CLAUDE.md into a reusable trigger pack.

**T-22 `jtbd/SKILL.md`** — `description: Use when analyzing user motivation, writing user stories, or distinguishing the "job" from the solution. Provides JTBD framework and the 8-step job map.`

**T-23 `kano/SKILL.md`** — `description: Use when prioritizing features or scoping MVPs. Provides Kano classification (Must-have / Performance / Excitement / Indifferent / Reverse).`

**T-24 `nielsen-heuristics/SKILL.md`** — `description: Use when reviewing or designing UI. Provides Nielsen's 10 usability heuristics (NN/g, Jan 2024 update).`

**T-25 `testing-pyramid/SKILL.md`** — `description: Use when planning tests or evaluating test suite balance. Provides the 70/20/10 unit/integration/E2E pyramid and ice-cream-cone anti-pattern detection.`

**T-26 `owasp-mobile/SKILL.md`** — `description: Use when auditing mobile or native-client code for security. Provides OWASP Mobile Top 10 (2024) with check patterns per category.`

**T-27 `owasp-llm/SKILL.md`** — `description: Use when auditing LLM/AI features for security. Provides OWASP Top 10 for LLM Applications (2025) with check patterns.`

**T-28 `stride/SKILL.md`** — `description: Use when threat-modeling a new component or system. Provides STRIDE per-component process (Spoofing/Tampering/Repudiation/Info Disclosure/DoS/Elevation).`

**T-29 `cvss/SKILL.md`** — `description: Use when scoring a security finding's severity. Provides CVSS 4.0 base metrics and severity bands.`

**Verification after Phase 2:** every SKILL.md has valid frontmatter with a *triggering* description (not just a topic label). Commit: `feat(skills): extract 10 reusable methodology skills (route, memory-protocol, jtbd, kano, nielsen-heuristics, testing-pyramid, owasp-mobile, owasp-llm, stride, cvss)`.

### Phase 3 — Slash commands (user shortcuts)

Each command body is a thin prompt that spawns the matching subagent. Template:

```markdown
---
description: <one-line user-facing description>
---

Spawn the `<subagent-name>` subagent via the Agent tool. Pass `$ARGUMENTS` as the task.

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim, then stop and wait for the relevant gate decision per CLAUDE.md.
```

**T-30** through **T-38**: create one command file per role using the template above:
- `commands/research.md` → spawns `researcher` → Gate 1
- `commands/design.md` → spawns `designer` → Gate 2
- `commands/architect.md` → spawns `architect` → Gate 3
- `commands/qa.md` → spawns `qa` → (no gate, feeds Gate 4)
- `commands/security.md` → spawns `security` → (no gate, feeds Gate 4)
- `commands/validate.md` → spawns `ux-validator` → (no gate, feeds Gate 4)
- `commands/perf.md` → spawns `perf-engineer` → (no gate, feeds Gate 4)
- `commands/checkpoint.md` → main agent runs checkpoint logic (no subagent — this is meta, lives in main context)
- `commands/readiness.md` → main agent runs readiness logic (also meta)

**T-39 `commands/ship.md`** (composite) — body instructs the orchestrator subagent to **spawn QA + Security + UX Validator + Performance in parallel** (4 Agent tool calls in one message), collect all four contract blocks, then present a merged Gate 4 report.

**Verification after Phase 3:** typing `/research foo` would spawn the researcher subagent (we won't test live — just structural review). Commit: `feat(commands): add 10 slash commands routing to role subagents`.

### Phase 4 — Hooks (deterministic enforcement)

Edit `.claude/settings.json` to add hooks. Reference Claude Code docs (May 2026): `SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`.

**T-40 SessionStart hook** — `echo` a reminder that the model must read `PROJECT_STATE.md`, `CONVENTIONS.md`, `BACKLOG.md`, `DECISIONS.md`. The Memory Protocol skill does the heavy lifting; this hook just ensures the prompt is injected.

**T-41 PreToolUse hook on `git commit`** — run `npm run lint && npm run typecheck` if those scripts exist in `package.json`. Block commit on failure. **Note:** this repo has no `package.json` today; the hook should `exit 0` if no `package.json` exists (graceful no-op for the blueprint itself).

**T-42 PostToolUse hook on Agent tool** — when an Agent subagent returns and its output contains a `# CONTRACT:` block, spawn `eval-judge` to score it. *Implementation:* shell script in `.claude/hooks/post-agent-eval.sh` that greps for `# CONTRACT:` and triggers a follow-up. Keep MVP simple — script may just `echo` a reminder for now and be properly wired in T-42a later (track in BACKLOG).

**T-43 Stop hook** — if a Gate decision keyword appears in the recent transcript (`Gate 1 approved`, `Gate 2 approved`, etc.), remind the model to update `PROJECT_STATE.md` and `DECISIONS.md` before stopping.

**Verification after Phase 4:** `.claude/settings.json` parses as valid JSON; hook scripts (if any) are executable. Commit: `feat(hooks): add SessionStart, PreToolUse, PostToolUse, Stop hooks`.

### Phase 5 — Orchestrator update

**T-50 Add `engineer_output` contract** — Edit `.claude/contracts/schemas.md` to add an `engineer_output` schema (files_changed, tests_added, contract handoff for QA). Required because T-13 added the engineer subagent and there was no contract for it before. Commit: `feat(contracts): add engineer_output schema`.

**T-51 Rewrite orchestrator's "Parallel Execution Patterns"** — Edit `.claude/agents/orchestrator.md` to reflect the new agent roster. Specifically:
- Update §"Parallel Execution Patterns → Post-Implementation Validation" to spawn `qa`, `security`, `ux-validator`, `perf-engineer` (not the old runner names).
- Update §"Decomposition Quality Checklist" if it references old names.
- No structural changes — only the names and the model field (move orchestrator to opus per §3).

Commit: `refactor(orchestrator): wire to new agent roster`.

### Phase 6 — Cleanup

**T-60 Delete old flat-file skills** — Remove `.claude/skills/{research,design,architect,qa,security,validate,perf,route,checkpoint,readiness}.md` (the 10 flat files). Their content now lives in subagents (Phase 1), methodology skills (Phase 2), or commands (Phase 3).

**T-61 Update CLAUDE.md** — search/replace and rewrite affected sections:
- §"Agent Skills (Invocable Commands)" → rename to "Slash Commands & Subagents". Point each command at its subagent.
- §"How to Invoke the Team" → reference subagent spawning, not role-playing.
- §"Eval Behavior" table → keep as-is.
- Remove the line "Skills are defined in `.claude/skills/`" — replace with "Commands in `.claude/commands/`, subagents in `.claude/agents/`, reusable methodology in `.claude/skills/<name>/SKILL.md`."

**T-62 Update PROJECT_STATE.md** — Reflect new architecture. Update "What Exists" table. Add migration entry to Session Log.

**T-63 Update BACKLOG.md** — Mark this migration as completed; surface follow-ups (e.g., wiring T-42 eval-judge automation properly).

Commit: `refactor: delete legacy skill files; update CLAUDE.md, PROJECT_STATE, BACKLOG for new architecture`.

### Phase 7 — Smoke test

**T-70** Cold-read sanity check: ask Sonnet to act as if it just started a session. Confirm it reads memory files (Memory Protocol skill auto-loads), classifies an inbound task via Route skill, and identifies which subagent it would spawn. No code execution — verbal walk-through is enough for the blueprint repo.

**T-71** Frontmatter linter: `for f in .claude/agents/*.md .claude/skills/*/SKILL.md .claude/commands/*.md; do head -10 "$f" | grep -q '^---$' && echo "OK $f" || echo "MISSING FRONTMATTER $f"; done`. All files should print OK.

**T-72** Contract integrity: ensure every contract referenced in subagent prompts exists in `contracts/schemas.md`. Grep diff.

Commit: `chore: smoke-test new architecture`.

---

## 5 · Orchestration plan for Sonnet (Gate O-1)

Sonnet should run this as **L4 with the orchestrator subagent**, decomposed as:

```
Group A — Setup (sequential)
  T-00 → T-01 → T-02

Group B — Subagents (sequential, all write to .claude/agents/)
  T-10 → T-11 → T-12 → T-13 → T-14 → T-15 → T-16 → T-17

Group C — Skills (sequential, all write to .claude/skills/<name>/)
  T-20 → T-21 → ... → T-29

[Group B and Group C are independent — could be parallel if Sonnet trusts no merge conflicts;
 recommended: run sequentially to keep diffs reviewable]

Group D — Commands (sequential)
  T-30 → ... → T-39

Group E — Hooks (sequential, all edit settings.json + scripts)
  T-40 → T-41 → T-42 → T-43

Group F — Orchestrator & schema (sequential)
  T-50 → T-51

Group G — Cleanup (sequential, must be last)
  T-60 → T-61 → T-62 → T-63

Group H — Smoke test
  T-70 → T-71 → T-72
```

**Human gates:** Sonnet stops at O-1 (this plan acts as O-1; if approved, proceed). After Group G completes, stop at O-2 for human review before any push to remote.

**Rollback:** Before Group B starts, tag a checkpoint: `git tag pre-migration`. If any phase fails irrecoverably, `git reset --hard pre-migration`.

---

## 6 · Acceptance criteria (definition of done)

The migration is complete when **all of the following hold**:

- [ ] `.claude/agents/` contains 11 subagent files, each with valid frontmatter and correct model per §3.
- [ ] `.claude/skills/` contains 10 directories, each with a `SKILL.md` whose `description` is a *trigger condition* not a topic label.
- [ ] `.claude/commands/` contains 10 command files, each spawning the correct subagent.
- [ ] `.claude/settings.json` has at least 4 hooks (SessionStart, PreToolUse on commit, PostToolUse on Agent, Stop).
- [ ] Old flat `.claude/skills/*.md` files are deleted.
- [ ] `agents/qa-runner.md` and `agents/security-reviewer.md` are deleted (merged into qa/security).
- [ ] `CLAUDE.md` no longer references "skills" where it means "commands"; the agent invocation table points at subagents.
- [ ] `PROJECT_STATE.md`, `DECISIONS.md`, `BACKLOG.md` reflect the migration.
- [ ] `contracts/schemas.md` includes `engineer_output`.
- [ ] Smoke tests (T-70–T-72) pass.
- [ ] Blueprint version bumped: `v1.0.0 → v2.0.0` in `CHANGELOG.md` with a "Breaking — agent architecture" entry.

---

## 7 · What stays untouched

Do **not** modify in this migration:
- `.claude/contracts/schemas.md` *(except for the additive `engineer_output` in T-50)*
- `.claude/evals/rubrics/*` — the rubric files are agent-name-agnostic and stay correct.
- `.claude/evals/baselines/*`
- `CONVENTIONS.md`
- `DESIGN_SYSTEM.md`
- `SETUP.md`

---

## 8 · Estimated effort

~30 atomic subtasks. ~8–12 commits. Realistic Sonnet wall-clock: 60–90 minutes if cards are executed serially, 30–45 minutes if Groups B and C are parallelized via subagent fan-out.

---

## 9 · After O-2 approval

- Push branch `claude/review-agent-architecture-Cz07o` to origin.
- Do **not** open a PR unless the Product Owner explicitly asks for one (per remote-environment instructions).
- Update `UPSTREAM_CANDIDATES.md` flagging that this is a v2.0.0 candidate for upstream propagation to forks.
