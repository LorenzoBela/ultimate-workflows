---
name: ultimate-caching-workflow
description: >
  Master workflow for caching architectures and runtime performance tuning.
  Coordinates cache strategies (Redis, memory, HTTP), TTL design, list virtualization,
  and bundle size optimization.
  Triggers on "ultimate caching workflow", "/ultimate-caching-workflow", or when
  designing application caching or resolving latency bottlenecks.
argument-hint: "[cache-strategy | latency-issue]"
---

# Ultimate Caching & Performance Tuning Workflow

This workflow guides the design, implementation, and optimization of application caching layers and client-server response paths to minimize TTFB (Time to First Byte), prevent stale data states, and optimize runtime rendering speed.

---

## The 4-Phase Caching & Tuning Pipeline

### Phase 1: Cache Strategy & Architecture
*   **Action:**
    1. Select the appropriate caching tier: In-Memory (fastest, node-cache), Distributed (shared, Redis, or serverless Upstash Redis), or Client-Side (HTTP caching, LocalStorage).
    2. For serverless/edge environments (e.g., Next.js, Cloudflare Workers), prefer HTTP-based `@upstash/redis` to prevent connection-pooling exhaustion.
    3. Implement the **Cache-Aside** (Lazy Loading) pattern for expensive queries: check cache → miss → fetch database → write cache → return.
    4. **The TTL Law:** Every cached item must have a Time-To-Live (TTL). Never cache without an expiry condition. Leverage Upstash auto-serialization for storing native JS structures without manual stringification.
    5. Design cache invalidation hooks: delete/update cache keys immediately following database writes to prevent stale state.
    6. For rapid prototyping, use `upstash-redis-start` to provision a zero-config, no-signup Redis database instantly.

### Phase 2: Client-Side Performance & Asset Tuning
*   **Action:**
    1. Optimize assets: compress images to WebP/AVIF, lazy-load below-the-fold media, and define explicit height/width attributes to prevent Cumulative Layout Shift (CLS).
    2. Implement route-level and component-level code splitting (dynamic imports) to minimize initial JS bundle size.
    3. Apply list virtualization (windowing) for rendering lists exceeding 50+ items to preserve main thread frame rates.
    4. Use `next/image` for automatic image optimization in Next.js projects and `next/font` for zero-CLS font loading.
    5. In React Native, apply `React Native Performance Best Practices` for Hermes engine optimization and JS thread offloading.

### Phase 3: Network & API Optimization
*   **Action:**
    1. Bundle requests using debounce or throttle patterns for high-frequency client actions (typing searches, scrolling).
    2. Implement rate limiting on API gateways or serverless Edge Middleware using `@upstash/ratelimit` (sliding window, token bucket, or fixed window) to protect endpoints from abuse.
    3. Enable HTTP/2, Gzip/Brotli compression, and configure Cache-Control headers (e.g. `s-maxage`, `stale-while-revalidate`) on API gate boundaries.
    4. Prefetch critical routes or data dependencies asynchronously before the user completes navigation.
    5. For long-running background processing, use `upstash-qstash-js` to offload work and `upstash-workflow-js` for durable multi-step pipelines.
    6. Apply `PostgreSQL & Database Optimization Patterns` query optimization (indexes, EXPLAIN analysis) to reduce database response times.

### Phase 4: Verification & Benchmarking
*   **Action:**
    1. Profile cache hit rates, database read volume changes, and API latency improvements.
    2. Measure client-side metrics: Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), First Input Delay (FID).
    3. Verify that memory usage is bounded and that no caching leaks occur under heavy load.
    4. Run Web Interface & Accessibility Standards (WCAG 2.2) validation for Core Web Vitals compliance.
    5. Use `systematic-debugging` to trace any performance regression root causes.

---

## Cross-Cutting Concerns
*   **Vector Caching:** Use `upstash-vector-js` for caching AI embedding results with similarity-based retrieval.
*   **Search Caching:** Use `upstash-search-js` for caching full-text search indexes close to the edge.
*   **Research:** Use Web Search and official library documentation for discovering caching framework APIs and Redis patterns.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist caching architecture decisions across conversations.
