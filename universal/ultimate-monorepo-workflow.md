---
name: ultimate-monorepo-workflow
description: >
  Flawless 10/10 Master Workflow for monorepos, multi-package workspaces, dependency boundary enforcement,
  Turborepo/Nx caching pipelines, Syncpack version alignment, and Changesets multi-package releases.
  Triggers on "ultimate monorepo workflow", "/ultimate-monorepo-workflow", or when
  configuring workspaces, link dependencies, or designing monorepo pipeline builds.
argument-hint: "[workspace-setup | package-link | changeset-version | --turbo | --syncpack]"
---

# Ultimate Monorepo & Multi-Package Architecture Workflow (10/10 Master Engine)

This workflow guides the structure, dependency boundary isolation, computational cache reuse (Turborepo/Nx), dependency version unification (Syncpack), and atomic versioned publishing (Changesets) across multi-package workspaces.

```
                                      [MONOREPO ROOT WORKSPACE]
                                                  │
                       ┌──────────────────────────┴──────────────────────────┐
                       ▼                                                     ▼
           [PHASE 1: WORKSPACE ARCHITECTURE]                     [PHASE 2: PIPELINE ORCHESTRATION]
           ├─ apps/ (Deployable Services)                        ├─ Turborepo / Nx Task Graphs
           ├─ packages/ (Shared Types, UI, Config)               ├─ Remote Computation Caching
           └─ Strict pnpm-workspace.yaml Isolation               └─ Topological Task Ordering (^build)
                       │
                       ▼
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │                 PHASE 3: DEPENDENCY UNIFICATION & BOUNDARY ENFORCEMENT       │
     │  • Syncpack Version Alignment • Zero Phantom Dependencies • Shared TSConfigs │
     └──────────────────────────────────────┬──────────────────────────────────────┘
                                            ▼
                               [PHASE 4: MULTI-PACKAGE RELEASES & CHANGESETS]
                 ┌──────────────────────────┼──────────────────────────┐
                 ▼                          ▼                          ▼
         ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
         │ 📦 CHANGESET │           │ 🏷️ SEMVER    │           │ 🚀 ATOMIC    │
         │ PR Markdown  │           │ Major/Min/Pat│           │ Publish Gate │
         └──────────────┘           └──────────────┘           └──────────────┘
```

---

## 🏛️ Iron Laws of Monorepo Architecture

1. **Explicit Package Boundaries**: No package may import from another package without declaring it in its `package.json` `dependencies` or `devDependencies`.
2. **Zero Phantom Dependencies**: All builds must run with strict package managers (pnpm or Yarn Berry) that isolate unhoisted dependencies.
3. **Deterministic Task Graphs**: Tasks defined in `turbo.json` or `nx.json` must declare explicit dependencies (`"^build"`, `"$TURBO_DEFAULT$"`).
4. **Unified Dependency Coordinates**: All packages in the monorepo must share identical major/minor versions of third-party libraries (`syncpack`).
5. **Atomic Changeset Publishing**: Every pull request that modifies code in a publishable package must include a corresponding Changeset file (`.changeset/*.md`).

---

## 🔬 The 4-Phase Monorepo Pipeline

### Phase 1: Workspace Architecture & Directory Layout
```text
monorepo-root/
├── apps/
│   ├── web/               # Next.js 15 App Router
│   ├── mobile/            # React Native / Expo
│   └── api/               # Express / Fastify / Node
├── packages/
│   ├── ui/                # Shared React Design Tokens & Components
│   ├── database/          # Prisma schema, migrations, and Supabase client
│   ├── tsconfig/          # Base TypeScript configurations
│   └── eslint-config/     # Shared ESLint & Prettier rules
├── pnpm-workspace.yaml
├── turbo.json
└── package.json
```

### Phase 2: Pipeline Orchestration (`turbo.json`)
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "lint": {
      "dependsOn": ["^build"]
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### Phase 3: Dependency Unification with Syncpack
- Run `npx syncpack list-mismatches` to detect conflicting dependency versions across workspace packages.
- Fix mismatches using `npx syncpack fix-mismatches` to ensure uniform dependency versions.

### Phase 4: Atomic Multi-Package Release with Changesets
- Add a changeset: `npx changeset` (prompts for patch/minor/major and description).
- Version packages: `npx changeset version` (updates package.jsons and changelogs).
- Publish packages: `npx changeset publish` (publishes packages in topological dependency order).
