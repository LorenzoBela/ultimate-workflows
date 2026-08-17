---
name: ultimate-document-workflow
description: >
  Flawless 10/10 Master Workflow for creating, parsing, editing, and converting Word documents (.docx files).
  Coordinates JS docx-builder setups, OOXML XML unpacking/repacking, tracked changes auditing,
  comment injections, and high-fidelity PDF exports.
  Triggers on "ultimate document workflow", "/ultimate-document-workflow", or when
  manipulating Word docs, templates, tracked changes, or exporting docx to PDF.
argument-hint: "[docx-generate | xml-edit | pdf-export | --track-changes | --pdf]"
---

# Ultimate Document & Publication Workflow (10/10 Master Engine)

This workflow drives professional document engineering—governing programmatic Word generation (docx-js), OOXML-level tracked edits, and high-fidelity PDF/print publication conversions.

```
                                      [DOCUMENT GENERATION / EDIT REQUEST]
                                                        │
                          ┌─────────────────────────────┴─────────────────────────────┐
                          ▼                                                           ▼
              [PHASE 1: PAGE FORMAT & TYPOGRAPHY]                           [PHASE 2: DOCX-JS CODE GENERATOR]
              ├─ US Letter (12240x15840 DXA) / A4                           ├─ Table Widths in DXA (WidthType.DXA)
              ├─ 1-inch Margins (1440 DXA)                                  ├─ Numbering XML (No Unicode Bullets)
              └─ Arial / Custom Heading Styles                              └─ Paragraph-Wrapped PageBreaks
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: OOXML TRACKED CHANGES & SMART COMMENTS             │
        │  • unpack.py • Run-Level <w:ins> / <w:del> • Smart Quotes • Direct Comments │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: REPACK, SCHEMA VALIDATE & PDF CONVERT]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 📦 pack.py   │           │ 🔍 validate  │           │ 📄 SOFFICE   │
            │ Repack XML   │           │ Schema Check │           │ PDF Export   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Document Engineering

1. **Explicit Dimensions in DXA**: Page sizes and table widths must be explicitly defined in twips/DXA ($1\text{ inch} = 1440\text{ DXA}$).
2. **Cell Width Sum Invariant**: The sum of all individual cell widths in a table MUST equal the defined table width exactly.
3. **No Raw Unicode Bullets in Word XML**: Lists must use OOXML `<w:numPr>` numbering configurations, never pasted Unicode `•` symbols.
4. **Run-Level Tracked Revisions**: Tracked insertions (`<w:ins>`) and deletions (`<w:del>`) must be executed strictly at the run level (`<w:r>`), preserving `<w:rPr>` formatting.
5. **Smart Quotes & Typography**: Use proper typographic XML entities (`&#x2019;` for apostrophe/right-quote, `&#x201C;`/`&#x201D;` for curved double quotes).

---

## 🔬 The 4-Phase Document Pipeline

### Phase 1: Programmatic docx-js Document Generation
```typescript
import { Document, Packer, Paragraph, Table, TableRow, TableCell, WidthType, HeadingLevel } from 'docx';
import * as fs from 'fs';

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      new Paragraph({ text: 'Executive Architecture Summary', heading: HeadingLevel.HEADING_1 }),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        rows: [
          new TableRow({
            children: [
              new TableCell({ width: { size: 3120, type: WidthType.DXA }, children: [new Paragraph('Component')] }),
              new TableCell({ width: { size: 6240, type: WidthType.DXA }, children: [new Paragraph('Status')] }),
            ]
          })
        ]
      })
    ]
  }]
});

Packer.toBuffer(doc).then((buffer) => fs.writeFileSync('Architecture_Summary.docx', buffer));
```

### Phase 2: OOXML Tracked Changes via XML Manipulation
- Unpack: `python scripts/unpack.py input.docx workspace/`
- Insert revision XML:
  ```xml
  <w:ins w:id="1" w:author="Claude" w:date="2026-08-15T10:00:00Z">
    <w:r><w:t>Approved production architecture</w:t></w:r>
  </w:ins>
  ```
- Repack and Validate: `python scripts/pack.py workspace/ output.docx`
- Export to PDF: `soffice --headless --convert-to pdf output.docx`
