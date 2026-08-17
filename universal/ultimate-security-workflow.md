---
name: ultimate-security-workflow
description: >
  Flawless 10/10 Master Workflow for application security hardening, zero-trust architectures,
  cryptographic protection, input sanitization, automated CORS/CSP headers, Upstash rate limiting,
  and database Row-Level Security (RLS).
  Triggers on "ultimate security workflow", "/ultimate-security-workflow", or when
  handling authentication, user data, cryptographic functions, or production hardening.
argument-hint: "[security-audit | auth-flow | rls-policy | --hardening | --zero-trust]"
---

# Ultimate Security & Application Hardening Workflow (10/10 Master Engine)

This workflow drives full-spectrum application hardening, data privacy defense, zero-trust authentication, cryptographic safety, and database multi-tenant isolation.

```
                                      [UNTRUSTED CLIENT REQUEST / INGRESS]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: BOUNDARY DEFENSE & WAF]                             [PHASE 2: ZERO-TRUST AUTH]
              ├─ Strict Zod / Schema Sanitization                           ├─ Ephemeral JWT + HttpOnly Cookies
              ├─ Parameterized SQL (Zero Interpolation)                     ├─ Role-Based RBAC & Scope Guards
              └─ Upstash Sliding-Window Rate Limiting                       └─ Argon2id Password Hashing
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: INFRASTRUCTURE & NETWORK HARDENING                 │
        │  • Strict CSP & HSTS Headers • CORS Whitelist • Signed QStash Webhooks      │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: DATABASE RLS & AUDIT INTEGRITY]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔒 SUPABASE  │           │ 📜 AUDIT LOG │           │ 🔐 SECRETS   │
            │ Strict RLS   │           │ Immutable Log│           │ Zero Git Leak│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Security & Hardening

1. **Never Trust External Input**: 100% of incoming payloads must be strictly validated and sanitized at the boundary (Zod, Pydantic, JSON Schema).
2. **Zero SQL Concatenation**: Raw SQL string interpolation is an unconditional blocking defect. Use parameterized queries or typed ORMs.
3. **Zero Secrets in Source Code**: API keys, private keys, database credentials, and signing secrets must never be committed to git repositories.
4. **Least Privilege by Default**: Services, IAM roles, and database users must operate with minimum permissions necessary.
5. **No Auth Tokens in Browser Storage**: JWTs and session secrets must never reside in `localStorage` or `sessionStorage`. Use `httpOnly`, `secure`, `sameSite=strict` cookies.
6. **Row-Level Security (RLS) on 100% of User Tables**: Every multi-tenant database table must enforce explicit RLS policies tied to authenticated user/organization IDs.
7. **Cryptographic Standard**: Passwords hashed exclusively with **Argon2id** or **bcrypt** ($\ge 12$ rounds). Symmetric data encryption uses **AES-256-GCM** or **ChaCha20-Poly1305**.
8. **Automated Rate Limiting on All Public Endpoints**: Sensitive endpoints (auth, search, checkout, AI calls) MUST be protected by sliding-window rate limiters (Upstash Redis).

---

## 🛡️ The 4-Phase Security Pipeline

### Phase 1: Boundary Input Sanitization & WAF Protection
*   **Action:**
    1. **Strict Type Coercion & Schema Validation:**
       ```typescript
       import { z } from 'zod';
       
       export const CheckoutSchema = z.object({
         amountInCents: z.number().int().positive().max(10000000), // Max $100k
         currency: z.enum(['usd', 'eur', 'gbp']),
         idempotencyKey: z.string().uuid(),
       }).strict(); // Disallow unexpected unknown properties
       ```
    2. **XSS & Content Security Policy (CSP):**
       - Configure strict nonces or hashes for scripts; ban `unsafe-inline` and `eval`.
    3. **Upstash Sliding-Window Rate Limiting:**
       ```typescript
       import { Ratelimit } from '@upstash/ratelimit';
       import { Redis } from '@upstash/redis';

       const ratelimit = new Ratelimit({
         redis: Redis.fromEnv(),
         limiter: Ratelimit.slidingWindow(10, '10 s'),
         analytics: true,
       });
       ```

### Phase 2: Zero-Trust Authentication & Session Lifecycle
*   **Action:**
    1. **Short-Lived Access Tokens (15m) + Rotating Refresh Tokens:**
       - Issue short-lived tokens. On refresh, rotate refresh token family; invalidate all sessions if token reuse is detected.
    2. **Role-Based Access Control (RBAC):**
       - Enforce permission checks *inside* the business logic layer, not merely at route middleware.
    3. **MFA & Step-Up Auth:**
       - Require re-authentication / TOTP confirmation for high-privilege actions (password change, payout account modification).

### Phase 3: Network & Infrastructure Hardening
*   **Action:**
    1. **Security Headers Configuration:**
       - `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
       - `X-Content-Type-Options: nosniff`
       - `X-Frame-Options: DENY`
       - `Referrer-Policy: strict-origin-when-cross-origin`
    2. **Strict CORS Whitelist:**
       - Explicit origin array matching; reject wildcard `*` in authenticated APIs.
    3. **Cryptographically Signed Webhooks (QStash / Stripe):**
       - Verify HMAC signatures on all inbound webhook requests before processing payloads.

### Phase 4: Database RLS & Immutable Audit Trails
*   **Action:**
    1. **Postgres Row-Level Security (Supabase):**
       ```sql
       ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;

       CREATE POLICY "Users can only view their own profile"
       ON user_profiles FOR SELECT
       USING (auth.uid() = user_id);

       CREATE POLICY "Users can only update their own profile"
       ON user_profiles FOR UPDATE
       USING (auth.uid() = user_id)
       WITH CHECK (auth.uid() = user_id);
       ```
    2. **Immutable Audit Logging:**
       - Log all permission changes, authentication events, and financial mutations to an append-only audit log table.
