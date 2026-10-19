---
name: ultimate-document-intelligence-workflow
description: >
  Flawless 10/10 Master Workflow for AST-based multi-modal parsing, OCR scraping (Tesseract with Otsu thresholding),
  streaming spreadsheet processing, tabular semantic preservation, and RAG-ready vector chunking across mixed corpora.
  Triggers on "ultimate document intelligence workflow", "/ultimate-document-intelligence-workflow", or when
  extracting data, parsing PDFs/DOCX/XLSX, or running OCR pipelines.
argument-hint: "[document-path | ocr-target | rag-chunking | --ocr | --ast | --table]"
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

# Ultimate Document Intelligence & Scraper Workflow (10/10 Master Engine)

This workflow defines the standards, streaming pipelines, and algorithms for parsing, extracting, and understanding structured and unstructured data from mixed-media documents (Office, OpenDocument, PDFs, spreadsheets, and scanned images).

```
                                      [MIXED-MEDIA DOCUMENT CORPUS / SCAN]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: FORMAT DISCOVERY & AST TRIAGE]                      [PHASE 2: OCR & STREAMING PARSERS]
              ├─ PDF / Office -> AST Hierarchy                              ├─ Tesseract OCR + Otsu Binarization
              ├─ Excel / Spreadsheets -> ExcelJS Streaming                  ├─ Tabular Grid Structure Preservation
              └─ Unstructured Images -> Vision OCR Queue                    └─ Strip Pagination & Running Headers
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: TEXT NORMALIZATION & UNICODE REBUILD               │
        │  • Reassemble Hyphenated Breaks • Clean Nonce Artifacts • UTF-8 Conversion  │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: SEMANTIC CHUNKING & VECTOR PERSISTENCE]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🧱 CHUNKING  │           │ ⚡ UPSTASH   │           │ 📊 METADATA  │
            │ Heading-Aware│           │ Vector Index │           │ Extracted JSON│
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Document Intelligence

1. **AST Representation Before Flattening**: Always parse documents into a format-agnostic Abstract Syntax Tree (AST) before generating Markdown or plain text.
2. **Streaming Large Files**: Spreadsheets ($> 10\text{MB}$) and PDFs ($> 50\text{MB}$) MUST be read via streaming chunk iterators to prevent Node heap exhaustion.
3. **Tabular Semantics Preservation**: Never flatten tables into unstructured sentences. Convert tables to standardized Markdown or CSV arrays preserving column headers.
4. **Adaptive Image Pre-Processing**: Scanned images must undergo grayscale conversion, rotation deskewing, and Otsu binarization before OCR execution.
5. **Structural Heading-Aware Chunking**: Slicing for RAG must split at structural boundaries (headings, section breaks), preserving parent section metadata on each chunk.

---

## 🔬 The 4-Phase Document Intelligence Pipeline

### Phase 1: AST Multi-Format Parsing
```typescript
import { parseOffice } from 'officeparser';

export async function parseDocumentAST(filePath: string) {
  const ast = await parseOffice(filePath, {
    extractAttachments: false,
    ocr: true
  });
  return ast;
}
```

### Phase 2: Streaming Spreadsheet Parsing
```typescript
import ExcelJS from 'exceljs';

export async function streamSpreadsheet(filePath: string, onRow: (row: any) => Promise<void>) {
  const workbookReader = new ExcelJS.stream.xlsx.WorkbookReader(filePath, {});
  for await (const worksheetReader of workbookReader) {
    for await (const row of worksheetReader) {
      await onRow(row.values);
    }
  }
}
```

### Phase 3: OCR Preprocessing & Extraction
- Apply image rotation and contrast enhancement.
- Run Tesseract OCR with page segmentation mode 6 (uniform block of text).

### Phase 4: Structural Semantic Chunking for RAG
- Split documents on `HeadingLevel.HEADING_2` boundaries with 100-character context overlaps.
- Index chunks to `upstash-vector-js` with metadata payload (`source_path`, `heading`, `page_number`).
