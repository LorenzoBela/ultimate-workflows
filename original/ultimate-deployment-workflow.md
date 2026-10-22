---
name: ultimate-deployment-workflow
description: >
  Workflow for CI/CD, multi-stage Docker packaging, blue-green / canary rollouts,
  automated health check synthetic probes, feature flag safety shields, and zero-downtime rollbacks.
  Triggers on "ultimate deployment workflow", "/ultimate-deployment-workflow", or when
  handling releases, Dockerfiles, CI configurations, or service deployments.
argument-hint: "[ci-config | dockerfile | deploy-target | --canary | --blue-green | --rollback]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Deployment and Release Workflow

## Inputs and release boundary

Identify application/runtime versions, target environment, authorized action, source commit, platform, schema/data compatibility, SLO/baseline, traffic volume, rollback owner and recovery constraints. Discover actual CI/deploy tools and credentials scope. Preserve provider; containers/canaries are not mandatory for every project. Local build success does not mean deployed.

## Reproducible package

Pin runtime/base image digest when immutable reproduction is required; specific tags can move. Record package-manager version/lockfile, use frozen installs, build once and promote the same artifact. Maintain a digest/security-update process.

Use supported runtime, minimal production dependencies and non-root identity where supported. Alpine is not distroless; test native/libc compatibility. Include runtime manifests/assets and exclude secrets/dev artifacts. Verify artifact identity/provenance and scans required by project policy. Do not replace a working Dockerfile with mismatched boilerplate.

## Migration and rollout

Review schema changes before rollout. Use production migration commands, lock/time limits, resumable backfill and expand-contract compatibility with old/new revisions. Destructive down SQL can lose new data; specify forward recovery or tested restore meeting RPO/RTO.

Choose rolling, blue/green or canary to fit platform/traffic. Define baseline-relative error/latency/business gates, minimum sample and observation window. Fixed percentages mislead on sparse traffic. Include queue lag/saturation/region/tenant effects where relevant. Flags need safe outage defaults, owner/expiry and measured propagation; remote switches are not guaranteed instantaneous.

## Bounded health and shutdown example

Illustrative Express/Node integration with injected operations. Adapt API versions and host grace timing. Dependency functions must honor signals or enforce driver timeouts. Response timeout does not stop noncooperative background work. Never expose raw dependency errors.

```javascript
export function installHealth(app, { checkDependencies, isDraining,
  probeMs = 1000 }) {
  app.get('/healthz', (req, res) => res.status(200).send('OK'));
  app.get('/ready', async (req, res) => {
    if (isDraining()) return res.status(503).json({ status: 'UNAVAILABLE' });
    const controller = new AbortController();
    let timer;
    try {
      await Promise.race([
        Promise.resolve().then(() => checkDependencies({ signal: controller.signal })),
        new Promise((_, reject) => {
          timer = setTimeout(() => {
            controller.abort();
            reject(new Error('Probe timeout'));
          }, probeMs);
        }),
      ]);
      const draining = isDraining();
      return res.status(draining ? 503 : 200).json({
        status: draining ? 'UNAVAILABLE' : 'READY',
      });
    } catch {
      return res.status(503).json({ status: 'UNAVAILABLE' });
    } finally {
      clearTimeout(timer);
    }
  });
}

export function installShutdown({ server, markDraining, closeResources,
  deadlineMs = 30000 }) {
  let started = false;
  const shutdown = () => {
    if (started) return;
    started = true;
    markDraining();
    const deadline = setTimeout(() => {
      server.closeAllConnections?.();
      process.exit(1); // Hard stop; unfinished work must be recoverable.
    }, deadlineMs);
    server.close((serverError) => {
      Promise.resolve().then(closeResources).then(() => {
        clearTimeout(deadline);
        process.exit(serverError ? 1 : 0);
      }, () => {
        clearTimeout(deadline);
        process.exit(1);
      });
    });
    server.closeIdleConnections?.();
  };
  process.once('SIGTERM', shutdown);
  process.once('SIGINT', shutdown);
}
```

Decide which dependencies truly block readiness: optional/shared outages should not unnecessarily drain all replicas. Liveness avoids expensive dependency checks; startup probes may cover initialization. Bound probe load/frequency.

Configure load-balancer deregistration/host grace period; propagate not-ready before termination where platform permits. Handle WebSockets/long requests explicitly. Serverless hosts require their lifecycle, not generic process handlers.

## Verification, recovery and evidence

Test actual artifact in disposable infrastructure: startup, probe timeout/redaction, auth smoke, mixed-schema compatibility, dependency outage, SIGTERM with active/hung requests and failed canary recovery. Use safe synthetic data. Rehearse rollback/forward repair rather than only writing commands.

Record commit/digest, environment, revision/migration IDs, actual commands/results, gate observations and recovery path. Keep old artifact/config until stable. Without authorized release, finish reviewable package/config/evidence and state undeployed status; never invent revision/health results.

Sources: [Docker pinned images](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions), [Kubernetes probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/), [Node HTTP shutdown](https://nodejs.org/api/http.html#serverclosecallback).
