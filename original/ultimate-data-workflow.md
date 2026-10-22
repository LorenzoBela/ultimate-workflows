---
name: ultimate-data-workflow
description: >
  Workflow for data pipeline engineering, streaming ETL pipelines,
  backpressure flow control, transactional batch COPY upserts, and Dead-Letter Queue (DLQ) error recovery.
  Triggers on "ultimate data workflow", "/ultimate-data-workflow", or when designing
  batch pipelines, parser scripts, database aggregations, or data transformations.
argument-hint: "[etl-pipeline | parser-script | database-aggregation | --stream | --batch | --dlq]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Data Pipeline and ETL Workflow

## Inputs and invariants

Record source format/schema/version, source identity, expected size, maximum record bytes, destination constraints, ordering requirements, privacy, throughput target and checkpoint/replay semantics. Preserve chosen storage/transport. Establish a representative baseline and small sample before a full import.

Use bounded streaming readers. A row-count cap alone does not bound memory: configure parser record/field byte limits and downstream batch bytes, concurrency and queue length. Reject or quarantine oversized input before materializing it where the parser supports this. Backpressure must reach the source.

## Executable batch sink example

JavaScript for Node streams. Input is already parsed records. Configure the upstream parser's byte limit separately. The sink checks serialized record/batch size, forwards rejected flushes to callbacks exactly once, and clears a batch only after successful flush. `flushBatch` must implement the transaction/checkpoint contract below. This sink's JSON sizing is appropriate for JSON-compatible records; use the actual wire encoding for other inputs.

```javascript
import { Writable } from 'node:stream';

export function createBatchSink({ flushBatch, maxRows = 5000,
  maxBytes = 4 * 1024 * 1024, maxRecordBytes = 256 * 1024 }) {
  if (!Number.isInteger(maxRows) || maxRows < 1 ||
      !(maxBytes > 0 && maxRecordBytes > 0 && maxRecordBytes <= maxBytes)) {
    throw new RangeError('Invalid batch limits');
  }
  let rows = [];
  let bytes = 0;
  async function flush() {
    if (!rows.length) return;
    await flushBatch(rows);
    rows = [];
    bytes = 0;
  }
  return new Writable({
    objectMode: true,
    highWaterMark: 1,
    write(row, encoding, callback) {
      (async () => {
        const json = JSON.stringify(row);
        if (json === undefined) throw new TypeError('Record must be JSON-compatible');
        const size = Buffer.byteLength(json);
        if (size > maxRecordBytes) throw new RangeError('Record too large');
        if (rows.length && bytes + size > maxBytes) await flush();
        rows.push(row);
        bytes += size;
        if (rows.length >= maxRows || bytes >= maxBytes) await flush();
      })().then(() => callback(), (error) => callback(error));
    },
    final(callback) {
      flush().then(() => callback(), (error) => callback(error));
    },
  });
}
```

Use `await pipeline(source, parser, sink, {signal})` from `node:stream/promises` on a supported runtime. Parser and database adapters must support bounded I/O/cancellation. Do not claim constant process memory solely from batch size: object overhead, upstream buffering and individual record allocation also matter.

## Transform and load contract

1. Validate fields against versioned schema. Normalize timestamps with a documented source timezone; preserve raw values/provenance when necessary. Define decimal precision, currency scale, rounding and overflow handling; do not assume every currency is cents.
2. Keep transformations deterministic or version external enrichment/model outputs with source data. Define deduplication natural key, source revision and conflict rules. A blind upsert can replay an old state over newer data.
3. For PostgreSQL, consider COPY into staging then validated merge; direct upsert is appropriate for smaller batches. Include keys, relevant columns and source revision guard; avoid changing business timestamps on identical replay.
4. Commit the batch mutation and checkpoint atomically when they share a database. For external queues, acknowledge only after durable state and use idempotent replay. State the at-least-once/ordering assumptions; do not promise exactly-once across independent systems.
5. Handle final partial batch, duplicate keys within a batch, transaction timeout/deadlock, partial source read and schema drift. Bound retries and stop on infrastructure/auth failures rather than sending everything to DLQ.

## Quarantine and recovery

DLQ entries need run/source/offset ID, schema/transform version, safe payload reference, reason, attempt count and timestamps. Restrict access, redact secrets and set retention. Define maximum rejected proportion/count; a broken schema must not silently quarantine an entire import. Replay through the same validation/idempotency rules, recording disposition.

Persist run identity, source checksum/version, checkpoint and processed/loaded/quarantined counts. Resume only if source and transform identity match; otherwise explicitly start/reconcile a new run. Use staging/swap, compensating operations or a tested restore according to data-loss tolerance.

## Evidence

Inject flush rejection and require pipeline rejection without hanging/unhandled rejection. Verify empty source, last partial batch, oversized record, malformed row, DB outage, crash after commit before acknowledgement, replay and out-of-order revisions. Record peak memory under representative input rather than guaranteeing it from row count. No full production import is a test. Return actual row reconciliation, checks/results, checkpoint and remaining recovery limitations.

Source: [Node stream implementer completion/error contract](https://nodejs.org/api/stream.html#transform_transformchunk-encoding-callback).
