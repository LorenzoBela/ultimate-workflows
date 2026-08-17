---
name: ultimate-database-workflow
description: >
  Flawless 10/10 Master Workflow for database schema design, query optimization, indexing strategies,
  and transaction planning. Integrates Postgres/Supabase best practices, query plan analysis (EXPLAIN ANALYZE),
  keyset cursor pagination, deadlock tree diagnostics, and connection pooling.
  Triggers on "ultimate database workflow", "/ultimate-database-workflow", or when
  designing SQL schemas or optimizing slow queries.
argument-hint: "[table-schema | slow-query | --explain | --index | --migration]"
---

# Ultimate Database & Query Optimization Workflow (10/10 Master Engine)

This workflow guides the design, index planning, execution optimization, and securing of relational and distributed databases. It guarantees sub-millisecond query performance, absolute mathematical data integrity, and bulletproof Row-Level Security (RLS).

```
                                      [DATABASE SCHEMA / QUERY TARGET]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: SCHEMA CONSTRAINTS]                         [PHASE 2: INDEX STRATEGY & EXPLAIN]
              ├─ Primary Keys & Strict Types                        ├─ B-Tree / GIN / GiST Selection
              ├─ Foreign Keys & Cascade Policies                    ├─ EXPLAIN (ANALYZE, BUFFERS) Profiling
              └─ Check Constraints & Timestamps                     └─ Partial & Covering Indexes
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: HIGH-PERFORMANCE QUERYING & KEYSET CURSORS         │
        │  • Zero `SELECT *` • Keyset Pagination (O(1)) • Avoid N+1 Join Optimizations│
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: ROW-LEVEL SECURITY & LOCK DIAGNOSTICS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🔒 RLS POLICY│           │ ⚡ DEADLOCK  │           │ 🏊 PGBOUNCER │
            │ auth.uid()   │           │ pg_locks SQL │           │ Port 6543    │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Database Engineering

1. **Schema Is the Absolute Source of Truth**: Business invariants belong in database constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`), not in application code.
2. **Zero Floating-Point Numbers for Currency**: Always use `integer` minor units (cents) or `numeric(19,4)`.
3. **No `SELECT *` in Production**: Specify exact columns to allow index-only scans and prevent bandwidth bloat.
4. **Explain Before Optimizing**: Every query modification must be verified with `EXPLAIN (ANALYZE, BUFFERS)`.
5. **Reversible Migrations Only**: Every schema alteration must have a documented, tested down/rollback migration.
6. **Keyset Pagination for Deep Sets**: Keyset (`WHERE id > $last_id LIMIT 50`) is required over `OFFSET` for tables $> 1000$ rows.
7. **Serverless Connection Pooling**: All serverless connections MUST connect via PgBouncer in transaction mode (port 6543) with `connection_limit=1`.

---

## 🔬 The 6-Phase Database Pipeline

### Phase 1: Schema Design & Strict Typing
*   **Primary Keys:** `uuid` with `gen_random_uuid()` or `bigint generated always as identity`.
*   **Timestamps:** Always `timestamptz` (with timezone).
*   **Text/Enums:** Prefer `text` + `CHECK (status IN ('PENDING', 'ACTIVE', 'COMPLETED'))` over native Postgres ENUM for smooth migrations.

### Phase 2: Index Strategy Matrix
| Query Pattern | Optimal Index Type | Example |
|---|---|---|
| Foreign Keys & ID Lookups | B-Tree | `CREATE INDEX idx_deliveries_rider ON deliveries(rider_id)` |
| Filtered Subsets (Active only) | Partial B-Tree | `CREATE INDEX idx_active_tasks ON tasks(status) WHERE status != 'DONE'` |
| Multi-column `WHERE A = 1 AND B = 2` | Composite B-Tree | `CREATE INDEX idx_user_org ON members(org_id, user_id)` |
| JSONB Key-Value Search | GIN (jsonb_path_ops) | `CREATE INDEX idx_meta ON logs USING gin(metadata jsonb_path_ops)` |
| Full-Text Search | GIN (to_tsvector) | `CREATE INDEX idx_search ON articles USING gin(to_tsvector('english', title))` |
| Geospatial Proximity | GiST | `CREATE INDEX idx_geo ON places USING gist(geom)` |

### Phase 3: EXPLAIN (ANALYZE, BUFFERS) Profiling
- **Red Flag 1:** `Seq Scan` on table with $> 1000$ rows $\rightarrow$ Add B-Tree index.
- **Red Flag 2:** `Sort: external merge Disk` $\rightarrow$ Increase `work_mem` or add covering index.
- **Red Flag 3:** `Buffers: shared read` high $\rightarrow$ Cache cold or table exceeds `shared_buffers`.

### Phase 4: Row-Level Security (RLS) Policy Design
```sql
ALTER TABLE deliveries ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Rider view assigned deliveries"
ON deliveries FOR SELECT
USING (rider_id = auth.uid());

CREATE POLICY "Rider update assigned deliveries"
ON deliveries FOR UPDATE
USING (rider_id = auth.uid())
WITH CHECK (rider_id = auth.uid());
```

### Phase 5: Keyset (Cursor-Based) Pagination
```sql
SELECT id, title, created_at
FROM events
WHERE (created_at, id) < ($last_created_at, $last_id)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

### Phase 6: Deadlock & Lock Tree Diagnostics
```sql
SELECT blocked_locks.pid AS blocked_pid,
       blocked_activity.query AS blocked_query,
       blocking_locks.pid AS blocking_pid,
       blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks ON blocking_locks.locktype = blocked_locks.locktype
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```
