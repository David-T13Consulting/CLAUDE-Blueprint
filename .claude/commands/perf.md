---
description: Run Performance Engineering review on a feature. Audits render performance, memory, network efficiency, bundle impact, and AI/LLM cost. Presents a final Gate 4 summary for Product Owner ship decision. One of four parallel validators.
---

Spawn the `perf-engineer` subagent via the Agent tool. Pass `$ARGUMENTS` as the feature name to analyze.

**Prerequisite check:** The performance review is the final validator. It ideally runs after QA, Security, and UX Validation have passed (or in parallel with them via `/ship`).

The subagent will produce a full Performance Report including:
- Performance budget checks (JS bundle <200KB, TTI <3s on 3G, 60fps, memory <50MB/30min, API p95 <2s)
- Render performance audit (unnecessary re-renders, animation thread, list virtualization)
- Memory analysis (bounded data structures, cleanup on unmount, leak risks)
- Network efficiency audit (caching, retry with backoff, timeouts, deduplication)
- Bundle impact (size in KB gzipped, new dependencies justified)
- Cost analysis for AI features (tokens per interaction, cost per user per day/month, margin)
- SHIP IT / OPTIMIZE FIRST / BLOCK verdict
- Structured `# CONTRACT: perf_output` YAML block

After the subagent returns its full report (including the `# CONTRACT:` block), present the report to the user verbatim.

**The Performance Engineer also presents Gate 4.** After the perf report, if all four validators (QA, Security, UX, Perf) have run, present the final Gate 4 summary:

> **GATE 4: SHIP?**
> All agents have reviewed this feature. Summary:
> - QA: [PASS/BLOCK]
> - Security: [PASS/BLOCK]
> - UX Validation: [DELIGHTFUL/USABLE/REDESIGN]
> - Performance: [SHIP IT/OPTIMIZE/BLOCK]
> - Outstanding issues: [list or "none"]
>
> Ready to ship, or fix something first?

**Veto rule:** VETO (BLOCK verdict) if animations drop below 60fps, AI cost per user exceeds revenue per user, or any performance budget is violated by >2×.

Do NOT ship, merge, or mark complete without explicit Product Owner approval at Gate 4.
