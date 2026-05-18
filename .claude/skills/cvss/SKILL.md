---
name: cvss
description: Use when scoring the severity of a security vulnerability. Provides CVSS 4.0 base metrics, severity levels, scoring guidance, and a CWE reference. Ensures consistent, defensible severity ratings across all security findings. Referenced by the security subagent.
---

# CVSS 4.0 Vulnerability Severity Scoring

Source: FIRST (Forum of Incident Response and Security Teams) — Common Vulnerability Scoring System v4.0 (2023). The industry-standard framework for communicating vulnerability severity. Use CVSS to replace subjective "this feels bad" severity labels with defensible, reproducible scores.

## Why CVSS

Without a consistent scoring system:
- "Critical" means different things to different people
- Severity is influenced by who reported the bug (politics)
- Priority decisions are arbitrary
- Stakeholders can't compare findings across audits

With CVSS 4.0:
- Every finding has a reproducible numeric score
- Score can be challenged and corrected based on metrics
- Enables consistent prioritization

## Severity Levels

| Severity | Score Range | Action Required |
|----------|-------------|-----------------|
| **Critical** | 9.0–10.0 | Fix immediately. Block release. Wake people up. |
| **High** | 7.0–8.9 | Fix before release. Block if remotely exploitable without auth. |
| **Medium** | 4.0–6.9 | Fix in current cycle. Document accepted risk if deferred. |
| **Low** | 0.1–3.9 | Fix when convenient. Hardening opportunity. |
| **None** | 0.0 | Informational only. No action required. |

## CVSS 4.0 Base Metrics

Score every finding by specifying each metric. Base metrics reflect the vulnerability's intrinsic characteristics — they don't change based on the environment.

### Attack Vector (AV) — How is the vulnerability reached?

| Value | Label | Description | Example |
|-------|-------|-------------|---------|
| N | **Network** | Exploitable remotely, over the internet | Unauthenticated API endpoint |
| A | **Adjacent** | Requires access to same network/segment | Local network only |
| L | **Local** | Requires local access (shell, device) | Requires app installed on device |
| P | **Physical** | Requires physical device access | Requires stolen unlocked phone |

**Scoring rule:** Network = most severe. Physical = least severe.

### Attack Complexity (AC) — How hard is it to exploit?

| Value | Label | Description |
|-------|-------|-------------|
| L | **Low** | No special conditions; exploit is repeatable | Default — assume Low unless there's a real barrier |
| H | **High** | Requires specific conditions, timing, or race condition |

**Rule:** Don't give High because exploitation requires skill. High means there's a genuine environmental prerequisite (specific config, race condition, non-default state).

### Attack Requirements (AT) — Are there deployment prerequisites?

| Value | Label | Description |
|-------|-------|-------------|
| N | **None** | No specific system configuration needed |
| P | **Present** | Requires a specific pre-existing condition |

### Privileges Required (PR) — What access level does the attacker need?

| Value | Label | Description |
|-------|-------|-------------|
| N | **None** | No prior authentication required |
| L | **Low** | Regular user account |
| H | **High** | Admin or elevated privilege |

### User Interaction (UI) — Does someone need to be tricked?

| Value | Label | Description |
|-------|-------|-------------|
| N | **None** | No user interaction required |
| P | **Passive** | Victim browses to a page or opens content |
| A | **Active** | Victim must perform a specific action (click link, install extension) |

### Vulnerable System Impact — What happens to the vulnerable component?

| Metric | Values | Meaning |
|--------|--------|---------|
| **VC** (Confidentiality) | N / L / H | None / Low / High data exposure |
| **VI** (Integrity) | N / L / H | None / Limited / Complete data modification |
| **VA** (Availability) | N / L / H | None / Reduced / Full unavailability |

### Subsequent System Impact — What happens to other systems?

| Metric | Values | Meaning |
|--------|--------|---------|
| **SC** (Confidentiality) | N / L / H | Impact on other systems (e.g., backend after compromising mobile app) |
| **SI** (Integrity) | N / L / H | Data corruption in downstream systems |
| **SA** (Availability) | N / L / H | Denial of service to dependent systems |

## Scoring Common Vulnerability Types

Use these as calibration anchors:

| Vulnerability | Typical CVSS Vector | Score |
|--------------|---------------------|-------|
| Hardcoded API key (read-only) | AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N | ~8.7 (High) |
| SQL injection (unauthenticated) | AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H | 10.0 (Critical) |
| Stored XSS | AV:N/AC:L/AT:N/PR:L/UI:P/VC:L/VI:L/VA:N | ~5.3 (Medium) |
| Insecure local storage (token) | AV:P/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N | ~4.6 (Medium) |
| No rate limiting on login | AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:L | ~5.3 (Medium) |
| Sensitive data in logs | AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:N/VA:N | ~4.0 (Medium) |
| Missing HTTPS cert pinning | AV:A/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:N | ~6.5 (Medium) |
| Prompt injection (LLM) | AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N | ~5.3 (Medium) |
| Unbounded API consumption | AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H | ~7.5 (High) |

## Finding Report Format

Every security finding must include:

```
FINDING: [VULN-001]
Title: [Short descriptive name]
Severity: [Critical/High/Medium/Low] (CVSS [score])
CVSS Vector: CVSS:4.0/AV:[N/A/L/P]/AC:[L/H]/AT:[N/P]/PR:[N/L/H]/UI:[N/P/A]/VC:[N/L/H]/VI:[N/L/H]/VA:[N/L/H]/SC:[N/L/H]/SI:[N/L/H]/SA:[N/L/H]
CWE: [CWE-XXX — name]
OWASP: [M1-M10 or LLM01-LLM10]

File: [file path]
Line: [line number or null]

Description:
  [What is vulnerable. What an attacker can do. Concrete impact.]

Proof of Concept:
  [Steps to reproduce, or code snippet showing the vulnerability]

Impact:
  [Specific harm — data exposed, user accounts compromised, cost incurred]

Remediation:
  [Specific fix with code example where appropriate]
```

## Common CWE References

| CWE | Name | Common OWASP Category |
|-----|------|----------------------|
| CWE-798 | Use of Hardcoded Credentials | M1 |
| CWE-89 | SQL Injection | M4 |
| CWE-79 | Cross-Site Scripting (XSS) | M4 |
| CWE-306 | Missing Authentication | M3 |
| CWE-862 | Missing Authorization | M3 |
| CWE-312 | Cleartext Storage of Sensitive Info | M9 |
| CWE-319 | Cleartext Transmission of Sensitive Info | M5 |
| CWE-327 | Use of Broken Algorithm | M10 |
| CWE-502 | Deserialization of Untrusted Data | M4 |
| CWE-400 | Uncontrolled Resource Consumption | LLM10 |
| CWE-20 | Improper Input Validation | M4, LLM01 |
| CWE-200 | Exposure of Sensitive Information | M6, LLM02 |

## Calibration Rules

To avoid scoring drift:

1. **Attack Vector = Network unless there's a real barrier.** Most mobile app vulnerabilities are reachable over the network (the user's phone is connected to the internet).

2. **Attack Complexity = Low unless there's a documented prerequisite.** Don't give High because exploitation requires skill — that's not what AC measures.

3. **Don't inflate severity to drive urgency.** Call a Medium a Medium. If it needs to be fixed urgently despite being Medium, explain why in the impact section — don't lie about the CVSS score.

4. **Don't deflate severity to avoid difficult conversations.** A Critical is a Critical. Document it accurately and deal with the conversation.

5. **Subsequent system impact (SC/SI/SA) is often overlooked.** Think about what downstream systems are affected if the vulnerable component is compromised. Mobile app → backend API is the classic chain.

## Priority Decision Matrix

After scoring all findings:

```
Priority 1 (Fix NOW — block release):
  All Critical (9.0+)
  High with AV:N/PR:N (remotely exploitable, unauthenticated)

Priority 2 (Fix before ship):
  All remaining High (7.0-8.9)

Priority 3 (Fix this cycle):
  Medium (4.0-6.9)
  Accepted risk requires PM + legal sign-off + DECISIONS.md entry

Priority 4 (Fix when convenient):
  Low (0.1-3.9)
  Document in Known Issues or BACKLOG.md
```
