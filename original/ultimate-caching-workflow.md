---
name: ultimate-caching-workflow
description: >
  Workflow for caching architectures and runtime performance tuning.
  Coordinates multi-tier caching (L1 In-Memory + L2 Distributed Redis + L3 Edge CDN),
  cache stampede / dogpiling mutex prevention, Stale-While-Revalidate (SWR), tag-based invalidations,
  and bundle virtualization.
  Triggers on "ultimate caching workflow", "/ultimate-caching-workflow", or when
  designing application caching or resolving latency bottlenecks.
argument-hint: "[cache-strategy | latency-issue | --stampede | --swr | --redis]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Caching and Performance Workflow

## Inputs and freshness contract

Start with the slow operation, representative key distribution, deployment topology, data sensitivity, baseline latency/query rate and acceptable staleness. Specify tenant/user partitioning, serialization/schema version, size cap, TTL or explicit lifecycle, negative-cache policy and cache failure behavior. Cache only if evidence justifies added consistency complexity. Keep existing provider and client.

## Choose the relevant layers

- Process-local LRU: bound bytes and entries; instances do not share invalidations. Ephemeral memory is an optimization, never durable state.
- Shared cache: account for region latency, eviction, connection limits and outage. Key by authorization scope and schema version; never place secrets in keys/logs.
- CDN: cache public representations with correct cache key and `Vary`; private/authenticated responses need explicit safe policy. Review cookies, cache poisoning and header behavior on the actual CDN.
- Framework cache: check installed version and current invalidation semantics. Do not copy an old `revalidateTag` signature into another framework/version.

Measure hits, misses, eviction, stale serves, backend amplification and p50/p95/p99 latency against the baseline. No universal hit-rate or latency guarantee applies.

## Owner-safe bounded stampede protection example

Executable JavaScript with an injected adapter. Adapter operations accept `{signal}` and MUST honor it with bounded network timeouts. Contract: `get(key, options)`, `set(key,value,{ttlSeconds,signal})`, `tryAcquire(key,token,{leaseMs,signal})`, `releaseIfOwner(key,token,{signal})`. Last two are atomic Redis SET NX PX and token compare/delete (Lua or supported conditional-delete), not GET then DEL. Tokens must be unique per acquisition. Use null as a miss; encode cached null explicitly if needed.

```javascript
import { randomUUID } from 'node:crypto';
import { setTimeout as delay } from 'node:timers/promises';

export async function fetchWithStampedeProtection({
  cache, key, fetcher, ttlSeconds = 300, leaseMs = 10000,
  waitMs = 15000, signal,
}) {
  if (!(ttlSeconds > 0 && leaseMs > 0 && waitMs > 0)) {
    throw new RangeError('Positive TTL, lease and wait budgets required');
  }
  const bounded = signal
    ? AbortSignal.any([signal, AbortSignal.timeout(waitMs)])
    : AbortSignal.timeout(waitMs);
  const lockKey = `lock:${key}`;
  while (true) {
    bounded.throwIfAborted();
    const cached = await cache.get(key, { signal: bounded });
    if (cached !== null) return cached;
    const token = randomUUID();
    if (await cache.tryAcquire(lockKey, token, { leaseMs, signal: bounded })) {
      try {
        const fresh = await fetcher({ signal: bounded });
        bounded.throwIfAborted();
        await cache.set(key, fresh, { ttlSeconds, signal: bounded });
        return fresh;
      } finally {
        // Cleanup gets a separate short budget after caller cancellation.
        // Failure leaves a lease to expire; it must not mask the main result.
        try {
          await cache.releaseIfOwner(lockKey, token, {
            signal: AbortSignal.timeout(500),
          });
        } catch { /* Report through adapter telemetry without leaking keys. */ }
      }
    }
    await delay(50 + Math.floor(Math.random() * 100), undefined, { signal: bounded });
  }
}
```

This sample bounds waits with cooperative adapters on a compatible Node runtime; it does not stop a fetcher that ignores cancellation. Lease expiry can allow duplicate computation, and a late writer can overwrite fresher data. Use it for recomputable data only where the freshness contract tolerates this. For stronger ordering, add atomic ownership/fencing checks at publication or version checks enforced by the destination; do not use the mutex as payment correctness. Lease renewal must compare owner and have a maximum lifetime.

Atomic conditional-release Lua adapter fragment (illustrative; bind through the installed client and verify server support):

```lua
if redis.call('get', KEYS[1]) == ARGV[1] then
  return redis.call('del', KEYS[1])
end
return 0
```

## Invalidation and recovery

Document the database commit/cache invalidation race. Synchronous eviction can fail after commit or be followed by a stale read's cache publication. Use versioned values, durable invalidation/outbox, bounded stale TTL or bypass according to the required consistency. Specify L1 propagation and retry/repair; do not claim a cross-system transaction.

Choose fail-open to backend, serve-stale within an explicit age bound, or fail-closed for sensitive data. Protect the origin from outage traffic with concurrency/rate limits and circuit behavior. Never turn cache unavailability into an unbounded retry.

## Acceptance evidence

Inject lease expiry: A's cleanup cannot remove B's newer lock. Exercise cancellation, hung adapter, backend rejection, cache outage, tenant partition, negative cache and stale publication. Record actual deadline behavior and freshness limits. Compare load tests on equivalent workload; report untested provider adapter/lease assumptions. Roll back by disabling the cache or moving namespace while monitoring backend capacity.

Source: [Redis lock ownership and expiry](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/).
