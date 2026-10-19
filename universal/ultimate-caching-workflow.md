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

<!-- INVARIANT_START:ANTI_AI_SLOP -->
## 🛑 HARDENED ANTI-AI SLOP MANDATE: NATURAL PROSE & BESPOKE DESIGN CRAFT
All agent communications, architectural plans, reviews, code comments, and frontend implementations MUST strictly adhere to natural human engineering standards. Both corporate AI prose slop and cookie-cutter "vibecoded" UI slop are strictly banned.

### 1. Zero Prose & Grammar Slop (Natural Human Voice)
- **Banned Lexicon:**
  - *Empty Verbs:* delve, embark, foster, resonate, underscore, leverage, elevate, harness, navigate, empower, illuminate, facilitate, tailor, showcase, unveil.
  - *Corporate Buzz-Adjectives:* testament, tapestry, beacon, cornerstone, robust, seamless, pivotal, crucial, paramount, cutting-edge, vibrant, bespoke, game-changer, journey, realm, landscape, holistic, comprehensive, multifaceted, versatile, transformative.
  - *Formulaic Transitions:* furthermore, moreover, in conclusion, it is worth noting, at the end of the day, without further ado, needless to say.
- **Banned Syntactical Patterns:**
  - **Zero Sycophancy / Pleasantries:** NEVER start responses with "Certainly!", "Great question!", "I'd be happy to help!", "Awesome!", or "Let's dive in!".
  - **Zero Summary Outros:** NEVER end answers with a repetitive paragraph restating earlier points using generic corporate filler.
  - **Zero Formulaic "Rule-of-Three" Bullets:** Do not default to 3-bullet lists where each bullet starts with a bold abstract noun followed by a colon and fluff.
  - **Zero Hedging:** Do not write "You might want to potentially consider checking...". Write "Check X, or Y crashes."
- **Natural Voice Standard:** Speak like a systems developer in terminal, Slack, or GitHub issues: blunt, concise, precise, pragmatic. Code and runnable shell commands come first.

### 2. Zero Visual & UI/UX Design Slop (Bespoke Engineering Craft)
- **Banned Color Clichés:**
  - BAN default AI Blue-to-Indigo/Purple gradients (`bg-gradient-to-r from-blue-600 to-indigo-700` or violet hues).
  - BAN colored ambient glowing shadows (`box-shadow` with >= 24px blur matching accent color).
  - BAN washed-out low-contrast gray text (`text-gray-400` / `text-gray-500` failing WCAG AA 4.5:1).
  - BAN gradient headline text (`bg-clip-text text-transparent bg-gradient-to-r` on H1s).
- **Banned Layout & Component Tropes:**
  - BAN cookie-cutter Bento Grid walls filled with fake stats, empty cards, or generic Lucide icon spam.
  - BAN centered hero boilerplate with a floating pill above H1 (`"✨ New: [Feature]"`).
  - BAN unmodified shadcn/ui defaults (`--radius: 0.5rem`, stock button/card exports without brand styling).
  - BAN tinted circular icon containers (`bg-primary/10 text-primary p-3 rounded-full`).
  - BAN static terminal window mockups with red/yellow/green dots in the hero.
  - BAN raw emojis used as icons (`✨`, `🚀`, `⚡`, `🔒`) in production UI markup.
- **Bespoke Design Standard:**
  - Commit to an intentional aesthetic: brutalist, high-density telemetry, refined editorial, or precision dark-mode.
  - High information density (Linear/Stripe standard), micro-borders (`rgba(255,255,255,0.08)`), and tabular numerals (`tabular-nums`).
  - Every component must implement all 7 states: `Default, Hover, Focus-Visible, Active, Loading (Skeleton), Disabled, Error`.
<!-- INVARIANT_END:ANTI_AI_SLOP -->

<!-- INVARIANT_START:GRAPHIFY -->
## 🧠 HARDENED GRAPHIFY KNOWLEDGE ENGINE GATE (AST-FIRST CODE INTELLIGENCE)
Whenever `graphify-out/graph.json` exists in the repository root, agents MUST interact with the AST knowledge graph. Blind directory traversal and unconstrained multi-file context dumping are strictly banned.

1. **Zero-Blind-Grep Invariant:**
   - Running unstructured grep (`grep -r`, `Select-String *.*`, `ripgrep` across entire project) to locate callers or symbol references is FORBIDDEN when `graph.json` is present.
   - Agents must query Graphify first: `graphify query "<symbol_or_concept>"`.

2. **Blast Radius Gate (`graphify explain "<symbol>"`):**
   - Before modifying, refactoring, or deleting any shared interface, model, route, or function, the agent MUST run `graphify explain "<symbol>"`.
   - If incoming edge count > 0, every caller surfaced by Graphify MUST be explicitly enumerated in the task DAG or implementation plan before touching code.

3. **Call-Path Fault Tracing (`graphify path "<source>" "<target>" --undirected`):**
   - When debugging multi-hop failures (e.g. UI -> API -> DB), the agent must run `graphify path` to map the exact shortest call chain between entry point and crash sink before reading source code.

4. **Leiden Community Worktree Partitioning:**
   - When spawning parallel subagents in `ultimate-multi-agent-invoker`, tasks MUST be partitioned by Leiden community clusters (from `graphify-out/graph.json`).
   - If two tasks share a God Node (identified in `graphify-out/GRAPH_REPORT.md`), they CANNOT run concurrently without explicit file-level mutex locks.

5. **Subagent Context Clamp (70% Token Reduction):**
   - Never dump entire raw source files into subagent prompts. Inject only the scoped subgraph from `graphify query "<task_scope>"`.

6. **Post-Commit AST Synchronization (`graphify update .`):**
   - After completing code modifications or merging Git worktrees, the agent MUST run `graphify update .` (local AST delta update, 2s runtime, 0 API tokens) to maintain graph synchronization.
<!-- INVARIANT_END:GRAPHIFY -->

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
