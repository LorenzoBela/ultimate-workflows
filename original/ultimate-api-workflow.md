---
name: ultimate-api-workflow
description: >
  Master workflow for API design, gateway management, GraphQL, gRPC, and reverse proxies.
  Coordinates Nginx/Traefik configurations, GraphQL resolvers, Protobuf specs, and API versioning.
  Triggers on "ultimate api workflow", "/ultimate-api-workflow", or when designing
  gRPC, GraphQL, Nginx routes, or planning API gateway policies.
argument-hint: "[graphql-schema | grpc-proto | gateway-config]"
---

# Ultimate API Design & Gateway Workflow

This workflow guides the design, routing, security, and versioning of APIs at the boundary—coordinating HTTP gateways, GraphQL schemas, gRPC endpoints, and reverse proxies.

---

## The 4-Phase API Design Pipeline

### Phase 1: Boundary Routing & Reverse Proxy (Nginx/Traefik)
*   **Sub-skills:** `upstash-ratelimit-js`, `upstash-qstash-js`
*   **Action:**
    1. Define proxy rules, redirect rules, and rewrite paths using standard reverse proxy formats (Nginx configs, Traefik dynamic files).
    2. Secure gateway configurations: enforce HTTPS redirection, set up SSL/TLS settings, and configure rate limit zones.
    3. Configure custom headers (e.g. `X-Request-ID` propagation, `X-Forwarded-For`, and secure CORS rules).
    4. Implement server-side rate limiting using `@upstash/ratelimit` (sliding window, token bucket, or fixed window) on gateway boundaries.
    5. For async webhook delivery and scheduled API calls, use `@upstash/qstash` to decouple request handling from execution.

### Phase 2: GraphQL Schema & Resolver Design
*   **Sub-skills:** `supabase-postgres-best-practices`, `upstash-redis-js`
*   **Action:**
    1. Construct clear, type-safe GraphQL schemas (SDL) defining queries, mutations, subscriptions, and types.
    2. Write efficient, N+1 free database resolvers. Use DataLoader patterns to batch and cache nested database hits.
    3. For federated systems, define schema boundaries and entity resolvers to enable clean gateway stitching.
    4. Cache expensive resolver results using `@upstash/redis` with TTL-controlled keys to reduce database pressure on hot queries.

### Phase 3: gRPC & Protobuf Engineering
*   **Sub-skills:** `lint-and-validate`
*   **Action:**
    1. Write protocol buffer specifications (`.proto` files) following style guides (CamelCase for messages, snake_case for fields).
    2. Explicitly specify message tags and manage field deprecation markers safely (never reuse tag numbers).
    3. Configure build pipelines to automatically compile `.proto` files into typed client/server stubs.
    4. Run `lint-and-validate` on generated stubs to ensure type consistency and zero compilation errors.

### Phase 4: API Versioning & Lifecycle Management
*   **Sub-skills:** `ultimate-fullstack-workflow`, `ultimate-documentation-workflow`, `ultimate-security-workflow`
*   **Action:**
    1. Enforce a strict versioning strategy: URI paths (e.g. `/v1/`), Accept Headers, or Custom Request Headers.
    2. Document deprecated endpoints clearly. Expose warning headers (e.g. `Sunset`, `Deprecation`) on API responses.
    3. Design backward-compatible contracts: when adding optional parameters or output fields, ensure old client integrations do not break.
    4. Use `ultimate-documentation-workflow` to generate OpenAPI/Swagger specs for all public endpoints.
    5. Apply `ultimate-security-workflow` boundary sanitization rules at every API entry point.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `context7/get-library-docs` for verifying API framework documentation and version compatibility.
*   **Testing:** Use `playwright` MCP for E2E API flow testing and `superpowers-tdd` for contract test coverage.
*   **Observability:** Use `upstash-workflow-js` to define multi-step API orchestration flows with durable step execution.
