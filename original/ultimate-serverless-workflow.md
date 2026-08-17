---
name: ultimate-serverless-workflow
description: >
  Flawless 10/10 Master Workflow for configuring, deploying, and managing serverless backend platforms
  (Supabase/Firebase), Edge Functions, connection poolers (PgBouncer), and ORM systems (Prisma)
  using Model Context Protocol (MCP) integrations.
  Triggers on "ultimate serverless workflow", "/ultimate-serverless-workflow", or when
  configuring database schemas, deploying Edge/Cloud functions, or writing RLS security rules.
argument-hint: "[supabase-deploy | firebase-rules | prisma-migrate | --edge | --pgbouncer]"
---

# Ultimate Serverless Backend Workflow (10/10 Master Engine)

This workflow coordinates operations, schema migrations, function deployments, cold-start mitigations, and environment configuration across serverless backends (Supabase, Firebase) and ORM systems (Prisma) using specialized MCP integrations.

```
                                      [SERVERLESS BACKEND TARGET]
                                                   │
                        ┌──────────────────────────┴──────────────────────────┐
                        ▼                                                     ▼
            [PHASE 1: ENVIRONMENT & MCP AUTH]                     [PHASE 2: SCHEMA MIGRATIONS & ORM]
            ├─ Supabase / Firebase Environment Scoping            ├─ Prisma migrate-dev / apply_migration
            ├─ Project Secrets & Connection Strings               ├─ PgBouncer Port 6543 (Pooler) Direct 5432
            └─ SDK Configs Generation                             └─ Typed TypeScript Definitions Gen
                        │
                        ▼
      ┌─────────────────────────────────────────────────────────────────────────────┐
      │                 PHASE 3: SECURITY POLICIES & RLS VERIFICATION               │
      │  • Supabase execute_sql (RLS Policies) • Firebase Security Rules • get_advisors│
      └──────────────────────────────────────┬──────────────────────────────────────┘
                                             ▼
                                [PHASE 4: EDGE FUNCTIONS & DURABLE WORKFLOWS]
                  ┌──────────────────────────┼──────────────────────────┐
                  ▼                          ▼                          ▼
          ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
          │ ⚡ DENO EDGE │           │ 🔄 WORKFLOW  │           │ 📬 QSTASH    │
          │ Deno Deploy  │           │ Upstash Flow │           │ Webhook Msg  │
          └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Serverless Backends

1. **Transaction Pooling on Port 6543**: Serverless functions must connect via PgBouncer transaction mode (`?pgbouncer=true&connection_limit=1`), reserving direct port 5432 strictly for ORM migrations.
2. **Cold-Start Budget ($< 250\text{ms}$)**: Edge functions must optimize dependencies, minimize global imports, and use lightweight HTTP clients (`@upstash/redis` over raw TCP drivers).
3. **Strict Row-Level Security**: No table may be deployed to production without explicit RLS policies for `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
4. **Zero State in Edge Memory**: Serverless and edge instances are ephemeral; state must reside in PostgreSQL, Upstash Redis, or QStash queues.
5. **Durable Multi-Step Execution**: Long-running or multi-stage operations MUST use `upstash-workflow-js` to guarantee execution resilience across cold-restarts.

---

## 🔬 The 4-Phase Serverless Pipeline

### Phase 1: Environment & Project Scoping
- Retrieve project configurations and publishable keys via MCP tools:
  - `supabase-mcp-server/get_project`, `supabase-mcp-server/get_publishable_keys`.
  - `firebase-mcp-server/firebase_get_sdk_config`, `firebase-mcp-server/firebase_get_environment`.

### Phase 2: Schema Migrations & Dual Connection Strings (Prisma)
- Configure `schema.prisma` with pooler and direct URL separation:
  ```prisma
  datasource db {
    provider  = "postgresql"
    url       = env("DATABASE_URL")      // PgBouncer Port 6543 (transaction mode)
    directUrl = env("DIRECT_URL")        // Direct Port 5432 (migrations only)
  }
  ```
- Run migrations via `prisma-mcp-server/migrate-dev` or `supabase-mcp-server/apply_migration`.
- Generate TypeScript client types using `supabase-mcp-server/generate_typescript_types`.

### Phase 3: RLS Security Policies & Advisor Audits
- Apply strict tenant policies using `supabase-mcp-server/execute_sql`:
  ```sql
  ALTER TABLE user_data ENABLE ROW LEVEL SECURITY;
  CREATE POLICY "Tenant isolation" ON user_data
    FOR ALL USING (tenant_id = auth.jwt()->>'tenant_id');
  ```
- Run `supabase-mcp-server/get_advisors` to detect missing policies or unindexed foreign keys.

### Phase 4: Edge Functions & Durable Upstash Workflows
- Deploy Deno edge functions using `supabase-mcp-server/deploy_edge_function`.
- Deploy durable serverless workflows with `upstash-workflow-js`:
  ```typescript
  import { serve } from '@upstash/workflow/nextjs';

  export const { POST } = serve(async (context) => {
    const data = await context.run('step-1', async () => fetchData());
    await context.sleep('wait-for-webhook', 300); // 5 minutes durable sleep
    await context.run('step-2', async () => processData(data));
  });
  ```
