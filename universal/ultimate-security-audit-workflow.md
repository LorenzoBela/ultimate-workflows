---
name: ultimate-security-audit-workflow
description: >
  Engineering workflow for automated security vulnerability audits, static code analysis (SAST),
  dependency CVE scans, OWASP Top 10 penetration testing vectors, SLSA Level 3 supply chain checks,
  and regulatory compliance (SOC2, GDPR, HIPAA).
  Triggers on "ultimate security audit workflow", "/ultimate-security-audit-workflow",
  or when auditing dependencies, setting up SAST, checking compliance, or verifying OWASP.
argument-hint: "[cve-scan | compliance-check | sast-audit | --owasp | --supply-chain]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Security Auditing & Compliance Workflow (Engineering Workflow)

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

1. **Zero High/Critical CVEs Allowed in Production**: Treat severity as a triage input alongside affected version, deployed reachability, known exploitation, mitigations and the project's risk policy; exceptions require a recorded owner, evidence and expiry.
2. **Deterministic Lockfile Integrity**: All dependencies must be strictly pinned with cryptographic integrity hashes (`package-lock.json`, `pnpm-lock.yaml`).
3. **AST Source-to-Sink Verification**: Track untrusted input sources (`req.body`, `searchParams`) to dangerous execution sinks (`eval`, `innerHTML`, `exec`, unparameterized queries).
4. **Automated Pre-Commit Secrets Scanning**: Commits containing API keys, private keys, or passwords must be blocked at pre-commit gates (`gitleaks`).
5. **Continuous Compliance Governance**: Map applicable controls to evidence, owners and verification methods. Automated assertions cover technical subsets; they cannot certify SOC 2, GDPR or HIPAA compliance.

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
       - If a secret is detected in git history, treat as compromised immediately: report a redacted finding and coordinate revocation/rotation under the session's authorization. History rewrite is a separate shared-history action requiring explicit scope, collaborator coordination and recovery; an audit does not authorize it.

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
    1. **GDPR / CCPA:** Verify required export/deletion behavior against the data inventory, retention/legal-hold requirements and applicable policy; do not prescribe unconditional hard deletion or invent endpoints.
    2. **SOC 2 Type II:** Verify tamper-proof audit trails for administrative access, role elevation, and security configuration edits.
    3. **HIPAA / PCI-DSS:** Verify PII / cardholder data isolation, tokenization, and encryption key segregation.

## Authorized audit, triage and completion

Preflight records repositories/environments, allowed read-only and active probes, accounts/roles, exclusions and inherited authorization. Start with non-mutating inspection. An audit finding does not authorize credential rotation, history rewrite, dependency upgrade, production request or destructive test. Preserve raw scanner results with secrets redacted; findings include advisory ID, affected/fixed range, deployed exposure, source-to-sink evidence, trigger, impact, mitigating controls and actual verification limits. Scanner severity alone is not exploitability proof.

For SSRF, normalize and validate parsed URLs, permitted schemes/ports, DNS answers (IPv4/IPv6, mapped forms and private/link-local ranges), and every redirect hop. Prevent resolution/rebinding races using a supported transport/egress policy; a hostname allowlist plus one string check is insufficient. Exercise these cases only against authorized disposable targets.

Discover scanner/package versions and map the project's applicable OWASP/ASVS version rather than assuming an abbreviated numbered list is complete. Separate verified vulnerability, plausible candidate, false positive, accepted risk and unavailable check. Preserve secret fingerprints/locations without printing token values; store only necessary evidence with suitable retention/access. Compliance output is a control-evidence gap assessment, never certification.
