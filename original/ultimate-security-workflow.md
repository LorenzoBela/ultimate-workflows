---
name: ultimate-security-workflow
description: >
  Master workflow for securing and hardening applications. Coordinates input
  sanitization, authentication architectures, secure HTTP headers, CORS controls,
  rate limiting, and database Row-Level Security (RLS).
  Triggers on "ultimate security workflow", "/ultimate-security-workflow", or when
  handling authentication, user data, cryptographic functions, or production hardening.
argument-hint: "[security-audit | auth-flow | rls-policy]"
---

# Ultimate Security & Hardening Workflow

This workflow drives security audits and implementation to protect user data, prevent exploitation (injection, XSS, CSRF), and lock down application environments.

---

## The 4-Phase Security Pipeline

### Phase 1: Boundary & Input Sanitization
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`
*   **Action:**
    1. **Trust No Client:** Validate and sanitize all incoming payloads at the boundary using schema validators (Zod, Pydantic, etc.).
    2. Prevent SQL injection by using parameterized queries or typed ORM builders. Never string-interpolate queries with user input.
    3. Prevent Cross-Site Scripting (XSS) by HTML-escaping dynamic content before rendering and implementing a strict Content Security Policy (CSP).
    4. Protect file upload paths: validate file types (MIME-types, magic bytes) and upload directly to secure, isolated storage (e.g. S3 presigned PUT).
    5. Run `lint-and-validate` to verify no unsafe code patterns exist in input handling code.

### Phase 2: Authentication & Session Security
*   **Sub-skills:** `upstash-redis-js`, `upstash-ratelimit-js`
*   **MCP Tools:** `firebase-mcp-server/firebase_login`, `supabase-mcp-server/execute_sql`
*   **Action:**
    1. Enforce short-lived access tokens (e.g. 15-minute JWTs) paired with secure refresh tokens stored in `httpOnly`, `secure`, `sameSite: strict` cookies.
    2. Never store authentication tokens or PII in `localStorage` or `sessionStorage` (XSS extraction risk).
    3. Implement Role-Based Access Control (RBAC): verify route permissions using middleware *before* invoking handler functions.
    4. Hash passwords using slow cryptographic algorithms (bcrypt, Argon2) with custom salts.
    5. Use `upstash-redis-js` for distributed session storage with automatic TTL expiration.
    6. Use `upstash-ratelimit-js` for brute-force login attempt protection.

### Phase 3: Network & Infrastructure Hardening
*   **Sub-skills:** `upstash-ratelimit-js`, `upstash-qstash-js`
*   **Action:**
    1. Configure secure HTTP headers using `Helmet` or equivalent configurations (HSTS, clickjacking prevention, X-Content-Type-Options).
    2. Configure strict Cross-Origin Resource Sharing (CORS) rules. Explicitly list allowed origins; never allow wildcard (`*`) origins in production.
    3. Implement rate-limiting and API throttling on boundary gates to protect against Denial of Service (DoS) and brute-force attempts using `upstash-ratelimit-js`.
    4. Validate environment variable configurations at application startup. Fail fast on missing cryptographic secrets.
    5. Use `upstash-qstash-js` for secure, signed webhook delivery to prevent request spoofing.

### Phase 4: Database & Dependency Auditing
*   **Sub-skills:** `supabase-postgres-best-practices`, `ultimate-security-audit-workflow`
*   **MCP Tools:** `supabase-mcp-server/get_advisors`, `supabase-mcp-server/execute_sql`, `firebase-mcp-server/firebase_get_security_rules`
*   **Action:**
    1. Enable Row-Level Security (RLS) on all database tables. Define strict RLS policies (e.g., matching authenticated user IDs).
    2. Run automated dependency vulnerability scans (e.g., `npm audit`, `pip-audit`, Snyk). Upgrade deprecated or compromised libraries.
    3. Verify that log files do not leak sensitive information (passwords, JWTs, credit card numbers, or full PII).
    4. Use `supabase-mcp-server/get_advisors` for automated RLS, index, and locking conflict audits.
    5. Use `firebase_get_security_rules` to verify Firebase Realtime Database and Firestore security rules.
    6. Apply `ultimate-security-audit-workflow` for comprehensive OWASP Top 10 and compliance auditing.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `perplexity-ask`, and `context7/get-library-docs` for security best practices, OWASP resources, and framework-specific hardening guides.
*   **Memory:** Use `memory` MCP to persist security configurations, RLS policies, and audit findings across conversations.
*   **Testing:** Use `playwright` MCP for E2E security testing (XSS probing, CSRF verification, auth flow testing).
*   **Review:** Use `superpowers-review` and `caveman-review` for security-focused code review.
