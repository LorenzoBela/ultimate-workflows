---
name: ultimate-architecture-workflow
description: >
  Design system boundaries, domain models, event delivery and architecture decisions. Use for architecture or ADR work; justify distributed complexity and scale modeling to the actual system.
argument-hint: "[system-boundary | event-flow | adr]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# System architecture and domain boundaries

Use for architecture decisions, domain models and event flows. Start from the actual system and the simplest viable boundary, including an existing modular monolith. Distributed services, event buses, DDD and three C4 diagrams are choices to justify, not prerequisites for every change.

## Inputs

Record business outcome, current implementation and topology, deployment/runtime constraints, data ownership, authorization boundaries, availability/latency/recovery needs, workload evidence and migration limits. Separate measured facts from estimates. When research is invoked, the research workflow's all-15 substantive inputs and rich query floors remain mandatory.

## 1. Boundaries and decisions

- Identify core, supporting and generic capabilities when domain modeling helps. Use shared terminology and explicit business invariants.
- Compare a local module boundary with remote/event-driven alternatives. Consider transactions, operational ownership, coupling, consistency, deploy independence and failure isolation.
- Define interface schemas, versioning, error semantics and caller compatibility. Anti-corruption layers are useful at incompatible models, not wrappers required for every call.
- Diagram only useful C4 levels. Annotate trust boundaries, data direction and external dependencies; do not label a queue/database as proof of a reliability property.
- Define quality-attribute scenarios: under a stated workload/failure, what measurable response is required? Use load/profile evidence to size pools, timeouts and isolation.

## 2. Event delivery and transactional outbox

Use an outbox when a database mutation must reliably lead to asynchronous publication and the selected infrastructure supports this pattern. A table alone does not implement delivery.

**Design pseudocode, not executable SQL or an implemented relay:**

```text
producer transaction:
  update aggregate with expected version
  insert outbox event with stable ID, aggregate ID/version,
    event type/schema version, payload, created timestamp
  commit both or neither

relay:
  claim a bounded batch using the database's supported lease/locking model
  publish stable event ID and schema/aggregate version
  record successful delivery; retry transient failures with a bounded policy
  preserve failed events for diagnosis/replay under authorized scope

consumer transaction:
  if event ID already processed: acknowledge without repeating business effect
  validate schema/version, tenant and ordering expectations
  apply business mutation and record processed event ID atomically
  commit; acknowledge transport delivery
```

Publication can succeed before the relay records success: duplicate delivery is expected. Consumer deduplication must cover the intended effect; for another external effect, use an idempotent endpoint or a new outbox rather than claiming one local transaction guarantees exactly-once execution everywhere.

Specify poison-message/dead-letter handling, retention, replay authorization, aggregate ordering, concurrent consumers, deduplication lifetime and schema evolution. A finite deduplication TTL must match replay/retention policy. Expose oldest unprocessed event age, attempts and failures without leaking payload secrets.

Required scenarios: producer rollback publishes nothing; crash after publish before marking delivery; concurrent relay claims; duplicate/out-of-order events; unsupported schema; dead-letter/replay; cancellation or prolonged downstream outage. Verify final business state, not merely number of messages received.

## 3. Reliability and capacity

Use bounded external calls, jittered transient retries, idempotency and uncertain-outcome reconciliation. Allocate resource pools/bulkheads where a low-priority workload can harm critical traffic. Select circuit breakers and fallbacks based on real failure modes and acceptable degradation.

Inspect the actual database provider, pooler mode/version and client before recommending connection limits or prepared-statement settings. No universal port, `connection_limit=1`, or prepared-statement prohibition applies to every deployment. Test representative concurrency and migration connectivity separately.

## 4. Decisions and migration

Record a lasting choice in an ADR: context, constraints, options/evidence, decision, accepted consequences, status/date and revisit trigger. Supersede accepted decisions with a linked new record; correct factual errors transparently rather than silently rewriting history.

Plan compatible rollout, data backfill/reconciliation, mixed-version operation and recovery. Rehearse risky restoration or forward repair in a disposable environment. Preserve user work and never run destructive production experiments as architecture discovery.

Complete with diagrams/contracts relevant to the scope, decision evidence, actual checks, unresolved risks and migration/recovery ownership. Mark unrun runtime/load/production checks explicitly.
