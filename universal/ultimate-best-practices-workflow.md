---
name: ultimate-best-practices-workflow
description: >
  Apply version-aware React, Next.js, React Native, Expo and native Android practices with workload-based verification. Use for relevant engineering-practices work while preserving the existing stack.
argument-hint: "[react | nextjs | react-native | android]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Framework-specific engineering practices

Use for a requested engineering-practices review or relevant implementation. Detect the actual framework, version, compiler/build mode and target platform first. Preserve the existing stack and architecture; apply only relevant sections. Avoid introducing dependencies or layers to satisfy a generic checklist.

## Inputs and checks

Read manifests, supported devices/browsers, existing conventions, critical behavior, accessibility requirements and performance evidence. Prefer repository scripts and available pinned tools. Run focused checks during edits and appropriate integrated checks at completion; re-run broad checks when new failures/changes justify it.

## React and Next.js

- Prefer clear composition and explicit state ownership. Compound components help certain reusable APIs; do not replace simple props with context without a reason.
- Respect server/client boundaries and framework version semantics. Keep secrets/server-only code off the client; interactive leaves use appropriate client boundaries.
- Fetch independent work concurrently where safe and avoid accidental waterfalls; define cache/freshness/error behavior against the installed Next.js version.
- Use supported image/font optimizations with correct sizing and layout behavior. Check actual layout shift rather than promising zero shift from one API.
- Profile before adding memoization. Account for React compiler/toolchain capabilities; a blanket useMemo/useCallback rule can add noise without benefit. React-version-specific ref/context features require verified support.

## React Native and Expo

- Profile representative release builds/devices for JS/UI thread time, startup, memory and scroll behavior. Emulator/development measurements do not prove real-device results.
- Choose FlatList, FlashList or another existing list based on workload, item complexity, library/runtime compatibility and measured behavior. Item count alone is not a valid install threshold.
- Use safe-area/keyboard behavior and platform-appropriate accessible touch targets, labels, focus and scaling. Verify screen-reader and keyboard behavior where supported.
- Move gesture/animation work to supported UI/native mechanisms when profiling shows JS contention. Verify Reanimated/new architecture compatibility rather than assuming every animation needs a new dependency.
- Optimize Hermes/runtime behavior using current supported documentation and measurement; do not ban language features such as Proxy without an actual compatibility/performance finding.

## Android native

- Use project-supported Kotlin/Compose or existing UI framework. Hoist state where useful, manage lifecycle/collections correctly and preserve cancellation.
- Keep blocking IO and expensive work off the main thread with appropriate dispatchers; do not assume every suspend function automatically runs in the background.
- Use ViewModels/repositories/domain layers when they clarify ownership. Do not require a use-case wrapper or strict Clean Architecture for every operation.
- Respect actual design system, platform accessibility, state restoration and adaptive layout requirements. Test target SDK/device behavior and supported build configuration.

## Quality and design

Maintain clear boundaries, validate public inputs and preserve meaningful typed errors. Prefer straightforward code over speculative abstractions. Function length and layer count are review signals, not automatic defects. Preserve branding and choose state handling suited to each control; static elements do not need loading/disabled/error states.

Use semantic design tokens when appropriate, keyboard/focus behavior, labels, contrast, reduced-motion and responsive content. Verify relevant standards and platform exceptions rather than equating a color class or one contrast number with accessibility conformance.

## Evidence and completion

Tie each recommendation to file/behavior, framework version, user impact and a concrete verification or profile. Distinguish measured bottlenecks from hypotheses. Acceptance includes representative regression behavior, actual check outputs and unrun device/production limitations. When research is invoked, all 15 substantive engine inputs and rich per-engine query floors remain mandatory; do not silently replace that contract with a single documentation search.
