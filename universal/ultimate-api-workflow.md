---
name: ultimate-api-workflow
description: >
  Flawless 10/10 Master Workflow for API design, gateway management, GraphQL DataLoader,
  gRPC Protobuf contracts, date-based versioning (Stripe standard), and reverse proxy routing.
  Triggers on "ultimate api workflow", "/ultimate-api-workflow", or when designing
  gRPC, GraphQL, Nginx routes, or planning API gateway policies.
argument-hint: "[graphql-schema | grpc-proto | gateway-config | --versioning | --protobuf]"
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
