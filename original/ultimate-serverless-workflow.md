---
name: ultimate-serverless-workflow
description: >
  Workflow for configuring, deploying, and managing serverless backend platforms
  (Supabase/Firebase), Edge Functions, connection poolers (PgBouncer), and ORM systems (Prisma)
  using Model Context Protocol (MCP) integrations.
  Triggers on "ultimate serverless workflow", "/ultimate-serverless-workflow", or when
  configuring database schemas, deploying Edge/Cloud functions, or writing RLS security rules.
argument-hint: "[supabase-deploy | firebase-rules | prisma-migrate | --edge | --pgbouncer]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Serverless Backend Workflow

## Inputs and environment preflight

Identify provider/project/environment, runtime/version, execution limits, auth, database/queue client, schema tool, delivery semantics and owner. Discover actual MCP/CLI capabilities; don't assume exact tool names exist. Preserve provider rather than requiring Supabase/Firebase/Upstash. Confirm target before mutation and never print keys/connection strings.

Separate emulator, staging and production. Configuration inspection does not prove deployment/policy application. Prepare reviewable changes and recovery within authorization; never deploy to an unrelated project.

## Data and production migrations

Use provider-supported driver/pooler for runtime networking/concurrency. Ports, connection URL flags, prepared statements and Prisma datasource configuration vary with versions. Verify actual transaction/session limitations; no universal connection_limit=1 rule applies.

Generate/test migrations in development. Apply reviewed migrations using the installed tool's production deploy path; never run reset-capable development migration tooling in production. Detect drift; never silently reset it. Use expand-contract, resumable backfills, lock/statement timeouts and mixed-client compatibility. Recovery may be code rollback, forward fix, retained columns/data or backup/PITR restore; down SQL is not automatically lossless. Generate types and inspect breaking changes.

## Authorization and policies

For client-exposed PostgreSQL enforce least-privilege grants and applicable RLS. Firebase needs its own rules/emulator checks; do not paste SQL there. Intentionally denied operations need no policy; don't grant all CRUD merely for checklist completeness.

Trusted tenant identity derives from verified auth/protected claims. Check claim types/nulls, membership revocation and actual runtime role. Test all CRUD, tenant reassignment, views, functions, owner/service bypass and expired credentials. Advisors are useful, not authorization proofs.

Illustrative PostgreSQL policy for UUID tenant claims; adapt role/function, verify protected claim origin and current membership before use:

```sql
ALTER TABLE tenant_records ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_scope ON tenant_records
FOR ALL TO authenticated
USING (tenant_id = ((auth.jwt() -> 'app_metadata' ->> 'tenant_id')::uuid))
WITH CHECK (tenant_id = ((auth.jwt() -> 'app_metadata' ->> 'tenant_id')::uuid));
```

Server-maintained claims can remain stale until token refresh. Sensitive actions may need current database membership; service/owner roles can bypass RLS. Test serving credentials.

## Functions, events and durable steps

Keep durable state outside ephemeral memory. Reuse safe clients, minimize dependencies and measure cold/warm p95 in target regions; no arbitrary cold-start guarantee.

Bound body, concurrency, external calls and execution to provider limits. Authenticate events using actual verifier/raw-body requirements; deduplicate trusted event/operation IDs. Expect retries, duplicates and possibly out-of-order delivery.

Use the selected durable queue/workflow engine when request lifetime or delayed/retried steps require it. Define step IDs, retryable/terminal failure, attempt/time budget, timeout/cancellation, DLQ/alerts, compensation and uncertain-effect reconciliation. Persist before acknowledgement as required; don't mandate one vendor for every multistep operation.

## Deployment, recovery and evidence

Package against runtime APIs and verify secret names without exposing values. Test emulator/unit plus disposable integration where available: tenant CRUD, duplicate/out-of-order events, timeout, credential expiry, migration interruption and partial workflow failure. Keep revision/schema compatibility and release manifest. Rollback cannot undo emitted events or charges.

Return safe project/environment identity, revision/migration IDs, actual checks and unverified limits. Without connected deployment infrastructure, deliver reviewed source/config and explicitly mark deployment/runtime checks incomplete.

Sources: [Prisma migration environments](https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production), [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security).
