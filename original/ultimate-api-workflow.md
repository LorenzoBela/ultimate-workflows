---
name: ultimate-api-workflow
description: >
  Flawless 10/10 Master Workflow for API design, gateway management, GraphQL DataLoader,
  gRPC Protobuf contracts, date-based versioning (Stripe standard), and reverse proxy routing.
  Triggers on "ultimate api workflow", "/ultimate-api-workflow", or when designing
  gRPC, GraphQL, Nginx routes, or planning API gateway policies.
argument-hint: "[graphql-schema | grpc-proto | gateway-config | --versioning | --protobuf]"
---

# Ultimate API Design & Gateway Architecture Workflow (10/10 Master Engine)

This workflow guides the design, routing, security, versioning, and contract enforcement of public and internal APIs—spanning REST OpenAPI, GraphQL, and high-throughput gRPC.

```
                                      [API CLIENT REQUEST / RPC CALL]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [GATEWAY & REVERSE PROXY LAYER]                       [CONTRACT DEFINITION (OPENAPI/GRPC)]
              ├─ Traefik / Nginx / Cloudflare                       ├─ Strict Schema First (No Phantom APIs)
              ├─ TLS 1.3 & HSTS Termination                         ├─ Protobuf Tag Immutability
              └─ X-Request-ID & Traceparent Header                  └─ Date-Based Versioning (Stripe)
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 API PROTOCOL DISPATCH & ENGINE SELECTION                    │
        │  • REST (OpenAPI 3.1) • GraphQL (DataLoader N+1 Shield) • gRPC (Binary Fast)│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [IDEMPOTENCY & RATE-LIMITING CONTROLS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 💳 IDEMPOTENT│           │ ⚡ RATELIMIT │           │ 🛡️ BACKWARD  │
            │ Idempotency-K│           │ Upstash Slid.│           │ Transform Mod│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of API Design

1. **Contract-First Architecture**: Write the OpenAPI 3.1, GraphQL SDL, or Protobuf definition *before* implementing handler logic.
2. **Never Break Existing Integrations**: Public API changes must be non-breaking (additive) or encapsulated within version transformation layers.
3. **Mandatory Idempotency Keys on Mutations**: All `POST`/`PUT`/`PATCH` endpoints must support `Idempotency-Key` headers (UUIDv4) cached for 24-72 hours.
4. **Zero N+1 in GraphQL**: All nested GraphQL relations MUST use DataLoader batching.
5. **Protobuf Tag Immutability**: In `.proto` specs, never change a tag number or data type. Mark deprecated fields `reserved`.
6. **Explicit Error Shapes**: All error responses must adhere to RFC 7807 (Problem Details for HTTP APIs) containing `type`, `title`, `status`, `detail`, and `instance`.

---

## 🔬 The 4-Protocol Engineering Matrix

### 1. REST & Date-Based Versioning (Stripe Standard)
- New users pinned to current date version (e.g. `2026-08-15`).
- Core service writes code against the latest version; backward transformation modules translate modern JSON into older pinned formats.
- Standard Error Response (RFC 7807):
  ```json
  {
    "type": "https://api.example.com/errors/invalid-parameters",
    "title": "Invalid Request Parameters",
    "status": 400,
    "detail": "The amountInCents field must be a positive integer.",
    "instance": "/api/v1/charges/req_98765"
  }
  ```

### 2. GraphQL Schema & DataLoader N+1 Protection
```typescript
import DataLoader from 'dataloader';

// Batch loader function
export const userLoader = new DataLoader(async (userIds: readonly string[]) => {
  const users = await db.user.findMany({
    where: { id: { in: [...userIds] } }
  });
  const userMap = new Map(users.map(u => [u.id, u]));
  return userIds.map(id => userMap.get(id) || null);
});
```

### 3. gRPC & Protobuf Contract Spec
```protobuf
syntax = "proto3";

package payment.v1;

service PaymentService {
  rpc ProcessCharge (ChargeRequest) returns (ChargeResponse);
}

message ChargeRequest {
  string idempotency_key = 1;
  int64 amount_in_cents = 2;
  string currency = 3;
}

message ChargeResponse {
  string transaction_id = 1;
  string status = 2;
  int64 created_at = 3;
}
```
