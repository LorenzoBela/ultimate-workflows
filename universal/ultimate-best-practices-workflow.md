---
name: ultimate-best-practices-workflow
description: >
  Master workflow for engineering best practices across React, Next.js, Expo,
  Android Native, and general clean code.
  Coordinates compound composition, RSC boundaries, Hermes engine optimizations, Jetpack Compose,
  and senior-level software craftsmanship.
  Triggers on "ultimate best practices", "/ultimate-best-practices-workflow", or when
  initiating component refactoring or multi-platform native development.
argument-hint: "[react | nextjs | expo | android-native | clean-code]"
---

# Ultimate Engineering Best Practices Workflow

This workflow enforces production-grade engineering standards and platform-native conventions across React, Next.js, Expo/React Native, Android Native, and general software architecture.

---

## 1. Core React & Composition Patterns
*   **Sub-skills:** `vercel-composition-patterns`, `vercel-react-best-practices`
*   **Best Practices:**
    1. **Avoid Boolean Prop Proliferation:** Do not customize component behavior by adding endless boolean flags. Use Compound Components (with shared context) to compose complex children.
    2. **State Management:** Decouple state management logic. Keep context interfaces generic with clear state and action boundaries.
    3. **React 19 Standards:** (If using React 19) Avoid `forwardRef`; pass refs as standard props. Use the `use()` hook for consuming context or promises dynamically.
    4. **Separate Logic from Render:** Extract complex logic, API queries, or event handlers into custom hooks (e.g. `useOrderDetails`) to keep rendering components clean.
    5. **Performance:** Apply `useMemo`, `useCallback`, and `React.memo` judiciously. Profile with React DevTools before optimizing.

## 2. Next.js (App Router) Best Practices
*   **Sub-skills:** `next-best-practices`, `vercel-react-best-practices`
*   **Best Practices:**
    1. **Server vs. Client Components (RSC):** Default all components to React Server Components (RSC) for faster page loads. Move interactive behaviors (inputs, buttons, hooks) to leaf-level Client Components using `"use client"`.
    2. **Data Fetching:** Fetch data at the component level using native async/await. Avoid nesting multiple fetches that block rendering (waterfalls); run independent fetches in parallel (`Promise.all`).
    3. **Route Handlers:** Write REST endpoints in `route.ts`. Return structured JSON with consistent error formats and HTTP status codes.
    4. **Metadata & SEO:** Use the `generateMetadata` export for dynamic page titles, descriptions, and Open Graph tags.
    5. **Image & Font:** Use `next/image` with explicit width/height to prevent CLS. Use `next/font` for zero-layout-shift font loading.

## 3. Expo & React Native Best Practices
*   **Sub-skills:** `vercel-react-native-skills`, `react-native-best-practices`, `react-native-best-practices-callstack`
*   **Best Practices:**
    1. **Performance Tuning:** Keep the JS thread free of heavy operations. Memoize expensive computations (`useMemo`) and callbacks (`useCallback`) to avoid unnecessary re-renders.
    2. **Virtual Lists:** For lists containing 50+ elements, use `FlashList` (Shopify) instead of `FlatList` to recycle item views and prevent frame drops.
    3. **Mobile Layout Constraints:** Respect top/bottom safe areas (Dynamic Island, navigation bars). Use `KeyboardAvoidingView` with correct behavioral offsets to prevent input fields from being covered by the keyboard.
    4. **Touch Targets:** Verify all tap targets are at least 44×44pt. Use `hitSlop` to extend tap ranges on smaller UI icons.
    5. **Hermes Engine:** Optimize for Hermes bytecode compilation. Avoid `eval()`, dynamic `require()`, and Proxy objects.
    6. **Animations:** Use Reanimated for 60fps UI thread animations. Never animate on the JS thread for gestures or scroll-driven effects.

## 4. Android Native Development Best Practices
*   **Sub-skills:** `android-native-dev`
*   **Best Practices:**
    1. **Jetpack Compose:** Use declarative layout structures. Host state in ViewModels and hoist state parameters to keep UI composables stateless and testable.
    2. **Concurrency:** Execute async and IO actions on background threads using Kotlin Coroutines with appropriate dispatchers (`Dispatchers.IO` for storage/network).
    3. **Architecture:** Enforce Clean Architecture with a strict separation between UI layers (Composables, ViewModels), Domain layers (UseCases, Entities), and Data layers (Repositories, DB/API).
    4. **Material Design 3:** Use official M3 components and token scales for colors, typography shapes, and transitions.

## 5. Senior-Level Craftsmanship (Clean Code)
*   **Sub-skills:** `kaizen`, `ponytail`, `superpowers-review`
*   **Best Practices:**
    1. **Single Responsibility:** A module or function should do exactly one thing and do it completely. If a function exceeds 50 lines, evaluate splitting it.
    2. **Fail Fast:** Validate inputs and configurations early. Raise descriptive, operational exceptions immediately instead of allowing null values to propagate.
    3. **YAGNI (You Ain't Gonna Need It):** Do not write code, abstractions, or configurations for speculative future requirements. Keep code bases minimal.
    4. **Self-Documenting Code:** Write clean, intention-revealing variable and function names. Use comments only to explain *why* a specific tradeoff or limitation exists, not *what* the code does.
    5. **Continuous Improvement:** Apply `kaizen` principles for iterative code quality improvements. Use `superpowers-review` for structured severity-rated code audits.

## 6. Design System & UI Quality
*   **Sub-skills:** `ui-ux-pro-max`, `ckm:design-system`, `ckm:ui-styling`, `web-design-guidelines`, `web-artifacts-builder`, `theme-factory`
*   **Best Practices:**
    1. **Token Architecture:** Build three-layer design tokens (Primitive → Semantic → Component) and sync to CSS variables.
    2. **Accessibility:** WCAG 4.5:1 contrast, `aria-label` on icon buttons, visible focus rings, `prefers-reduced-motion` compliance.
    3. **Responsive:** Test at 375px / 768px / 1024px / 1440px breakpoints. No content hidden behind fixed elements.
    4. **Theming:** Use `theme-factory` for pre-set theme application. Support light/dark modes via token-driven contrast.

## 7. Validation & Linting
*   **Sub-skills:** `lint-and-validate`, `systematic-debugging`, `superpowers-tdd`
*   **Best Practices:**
    1. Run linters, type-checkers, and formatters after every code change.
    2. Use `systematic-debugging` for any test failure or unexpected behavior before proposing fixes.
    3. Enforce strict TypeScript mode with no `any` types unless explicitly justified.
    4. Apply `superpowers-tdd` test-driven development for all critical path logic (Red → Green → Refactor).

## 8. Code Review & Audit
*   **Sub-skills:** `superpowers-review`, `caveman-review`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`
*   **Best Practices:**
    1. Use `superpowers-review` for severity-rated code quality audits (Blocker / Major / Minor / Nit).
    2. Use `caveman-review` for terse, one-line-per-finding review feedback.
    3. Use `ponytail-review` to flag over-engineering, speculative abstractions, and unnecessary wrappers.
    4. Use `ponytail-audit` and `ponytail-debt` to scan for deferred technical debt and code bloat.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search`, `context7/get-library-docs`, and `perplexity-ask` for best-practice research and framework documentation.
*   **Memory:** Use `memory` MCP to persist best-practice decisions and code quality standards across conversations.
*   **Security:** Apply `ultimate-security-workflow` and `ultimate-security-audit-workflow` for security-first development practices.
*   **Documentation:** Use `ultimate-documentation-workflow` for maintaining best-practice guides and code standards documentation.
*   **Deployment:** Use `ultimate-deployment-workflow` for CI/CD pipeline best practices and pre-release validation.
