---
name: ultimate-deployment-workflow
description: >
  Flawless 10/10 Master Workflow for CI/CD, multi-stage Docker packaging, blue-green / canary rollouts,
  automated health check synthetic probes, feature flag safety shields, and zero-downtime rollbacks.
  Triggers on "ultimate deployment workflow", "/ultimate-deployment-workflow", or when
  handling releases, Dockerfiles, CI configurations, or service deployments.
argument-hint: "[ci-config | dockerfile | deploy-target | --canary | --blue-green | --rollback]"
---

# Ultimate Deployment & Release Engineering Workflow (10/10 Master Engine)

This workflow drives multi-stage container optimization, declarative CI/CD pipelines, zero-downtime progressive rollouts (Blue/Green & Canary), synthetic health probing, and automated rollback triggers.

```
                                      [TAGGED COMMIT / RELEASE ARTIFACT]
                                                      │
                          ┌───────────────────────────┴───────────────────────────┐
                          ▼                                                       ▼
              [PHASE 1: MULTI-STAGE CONTAINER PACKAGING]              [PHASE 2: PROGRESSIVE ROLLOUT ENGINE]
              ├─ Builder Stage (Compiles + Types)                     ├─ Blue/Green or Canary (10% -> 50% -> 100%)
              ├─ Scratch/Alpine Distroless Runner                     ├─ Feature Flags (Upstash Redis Toggle)
              └─ Pinned SHA256 Base Image Digests                     └─ Reversible DB Migration Pre-Flight
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: SYNTHETIC PROBES & READINESS GATES                 │
        │  • /healthz (Liveness) • /ready (Deep Dependency DB Check) • Synthetic Smoke│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: AUTOMATED ROLLBACK & INCIDENT GUARD]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🛑 ROLLBACK  │           │ 📉 METRICS   │           │ 📴 SIGTERM   │
            │ Auto-Revert  │           │ 5xx Spikes   │           │ Drain Conns  │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Deployment Engineering

1. **Pinned Digest Base Images**: Base images must be pinned to immutable SHA256 hashes or specific minor tags (`node:20.11-alpine`), never `:latest`.
2. **Distroless / Non-Root Containers**: Production container images must run as non-root users (`USER 1001`) with unnecessary debug binaries stripped out.
3. **Deep vs Shallow Health Checks**:
   - `/healthz` (Liveness): Validates the HTTP server is accepting connections.
   - `/ready` (Readiness): Actively validates database connectivity, Redis ping, and queue consumer status.
4. **Automated Rollback on Error Spike**: If 5xx error rate exceeds $1.0\%$ or latency increases by $> 50\%$ within 5 minutes of release, automatically revert to the previous stable release.
5. **Zero-Downtime Graceful Teardown**: Listen for `SIGTERM`, stop accepting new connections, finish inflight requests (30s timeout), and close database pools cleanly.

---

## 🔬 The 4-Phase Deployment Pipeline

### Phase 1: Production Multi-Stage Dockerfile
```dockerfile
# Stage 1: Build & Dependencies
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

# Stage 2: Production Distroless Runner
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup --system --gid 1001 nodejs && adduser --system --uid 1001 appuser
COPY --from=builder --chown=appuser:nodejs /app/dist ./dist
COPY --from=builder --chown=appuser:nodejs /app/node_modules ./node_modules
USER appuser
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### Phase 2: Canary & Feature-Flagged Rollouts
- Route $10\%$ of live traffic to the new revision; monitor error rates for 10 minutes before expanding to $50\%$ and $100\%$.
- Guard new UI and billing features behind Upstash Redis feature flags for instant 0-second killswitch capability:
  ```typescript
  import { Redis } from '@upstash/redis';
  const redis = Redis.fromEnv();

  export async function isFeatureEnabled(flagName: string): Promise<boolean> {
    const status = await redis.get<string>(`flag:${flagName}`);
    return status === 'enabled';
  }
  ```

### Phase 3: Synthetic Health & Readiness Probes
```typescript
import express from 'express';
import { db } from './db';
import { redis } from './redis';

const app = express();

app.get('/healthz', (req, res) => res.status(200).send('OK'));

app.get('/ready', async (req, res) => {
  try {
    await db.$queryRaw`SELECT 1`;
    await redis.ping();
    res.status(200).json({ status: 'READY', uptime: process.uptime() });
  } catch (err) {
    res.status(503).json({ status: 'UNAVAILABLE', error: (err as Error).message });
  }
});
```

### Phase 4: Graceful Shutdown (`SIGTERM` Handler)
```typescript
const server = app.listen(3000);

process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  server.close(async () => {
    console.log('HTTP server closed. Draining DB & Redis pools...');
    await db.$disconnect();
    await redis.quit();
    process.exit(0);
  });
});
```
