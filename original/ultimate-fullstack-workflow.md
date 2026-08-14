---
name: ultimate-fullstack-workflow
description: >
  Master workflow for building full-stack applications and backend services.
  Coordinates database schemas, REST/GraphQL APIs, auth middleware, CORS, real-time sync,
  and API client integrations.
  Triggers on "ultimate fullstack workflow", "/ultimate-fullstack-workflow", or when
  initiating backend, full-stack, or API integration tasks.
argument-hint: "[api-spec | database-schema | fullstack-feature]"
---

# Ultimate Full-Stack Integration Workflow

This workflow guides the end-to-end design, implementation, and hardening of full-stack systems—linking databases, backend APIs, and frontend client boundaries securely and performantly.

---

## The 5-Phase Full-Stack Pipeline

### Phase 1: Requirements & Stack Selection
*   **Sub-skills:** `concise-planning`, `superpowers-brainstorm`, `sequential-thinking/sequentialthinking`
*   **Action:**
    1. Define the stack configuration (e.g. Node/Express + React, Next.js monolith, Go + SQLite).
    2. Determine boundary contracts (REST, GraphQL, tRPC, or OpenAPI).
    3. Specify storage systems (SQL connection pools, Redis cache, S3 file buckets).
    4. Confirm real-time triggers (SSE, WebSockets, or polling) and authentication strategy (JWT, cookie sessions, OAuth).
    5. Use `concise-planning` for atomic task breakdown and `superpowers-brainstorm` for evaluating stack alternatives.

### Phase 2: Database Schema & Migration Engineering
*   **Sub-skills:** `supabase-postgres-best-practices`, `upstash-redis-js`, `upstash-vector-js`, `upstash-search-js`
*   **MCP Tools:** `supabase-mcp-server/apply_migration`, `prisma-mcp-server/migrate-dev`, `supabase-mcp-server/list_tables`
*   **Action:**
    1. Define declarative database schemas, ensuring proper relational constraints, foreign keys, and indexes.
    2. Author and run migrations (never manual database changes). Ensure migrations are reversible.
    3. Configure connection pooling (timeout, idle bounds, pool size) to prevent database resource starvation.
    4. Use `upstash-redis-js` for session caching and ephemeral state alongside the primary SQL database.
    5. For AI features, design vector schemas using `upstash-vector-js` and full-text search using `upstash-search-js`.
    6. Generate TypeScript types from schema using `supabase-mcp-server/generate_typescript_types`.

### Phase 3: Backend API & Middleware Architecture
*   **Sub-skills:** `ultimate-security-workflow`, `upstash-ratelimit-js`, `upstash-qstash-js`, `upstash-workflow-js`
*   **Action:**
    1. Enforce **feature-first** organization: group controllers, services, and repositories by feature (not technical layer).
    2. Layer logic: Controllers handle HTTP requests/responses; Services contain pure business logic; Repositories manage database access.
    3. **Trust No Client:** Perform strict schema input validation (Zod, Pydantic, Go validator) at the trust boundary.
    4. Configure security middleware in order: RequestID → JSON Logging → CORS (explicit origins only) → Rate Limiting → Auth → Authz → Input Validation → Handler → Global Error Handler.
    5. Use `upstash-ratelimit-js` for serverless rate limiting and `upstash-qstash-js` for async webhook delivery.
    6. For durable multi-step backend processes, use `upstash-workflow-js` with idempotent step definitions.

### Phase 4: Cross-Boundary API Client Integration
*   **Sub-skills:** `next-best-practices`, `vercel-react-best-practices`, `vercel-react-native-skills`
*   **Action:**
    1. Set up a typed API client (Fetch wrapper, React Query hooks, tRPC routers, or generated OpenAPI SDKs) pointing to base URLs fed from environment configurations.
    2. Enforce cross-boundary error handling: catch backend HTTP errors and map them to human-readable UI messages.
    3. Implement automatic access token refreshes (using httpOnly cookies and interceptors).
    4. For Next.js, apply `next-best-practices` for RSC data fetching, route handlers, and metadata.
    5. For React Native, apply `vercel-react-native-skills` for native networking patterns and offline-first caching.

### Phase 5: Hardening, Smoke Testing & Handoff
*   **Sub-skills:** `lint-and-validate`, `superpowers-tdd`, `superpowers-review`, `systematic-debugging`
*   **Action:**
    1. Run build verifications to ensure clean compiles for both frontend and backend assets.
    2. Perform smoke tests: test endpoint payloads, CORS limits, and database transactions under simulated failures.
    3. Document deployment instructions, entry files, environmental requirements, and gracefully handle SIGTERM shutdowns.
    4. Run `lint-and-validate` for final code quality checks.
    5. Use `superpowers-tdd` for test-driven verification and `superpowers-review` for severity-rated code audit.

---

## Cross-Cutting Concerns
*   **MCP Integrations:** Use `firebase-mcp-server` for Firebase Auth, hosting, and Cloud Functions; `supabase-mcp-server` for Supabase Edge Functions, RLS, and SQL operations.
*   **Deployment:** Use `ultimate-deployment-workflow` for CI/CD pipeline configuration and `ultimate-serverless-workflow` for serverless backend operations.
*   **Research:** Use `tavily-search`, `context7/get-library-docs` for framework documentation and API references.
*   **Memory:** Use `memory` MCP to persist full-stack architecture decisions and API contracts across conversations.
*   **Documentation:** Use `ultimate-documentation-workflow` for API specs, README, and onboarding guides.
