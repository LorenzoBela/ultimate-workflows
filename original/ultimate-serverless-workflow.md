---
name: ultimate-serverless-workflow
description: >
  Master workflow for configuring, deploying, and managing serverless backend platforms (Supabase/Firebase)
  and ORM systems (Prisma) using Model Context Protocol (MCP) integrations.
  Triggers on "ultimate serverless workflow", "/ultimate-serverless-workflow", or when
  configuring database schemas, deploying Edge/Cloud functions, or writing RLS security rules.
argument-hint: "[supabase-deploy | firebase-rules | prisma-migrate]"
---

# Ultimate Serverless Backend Workflow

This workflow coordinates operations, schema migrations, function deployments, and environment configuration across serverless backends (Supabase, Firebase) and ORM systems (Prisma) using specialized MCP integrations.

---

## The 4-Phase Serverless Backend Pipeline

### Phase 1: Environment & Project Scoping (Supabase / Firebase)
*   **MCP Tools:** `supabase-mcp-server/list_projects`, `supabase-mcp-server/get_project`, `supabase-mcp-server/get_project_url`, `supabase-mcp-server/get_publishable_keys`, `firebase-mcp-server/firebase_list_projects`, `firebase-mcp-server/firebase_get_project`, `firebase-mcp-server/firebase_list_apps`, `firebase-mcp-server/firebase_get_sdk_config`, `firebase-mcp-server/firebase_get_environment`
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`
*   **Action:**
    1. Verify authentication states. Use `firebase_login` or verify Supabase API credentials.
    2. Check target projects using `list_projects` or `firebase_list_projects`. Get SDK configs and credentials.
    3. Configure environment variables (CORS origins, auth settings) via `firebase_update_environment` or local env bindings.
    4. Use `get_project_url` and `get_publishable_keys` for retrieving API base URLs and public keys.
    5. Use `firebase_list_apps` and `firebase_get_sdk_config` for multi-app platform configuration.
    6. Run `lint-and-validate` to verify all configuration files are syntactically correct.

### Phase 2: Schema Migrations & Database Synchronization (Prisma / Supabase)
*   **MCP Tools:** `prisma-mcp-server/migrate-dev`, `prisma-mcp-server/migrate-status`, `prisma-mcp-server/migrate-reset`, `supabase-mcp-server/apply_migration`, `supabase-mcp-server/list_migrations`, `supabase-mcp-server/list_tables`, `supabase-mcp-server/list_extensions`, `supabase-mcp-server/generate_typescript_types`
*   **Sub-skills:** `supabase-postgres-best-practices`, `upstash-redis-js`
*   **Action:**
    1. Define declarative models in `schema.prisma` or write SQL migration scripts.
    2. Synchronize schemas: execute `migrate-dev` for local database environments or `apply_migration` for Supabase targets.
    3. Check migration status using `migrate-status` to detect schema drift. Use `migrate-reset` only on development databases.
    4. List existing migrations using `list_migrations` and inspect tables using `list_tables`.
    5. Generate Type Safety: run `generate_typescript_types` to output TypeScript types matching database tables, ensuring end-to-end type safety.
    6. Run `Prisma-Studio` to inspect table records visually when testing local data payloads.
    7. Use `list_extensions` to verify required PostgreSQL extensions are enabled (e.g. `pgvector`, `uuid-ossp`).
    8. Apply `supabase-postgres-best-practices` for schema design, constraint enforcement, and index planning.
    9. Use `upstash-redis-js` for caching layer alongside serverless database operations.

### Phase 3: Security Policies & RLS Rules
*   **MCP Tools:** `firebase-mcp-server/firebase_get_security_rules`, `supabase-mcp-server/execute_sql`, `supabase-mcp-server/get_advisors`
*   **Sub-skills:** `ultimate-security-workflow`, `upstash-ratelimit-js`
*   **Action:**
    1. **Supabase RLS:** Define strict Row-Level Security (RLS) policies by executing SQL blocks (`execute_sql`). Verify policy filters index joined tables correctly.
    2. **Firebase Rules:** Retrieve existing rules using `firebase_get_security_rules`, modify configuration schemas, and push secure rules to production.
    3. **Advisor Audits:** Run `get_advisors` on Supabase to inspect tables for missing RLS policies, indexing gaps, or locking conflicts.
    4. Apply `ultimate-security-workflow` for comprehensive boundary sanitization and auth hardening.
    5. Implement serverless rate limiting using `upstash-ratelimit-js` on Edge Functions and API routes.

### Phase 4: Serverless Code Deployment & Branching
*   **MCP Tools:** `supabase-mcp-server/deploy_edge_function`, `supabase-mcp-server/list_edge_functions`, `supabase-mcp-server/get_edge_function`, `supabase-mcp-server/create_branch`, `supabase-mcp-server/list_branches`, `supabase-mcp-server/merge_branch`, `supabase-mcp-server/delete_branch`, `supabase-mcp-server/reset_branch`, `supabase-mcp-server/rebase_branch`, `supabase-mcp-server/get_logs`, `supabase-mcp-server/get_cost`, `supabase-mcp-server/confirm_cost`, `firebase-mcp-server/firebase_deploy`, `firebase-mcp-server/firebase_deploy_status`, `firebase-mcp-server/firebase_init`, `firebase-mcp-server/firebase_create_project`, `firebase-mcp-server/firebase_create_app`, `firebase-mcp-server/firebase_create_android_sha`
*   **Sub-skills:** `upstash-workflow-js`, `upstash-qstash-js`, `upstash-vector-js`, `upstash-search-js`
*   **Action:**
    1. **Function Deployments:** Package and deploy serverless functions: run `deploy_edge_function` (for Supabase Deno Edge functions) or `firebase_deploy` (for Firebase Cloud functions and static hosting).
    2. **Function Management:** List and inspect deployed functions using `list_edge_functions` and `get_edge_function`.
    3. **Branch Staging:** For collaborative environments, manage test branches using `create_branch`, `list_branches`, `merge_branch`, `delete_branch`, `reset_branch`, and `rebase_branch` to run integration checks before database merges.
    4. **Deployment Logs:** Track runtime execution, latency, and errors using `get_logs` or `firebase_deploy_status`.
    5. **Cost Management:** Monitor project costs using `get_cost` and confirm cost-impacting operations with `confirm_cost`.
    6. **Firebase Project Setup:** Use `firebase_init`, `firebase_create_project`, `firebase_create_app`, and `firebase_create_android_sha` for new Firebase project bootstrapping.
    7. **Durable Workflows:** For multi-step serverless orchestration, use `upstash-workflow-js` with idempotent step definitions and automatic retries.
    8. **Async Messaging:** Use `upstash-qstash-js` for scheduled tasks, webhook delivery, and message queues in serverless environments.
    9. **AI Features:** Use `upstash-vector-js` for vector similarity search and `upstash-search-js` for full-text search in Edge Functions.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `context7/get-library-docs`, and `perplexity-ask` for Supabase/Firebase/Prisma documentation and serverless architecture patterns.
*   **Memory:** Use `memory` MCP to persist serverless configurations, deployment states, and branch strategies across conversations.
*   **Documentation:** Use `ultimate-documentation-workflow` for API specs, function documentation, and environment setup guides.
*   **Testing:** Use `superpowers-tdd` for serverless function unit testing and `playwright` for E2E integration testing.
*   **Deployment:** Use `ultimate-deployment-workflow` for CI/CD pipeline integration with serverless deployments.
*   **Caching:** Use `upstash-redis-js` and `upstash-redis-start` for serverless-compatible caching (HTTP-based, no connection pooling).
*   **Rate Limiting:** Use `upstash-ratelimit-js` for Edge Middleware rate limiting.
*   **Developer Knowledge:** Use `firebase-mcp-server/developerknowledge_search_documents`, `developerknowledge_answer_query`, and `developerknowledge_get_documents` for Firebase developer knowledge base queries.
