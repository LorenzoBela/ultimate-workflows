---
name: ultimate-document-workflow
description: >
  Master workflow for creating, parsing, editing, and converting Word documents
  (.docx files).
  Coordinates JS docx-builder setups, XML unpacking/repacking, tracked changes auditing,
  comment injections, and PDF conversions.
  Triggers on "ultimate document workflow", "/ultimate-document-workflow", or when
  manipulating Word docs, templates, tracked changes, or exporting docx to PDF.
argument-hint: "[docx-generate | xml-edit | pdf-export]"
---

# Ultimate Document & Publication Workflow

This workflow drives professional document engineering—governing program-based Word generation, XML-level tracked edits, and high-fidelity publication conversions.

---

## The 4-Phase Document Pipeline

### Phase 1: Format Definition & Setup
*   **Sub-skills:** `docx`, `ckm:brand`, `theme-factory`
*   **Action:**
    1. Determine the paper format: explicitly declare US Letter (12240×15840 DXA) or A4 (11906×16838 DXA) with 1-inch margins (1440 DXA).
    2. Convert legacy formats: convert `.doc` inputs to `.docx` using headless LibreOffice prior to processing.
    3. Choose typography: use Arial (default) or custom fonts. Override built-in headings using exact IDs (`Heading1`, `Heading2`) and set `outlineLevel` (0 for H1, 1 for H2) for Table of Contents (TOC) mappings.
    4. Apply `ckm:brand` guidelines for branded document templates (logo placement, color scheme, tone of voice).
    5. Use `theme-factory` to apply pre-set visual themes (colors, fonts, spacing) to document layouts.

### Phase 2: Program-Driven Document Generation (docx-js)
*   **Sub-skills:** `docx`, `ckm:slides`, `ckm:design-system`
*   **Action:**
    1. **Dual Table Widths:** Always define table widths (in DXA, type `WidthType.DXA`) and ensure individual cell widths sum exactly to the table width. Use `ShadingType.CLEAR` (never SOLID).
    2. **List Formats:** Never use raw Unicode bullets. Configure lists using `numbering` configurations (`LevelFormat.BULLET` or `LevelFormat.DECIMAL`).
    3. **Image Runs:** Always declare image `type` parameter (png/jpg) and provide all three alt-text parameters (title, description, name).
    4. **Layout elements:** Wrap all `PageBreak` calls inside a Paragraph element.
    5. Align document design tokens (colors, spacing, typography) with `ckm:design-system` token architecture.

### Phase 3: XML Unpacking, Tracked Changes & Comments
*   **Sub-skills:** `docx`, `lint-and-validate`
*   **Action:**
    1. **Unpack:** Extract raw package layers (`word/document.xml`, `word/_rels/`) using `unpack.py`.
    2. **Tracked Edits:** Implement insertions (`<w:ins>`) and deletions (`<w:del>`) at the run level. Preserve original formatting properties (`<w:rPr>`). Tag author attribute as "Claude".
    3. **Smart Quotes:** Always use XML entities for professional quotation layouts:
       *   `&#x2019;` for apostrophes and right-single quotes.
       *   `&#x201C;` and `&#x201D;` for double quotes.
    4. **Comments:** Insert comments using `comment.py`. Place start/end markers as siblings of runs (direct children of `<w:p>`).
    5. Run `lint-and-validate` on generated XML to verify structural integrity before repacking.

### Phase 4: Repack, Validate & Convert
*   **Sub-skills:** `docx`, `systematic-debugging`
*   **Action:**
    1. **Repack:** Compress edited XML files back to `.docx` using `pack.py`, invoking automatic verification.
    2. **Validate:** Run validation checks (`validate.py`). Fix schema validation errors or mismatched namespace tags.
    3. **Convert:** Export documents to PDF or JPEG images (using soffice and pdftoppm) to generate visual renderings and verify layout consistency.
    4. Use `systematic-debugging` to diagnose validation failures, corrupt XML, or rendering inconsistencies.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` and `context7/get-library-docs` for docx-js API documentation and OOXML specification references.
*   **Memory:** Use `memory` MCP to persist document template configurations and style decisions across conversations.
*   **Presentations:** Use `ckm:slides` for generating companion HTML presentations alongside formal documents.
*   **Banner Design:** Use `ckm:banner-design` for creating cover pages, headers, and branded visual elements within documents.
