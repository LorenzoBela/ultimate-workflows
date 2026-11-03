---
name: ultimate-document-workflow
description: "Create, edit and review Word documents while preserving styles, numbering and layout. Use supported document tools and render results. Handle tracked changes or OOXML when the task requires them."
argument-hint: "[docx-generate | xml-edit | pdf-export | --track-changes | --pdf]"
---

# Word document workflow

Identify the requested output, source/template, authoring tool and render environment. Use the host's supported document workflow and library for routine edits. Keep the source available for comparison and preserve styles, list definitions, section settings, fields and other unrelated content.

1. Inspect the source and select the narrowest supported editing operation. Use document styles and semantic lists. Use widths appropriate to the template, page geometry and table behavior.
2. For tracked changes, use the supported revision API when available. Use direct OOXML only for required features the library cannot express. Work from a copy and preserve relationships, namespaces, package parts and surrounding markup. Validate unique IDs, actual author and timestamps, insertion/deletion markup and reference integrity. Verify any signing or protection implications before modifying a protected package.
3. Open and render the result using the available Word-compatible renderer. Inspect affected pages and adjacent pagination, headings, numbering, tables and margins. For revisions, verify author/time and the visible result of accepting and rejecting a representative change on separate review copies where supported.
4. Deliver the requested artifact with any render or compatibility limits. Preserve originals and report unsupported revision or rendering features explicitly.

## Role and handoffs

**Word production specialist.** Own document editing, layout, and tracked changes. Use [ultimate-document-intelligence-workflow](../ultimate-document-intelligence-workflow/SKILL.md) and [ultimate-documentation-workflow](../ultimate-documentation-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Edit a numbered document with a section break and render before and after. Check affected and adjacent pages. On separate copies, accept and reject a tracked change and compare visible results where supported.
