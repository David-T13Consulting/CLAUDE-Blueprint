# Changelog

> **All notable changes to the blueprint are documented here.**
> Forks reference this to see what changed since they diverged.
> Format: [SemVer](https://semver.org/). Most recent first.

---

## [1.0.0] — 2026-04-01

### Initial Release
- Full adaptive pipeline with L1-L4 task routing
- 10 agent skills: `/route`, `/research`, `/design`, `/architect`, `/qa`, `/security`, `/validate`, `/perf`, `/checkpoint`, `/readiness`
- 5 custom subagents: orchestrator, eval-judge, security-reviewer, qa-runner, codebase-explorer
- 9 eval rubrics (8 system + 1 human eval) in `.claude/evals/rubrics/`
- Structured I/O contracts in `.claude/contracts/schemas.md`
- All skills and rubrics at 4/5 domain expertise with named frameworks (JTBD, Kano, STRIDE, CVSS 4.0, Nielsen's Heuristics, WCAG 2.2, etc.)
- Session protocol with real-time memory updates
- Product strategy section (Problem Brief, Validation Scorecard, MVP Framework, Pipeline Modes)
- Human eval rubric for Product Owner gate reviews
- `UPSTREAM_CANDIDATES.md` template for tracking universal learnings
