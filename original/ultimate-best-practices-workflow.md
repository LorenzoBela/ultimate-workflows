---
name: ultimate-best-practices-workflow
description: "Review React, Next.js, React Native, Expo or native Android work using the installed version and measured workload. Route to platform-specific checks without changing the stack."
argument-hint: "[react | nextjs | react-native | android]"
---

# Framework engineering practices

Read the manifest/lockfile and build configuration. Identify installed version, target, production or development mode, reported symptom and baseline. Apply only the matching section. Preserve the project's framework, architecture and toolchain.

| Platform | Investigate | Verify |
|---|---|---|
| React | Unnecessary renders, expensive work, state ownership and effect cleanup. Profile before adding memoization. | Use React Profiler or equivalent in a representative build. Compare commit duration, renders and interaction behavior using the same flow. |
| Next.js | Use the installed router and version to verify rendering boundaries, data freshness, cache scope and authorization. Inspect bundle and request waterfalls. | Run the project build and exercise server/client navigation, revalidation and tenant boundaries. Compare route assets and observed request behavior. |
| React Native / Expo | Separate native launch, JS startup, network and frame costs. Inspect build mode, runtime, list workload and thread contention. | Use a release or profiling build on a representative device. Record cold/warm starts, frame times or memory under the affected flow. Recheck navigation or list behavior. |
| Native Android | Inspect lifecycle, main-thread I/O, startup path, state restoration and Compose recomposition where relevant. | Use supported device traces, Macrobenchmark or project tooling for the measured path. Exercise recreation, background/foreground and target API behavior as relevant. |

Tie each finding to a file or behavior, version, impact and check. Distinguish a hypothesis from a measured bottleneck. If the target or profiler is unavailable, report the missing measurement and preserve any supported static findings.

## Role and handoffs

**Platform diagnostics specialist.** Own version-aware performance and framework behavior. Use [ultimate-frontend-workflow](../ultimate-frontend-workflow/SKILL.md) and [ultimate-testing-workflow](../ultimate-testing-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Pick one installed platform. Measure React commits, Next.js route/network behavior, React Native release startup, or Android device traces as applicable. Use the same workload for baseline and candidate, and keep unmeasured hypotheses separate.
