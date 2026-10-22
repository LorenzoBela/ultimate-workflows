---
name: ultimate-database-workflow
description: >
  Workflow for database schema design, query optimization, indexing strategies,
  and transaction planning. Integrates Postgres/Supabase best practices, query plan analysis (EXPLAIN ANALYZE),
  keyset cursor pagination, deadlock tree diagnostics, and connection pooling.
  Triggers on "ultimate database workflow", "/ultimate-database-workflow", or when
  designing SQL schemas or optimizing slow queries.
argument-hint: "[table-schema | slow-query | --explain | --index | --migration]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Database and Query Optimization Workflow

## Inputs and scope

Identify engine/version, runtime role, schema/migration tooling, representative cardinality/skew, critical queries, concurrency, latency baseline, downtime allowance, backup/RPO/RTO and existing pooler. Preserve the chosen database. Provider-specific ports, pool settings, auth functions and MCP tools are examples only; inspect actual configuration and supported driver behavior.

## Schema and query decisions

- Enforce local data invariants with NOT NULL/UNIQUE/CHECK/foreign keys where suitable; cross-system business rules still need application/workflow enforcement. Decide delete/cascade and retention intentionally.
- Choose decimal/fixed-point or integer minor units with explicit currency scale, range and rounding. Use appropriate timezone-aware instants; distinguish wall-clock business dates.
- Select only needed columns in application queries. A sequential scan can be optimal for broad selections or small tables; do not add an index because a table exceeds an arbitrary row count.
- Compare query plans against actual workload, statistics, selectivity, buffer use, write cost and index size. B-tree supports many equality/range/order patterns; composite order and selectivity matter. Choose partial, covering, GIN/GiST/BRIN indexes only for matching operators/workload.
- Stable keyset pagination needs a unique tie-breaker, matching ordering/index, null policy and a versioned validated cursor. OFFSET remains suitable for some small/admin datasets. Do not claim universal O(1) behavior.

Illustrative PostgreSQL cursor query (bind types/tenant filter through the installed driver):

```sql
SELECT id, title, created_at
FROM events
WHERE tenant_id = $1
  AND (created_at, id) < ($2, $3)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

## Safe plan collection

Default to non-executing `EXPLAIN (FORMAT JSON)` for unknown or mutating statements. `EXPLAIN ANALYZE` actually runs the statement, including writes and functions. Use representative disposable data or a controlled read-only transaction for suitable reads, with statement/lock timeout. For writes, use an isolated clone; BEGIN/ROLLBACK does not undo every possible external function/sequence effect. Never execute production writes merely to inspect a plan.

Record engine/version, parameters (redacted), cardinality, stats freshness, execution environment and actual result. Profile before/after equivalent workloads; account for network time and measurement overhead. Investigate estimate mismatch and statistics before forcing plan choices. Changing global work_mem has multiplicative concurrency cost; scope and measure adjustments.

## Actual blockers, not lock-type guesses

Illustrative PostgreSQL read-only diagnostic; requires appropriate visibility permissions. `pg_blocking_pids` identifies real blockers, unlike joining every lock with the same locktype. Query text can be sensitive; limit/redact output.

```sql
SELECT blocked.pid AS blocked_pid,
       blocker.pid AS blocking_pid,
       blocked.wait_event_type,
       blocked.wait_event,
       blocker.state AS blocking_state
FROM pg_stat_activity AS blocked
CROSS JOIN LATERAL unnest(pg_blocking_pids(blocked.pid)) AS p(blocking_pid)
JOIN pg_stat_activity AS blocker ON blocker.pid = p.blocking_pid;
```

Identify transaction age, ownership, lock mode and workload before cancellation. Killing sessions/queries requires task authorization; a diagnostic result alone is not permission.

## Migration and recovery

Use development migration generation only in development. Apply reviewed immutable migrations using the production deployment command/tool for the installed ORM/provider. Detect drift before applying; never silently reset a database.

Prefer expand-contract: add compatible structure, deploy dual-compatible code, backfill in bounded resumable batches, verify, switch reads/writes, then remove old structure after the compatibility window. Test locks/rewrite cost and use engine-supported concurrent/online operations where suitable (some cannot run inside a transaction). Set timeouts and monitor replication lag.

A destructive change may not have a meaningful down migration. Record whether recovery is code rollback, forward fix, staged data copy or backup/PITR restore; rehearse it in a disposable environment. Verify backup retention and restore viability instead of claiming reversibility from a filename. Avoid rollback that drops newly written data.

## Isolation and pooling

RLS examples such as `auth.uid()` are provider-specific. Test actual runtime role and owner/service bypass, SELECT/INSERT/UPDATE/DELETE, WITH CHECK, tenant reassignment, views and SECURITY DEFINER functions. Trusted identity must come from verified auth; authorization checks must cover all paths.

Derive pooling from provider limits, driver/ORM version, transaction/session requirements and expected concurrency. Transaction pooling can conflict with session state or unsupported prepared-statement behavior. Do not hardcode a port or `connection_limit=1` universally.

## Completion evidence

Show schema/query diff, representative plan comparisons, constraints and cross-tenant negative tests; controlled contention must identify the real blocker. Confirm unknown write profiling executes nothing by default. Exercise old/new application compatibility, failed/partial backfill resume, timeout and recovery rehearsal. Report unavailable infrastructure checks as unverified with required environment; no sub-millisecond or absolute integrity promises.

Sources: [PostgreSQL EXPLAIN execution caveat](https://www.postgresql.org/docs/current/using-explain.html), [PostgreSQL information functions](https://www.postgresql.org/docs/current/functions-info.html), [Prisma development vs production](https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production).
