---
name: ultimate-security-audit-workflow
description: >
  Flawless 10/10 Master Workflow for automated security vulnerability audits, static code analysis (SAST),
  dependency CVE scans, OWASP Top 10 penetration testing vectors, SLSA Level 3 supply chain checks,
  and regulatory compliance (SOC2, GDPR, HIPAA).
  Triggers on "ultimate security audit workflow", "/ultimate-security-audit-workflow",
  or when auditing dependencies, setting up SAST, checking compliance, or verifying OWASP.
argument-hint: "[cve-scan | compliance-check | sast-audit | --owasp | --supply-chain]"
---

# Ultimate Security Auditing & Compliance Workflow (10/10 Master Engine)

This workflow drives systematic static code analysis (SAST), software composition analysis (SCA / CVEs), automated secrets detection, supply-chain verification (SLSA 3), and regulatory compliance mapping.

```
                                      [REPOSITORY AUDIT TARGET / PR DIFF]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: DEPENDENCY SCA & CVE AUDIT]                         [PHASE 2: SAST & SECRETS SCAN]
              ├─ Automated CVSS Scans (Trivy / Snyk)                        ├─ Semgrep / AST Security Rules
              ├─ Lockfile Pinned Hashes & SLSA Level 3                      ├─ GitLeaks & TruffleHog Secrets Scan
              └─ Vulnerability Mitigation Matrix                            └─ Source-to-Sink Dataflow Tracking
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: OWASP TOP 10 PENETRATION AUDIT MATRIX              │
        │  • Injection • Broken Auth • SSRF • Cryptographic Failures • Security Misconfig│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: REGULATORY COMPLIANCE MAPPING]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🇪🇺 GDPR/CCPA │           │ 🏢 SOC 2 TYPE│           │ 🏥 HIPAA PII │
            │ Data Deletion│           │ Audit Logs   │           │ Encryption   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Security Auditing

1. **Zero High/Critical CVEs Allowed in Production**: Any dependency with a CVSS score $\ge 7.0$ (High/Critical) is an unconditional blocker.
2. **Deterministic Lockfile Integrity**: All dependencies must be strictly pinned with cryptographic integrity hashes (`package-lock.json`, `pnpm-lock.yaml`).
3. **AST Source-to-Sink Verification**: Track untrusted input sources (`req.body`, `searchParams`) to dangerous execution sinks (`eval`, `innerHTML`, `exec`, unparameterized queries).
4. **Automated Pre-Commit Secrets Scanning**: Commits containing API keys, private keys, or passwords must be blocked at pre-commit gates (`gitleaks`).
5. **Continuous Compliance Governance**: SOC2, GDPR, and HIPAA controls must be represented as automated unit/integration test assertions.

---

## 🔬 The 4-Phase Security Audit Pipeline

### Phase 1: Software Composition Analysis (SCA) & CVE Triage
*   **Action:**
    1. Run automated vulnerability scans: `npm audit`, `trivy fs .`, `pip-audit`.
    2. Grade vulnerabilities by CVSS score:
       - **Critical ($9.0 - 10.0$):** Immediate merge blocker. Upgrade or replace package.
       - **High ($7.0 - 8.9$):** Blocker unless an isolated workaround is formally verified.
       - **Medium ($4.0 - 6.9$):** Planned for immediate next sprint cycle.

### Phase 2: Static Application Security Testing (SAST) & Secrets Scanning
*   **Action:**
    1. **Semgrep / AST-Grep Custom Rules:**
       - Detect raw HTML injection, dynamic code evaluation, and unparameterized database queries.
    2. **Deep History Secrets Detection (GitLeaks / TruffleHog):**
       - Scan entire git history for leaked tokens, private keys, and OAuth client secrets.
       - If a secret is detected in git history, treat as compromised immediately: rotate credential + rewrite history.

### Phase 3: OWASP Top 10 Deep Audit Protocol
*   **Action:**
    1. **A01: Broken Access Control:** Audit every API route for user-ownership validation.
    2. **A02: Cryptographic Failures:** Ensure TLS 1.3 in transit, AES-256/ChaCha20 at rest, Argon2id for passwords.
    3. **A03: Injection:** Audit all SQL, NoSQL, OS command, and template interpolations.
    4. **A04: Insecure Design:** Validate rate limits, transaction timeouts, and circuit breakers.
    5. **A05: Security Misconfiguration:** Verify default credentials removed, debug routes disabled, verbose stack traces redacted.
    6. **A07: Identification & Auth Failures:** Verify brute-force lockout, session invalidation on logout.
    7. **A10: Server-Side Request Forgery (SSRF):** Restrict outbound URL fetchers to strict domain allowlists; block loopback addresses (`127.0.0.1`, `169.254.169.254`).

### Phase 4: Regulatory Compliance Mapping (SOC2, GDPR, HIPAA)
*   **Action:**
    1. **GDPR / CCPA:** Verify automated data export (`GET /api/user/export`) and hard deletion cascades (`DELETE /api/user/account`).
    2. **SOC 2 Type II:** Verify tamper-proof audit trails for administrative access, role elevation, and security configuration edits.
    3. **HIPAA / PCI-DSS:** Verify PII / cardholder data isolation, tokenization, and encryption key segregation.
