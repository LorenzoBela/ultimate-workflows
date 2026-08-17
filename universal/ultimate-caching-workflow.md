---
name: ultimate-caching-workflow
description: >
  Flawless 10/10 Master Workflow for caching architectures and runtime performance tuning.
  Coordinates multi-tier caching (L1 In-Memory + L2 Distributed Redis + L3 Edge CDN),
  cache stampede / dogpiling mutex prevention, Stale-While-Revalidate (SWR), tag-based invalidations,
  and bundle virtualization.
  Triggers on "ultimate caching workflow", "/ultimate-caching-workflow", or when
  designing application caching or resolving latency bottlenecks.
argument-hint: "[cache-strategy | latency-issue | --stampede | --swr | --redis]"
---

# Ultimate Caching & Performance Tuning Workflow (10/10 Master Engine)

This workflow guides the design, implementation, and optimization of multi-tier caching architectures. It eliminates cache stampedes, guarantees high hit rates ($> 95\%$), prevents stale data anomalies, and optimizes Time to First Byte (TTFB).

```
                                      [INCOMING DATA REQUEST / QUERY]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [L1: IN-MEMORY CACHE (LRU)]                           [L2: DISTRIBUTED REDIS (UPSTASH)]
              ├─ Sub-millisecond lookup (<1ms)                      ├─ Shared across serverless nodes (<15ms)
              └─ Process-local memory pool                          └─ Upstash HTTP / Redis REST
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 CACHE STAMPEDE & MUTEX PREVENTION (DOGPILING SHIELD)        │
        │  • Probabilistic Early Expiration (XFetch) • Distributed Mutex Lock (NX)    │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [L3: EDGE CDN & SWR INVALIDATION]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔄 SWR TAGS  │           │ 🌐 EDGE CDN  │           │ 🧹 INVALIDATE│
            │ revalidateTag│           │ s-maxage=3600│           │ On DB Write  │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Caching

1. **The TTL Law**: Every cached entry MUST have an explicit Time-To-Live (TTL). Permanent keys without expiration are banned.
2. **Prevent Cache Stampedes (Dogpiling)**: Hot keys nearing expiration must use **Probabilistic Early Expiration (XFetch)** or **Mutex Locking** to prevent concurrent DB thundering herds.
3. **Invalidate on Mutation**: State-mutating writes must synchronously evict or update related cache tags before returning.
4. **Cache Key Versioning**: Namespaces must include schema versions (e.g. `v2:user:123:profile`) to prevent deserialization crashes upon model refactoring.
5. **No PII or Secrets in Edge Caching**: Never cache authenticated private data in public CDN or unencrypted shared tiers.

---

## 🔬 The 4-Tier Caching Architecture

### 1. Cache Stampede Prevention (Mutex Pattern)
```typescript
import { Redis } from '@upstash/redis';

const redis = Redis.fromEnv();

export async function fetchWithStampedeProtection<T>(
  key: string,
  fetcher: () => Promise<T>,
  ttlSeconds: number = 300
): Promise<T> {
  const cached = await redis.get<T>(key);
  if (cached !== null) return cached;

  // Acquire mutex lock to compute value
  const lockKey = `lock:${key}`;
  const acquired = await redis.set(lockKey, 'locked', { nx: true, ex: 10 });

  if (acquired) {
    try {
      const freshData = await fetcher();
      await redis.set(key, freshData, { ex: ttlSeconds });
      return freshData;
    } finally {
      await redis.del(lockKey);
    }
  } else {
    // Another worker is fetching; wait and retry
    await new Promise((resolve) => setTimeout(resolve, 200));
    return fetchWithStampedeProtection(key, fetcher, ttlSeconds);
  }
}
```

### 2. Multi-Tier Cache Hierarchy
- **L1 In-Memory LRU (Node.js/Edge):** For read-heavy hot objects ($< 1\text{ms}$).
- **L2 Distributed Redis (Upstash):** Global shared cache with automatic TTL and JSON serialization ($< 15\text{ms}$).
- **L3 Edge CDN (Vercel / Cloudflare):** Static and semi-static assets with `Cache-Control: public, s-maxage=3600, stale-while-revalidate=86400`.

### 3. Tag-Based Revalidation (Next.js 15)
```typescript
import { revalidateTag, unstable_cache } from 'next/cache';

// Cached fetcher with tag
export const getCachedProduct = unstable_cache(
  async (productId: string) => db.product.findUnique({ where: { id: productId } }),
  ['product-detail'],
  { tags: ['products'], revalidate: 3600 }
);

// In Server Action after update
export async function updateProduct(id: string, data: any) {
  await db.product.update({ where: { id }, data });
  revalidateTag('products'); // Evicts all tagged cache entries immediately
}
```
