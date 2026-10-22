---
name: ultimate-monorepo-workflow
description: >
  Workflow for monorepos, multi-package workspaces, dependency boundary enforcement,
  Turborepo/Nx caching pipelines, Syncpack version alignment, and Changesets multi-package releases.
  Triggers on "ultimate monorepo workflow", "/ultimate-monorepo-workflow", or when
  configuring workspaces, link dependencies, or designing monorepo pipeline builds.
argument-hint: "[workspace-setup | package-link | changeset-version | --turbo | --syncpack]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Monorepo and Multi-Package Workflow

## Inputs and boundaries

Inventory package manager/lockfile, runtime/tool versions, apps/libraries, visibility, outputs, task graph, consumer platforms and release tooling. Preserve conventions; don't migrate every repository to pnpm/Turbo/Changesets. Discover installed commands.

Declare dependencies explicitly and use public exports/entrypoints. Prevent private-source imports and forbidden dependency directions. Check cycles/phantom dependencies with clean installs/builds. Package-manager isolation helps but does not prove consumer/runtime resolution.

Align dependency versions through intentional groups: shared tooling, runtime libraries, peers and platform exceptions. Blind uniformity can break native runtimes/peers. Review manifests/lockfile before applying fixes.

## Task graph and cache correctness

Use the actual runner schema for upstream builds, generated contracts, environment/config inputs, outputs and side effects. File inputs and dependency tasks are different concepts.

Cached tasks include build-affecting env, config, toolchain and generated inputs. Keep secrets out of artifacts/logs; verify remote-cache access/trust. Publishing/migrations are side effects and non-cacheable; dev servers may be persistent/non-cacheable. Capture relevant outputs, excluding transient caches.

Illustrative Turborepo configuration; validate installed version and adapt file/env scope:

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", ".env*"],
      "env": ["PUBLIC_API_BASE_URL"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "test": { "dependsOn": ["^build"], "outputs": ["coverage/**"] },
    "dev": { "cache": false, "persistent": true },
    "publish": { "dependsOn": ["build"], "cache": false }
  }
}
```

Declare root config/toolchain through the runner's actual global/package input mechanism; the example does not establish those inputs. Paths follow documented runner scope. Do not record secret env values in logs.

## Validation strategy

Use affected-package checks with verified merge base and downstream impact; retain full checks when graph completeness is uncertain. Run changed package/downstream contracts plus periodic clean full-workspace builds.

Verify unchanged-task hit; source/public-env/shared-config changes miss; outputs restore fully; irrelevant inputs do not rebuild everything. Cache correctness precedes hit-rate targets. Compare cold/warm measurements before claiming speed gains.

Pack libraries and test tarballs in temporary consumers: entrypoints, types, ESM/CJS, assets, peers and runtime dependencies. Workspace source resolution can hide missing dist files and undeclared dependencies.

## Releases and recovery

Use existing versioning policy, semver and changelog conventions. Release metadata covers consumer-visible changes; document internal/no-release exceptions. Review versions, ranges and dependency release order.

Registry publication across packages is generally not atomic. Record immutable manifest with package/version/content hash, dependencies, status and dist-tags. Dry-run/pack first; publish only within authorization. On interruption, inspect registry, verify artifact identity and resume missing publications. Never overwrite versions or unpublish shared dependencies as default rollback. Deprecation, corrected version and dist-tag recovery may be safer.

## Evidence

Return boundary/task/manifest changes, actual checks, cache invalidation evidence, consumer result and unverified registry/platform assumptions. Simulate interrupted publishing with a stub/disposable registry, never public production packages. Preserve unrelated manifest/lockfile edits and report remaining unpublished work.

Sources: [Turborepo caching](https://turborepo.com/docs/crafting-your-repository/caching), [Changesets](https://github.com/changesets/changesets).
