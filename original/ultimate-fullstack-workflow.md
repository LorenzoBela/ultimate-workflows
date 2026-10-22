---
name: ultimate-fullstack-workflow
description: >
  Workflow for building full-stack applications, scalable backend microservices,
  and seamless frontend client integrations. Coordinates database schema design, REST/GraphQL/tRPC APIs,
  auth middleware, CORS controls, real-time sync (SSE/WebSockets), Next.js 15 Server Actions,
  and typed end-to-end client SDKs.
  Triggers on "ultimate fullstack workflow", "/ultimate-fullstack-workflow", or when
  initiating backend, full-stack, or API integration tasks.
argument-hint: "[api-spec | database-schema | fullstack-feature | --monolith | --microservices]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Fullstack Integration Workflow

## Inputs and vertical slice

Identify the user-visible feature, acceptance cases, existing frontend/backend/database versions, deployment topology, auth/tenant model, data sensitivity and external effects. Preserve the stack/provider. Define the smallest complete slice from UI through persistence; do not scaffold Redis, offline sync or microservices without need.

## Boundaries and contracts

- Follow existing code organization. Controllers parse/serialize; services own business decisions; repositories encapsulate storage where useful. Avoid layers that merely forward calls.
- Use the existing transport or document why REST/OpenAPI, GraphQL, tRPC, gRPC, SSE or WebSockets fits. Specify runtime schemas, errors, auth, pagination, deadlines and retries. Generate types/clients when supported and check real consumer compatibility.
- Financial values need currency scale, representation, rounding and overflow behavior; integer minor units or decimal are options. Do not assume all currencies use two decimals.
- Authorize objects/properties inside server operations, not only middleware. Client tenant IDs, prices and permissions are untrusted.

## Persistence and migration

Model keys, relationships, local constraints, tenant scope, query/index patterns and retention. Use bounded transactions for local atomic changes. For external effects use durable operation/outbox state and reconciliation; a database transaction does not cover a remote charge.

Use reviewed production migration commands; reserve development generation/reset tooling for development. Expand-contract permits mixed revisions: add compatible structure, backfill bounded resumable batches, verify, switch, then remove old structure. Recovery may be forward repair or tested restore; destructive down SQL is not automatically safe. Derive pooling from actual provider/driver limits and concurrency, not fixed ports.

## Backend behavior

Inspect framework middleware order rather than imposing one universal chain. Establish request correlation/redacted logs, bounded parsing, explicit CORS where needed, authentication, object authorization, abuse controls and validation before effects. Return safe errors; apply CSRF protection to cookie-authenticated mutations.

Use idempotency for duplicate-effect risks: principal/operation key scope, payload fingerprint, atomic uniqueness/state transition, payload-mismatch rejection and defined pending/crash outcomes. HTTP method names alone do not determine policy.

Handle deadline/cancellation, outage, concurrency conflict and size limits. Long-lived servers stop readiness before draining and close within host termination budget; edge/serverless runtimes use their supported lifecycle.

## Client and realtime integration

Use the current framework data model. App Router keeps secrets server-side and authorizes inside actions; SPAs use the current query/cache library. Define loading/error/empty states and optimistic rollback; don't turn unavailable servers into fake local success.

Add offline storage only when needed; define conflict resolution, ordering, deletion/tombstones, auth expiry, sensitive data and mutation replay. For SSE/WebSockets define reconnect/backoff, event ID/resume, duplicate suppression, auth expiry and connection limits.

## Validation, recovery and evidence

Run a meaningful end-to-end slice with disposable persistence where available: happy path, unauthenticated/cross-tenant access, invalid input, concurrent writes, duplicate retry and dependency timeout. Test optimistic rollback and applicable offline/reconnect conflicts. Verify old/new revisions coexist during migration and injected partial failure resumes/reconciles.

Report contract/schema/UI changes, actual build/test results, migration/recovery order and unverified provider assumptions. Keep compatible flag/route rollback while accounting for committed data. TypeScript success alone does not prove tenant isolation or duplicate-effect safety.
