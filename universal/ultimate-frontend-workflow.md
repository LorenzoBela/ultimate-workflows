---
name: ultimate-frontend-workflow
description: >
  Unified master workflow for building premium, production-grade frontend interfaces.
  Synthesizes brand alignment, token systems, copywriting, local assets, utility-first
  styling, fluid motion, and strict UX/accessibility quality checks.
  Triggers on "ultimate frontend workflow", "/ultimate-frontend-workflow", or when
  coordinating high-fidelity UI/UX projects.
argument-hint: "[page | component | dashboard]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Frontend Workflow

## Inputs and design direction

Identify the actual framework/version, routes/components, users, task, brand, reference assets, content, data sources, devices and accessibility requirements. Preserve the project's design system and useful assets. A button fix does not require rebranding or a new animation dependency. Discover available skills/tools; missing image/browser tools must not cause fabricated output or verification.

Define success in user terms: primary action, information hierarchy, readable copy, realistic content and supported states. Do not invent testimonials, customer metrics or product capabilities. Ask only for missing decisions that materially block work; document reversible assumptions and proceed within scope.

## Design system and implementation

1. Choose visual direction appropriate to product and brand: intentional typography, spacing, layout rhythm and meaningful imagery. Familiar grids, system fonts, standard components and user palette are valid. Avoid novelty for its own sake.
2. Prefer existing tokens. For a new system, separate primitive values, semantic intent and component overrides where useful. Theme colors, spacing, type, radii and focus consistently; avoid unnecessary token layers for isolated details.
3. Use approved assets or generate requested imagery with an available tool. Preserve SVG/vector assets where suitable; bitmap generation is not mandatory. Store assets locally when permitted, record source/license, optimize sizes and include meaningful alt text; decorative images use empty alt.
4. Write concrete copy/action labels. Keep implementation details out of user flows unless useful to a decision. Provide honest empty/error feedback and recovery; skeletons reflect real loading, not artificial delay.
5. Match architecture to stack. Apply composition for meaningful variants/context; retain semantic links/buttons. Reuse accessible primitives rather than rebuilding complex keyboard behavior without reason.

## Rendering and state boundaries

In Next.js App Router, keep appropriate data/secret-bearing work in server components. Client boundaries belong where state, browser APIs, context or interactive libraries require them; providers/containers can validly be client components. Keep server-only modules out of client bundles. Do not force RSC into SPAs, static sites or native apps.

Fetch independent data in parallel; co-locate loading/error boundaries with meaningful sections. Avoid effect-driven derived state. Use the existing query library for client caching/mutations. Server actions/handlers require authentication, authorization, input validation and framework-appropriate CSRF protections; TypeScript is not runtime validation.

Optimistic updates need rollback, conflict handling and accessible feedback. Distinguish stale data, empty data, permission denial, timeout and offline states. Cancel stale requests and clean up subscriptions/observers. Do not mask server failure with fake local success.

## Layout, media and motion

Design mobile-first; test widths selected from actual layout stress points, narrow screens, long localized text and zoom. Container queries can help reusable components. Respect safe areas and platform touch targets; do not copy pt/dp directly into unrelated web requirements.

Reserve media space with dimensions/aspect ratio. Use responsive assets, font subsets and fallback metrics. Font swapping alone does not guarantee zero CLS. Prioritize actual LCP media using the installed framework API; do not preload every image.

Prefer transform/opacity for inexpensive motion. Filter/clip-path are not automatically GPU-only; inspect cost on target hardware. Use CSS for simple interactions and a suitable library when needed. Respect reduced motion, keep essential content visible and clean up observers/timelines. Measured layout animation is valid where benefit justifies cost.

Code-split heavy components where useful; disable SSR only for genuinely browser-only behavior in supported boundaries. Blanket `ssr:false` can delay content and is not a performance rule.

## Accessibility and performance evidence

Use the requested accessibility level, normally WCAG 2.2 AA for web work. Verify keyboard operation, logical focus, visible focus, headings/landmarks, names/labels, validation feedback, announcements where needed, contrast, target size and reduced motion. Modal focus containment is intentional; inescapable keyboard traps are defects. Automated scans do not replace manual checks.

Use one documented performance budget appropriate to product/baseline. Current Core Web Vitals are LCP, INP and CLS; FID is retired. Typical good field thresholds are LCP <=2.5s, INP <=200ms and CLS <=0.1 at p75; project targets may be stricter. Separate field evidence from lab proxies and specify device/network/test conditions. Without field data do not claim production p75 success. Bundle budgets follow actual runtime needs, not a universal cap.

## Verification, recovery and evidence

Verify relevant loading/error/retry/disabled/empty/success states and primary actions. Noninteractive elements need no invented disabled/error states. Inspect available screenshots, overflow and console/network failures at representative widths. Run relevant repository-native type/build/lint checks. If browser tools are unavailable, explicitly report visual checks unverified.

Deliver changed routes/assets, behavior, actual checks and limitations. Retain prior assets/tokens until migration is verified; use a scoped flag or revertible replacement for risky redesign. Do not claim pixel perfection, certification or measured speed without evidence.

Sources: [Web Vitals](https://web.dev/articles/vitals), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Next.js boundaries](https://nextjs.org/docs/app/getting-started/server-and-client-components).
