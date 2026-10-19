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
