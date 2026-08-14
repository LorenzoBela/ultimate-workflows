---
name: ultimate-database-workflow
description: >
  Master workflow for database schema design, query optimization, indexing strategies,
  and transaction planning.
  Integrates Postgres/Supabase best practices, query plan analysis (EXPLAIN), and
  connection management.
  Triggers on "ultimate database workflow", "/ultimate-database-workflow", or when
  designing SQL schemas or optimizing slow queries.
argument-hint: "[table-schema | slow-query]"
---

# Ultimate Database & Query Optimization Workflow

This workflow guides the design, index planning, execution optimization, and securing of database schemas. It is the definitive pipeline for sub-millisecond response times, airtight data integrity, and bulletproof RLS security.

---

## Iron Laws

1. **Schema Is the Source of Truth.** Business rules live in database constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`), not in application code. If the app crashes, the database must still reject invalid data.
2. **Never Trust Application-Only Invariants.** If a column must be unique, add a `UNIQUE` constraint. If a value must be positive, add a `CHECK (amount > 0)`. Application validation is a UX convenience; database constraints are the security layer.
3. **Migrations Are First-Class Citizens.** No manual `ALTER TABLE` in production. Every schema change is a versioned, tested, reversible migration file.
4. **No `SELECT *` in Production.** Always specify the exact columns needed. `SELECT *` wastes bandwidth, prevents covering indexes, and leaks schema changes.
5. **Explain Before Optimizing.** Never add an index, rewrite a query, or change a join order without first running `EXPLAIN (ANALYZE, BUFFERS)` to verify the current execution plan.

---

## The 6-Phase Database Pipeline

### Phase 1: Schema Design & Constraint Architecture
*   **Action:**
    1. **Data type selection:**

       | Data | Correct Type | Wrong Type | Why |
       |---|---|---|---|
       | Primary keys | `uuid` or `bigint` | `serial` / `int` | Serial exhausts at 2B rows, uuid is globally unique |
       | Money/Currency | `integer` (cents) or `numeric(19,4)` | `float` / `double` | Floating point has rounding errors |
       | Timestamps | `timestamptz` | `timestamp` | Without timezone, ambiguous across regions |
       | Email/URLs | `text` + `CHECK` constraint | `varchar(255)` | Arbitrary length limits cause future schema changes |
       | Status/Enum | `text` + `CHECK (status IN (...))` | Postgres `ENUM` | ENUM is painful to modify after creation |
       | JSON config | `jsonb` | `json` | jsonb is indexable and faster to query |
       | Boolean flags | `boolean NOT NULL DEFAULT false` | `integer` 0/1 | Explicit semantics, prevents null ambiguity |

    2. **Constraint checklist (per table):**
       *   [ ] Primary key defined (`uuid` with `gen_random_uuid()` default, or `bigint generated always as identity`)
       *   [ ] All foreign keys have explicit `ON DELETE` behavior (`CASCADE`, `SET NULL`, or `RESTRICT`)
       *   [ ] `NOT NULL` on every column unless null is a legitimate business state
       *   [ ] `UNIQUE` constraints on natural keys (email, tracking_number, slug)
       *   [ ] `CHECK` constraints on bounded values (status enum, positive amounts, valid ranges)
       *   [ ] `DEFAULT` values for timestamps (`now()`), booleans (`false`), and generated fields
       *   [ ] `created_at` and `updated_at` columns on every table
    3. **Inspect current schema** using `list_tables` and `list_extensions`.
    4. Check for schema drift using `migrate-status`.

### Phase 2: Migration Engineering
*   **Action:**
    1. **Migration rules:**
       *   Forward-compatible: add before remove. New columns are nullable or have defaults.
       *   Never rename a column in one step — add new, migrate data, drop old (3-step process).
       *   Never `DROP COLUMN` without verifying no running code references it.
       *   Every migration must be testable on a staging database.
    2. **Migration naming:** Use descriptive names: `add_tracking_number_to_deliveries`, not `migration_042`.
    3. **Rollback strategy:**

       | Change Type | Rollback Approach |
       |---|---|
       | Add column | `ALTER TABLE DROP COLUMN` |
       | Add constraint | `ALTER TABLE DROP CONSTRAINT` |
       | Create table | `DROP TABLE` |
       | Add index | `DROP INDEX` |
       | Data backfill | Restore from pre-migration backup |
       | Drop column | ⚠️ IRREVERSIBLE — backup data first |

    4. **Execution:**
       *   Local development: use `prisma-mcp-server/migrate-dev` for ORM-driven evolution.
       *   Supabase staging: use `supabase-mcp-server/apply_migration` for SQL migration execution.
       *   Reset development database: use `prisma-mcp-server/migrate-reset` (NEVER in production).
    5. Review migration history using `list_migrations`.

### Phase 3: Index Strategy & Optimization
*   **Action:**
    1. **Index decision matrix:**

       | When to Index | Index Type | Example |
       |---|---|---|
       | Foreign key columns | B-Tree (default) | `CREATE INDEX idx_deliveries_rider_id ON deliveries(rider_id)` |
       | `WHERE` clause filters | B-Tree | `CREATE INDEX idx_deliveries_status ON deliveries(status)` |
       | Full-text search | GIN | `CREATE INDEX idx_profiles_name_gin ON profiles USING gin(to_tsvector('english', name))` |
       | JSON field queries | GIN | `CREATE INDEX idx_config_data ON settings USING gin(config_data)` |
       | Geospatial queries | GiST | `CREATE INDEX idx_locations_coords ON locations USING gist(point)` |
       | Partial data subsets | Partial B-Tree | `CREATE INDEX idx_active_deliveries ON deliveries(status) WHERE status != 'COMPLETED'` |
       | Composite filters | Multi-column B-Tree | `CREATE INDEX idx_deliveries_rider_status ON deliveries(rider_id, status)` |
       | Covering queries | B-Tree + INCLUDE | `CREATE INDEX idx_deliveries_cover ON deliveries(rider_id) INCLUDE (status, created_at)` |

    2. **When NOT to index:**
       *   Tables with <1000 rows (sequential scan is faster).
       *   Columns with low cardinality (e.g., boolean columns with 50/50 distribution).
       *   Write-heavy tables where index maintenance cost exceeds read benefit.
    3. **Index audit:** Run `get_advisors` to detect:
       *   Missing indexes (queries doing sequential scans on large tables).
       *   Unused indexes (wasting disk and slowing writes).
       *   Duplicate indexes (same columns indexed multiple times).
       *   Locking conflicts.

### Phase 4: Query Writing & Profiling (EXPLAIN)
*   **Action:**
    1. **Query writing rules:**
       *   Specify columns explicitly — never `SELECT *`.
       *   Use parameterized queries — never string interpolation.
       *   Avoid N+1: use `JOIN`, subqueries, or batch preloading.
       *   Prefer `EXISTS` over `IN` for subquery checks on large tables.
       *   Use `LIMIT` and pagination (`OFFSET` or keyset) for large result sets.
    2. **EXPLAIN analysis:** Profile slow or frequent queries:
       ```sql
       EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ... ;
       ```
    3. **EXPLAIN red flags:**

       | Red Flag | What It Means | Fix |
       |---|---|---|
       | `Seq Scan` on large table | No matching index | Add appropriate index |
       | `Filter` removing >90% rows | Index exists but not selective | Use partial index or restructure query |
       | `Nested Loop` with high cost | Quadratic join | Use `Hash Join` by adding index on join column |
       | `Sort` with `external merge` | Insufficient `work_mem` | Increase `work_mem` or add covering index |
       | High `Buffers: shared read` | Data not cached, hitting disk | Check if table fits in `shared_buffers` |
       | `HashAggregate` with many batches | Grouping too many distinct values | Pre-filter before aggregation |

    4. **Query optimization checklist:**
       *   [ ] Verified with `EXPLAIN (ANALYZE, BUFFERS)` — no sequential scans on tables >1000 rows
       *   [ ] All `JOIN` columns have indexes
       *   [ ] `WHERE` clause columns have indexes
       *   [ ] `ORDER BY` columns have indexes (if used with `LIMIT`)
       *   [ ] No `SELECT *` — only needed columns
       *   [ ] No N+1 patterns — batch or join
       *   [ ] Pagination uses keyset (`WHERE id > $1`) not `OFFSET` for deep pages

### Phase 5: Row-Level Security (RLS) & Access Control
*   **Action:**
    1. **RLS policy design rules:**
       *   Enable RLS on EVERY table containing user data: `ALTER TABLE deliveries ENABLE ROW LEVEL SECURITY;`
       *   Write separate policies for `SELECT`, `INSERT`, `UPDATE`, `DELETE` — never a single "all" policy.
       *   Filter rows using `auth.uid()` matching the row's owner column.
       *   Service-role bypass is acceptable for server-side admin operations only.
    2. **RLS policy templates:**
       ```sql
       -- Users can only read their own deliveries
       CREATE POLICY "Users read own deliveries"
         ON deliveries FOR SELECT
         USING (rider_id = auth.uid());

       -- Users can only update their own profile
       CREATE POLICY "Users update own profile"
         ON profiles FOR UPDATE
         USING (id = auth.uid())
         WITH CHECK (id = auth.uid());

       -- Public read access (e.g., tracking page)
       CREATE POLICY "Public read via share_token"
         ON deliveries FOR SELECT
         USING (share_token IS NOT NULL);
       ```
    3. **RLS performance:** Ensure `auth.uid()` comparison columns have indexes. RLS adds a `Filter` step to every query — unindexed filters on large tables cause full scans.
    4. **Audit:** Run `get_advisors` to detect tables missing RLS policies.
    5. For Firebase: audit security rules using `firebase_get_security_rules`.
    6. Rate limit database-heavy endpoints using `upstash-ratelimit-js`.

### Phase 6: Transactions, Caching & Connection Pooling
*   **Action:**
    1. **Transaction rules:**
       *   Multi-step writes MUST use transactions. Partial writes are forbidden.
       *   Keep transaction blocks SHORT — long transactions hold locks and block concurrent writes.
       *   Transactions are NOT retryable by default. Combine with idempotency keys for safe retries.
       *   Use `SERIALIZABLE` isolation only when necessary — prefer `READ COMMITTED` (Postgres default).
    2. **Caching strategy (Redis):**

       | Cache Pattern | When to Use | TTL |
       |---|---|---|
       | **Cache-Aside** | Read-heavy, tolerate slight staleness | 60s–300s |
       | **Write-Through** | Must keep cache fresh on every write | No TTL (invalidate on write) |
       | **Read-Through** | Lazy population, cache miss triggers fetch | 60s–600s |
       | **Cache Invalidation** | After any write, delete the cache key | Immediate |

    3. Use `upstash-redis-js` for distributed caching. Use `upstash-redis-start` for ephemeral dev/test Redis.
    4. **Connection pooling:**
       *   Serverless (Edge Functions, Vercel): Use Supabase's built-in PgBouncer or HTTP-based connections (`@supabase/supabase-js`). Never open raw TCP connections from serverless functions.
       *   Long-running servers: Configure pool size, idle timeout, and connection lifetime.
       *   Monitor connection count — never exceed `max_connections`.
    5. Use `Prisma-Studio` for visual data inspection during development and debugging.

---

## Database Quality Checklist

### Schema
- [ ] Every table has a primary key (`uuid` or `bigint`)
- [ ] All foreign keys have explicit `ON DELETE` behavior
- [ ] `NOT NULL` on every column unless null is a valid business state
- [ ] `UNIQUE` constraints on natural keys
- [ ] `CHECK` constraints on bounded values
- [ ] `created_at` and `updated_at` on every table
- [ ] No `float`/`double` for money — use `integer` (cents) or `numeric`
- [ ] All timestamps are `timestamptz` (with timezone)

### Queries
- [ ] No `SELECT *` in production code
- [ ] All queries verified with `EXPLAIN (ANALYZE, BUFFERS)`
- [ ] No N+1 query patterns
- [ ] All `JOIN` columns indexed
- [ ] Pagination uses keyset, not deep `OFFSET`

### Security
- [ ] RLS enabled on ALL tables with user data
- [ ] Separate policies for SELECT, INSERT, UPDATE, DELETE
- [ ] `auth.uid()` filter columns are indexed
- [ ] No `service_role` key exposed to client-side code
- [ ] Database secrets loaded from environment variables, not hardcoded

### Operations
- [ ] Multi-step writes wrapped in transactions
- [ ] Connection pooling configured for serverless environments
- [ ] Hot query results cached in Redis with TTL
- [ ] Migration rollback strategy documented

---

## Advanced Database Performance & Troubleshooting Blueprints

### 1. Keyset Pagination Implementation (O(1) Scale)
When paginating through millions of rows, traditional `OFFSET` forces the engine to scan and discard all preceding records. Use the keyset (cursor-based) pattern instead:

```typescript
import { Client } from 'pg';

const client = new Client({ connectionString: process.env.DATABASE_URL });

export async function fetchDeliveriesKeyset(
  lastSeenId: string | null,
  pageSize: number = 50
) {
  const query = lastSeenId
    ? {
        text: `
          SELECT id, tracking_number, status, created_at
          FROM deliveries
          WHERE id > $1
          ORDER BY id ASC
          LIMIT $2;
        `,
        values: [lastSeenId, pageSize],
      }
    : {
        text: `
          SELECT id, tracking_number, status, created_at
          FROM deliveries
          ORDER BY id ASC
          LIMIT $1;
        `,
        values: [pageSize],
      };

  const res = await client.query(query);
  return res.rows;
}
```

### 2. Lock & Deadlock Diagnostic Queries
Run these queries via `supabase-mcp-server/execute_sql` when API requests hang or write operations timeout:

```sql
-- Identify blocking and blocked sessions in Postgres
SELECT
  blocked_locks.pid     AS blocked_pid,
  blocked_activity.query    AS blocked_statement,
  blocking_locks.pid    AS blocking_pid,
  blocking_activity.query   AS blocking_statement
FROM  pg_catalog.pg_locks         blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks         blocking_locks 
  ON blocking_locks.locktype = blocked_locks.locktype
  AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
  AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
  AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
  AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
  AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
  AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
  AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
  AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
  AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
  AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```

### 3. RLS Performance Audit
Ensure columns utilized in RLS policies (e.g. `rider_id`, `tenant_id`, `organization_id`) are indexed. Run `EXPLAIN` to isolate scans:

```sql
-- Profile query with active RLS to see filter cost
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM deliveries 
WHERE rider_id = 'e7b0b6d2-64f1-4db8-b572-132d29482d8c';
-- Look for "Filter: (rider_id = auth.uid())" inside a Seq Scan. 
-- Fix: CREATE INDEX idx_deliveries_rider_id ON deliveries(rider_id);
```

---

## Database Quality Checklist

### Schema
- [ ] Every table has a primary key (`uuid` or `bigint`)
- [ ] All foreign keys have explicit `ON DELETE` behavior
- [ ] `NOT NULL` on every column unless null is a valid business state
- [ ] `UNIQUE` constraints on natural keys
- [ ] `CHECK` constraints on bounded values
- [ ] `created_at` and `updated_at` on every table
- [ ] No `float`/`double` for money — use `integer` (cents) or `numeric`
- [ ] All timestamps are `timestamptz` (with timezone)

### Queries
- [ ] No `SELECT *` in production code
- [ ] All queries verified with `EXPLAIN (ANALYZE, BUFFERS)`
- [ ] No N+1 query patterns
- [ ] All `JOIN` columns indexed
- [ ] Pagination uses keyset, not deep `OFFSET`

### Security
- [ ] RLS enabled on ALL tables with user data
- [ ] Separate policies for SELECT, INSERT, UPDATE, DELETE
- [ ] `auth.uid()` filter columns are indexed
- [ ] No `service_role` key exposed to client-side code
- [ ] Database secrets loaded from environment variables, not hardcoded

### Operations
- [ ] Multi-step writes wrapped in transactions
- [ ] Connection pooling configured for serverless environments
- [ ] Hot query results cached in Redis with TTL
- [ ] Migration rollback strategy documented

---

## Anti-Patterns (Reject These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| `SELECT * FROM ...` | Wastes bandwidth, prevents covering indexes | Specify exact columns |
| `WHERE status = '` + userInput + `'` | SQL injection vulnerability | Use parameterized queries: `$1` |
| Adding index on every column | Slows writes, wastes disk | Index only queried columns |
| `OFFSET 10000` for deep pagination | Scans and discards 10K rows | Use keyset: `WHERE id > $last_id` |
| Manual `ALTER TABLE` in production | Unversioned, untested, unreproducible | Write a migration file |
| `float` for currency | Rounding errors: `0.1 + 0.2 ≠ 0.3` | Use `integer` cents or `numeric(19,4)` |
| Single "allow all" RLS policy | No real access control | Separate policies per operation |
| Long transactions (>1 second) | Holds locks, blocks concurrent writes | Minimize transaction scope |
| `timestamp` without timezone | Ambiguous across regions | Always use `timestamptz` |

---

## Universal Checklists & Reference Architecture

### 1. Database Best Practices Priority Rules (`PostgreSQL Indexing & Optimization Patterns`)
*   **Query Performance:** Implement missing indexes based on `EXPLAIN` statistics. Use partial and covering indexes to control memory overhead.
*   **Connection Sizing:** Limit simultaneous connections. Recommended sizing formula: `Max Pool Size = (CPU cores * 2) + spindle_count`.
*   **Security & RLS:** Enforce Row-Level Security on all user tables. Ensure joined policy columns are fully indexed to avoid sequential table scans.
*   **Data Accuracy:** Enforce integrity constraints (`NOT NULL`, `CHECK`, `FOREIGN KEY`) at write time.

### 2. Distributed Locking & Session Caching (`upstash-redis-js`)
*   **Deduplication Locks:** Use Redis keys with conditional options (`nx: true, ex: 10`) to prevent duplicate writes during concurrent updates.
*   **Cache-Aside Pattern:** Query Redis cache first; on cache miss, query Postgres, populate Redis with short TTL (e.g. 300s), and return data.

### 3. API Rate Limiting Defense (`upstash-ratelimit-js`)
*   **Defending Write Operations:** Limit write-heavy endpoints using token bucket or sliding window algorithms to block brute-force resource exhaustion.
*   **IP-Based Constraints:** Enforce separate thresholds for IP subnets vs authenticated user sessions.

---

## Cross-Cutting Concerns
*   **Frontend:** Chain with `ultimate-frontend-workflow` when building data-driven dashboards, tables, or list views.
*   **Debugging:** Chain with `ultimate-debugging-workflow` for database-specific bug investigation (schema drift, RLS denials, slow queries).
*   **Security:** Apply `ultimate-security-workflow` and `ultimate-security-audit-workflow` for RLS policy auditing and access control verification.
*   **Research:** Use Web Search, official library documentation, and `perplexity-ask` for Postgres documentation, indexing strategies, and query optimization techniques.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist schema decisions, constraint rationale, and indexing strategies across conversations.
*   **Serverless:** Use `ultimate-serverless-workflow` for Edge Function connection pooling and Supabase branch management.
*   **Caching:** Use `ultimate-caching-workflow` for Redis cache strategy design alongside database optimization.
*   **TypeScript:** Use `supabase-mcp-server/generate_typescript_types` for end-to-end type safety between database and application code.
