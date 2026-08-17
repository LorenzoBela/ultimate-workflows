---
name: ultimate-document-intelligence-workflow
description: >
  Flawless 10/10 Master Workflow for AST-based multi-modal parsing, OCR scraping (Tesseract with Otsu thresholding),
  streaming spreadsheet processing, tabular semantic preservation, and RAG-ready vector chunking across mixed corpora.
  Triggers on "ultimate document intelligence workflow", "/ultimate-document-intelligence-workflow", or when
  extracting data, parsing PDFs/DOCX/XLSX, or running OCR pipelines.
argument-hint: "[document-path | ocr-target | rag-chunking | --ocr | --ast | --table]"
---

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
