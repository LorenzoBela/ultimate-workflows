---
name: ultimate-security-audit-workflow
description: >
  Master workflow for security vulnerability audits, static code analysis (SAST),
  dependency CVE scans, and regulatory compliance.
  Triggers on "ultimate security audit workflow", "/ultimate-security-audit-workflow",
  or when auditing dependencies, setting up SAST, checking compliance, or verifying OWASP.
argument-hint: "[cve-scan | compliance-check | sast-audit]"
---

# Ultimate Security Auditing & Compliance Workflow

This workflow guides security auditing, vulnerability checking, secrets detection, dependency scanning, and compliance verification to ensure codebases are secure and conform to regulatory standards.

---

## The 4-Phase Security Audit Pipeline

### Phase 1: Dependency Scanning & CVE Auditing
*   **Action:**
    1. Run automated scanners (Snyk, Trivy, `npm audit`, `pip-audit`) to detect vulnerabilities in third-party libraries.
    2. Analyze severity metrics (CVSS scores) and prioritize upgrades for libraries matching Critical or High ratings.
    3. Pin dependency versions in lock files to prevent malicious dependency upgrades during builds.
    4. Use `upstash-cli` to audit Upstash service configurations and API key permissions.

### Phase 2: Static Analysis (SAST) & Secrets Detection
*   **Action:**
    1. Configure SAST tools (SonarQube, Semgrep, ESLint security plugins) to scan codebase syntax for insecure patterns.
    2. Scan commits and repository histories for hardcoded credentials (using Trufflehog, GitGuardian, or GitLeaks).
    3. Block commits containing secrets using pre-commit hook policies.
    4. Use `Codebase Bloat & Dead Code Audit` to identify code patterns that create unnecessary attack surface.

### Phase 3: Vulnerability Testing (OWASP Top 10)
*   **Action:**
    1. Systematically audit the application against the OWASP Top 10:
       *   **Broken Access Control:** Verify user permissions are checked at all boundaries.
       *   **Cryptographic Failures:** Ensure passwords use bcrypt/Argon2, and transmission runs on TLS 1.3.
       *   **Injection:** Check for parameterized query compliance.
       *   **Security Misconfiguration:** Validate that production debug flags are disabled.
    2. Audit RLS policies on database layers using `supabase-mcp-server/get_advisors` and `execute_sql`.
    3. Retrieve and audit Firebase security rules using `firebase_get_security_rules`.
    4. Verify rate limiting is enforced using `upstash-ratelimit-js` on all sensitive endpoints.

### Phase 4: Regulatory Compliance Mapping (SOC2, GDPR, HIPAA)
*   **Action:**
    1. **GDPR/CCPA:** Verify paths for user data deletion, extraction, and privacy notice consents.
    2. **SOC2/HIPAA:** Audit system logging structures: ensure all user logins, administrative modifications, and security events leave audit logs.
    3. Generate compliance matrices mapping application configurations to targeted controls.
    4. Use `docx` for generating formal compliance audit reports in Word document format.
    5. Use Data Presentation & Deck Layouts for creating stakeholder-facing compliance presentation decks.
    6. Persist audit findings and compliance status to `memory` graph for ongoing tracking.

---

## Cross-Cutting Concerns
*   **Research:** Use Web Search, Web Extraction Tool, and `perplexity-ask` for researching CVE details, OWASP guidelines, and compliance framework requirements.
*   **E2E Testing:** Use Playwright / Headless Browser Automation for browser-based security testing (XSS probing, CSRF verification, auth flow testing).
*   **Database:** Use `ultimate-database-workflow` for deep RLS and constraint auditing.
*   **Deployment:** Use `ultimate-deployment-workflow` for verifying pre-deployment security checklists.
