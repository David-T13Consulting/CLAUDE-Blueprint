---
name: owasp-mobile
description: Use when auditing a mobile app for security vulnerabilities. Provides the OWASP Mobile Top 10 (2024) checklist with specific checks, common findings, and remediation patterns. Referenced by the security subagent.
---

# OWASP Mobile Top 10 (2024)

Source: OWASP Mobile Application Security Project — Mobile Top 10 (2024 edition). The industry standard for mobile app security assessment. Apply systematically — not selectively.

## The 10 Categories

### M1: Improper Credential Usage

**What it is:** API keys, tokens, passwords, or secrets stored or transmitted insecurely.

**What to check:**
- Hardcoded credentials in source code (grep for `sk-ant-`, `Bearer `, `password =`, `secret =`)
- API keys in error messages logged to console
- Credentials in plaintext storage (AsyncStorage, UserDefaults, SharedPreferences)
- Tokens in URLs (visible in logs, proxies, referrer headers)
- Credentials committed to version control (check git history)

**Common findings:**
- API keys stored in `AsyncStorage` instead of Keychain / SecureStore
- `console.log(apiKey)` in development code shipped to production
- Tokens in URL query parameters (`/api/data?token=abc123`)

**Remediation:**
```typescript
// BAD
await AsyncStorage.setItem('api_key', key);

// GOOD — Use platform secure storage
import * as SecureStore from 'expo-secure-store';
await SecureStore.setItemAsync('api_key', key, {
  keychainAccessible: SecureStore.WHEN_UNLOCKED
});
```

**Detection tools:** `git secrets`, `trufflehog`, `gitleaks`, manual grep

---

### M2: Inadequate Supply Chain Security

**What it is:** Vulnerabilities introduced through third-party dependencies, malicious packages, or unverified sources.

**What to check:**
- `npm audit` / `yarn audit` — report all vulnerabilities (critical, high, medium, low)
- Unpinned versions in `package.json` (ranges like `^1.2.3` allow automatic upgrades)
- Packages with unusual names similar to popular packages (typosquatting)
- Dependencies with excessive permissions or access
- Transitive dependencies with known CVEs

**Common findings:**
- `package.json` using `^` ranges — auto-upgrades can introduce vulnerabilities
- Outdated dependencies with published CVEs
- No lockfile committed (`package-lock.json` / `yarn.lock` missing)

**Remediation:**
```json
// BAD — allows any patch update without review
"dependencies": { "some-lib": "^1.2.3" }

// GOOD — pinned exact version
"dependencies": { "some-lib": "1.2.3" }
```

Always commit `package-lock.json`. Use `npm ci` (not `npm install`) in CI — enforces lockfile.

---

### M3: Insecure Authentication / Authorization

**What it is:** Weak authentication flows, missing server-side authorization, or broken session management.

**What to check:**
- Is authentication checked server-side (not just client-side)?
- Token expiry — are expired tokens rejected?
- Token refresh mechanism exists and works?
- Can users access other users' data by changing IDs in requests?
- Are admin endpoints protected from regular users?

**Common findings:**
- Client-side-only auth checks (easy to bypass with a proxy)
- No token refresh — tokens never expire or app breaks silently when they do
- Sequential IDs in API paths (`/api/user/123/data`) allow enumeration

**Remediation:**
- Every API endpoint validates the session token server-side
- Tokens have a maximum lifetime (access: 1h, refresh: 30d)
- Use non-guessable IDs (UUID) in API paths, not sequential integers

---

### M4: Insufficient Input / Output Validation

**What it is:** User input not validated; API responses not sanitized before use.

**What to check:**
- Maximum length enforced on all user inputs?
- Special characters handled (especially `<`, `>`, `&`, `"`, `'`, `\`)
- API responses validated before rendering to UI?
- Numbers bounded (no negative values where positive expected)?
- File types validated on upload?

**Common findings:**
- Chat input with no max length — can send megabytes to the API
- Raw API response rendered directly to UI (XSS vector in web, injection in native)
- File uploads accepting all MIME types

**Remediation:**
```typescript
const MAX_MESSAGE_LENGTH = 4000;

function validateUserInput(text: string): string {
  const trimmed = text.trim();
  if (trimmed.length === 0) throw new ValidationError('Message cannot be empty');
  if (trimmed.length > MAX_MESSAGE_LENGTH) throw new ValidationError('Message too long');
  // Validate encoding — reject null bytes, control chars
  if (/[\x00-\x08\x0B\x0C\x0E-\x1F]/.test(trimmed)) {
    throw new ValidationError('Invalid characters in message');
  }
  return trimmed;
}
```

---

### M5: Insecure Communication

**What it is:** Data transmitted over HTTP, or HTTPS without certificate verification.

**What to check:**
- All network requests use HTTPS (not HTTP)?
- Certificate pinning implemented for sensitive APIs?
- Sensitive data in URL parameters (visible in server logs)?
- Mixed content (HTTPS page loading HTTP resources)?

**Common findings:**
- Debug builds using HTTP endpoints
- Sensitive data in query parameters (`?user_id=123&session=abc`)
- No certificate pinning (vulnerable to MITM with custom CA)

**Remediation:**
- Enforce `NSAppTransportSecurity` / `cleartextTrafficPermitted: false` in app config
- Sensitive data in request body (POST), not URL parameters (GET)
- Certificate pinning for API endpoints handling PII or financial data

---

### M6: Inadequate Privacy Controls

**What it is:** Excessive data collection, missing consent, or PII appearing where it shouldn't.

**What to check:**
- What data is collected? Is all of it necessary?
- Crash reports — do they include conversation content or PII?
- Analytics events — do they include user identifiers or content?
- Is consent obtained before data collection begins?
- Can users request deletion of their data?

**Common findings:**
- Sentry / Crashlytics crash reports include full conversation history
- Analytics events include user content or precise location
- No mechanism for users to delete their account and data

**Remediation:**
- Scrub PII from crash reports before sending (hook into Sentry's beforeSend)
- Analytics events include category/count, not content
- Implement data deletion endpoint and expose it to users

---

### M7: Insufficient Binary Protections

**What it is:** Debug builds shipped to production, lack of tamper detection, easy reverse engineering.

**What to check:**
- Are debug flags disabled in release builds?
- Is code obfuscation applied?
- Are root/jailbreak detection mechanisms in place (for high-security apps)?
- Are build logs excluded from release artifacts?

**Common findings:**
- `__DEV__` checks not disabled properly in production builds
- Debug logging visible in release builds via Xcode or Android logcat
- No obfuscation — source map reveals full business logic

**Remediation:**
- Separate environment configs: `.env.development` vs `.env.production`
- Strip console.log in production (Babel transform or ESLint rule)
- Enable minification and obfuscation in production build config

---

### M8: Security Misconfiguration

**What it is:** Overly permissive settings, default configurations, exposed endpoints.

**What to check:**
- CORS policy — allows only expected origins?
- Rate limiting configured on API endpoints?
- Debug endpoints disabled in production?
- Error responses — do they leak stack traces or internal details?
- Default credentials changed?

**Common findings:**
- CORS `Access-Control-Allow-Origin: *` in production
- No rate limiting on auth endpoints (enables brute force)
- Error responses include full stack traces

**Remediation:**
- CORS: explicit allowlist of origins
- Rate limiting: max N requests per minute per IP/user
- Error responses in production: generic message + error ID (look up internally)

---

### M9: Insecure Data Storage

**What it is:** Sensitive data stored in plaintext or in accessible storage.

**What to check:**
- Where is conversation history stored? Encrypted?
- API keys, tokens: in Keychain/SecureStore or AsyncStorage?
- Sensitive data in logs, temp files, clipboard?
- iCloud backup includes sensitive data?
- Screenshots include sensitive data in app switcher?

**Common findings:**
- `AsyncStorage` for session tokens (unencrypted on Android)
- Conversation history in SQLite without encryption
- API keys exposed in iCloud backup

**Remediation:**
```typescript
// Use platform-encrypted storage for sensitive data
// iOS: Keychain (via expo-secure-store)
// Android: Android Keystore

// Mark app as not backed up (or exclude sensitive files)
// iOS: NSURLIsExcludedFromBackupKey
// Android: android:allowBackup="false" in manifest
```

---

### M10: Insufficient Cryptography

**What it is:** Weak encryption algorithms, hardcoded keys, or improper key management.

**What to check:**
- Encryption algorithm: AES-256-GCM (strong) vs DES/3DES/RC4 (broken)?
- Password hashing: Argon2id/bcrypt (strong) vs MD5/SHA1 (broken)?
- Are encryption keys hardcoded in source?
- Is key derivation used for user-facing encryption?

**Common findings:**
- MD5 or SHA1 used for password hashing
- Hardcoded AES key in source code
- `Math.random()` used for cryptographic purposes (not CSPRNG)

**Remediation:**

| Purpose | Use | Never Use |
|---------|-----|-----------|
| Data at rest | AES-256-GCM | DES, 3DES, RC4 |
| Password hashing | Argon2id (preferred), bcrypt | MD5, SHA1, SHA256 (without salt) |
| Key derivation | PBKDF2, scrypt, Argon2 | Custom schemes |
| Token generation | CSPRNG (`crypto.getRandomValues`) | `Math.random()` |
| Transport | TLS 1.3 (prefer), TLS 1.2 (minimum) | TLS 1.0, TLS 1.1, SSL |

## Audit Checklist Format

```
OWASP MOBILE TOP 10 AUDIT: [Feature/App]

| Category | Status | Finding | Severity | Fix |
|----------|--------|---------|----------|-----|
| M1: Credential Usage | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M2: Supply Chain | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M3: Auth/AuthZ | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M4: Input Validation | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M5: Communication | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M6: Privacy | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M7: Binary Protections | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M8: Misconfiguration | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M9: Data Storage | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |
| M10: Cryptography | PASS/FAIL/N-A | [detail] | [C/H/M/L] | [fix] |

RESULT: [N PASS / N FAIL / N N-A]
CRITICAL/HIGH FAILURES: [list or "none — PASS"]
```
