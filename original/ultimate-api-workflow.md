---
name: ultimate-api-workflow
description: >
  Workflow for API design, gateway management, GraphQL DataLoader,
  gRPC Protobuf contracts, date-based versioning (Stripe standard), and reverse proxy routing.
  Triggers on "ultimate api workflow", "/ultimate-api-workflow", or when designing
  gRPC, GraphQL, Nginx routes, or planning API gateway policies.
argument-hint: "[graphql-schema | grpc-proto | gateway-config | --versioning | --protobuf]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate API Design and Gateway Workflow

## Inputs and scope

Identify consumers, deployed contract versions, protocol, authentication context, side effects, retry behavior, compatibility window and existing gateway. Preserve the selected protocol/provider. A small internal endpoint does not require a new gateway or version transformation platform. Discover available tools; use the repository's contract validator and generated-client tooling rather than assumed MCP names.

## Contract and protocol decisions

1. Define request/response schemas, authorization and error cases before handler changes. For REST, use the supported OpenAPI version and HTTP semantics. Use a documented version policy appropriate to existing clients; date-pinned transformations are one option, not a default.
2. Compatibility includes enum expansion, nullability, field removal, pagination order, numeric precision and generated-client behavior. Run schema diff and representative old-client checks. Deprecation needs owner, notice period, usage evidence and removal gate.
3. REST errors may use RFC 9457 Problem Details with stable `type`, suitable status, trace correlation and safe human-readable detail. Do not expose internals. GraphQL uses its error/extensions conventions; gRPC uses status/details. Do not force HTTP envelopes onto other protocols.
4. Bound body size, pagination size, request deadline and concurrency. Specify `Retry-After` for applicable throttling. Trust forwarded headers only from configured proxies. Propagate trace context without trusting caller-supplied identity.
5. For gRPC, never reuse deleted field numbers/names; reserve them. Check wire compatibility before changing types. Set deadlines, propagate cancellation, and choose retryable statuses only for safe/idempotent calls.
6. GraphQL needs field/object authorization, query depth/complexity limits, pagination and batching where it reduces actual N+1 access. A loader is not authorization.

## Request-scoped loader example

Executable JavaScript factory with injected DataLoader and database. Construct once per authenticated request; never export one shared loader instance. `tenantId` must come from verified server auth, not request payload. Authorization may require more than tenant membership; enforce those rules in the scoped query too.

```javascript
export function createUserLoader({ DataLoader, db, tenantId }) {
  if (!tenantId) throw new Error('Authenticated tenant required');
  return new DataLoader(async (ids) => {
    const users = await db.user.findMany({
      where: { tenantId, id: { in: [...ids] } },
      select: { id: true, name: true },
    });
    const byId = new Map(users.map((user) => [user.id, user]));
    return ids.map((id) => byId.get(id) ?? null);
  }, { maxBatchSize: 100 }); // Example limit; tune for query limits/workload.
}
```

Keep output order and length equal to input; handle missing/unauthorized records consistently with the contract. Clear/prime relevant request cache entries after mutations. Bound long-lived subscription caches separately.

## Idempotency and side effects

Determine which operations need deduplication. PUT's HTTP semantics do not require every API to invent an extra key. For operations with costly/non-repeatable side effects, define authenticated principal + operation + key scope, accepted key syntax, retention based on retry horizon and a canonical payload fingerprint.

- Atomically create a unique operation record and its local mutation within the same transaction where possible. Concurrent duplicate requests must not both execute. Same key/different fingerprint is an explicit conflict.
- Model pending, succeeded, retryable failure and terminal failure. Define response replay, in-progress response, lease recovery, crash behavior and expiry. A Redis response cache alone cannot ensure exactly one charge.
- For external effects, use the provider's idempotency facility plus durable outbox/operation state; reconcile uncertain outcomes before retry. Do not promise exactly-once delivery across independent systems.
- Authenticate and authorize before replaying a stored response. Redact secrets and bound stored response size.

## Validation, recovery and completion evidence

Exercise unauthorized/cross-tenant access, malformed and oversized requests, cancellation, dependency timeout, rate-limit behavior, missing batch items and shuffled database results. Two concurrent requests with the same operation key produce one intended effect; changed payload is rejected. Use separate request loaders for two tenants and verify no cache sharing.

Report contract/version diff, actual commands/results, query count baseline, idempotency storage boundary and untested deployment assumptions. Roll out compatible handlers first, monitor client failures, and retain a route/version rollback that remains compatible with committed data. Infrastructure-backed checks require a disposable environment; illustrative designs are not verified deployments.

Sources: [DataLoader](https://github.com/graphql/dataloader#caching-per-request), [HTTP Problem Details](https://www.rfc-editor.org/rfc/rfc9457), [Protobuf compatibility](https://protobuf.dev/programming-guides/proto3/#updating).
