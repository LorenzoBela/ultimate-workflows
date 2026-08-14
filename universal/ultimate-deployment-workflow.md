---
name: ultimate-deployment-workflow
description: >
  Master workflow for CI/CD, environments setup, builds, deployment pipelines,
  monitoring, and rollback engineering.
  Coordinates GitHub Actions, Docker packaging, staging/production boundaries,
  health check diagnostics, and serverless/edge functions deployments.
  Triggers on "ultimate deployment workflow", "/ultimate-deployment-workflow", or when
  handling releases, Dockerfiles, CI configurations, or service deployments.
argument-hint: "[ci-config | dockerfile | deploy-target]"
---

# Ultimate Deployment & Ops Workflow

This workflow drives reliable release engineering, containerization, staging/production delivery, automated health checks, and rollback safety.

---

## The 4-Phase Deployment Pipeline

### Phase 1: Configuration & Secrets Verification
*   **Action:**
    1. Verify all production environment variables are configured. Do not bundle secrets or API keys into static source code builds.
    2. Confirm secret keys (database URIs, auth keys) are injected securely via vault managers (AWS Secrets Manager, GitHub Secrets, Supabase environment variables).
    3. Run pre-flight checks to validate configuration variables before starting containers (fail fast).
    4. Use `firebase_get_environment` or `supabase/get_project` to verify remote project settings match local expectations.
    5. Run Strict Linting & Type Validation to ensure the codebase is error-free before building artifacts.

### Phase 2: Build & Containerization (Docker / CI)
*   **Action:**
    1. Write optimized, multi-stage `Dockerfiles` (compile in build stage, copy compiled binary to lean scratch/alpine release stage to minimize image footprint).
    2. Define CI configurations (GitHub Actions, GitLab CI): run linters (Strict Linting & Type Validation), typecheck scripts, and integration tests before packaging artifacts.
    3. Pin base image tags (e.g. `node:20.11-alpine` instead of `node:latest`) to guarantee build reproducibility.
    4. Use `Conventional Semantic Git Commits` for conventional, terse commit messages on deployment branches.

### Phase 3: Deployment Execution (Vercel / Supabase / Firebase / Cloud)
*   **Action:**
    1. Deploy static assets or edge/serverless functions using platform SDKs (e.g. `supabase db push`, `firebase deploy`, or `vercel deploy`).
    2. Run database migrations immediately prior to deploying API updates. Design migrations to be backward-compatible (so old code can query the schema during rollouts).
    3. Separate deployments into Staging first, verify behaviors, then promote to Production.
    4. Use `supabase-mcp-server/create_branch` for branch-based staging environments with schema isolation.
    5. For async deployment tasks, use `upstash-qstash-js` for scheduled post-deploy operations and `upstash-workflow-js` for multi-step deployment orchestration.

### Phase 4: Monitoring, Health Checks & Rollbacks
*   **Action:**
    1. Verify the deployment registers successful pings to `/health` and `/ready` endpoints.
    2. Observe runtime execution logs using `get_logs` or `firebase_deploy_status` for error tracking.
    3. Configure automated rollbacks: if health checks fail or error rates spike post-deployment, immediately trigger the rollback of the container or function version.
    4. Implement graceful shutdown handlers (`SIGTERM`) to finish active requests before terminating container instances.
    5. Use `upstash-redis-js` for deployment feature flags (Redis-backed toggle states) enabling instant rollback without redeployment.
    6. Apply `systematic-debugging` for diagnosing post-deployment incidents.

---

## Cross-Cutting Concerns
*   **Research:** Use Web Search and official library documentation for CI/CD platform documentation and Docker best practices.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist deployment configurations, rollback procedures, and incident responses across conversations.
*   **Security:** Apply `ultimate-security-workflow` and `ultimate-security-audit-workflow` for pre-deployment security verification.
*   **Documentation:** Use `ultimate-documentation-workflow` to maintain deployment runbooks and environment setup guides.
