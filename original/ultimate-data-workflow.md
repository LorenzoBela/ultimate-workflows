---
name: ultimate-data-workflow
description: >
  Flawless 10/10 Master Workflow for data pipeline engineering, streaming ETL pipelines,
  backpressure flow control, transactional batch COPY upserts, and Dead-Letter Queue (DLQ) error recovery.
  Triggers on "ultimate data workflow", "/ultimate-data-workflow", or when designing
  batch pipelines, parser scripts, database aggregations, or data transformations.
argument-hint: "[etl-pipeline | parser-script | database-aggregation | --stream | --batch | --dlq]"
---

# Ultimate Data Pipeline & ETL Workflow (10/10 Master Engine)

This workflow drives streaming data ingestion, bounded memory buffering, backpressure flow control, schema validation, transaction-safe bulk loading (PostgreSQL `COPY` / batch upsert), and Dead-Letter Queue (DLQ) anomaly isolation.

```
                                      [RAW SOURCE STREAM / BATCH DATA]
                                                     │
                          ┌──────────────────────────┴──────────────────────────┐
                          ▼                                                     ▼
              [PHASE 1: STREAMING EXTRACTION (E)]                   [PHASE 2: SCHEMA VALIDATION & CLEAN]
              ├─ Node.js / Python Reactive Streams                  ├─ Zod / Pydantic Row Validation
              ├─ Bounded Chunk Buffering (10k rows)                 ├─ Outlier Filtering & Normalization
              └─ Backpressure Ingestion Throttling                  └─ ISO-8601 UTC & Cents Conversion
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: DETERMINISTIC BUSINESS TRANSFORMATION (T)          │
        │  • Pure Functions • Idempotent Key Generation • Vector Embeddings (Upstash) │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: TRANSACTIONAL BULK LOAD (L) & DLQ]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🚀 PG COPY   │           │ 💾 DB TX     │           │ 📭 DEAD-LETT │
            │ Batch Upsert │           │ All-or-None  │           │ DLQ QStash   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Data Pipeline Engineering

1. **Bounded Memory Invariant**: Never load entire datasets into memory. Use streaming readers (`stream.Transform`, Python generators) with fixed buffer limits ($\le 10,000$ records).
2. **Backpressure Compliance**: Pipeline consumers must signal upstream producers to pause when ingestion queues reach high-water marks.
3. **Pure & Deterministic Transformations**: Given identical input rows, transformation logic must produce bit-for-bit identical output rows.
4. **Idempotent Loading via Upsert**: Bulk database insertions must utilize `ON CONFLICT (natural_key) DO UPDATE` to prevent duplicate record corruption.
5. **Dead-Letter Queue (DLQ) Quarantine**: Malformed or unparseable records must be routed to a quarantine DLQ (QStash / Kafka DLQ) without crashing the primary pipeline execution.

---

## 🔬 The 4-Phase Streaming ETL Pipeline

### Phase 1: Streaming Extraction with Backpressure
```typescript
import { createReadStream } from 'fs';
import { pipeline } from 'stream/promises';
import { Transform } from 'stream';
import csvParser from 'csv-parser';

export async function processDataPipeline(filePath: string) {
  let batch: any[] = [];
  const BATCH_SIZE = 5000;

  const transformer = new Transform({
    objectMode: true,
    async transform(chunk, encoding, callback) {
      batch.push(chunk);
      if (batch.length >= BATCH_SIZE) {
        await flushBatch(batch);
        batch = [];
      }
      callback();
    },
    async flush(callback) {
      if (batch.length > 0) await flushBatch(batch);
      callback();
    }
  });

  await pipeline(createReadStream(filePath), csvParser(), transformer);
}
```

### Phase 2: Transactional Batch Upsert
```sql
INSERT INTO transactions (id, user_id, amount_in_cents, status, created_at)
VALUES 
  ($1, $2, $3, $4, $5),
  ($6, $7, $8, $9, $10)
ON CONFLICT (id) 
DO UPDATE SET 
  status = EXCLUDED.status,
  updated_at = now();
```

### Phase 3: Dead-Letter Queue (DLQ) Logging
- Route rows failing schema validation directly to an isolated table `pipeline_quarantine_dlq` containing `raw_payload`, `error_reason`, `source_file`, and `quarantined_at`.
