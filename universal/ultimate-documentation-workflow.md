---
name: ultimate-documentation-workflow
description: >
  Flawless 10/10 Master Workflow for technical documentation, OpenAPI 3.1 specifications,
  interactive runnable code snippets, Architecture Decision Records (ADRs), and friction-free developer onboarding.
  Triggers on "ultimate documentation workflow", "/ultimate-documentation-workflow", or when
  generating documentation, writing READMEs, or documenting API interfaces.
argument-hint: "[readme-template | api-spec | onboarding-guide | --openapi | --adr]"
---

# Ultimate Technical Documentation & Onboarding Workflow (10/10 Master Engine)

This workflow guides the creation of high-clarity technical documentation, interactive OpenAPI 3.1 specifications, immutable Architecture Decision Records (ADRs), and 5-minute developer onboarding runbooks.

```
                                      [TECHNICAL DOCUMENTATION INITIATIVE]
                                                       │
                          ┌────────────────────────────┴────────────────────────────┐
                          ▼                                                         ▼
              [PHASE 1: MASTER REPOSITORY README]                       [PHASE 2: OPENAPI 3.1 & SDK SPECS]
              ├─ 30-Second Elevator Pitch & Architecture Map            ├─ Interactive Request/Response Schemas
              ├─ 1-Line Prerequisites & Copy-Paste Setup                ├─ Error Code Matrix (RFC 7807)
              └─ Environment Variable Matrix (.env.example)             └─ Auto-Generated Typed Client Snippets
                          │
                          ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                 PHASE 3: ARCHITECTURE DECISION RECORDS (ADR)                │
        │  • docs/adr/ • Context • Invariants • Rejected Alternatives • Trade-offs    │
        └──────────────────────────────────────┬──────────────────────────────────────┘
                                               ▼
                                  [PHASE 4: 5-MINUTE ONBOARDING & RUNBOOKS]
                    ┌──────────────────────────┼──────────────────────────┐
                    ▼                          ▼                          ▼
            ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
            │ 🚀 1-CMD RUN │           │ 🧪 SEED DB   │           │ 📊 ARCH DIAG │
            │ npm run dev  │           │ Mock Data    │           │ Mermaid C4   │
            └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Technical Documentation

1. **Code Explains HOW, Docs Explain WHY**: Never restate what obvious code lines do; document the constraints, domain invariants, and tradeoffs that forced the implementation.
2. **Copy-Paste Runnable Examples**: Every code snippet in documentation must be syntactically valid and runnable without undisclosed dependencies.
3. **The 5-Minute Developer Onboarding Law**: A new engineer must be able to clone the repo, run one setup command, seed the test database, and pass unit tests within 5 minutes.
4. **Strictly Synchronized `.env.example`**: Every environment variable referenced in `process.env` must have an annotated placeholder entry in `.env.example`.
5. **No Undocumented Public Endpoints**: 100% of HTTP endpoints must have corresponding OpenAPI 3.1 entries with request/response/error schemas.

---

## 🔬 The 4-Phase Documentation Pipeline

### Phase 1: Master Repository README Template
```markdown
# Project Name

> High-impact 1-sentence value proposition.

## 🚀 Quickstart (Under 3 Minutes)

```bash
git clone https://github.com/org/repo.git && cd repo
cp .env.example .env.local
pnpm install
pnpm db:seed
pnpm dev
```

## 🏗️ Architecture & Core Domains
- `apps/web`: Next.js 15 App Router Frontend
- `packages/database`: PostgreSQL schema & Supabase migrations
- `packages/ui`: Shared React design token components

## 🔑 Environment Variables
| Variable | Description | Default / Example | Required |
|---|---|---|---|
| `DATABASE_URL` | PgBouncer pooled connection | `postgresql://...:6543/postgres` | Yes |
```

### Phase 2: OpenAPI 3.1 Interactive Endpoint Spec
```yaml
openapi: 3.1.0
info:
  title: Core Billing API
  version: 2026-08-15
paths:
  /api/v1/charges:
    post:
      summary: Create an idempotent charge
      headers:
        Idempotency-Key:
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChargeRequest'
```

### Phase 3: Architecture Decision Record (ADR)
- Maintain sequential Markdown files under `docs/adr/0001-title.md` detailing Status, Context, Decision, Alternatives Considered, and Consequences.
