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

<!-- INVARIANT_START:ANTI_AI_SLOP -->
## 🛑 HARDENED ANTI-AI SLOP MANDATE: NATURAL PROSE & BESPOKE DESIGN CRAFT
All agent communications, architectural plans, reviews, code comments, and frontend implementations MUST strictly adhere to natural human engineering standards. Both corporate AI prose slop and cookie-cutter "vibecoded" UI slop are strictly banned.

### 1. Zero Prose & Grammar Slop (Natural Human Voice)
- **Banned Lexicon:**
  - *Empty Verbs:* delve, embark, foster, resonate, underscore, leverage, elevate, harness, navigate, empower, illuminate, facilitate, tailor, showcase, unveil.
  - *Corporate Buzz-Adjectives:* testament, tapestry, beacon, cornerstone, robust, seamless, pivotal, crucial, paramount, cutting-edge, vibrant, bespoke, game-changer, journey, realm, landscape, holistic, comprehensive, multifaceted, versatile, transformative.
  - *Formulaic Transitions:* furthermore, moreover, in conclusion, it is worth noting, at the end of the day, without further ado, needless to say.
- **Banned Syntactical Patterns:**
  - **Zero Sycophancy / Pleasantries:** NEVER start responses with "Certainly!", "Great question!", "I'd be happy to help!", "Awesome!", or "Let's dive in!".
  - **Zero Summary Outros:** NEVER end answers with a repetitive paragraph restating earlier points using generic corporate filler.
  - **Zero Formulaic "Rule-of-Three" Bullets:** Do not default to 3-bullet lists where each bullet starts with a bold abstract noun followed by a colon and fluff.
  - **Zero Hedging:** Do not write "You might want to potentially consider checking...". Write "Check X, or Y crashes."
- **Natural Voice Standard:** Speak like a systems developer in terminal, Slack, or GitHub issues: blunt, concise, precise, pragmatic. Code and runnable shell commands come first.

### 2. Zero Visual & UI/UX Design Slop (Bespoke Engineering Craft)
- **Banned Color Clichés:**
  - BAN default AI Blue-to-Indigo/Purple gradients (`bg-gradient-to-r from-blue-600 to-indigo-700` or violet hues).
  - BAN colored ambient glowing shadows (`box-shadow` with >= 24px blur matching accent color).
  - BAN washed-out low-contrast gray text (`text-gray-400` / `text-gray-500` failing WCAG AA 4.5:1).
  - BAN gradient headline text (`bg-clip-text text-transparent bg-gradient-to-r` on H1s).
- **Banned Layout & Component Tropes:**
  - BAN cookie-cutter Bento Grid walls filled with fake stats, empty cards, or generic Lucide icon spam.
  - BAN centered hero boilerplate with a floating pill above H1 (`"✨ New: [Feature]"`).
  - BAN unmodified shadcn/ui defaults (`--radius: 0.5rem`, stock button/card exports without brand styling).
  - BAN tinted circular icon containers (`bg-primary/10 text-primary p-3 rounded-full`).
  - BAN static terminal window mockups with red/yellow/green dots in the hero.
  - BAN raw emojis used as icons (`✨`, `🚀`, `⚡`, `🔒`) in production UI markup.
- **Bespoke Design Standard:**
  - Commit to an intentional aesthetic: brutalist, high-density telemetry, refined editorial, or precision dark-mode.
  - High information density (Linear/Stripe standard), micro-borders (`rgba(255,255,255,0.08)`), and tabular numerals (`tabular-nums`).
  - Every component must implement all 7 states: `Default, Hover, Focus-Visible, Active, Loading (Skeleton), Disabled, Error`.
<!-- INVARIANT_END:ANTI_AI_SLOP -->

<!-- INVARIANT_START:GRAPHIFY -->
## 🧠 HARDENED GRAPHIFY KNOWLEDGE ENGINE GATE (AST-FIRST CODE INTELLIGENCE)
Whenever `graphify-out/graph.json` exists in the repository root, agents MUST interact with the AST knowledge graph. Blind directory traversal and unconstrained multi-file context dumping are strictly banned.

1. **Zero-Blind-Grep Invariant:**
   - Running unstructured grep (`grep -r`, `Select-String *.*`, `ripgrep` across entire project) to locate callers or symbol references is FORBIDDEN when `graph.json` is present.
   - Agents must query Graphify first: `graphify query "<symbol_or_concept>"`.

2. **Blast Radius Gate (`graphify explain "<symbol>"`):**
   - Before modifying, refactoring, or deleting any shared interface, model, route, or function, the agent MUST run `graphify explain "<symbol>"`.
   - If incoming edge count > 0, every caller surfaced by Graphify MUST be explicitly enumerated in the task DAG or implementation plan before touching code.

3. **Call-Path Fault Tracing (`graphify path "<source>" "<target>" --undirected`):**
   - When debugging multi-hop failures (e.g. UI -> API -> DB), the agent must run `graphify path` to map the exact shortest call chain between entry point and crash sink before reading source code.

4. **Leiden Community Worktree Partitioning:**
   - When spawning parallel subagents in `ultimate-multi-agent-invoker`, tasks MUST be partitioned by Leiden community clusters (from `graphify-out/graph.json`).
   - If two tasks share a God Node (identified in `graphify-out/GRAPH_REPORT.md`), they CANNOT run concurrently without explicit file-level mutex locks.

5. **Subagent Context Clamp (70% Token Reduction):**
   - Never dump entire raw source files into subagent prompts. Inject only the scoped subgraph from `graphify query "<task_scope>"`.

6. **Post-Commit AST Synchronization (`graphify update .`):**
   - After completing code modifications or merging Git worktrees, the agent MUST run `graphify update .` (local AST delta update, 2s runtime, 0 API tokens) to maintain graph synchronization.
<!-- INVARIANT_END:GRAPHIFY -->

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
