---
name: ultimate-fullstack-workflow
description: >
  Flawless 10/10 Master Workflow for building full-stack applications, scalable backend microservices,
  and seamless frontend client integrations. Coordinates database schema design, REST/GraphQL/tRPC APIs,
  auth middleware, CORS controls, real-time sync (SSE/WebSockets), Next.js 15 Server Actions,
  and typed end-to-end client SDKs.
  Triggers on "ultimate fullstack workflow", "/ultimate-fullstack-workflow", or when
  initiating backend, full-stack, or API integration tasks.
argument-hint: "[api-spec | database-schema | fullstack-feature | --monolith | --microservices]"
---

# Ultimate Full-Stack Integration Workflow (10/10 Master Engine)

This workflow guides the end-to-end architecture, implementation, and production hardening of full-stack systems—linking high-performance databases, secure API layers, and fluid frontend client surfaces.

```
                                      [FULL-STACK FEATURE / SERVICE REQUIREMENT]
                                                          │
                          ┌───────────────────────────────┴───────────────────────────────┐
                          ▼                                                               ▼
              [PHASE 1: ARCHITECTURE & PROTOCOL]                              [PHASE 2: DATABASE & MIGRATIONS]
              ├─ Boundary Contract (tRPC / OpenAPI / gRPC)                    ├─ Relational Schemas & Indexes
              ├─ Storage Architecture (SQL + Redis)                           ├─ Reversible SQL Migrations
              └─ Real-Time Strategy (SSE / WebSockets)                        └─ Supabase / Postgres RLS Multi-Tenant
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: BACKEND CONTROLLERS & SECURE MIDDLEWARE            │
        │  • RequestID • CORS • RateLimit • Auth/RBAC • Input Validation (Zod) • Handlers │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: TYPED CLIENT INTEGRATIONS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🌐 REACT RSC │           │ 📱 REACT NAT │           │ 🔄 CACHE/SWR │
            │ Server Action│           │ Offline Sync │           │ TanStack Qry │
            └──────────────┘           └──────────────┘           └──────────────┘
                                               │
                                               ▼
                                  [PHASE 5: PRODUCTION HARDENING & SMOKE]
                    Build Verifications ──► DB Connection Pool Sizing ──► Graceful SIGTERM
```

---

## 🏛️ Iron Laws of Full-Stack Engineering

1. **Feature-First Modularity**: Group controllers, services, repositories, and UI components by **feature/domain** rather than technical layer.
2. **Strict Layer Separation**:
   - *Controllers / Handlers:* Handle HTTP parsing, parameter extraction, and status code serialization.
   - *Services:* Pure business logic with zero framework/HTTP coupling.
   - *Repositories:* Pure database access and query construction.
3. **Never Trust the Client**: Validate all data entering the backend via strict Zod schemas, regardless of frontend type-safety.
4. **Zero Float Currency Invariant**: Store financial amounts in integer minor currency units (cents).
5. **Mandatory Idempotency on Mutating Endpoints**: State-changing endpoints (`POST`/`PUT`/`PATCH`) must enforce `Idempotency-Key` headers.
6. **Graceful Teardown**: Listen for `SIGTERM` / `SIGINT` signals to flush connection pools, drain active requests, and close background queues cleanly.

---

## 🔬 The 5-Phase Full-Stack Pipeline

### Phase 1: Stack Architecture & Protocol Design
*   **Action:**
    1. Define boundary protocol: **tRPC** (type-safe monorepos), **OpenAPI REST** (public APIs), or **gRPC** (high-throughput microservices).
    2. Design database schemas and caching tiers (PostgreSQL + Upstash Redis).
    3. Specify real-time strategy (Server-Sent Events for one-way feeds, WebSockets for bidirectional collaboration).

### Phase 2: Database Schema & Migration Engineering
*   **Action:**
    1. Define declarative schema with explicit relational foreign keys, indexes on filtered/sorted fields, and check constraints.
    2. Write reversible migrations (`up` and `down` SQL).
    3. Configure connection pooling (PgBouncer in transaction mode on port 6543) to prevent connection starvation.
    4. Generate TypeScript definitions directly from the database schema.

### Phase 3: Backend API & Middleware Architecture
*   **Action:**
    1. Chain middleware in deterministic order:
       `RequestID` $\rightarrow$ `Structured Logger` $\rightarrow$ `CORS (Explicit)` $\rightarrow$ `Upstash Rate Limiter` $\rightarrow$ `Auth/JWT` $\rightarrow$ `RBAC Scope` $\rightarrow$ `Zod Validator` $\rightarrow$ `Handler` $\rightarrow$ `Global Error Catcher`.
    2. Implement transactional operations: wrap multi-table state mutations in database transactions with strict timeout limits.

### Phase 4: Typed Client & Frontend Integration
*   **Action:**
    1. In **Next.js 15 App Router**:
       - Default to React Server Components (RSC) for direct server-side data fetching.
       - Use Server Actions for mutations with authentication checks *inside* the action body.
    2. In **React / Client SPAs**:
       - Use TanStack Query (React Query) with optimistic updates and automatic cache invalidation.
    3. In **React Native**:
       - Implement offline-first local SQLite / WatermelonDB sync with background network reconciliation.

### Phase 5: Production Hardening, Smoke Testing & Handoff
*   **Action:**
    1. Execute end-to-end smoke test suite: verify happy path, authentication failure, validation errors, and network retry deduplication.
    2. Verify graceful process shutdown (`SIGTERM` handler closes database pool and Redis connection).
    3. Run `lint-and-validate` to guarantee clean TypeScript builds across all workspaces.
