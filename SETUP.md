# SETUP — How to Use This Blueprint

> Fork this repo to start any new Claude-assisted project.
> Follow the steps below to customize it for your project.

---

## Step 1: Create Your Project

Use this repo as a GitHub template, or clone and reinitialize:

```bash
gh repo create my-new-project --template David-T13Consulting/CLAUDE-Blueprint --private
cd my-new-project
```

## Step 2: Customize These Files

| File | What to Change |
|------|---------------|
| `CLAUDE.md` → **App Config** section | Replace all `[PLACEHOLDER]` values with your project's tech stack, directory structure, and data flow |
| `CLAUDE.md` → **Commands** section | Replace with your actual dev/build/test commands |
| `DESIGN_SYSTEM.md` | Customize colors, typography, spacing for your brand. Wire tokens into your framework's config |
| `PROJECT_STATE.md` | Update the status and session log for your project |
| `CONVENTIONS.md` | Will be populated automatically as Claude learns your preferences |
| `BACKLOG.md` | Add your initial work items |
| `DECISIONS.md` | Will be populated as you make decisions |

## Step 3: Start Building

Once App Config is filled in, tell Claude "let's build" or "set up the project." It will **automatically scaffold** all config files for your tech stack:

- `package.json`, `tsconfig.json`, linter, formatter, test config
- Styling config wired to your DESIGN_SYSTEM.md tokens
- CI/CD workflow (`.github/workflows/ci.yml`)
- Git hooks, `.gitignore`, `.env.example`

You don't need to create these manually — Claude generates them based on your App Config.

## Step 4: Review Platform-Specific Sections

Several sections in `CLAUDE.md` are marked with `> **TEMPLATE**:` notes. These cover:

- **Deployment & Release** — Adapt the pipeline for your platform (web, mobile, API, etc.)
- **Legal & Compliance** — Add your platform's specific requirements
- **Go-to-Market** — Adapt distribution strategy for your channel

## Step 4: Customize Agents & Skills (Optional)

The agents in `.claude/agents/` and skills in `.claude/skills/` are generic and work as-is. You can:

- Add project-specific agents (e.g., a domain-specific reviewer)
- Add project-specific skills (e.g., `/deploy`, `/audit-compliance`)
- Remove agents/skills you don't need

## What's Included

```
CLAUDE-Blueprint/
  CLAUDE.md              ← Operating system for Claude (your main config)
  SETUP.md               ← This file (delete after setup)
  DESIGN_SYSTEM.md       ← Visual design tokens and rules
  PROJECT_STATE.md       ← Current project status (read at session start)
  BACKLOG.md             ← Prioritized work items
  DECISIONS.md           ← Decision log
  CONVENTIONS.md         ← User preferences (auto-populated)
  .gitignore             ← Standard ignores
  .claude/
    agents/
      codebase-explorer.md  ← Fast read-only codebase mapping
      qa-runner.md           ← Test execution and analysis
      security-reviewer.md   ← Security audit (read-only)
    skills/
      architect.md     ← Architecture decisions
      checkpoint.md    ← Decision checkpoints
      design.md        ← UI/UX design
      perf.md          ← Performance analysis
      qa.md            ← Quality assurance
      readiness.md     ← Launch readiness checks
      research.md      ← Problem research
      security.md      ← Security review
      validate.md      ← Validation gates
```
