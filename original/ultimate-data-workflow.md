---
name: ultimate-data-workflow
description: >
  Master workflow for data pipeline engineering, ETL scripting, and data analysis.
  Coordinates data extraction, cleansing, structured transformation, and loading.
  Triggers on "ultimate data workflow", "/ultimate-data-workflow", or when designing
  batch pipelines, parser scripts, database aggregations, or data transformations.
argument-hint: "[etl-pipeline | parser-script | database-aggregation]"
---

# Ultimate Data Pipeline & ETL Workflow

This workflow drives reliable data pipeline engineering, schema parsing, validation, cleansing, and transaction-safe loads to ensure high data integrity and resource-efficient processing.

---

## The 4-Phase Data Pipeline

### Phase 1: Data Schema & Extraction (E)
*   **Sub-skills:** `supabase-postgres-best-practices`, `upstash-redis-js`, `upstash-ratelimit-js`
*   **Action:**
    1. Define the source data structure (CSV, JSON, XML, Parquet, or DB tables).
    2. Build robust extractors that read data in chunks or streams to keep memory footprints low. Never load massive files entirely into RAM.
    3. Implement rate-limiting, paginated queries, and retry-with-backoff strategies when extracting from external REST or GraphQL APIs.
    4. Use `upstash-ratelimit-js` to enforce extraction rate limits on external API sources.
    5. Cache intermediate extraction results in `upstash-redis-js` to support resumable extraction on failures.

### Phase 2: Data Cleansing & Validation
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`
*   **Action:**
    1. Validate input data structures against schemas at the extraction boundary.
    2. Filter out corrupt, missing, or malformed rows. Log anomalies separately.
    3. Normalize data formats (standardize datetime offsets, trim whitespace, deduplicate rows).
    4. Use `systematic-debugging` for tracing data corruption root causes when validation failures occur.

### Phase 3: Business Logic Transformation (T)
*   **Sub-skills:** `superpowers-tdd`, `upstash-vector-js`, `upstash-search-js`
*   **Action:**
    1. Apply business transformations (aggregations, joins, metric computations, value mapping).
    2. Ensure transform logic is pure (deterministic): given the same input, it must yield the exact same output.
    3. Write unit tests targeting transformation edge cases (null records, out-of-bound variables) using `superpowers-tdd`.
    4. For AI/ML pipelines, generate vector embeddings during transformation using `upstash-vector-js` and build search indexes using `upstash-search-js`.

### Phase 4: Transaction-Safe Loading (L)
*   **Sub-skills:** `ultimate-database-workflow`, `upstash-workflow-js`, `upstash-qstash-js`
*   **MCP Tools:** `supabase-mcp-server/execute_sql`, `prisma-mcp-server/migrate-dev`
*   **Action:**
    1. Perform database insertions using bulk/batch inserts rather than single-record insertions to reduce network roundtrips.
    2. Ensure loading processes are **Idempotent**: if a pipeline runs twice due to a crash, the final database state must remain unchanged.
    3. Use database Transactions for writing aggregated datasets. If loading fails midway, roll back completely.
    4. Implement dead-letter-queues (DLQ) or recovery logs for records that fail the load phase using `upstash-qstash-js`.
    5. For durable multi-step ETL orchestration, define step-by-step pipelines with `upstash-workflow-js` for automatic retries and failure recovery.
    6. Use `supabase-mcp-server/execute_sql` for direct SQL batch operations or `prisma-mcp-server/migrate-dev` for schema-driven data loads.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `tavily-extract`, and `context7/get-library-docs` for discovering ETL framework APIs and data format parsers.
*   **Documentation:** Use `docx` skill for generating formal data pipeline specification documents.
*   **Memory:** Use `memory` MCP to persist pipeline configurations, data source schemas, and transformation rules across conversations.
*   **Monitoring:** Use `upstash-redis-js` for pipeline health dashboards and real-time progress tracking.
