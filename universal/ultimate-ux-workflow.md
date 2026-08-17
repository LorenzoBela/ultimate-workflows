---
name: ultimate-ux-workflow
description: >
  Master workflow for User Experience (UX) audits, usability engineering, accessibility
  verification, and platform design compliance.
  Triggers on "ultimate ux workflow", "/ultimate-ux-workflow", or when conducting
  usability audits, reviewing interactive flows, or validating accessibility.
argument-hint: "[ux-audit | accessibility-check | component-flow]"
---

# Ultimate UX & Usability Workflow

This workflow drives comprehensive User Experience auditing, implementation, and verification. It ensures interfaces are accessible, responsive, navigable, performant, and genuinely delightful to use. This is the definitive quality gate for anything user-facing.

---

## Iron Laws

1. **Users Don't Read, They Scan.** Design for scanning: clear visual hierarchy, bold headings, short paragraphs, bullet points, and progressive disclosure.
2. **Feedback Is Non-Negotiable.** Every user action (tap, click, submit, swipe) must produce visible feedback within 100ms. If an operation takes >300ms, show a skeleton or progress indicator.
3. **Accessibility Is Not Optional.** WCAG 2.2 AA compliance is the minimum bar. Color is never the sole indicator of state. Every interactive element is keyboard-navigable.
4. **Layout Stability Is Sacred.** Cumulative Layout Shift (CLS) < 0.1. Reserve space for dynamic content, images, ads, and loading states. Skeleton dimensions must match final layout.
5. **Errors Are Opportunities.** Error states must tell the user: (1) what happened, (2) why it happened, and (3) what to do next. Never show raw error codes, stack traces, or blank screens.
6. **Form Friction is Conversion Death.** Minimize required fields, leverage native autofill, validate inputs inline, and preserve input state on error.

---

## Usability Heuristics Mapping (Nielsen's 10)

| Heuristic | Application in Code | Reject If |
|---|---|---|
| **Visibility of System Status** | Spinners, skeletons, progress bars, active tabs. | Long tasks with no feedback; dead buttons. |
| **Match Between System & Real World** | Plain language, natural categories, logical icons. | Tech jargon in user-facing copy; confusing glyphs. |
| **User Control & Freedom** | "Undo" buttons, cancel transitions, clear escapes. | Modal traps with no close button; un-cancellable actions. |
| **Consistency & Standards** | Shared typography scale, design tokens, standard UI. | Mix of custom scrollbars or distinct modal formats. |
| **Error Prevention** | Disabling invalid submit; date-pickers instead of input. | Letting user submit bad data, then throwing cryptic error. |
| **Recognition Rather than Recall** | Visible search history, persistence of state, hints. | Blank forms that clear themselves after a single validation error. |
| **Flexibility & Efficiency of Use** | Keyboard shortcuts, bulk actions, power-user flags. | Forcing power users to click through 5-step wizards. |
| **Aesthetic & Minimalist Design** | Generous padding, no noise, bento layout, clear space. | Crowding 50 inputs into a single viewport with tiny fonts. |
| **Help Users Recognize Errors** | Inline validation, red borders, actionable text hints. | Vague "Error 500" red banners; missing highlight on error fields. |
| **Help & Documentation** | Contextual tooltips, inline helpers, clean FAQs. | Missing labels on obscure mathematical configurations. |

---

## The 6-Phase UX Pipeline

### Phase 1: Information Architecture & Content Strategy
*   **Sub-skills:** `ui-ux-pro-max` (99 UX guidelines, 161 product types), `concise-planning`, `superpowers-brainstorm`
*   **Action:**
    1. Map the content hierarchy: define primary, secondary, and tertiary content zones for each page.
    2. Apply the **F-Pattern** (text-heavy pages) or **Z-Pattern** (landing pages) scanning model to place critical elements in natural eye-tracking positions.
    3. Define the information scent: every navigation label, button text, and link text must clearly communicate what the user will get when they interact.
    4. Establish a consistent vocabulary: use the same terms across the entire application (e.g., never mix "Settings" and "Preferences" for the same concept).
    5. Use `concise-planning` for atomic UX audit checklists.
    6. Use `superpowers-brainstorm` for evaluating alternative IA structures.

### Phase 2: Touch, Gesture & Interaction Design
*   **Sub-skills:** `ui-ux-pro-max`, `react-native-skills`, `react-native-best-practices`, `react-native-best-practices-callstack`, `android-native-dev`
*   **Action:**
    1. **Touch Targets:** Minimum dimensions enforced:

       | Platform | Minimum Size | Spacing Between |
       |---|---|---|
       | iOS (HIG) | 44×44pt | 8pt minimum |
       | Android (M3) | 48×48dp | 8dp minimum |
       | Web (WCAG) | 44×44px | 8px minimum (24px recommended) |

    2. **Interaction Feedback Matrix:**

       | Action | Feedback | Timing |
       |---|---|---|
       | Tap/Click | Scale down 0.97 + opacity 0.8 | < 80ms |
       | Hover (web) | Background tint shift | < 50ms |
       | Long press | Haptic + context menu | 300–500ms |
       | Swipe gesture | Rubber-band physics at edges | Real-time |
       | Submit/Save | Button → loading spinner → success check | Immediate → async |
       | Error | Shake animation + red border + inline message | < 100ms |

    3. **Gesture Safety:** Prevent gesture conflicts:
       *   No horizontal swipe gestures inside vertically scrollable lists.
       *   No nested scroll views without explicit `nestedScrollEnabled` control.
       *   Back-swipe (iOS) and edge gestures must never be hijacked by custom gestures.
    4. **Safe Areas:** Respect notch, Dynamic Island, status bar, home indicator using `env(safe-area-inset-*)` or `SafeAreaView`.
    5. Apply platform-specific skills for native gesture handling.

### Phase 3: Navigation & Flow Architecture
*   **Sub-skills:** `ui-ux-pro-max`, `next-best-practices`, `react-best-practices`, `composition-patterns`
*   **Action:**
    1. **Navigation Hierarchy Rules:**
       *   Top-level: Tabs (≤5 items), sidebar, or top nav. Always visible/accessible.
       *   Contextual: Breadcrumbs, back arrows, or "up" navigation within flows.
       *   Actions: FABs, toolbars, or context menus for operations within a view.
    2. **State Preservation:** When the user navigates back:
       *   ✅ Restore scroll position.
       *   ✅ Preserve filter/sort selections.
       *   ✅ Keep half-filled form inputs.
       *   ❌ Never force a full page reload or data refetch.
    3. **Progressive Disclosure:** Complex forms use multi-step wizards with:
       *   Clear step indicators (1/3, 2/3, 3/3) — not vague spinners.
       *   Back/Previous navigation at every step.
       *   Validation at each step before proceeding (fail-fast, not fail-at-end).
    4. **Loading State Hierarchy:**
       *   Global shell loads first (nav, sidebar always visible).
       *   Navigation always interactive — never blocked by content loading.
       *   Content areas load independently with per-section skeletons.
       *   **FORBIDDEN:** Blank screens, full-screen spinners for partial data, blocking navigation during loads.
    5. Apply `next-best-practices` for route-level code splitting, prefetching, and scroll restoration.

### Phase 4: Accessibility (a11y) — The Non-Negotiable Gate
*   **Sub-skills:** `ui-ux-pro-max`, `web-design-guidelines`, `ckm:ui-styling`
*   **MCP Tools:** `playwright` (browser_snapshot, browser_evaluate)
*   **Action:**
    1. **Color & Contrast:**

       | Element | Minimum Ratio | Tool to Verify |
       |---|---|---|
       | Body text (< 18px) | 4.5:1 | WebAIM Contrast Checker |
       | Large text (≥ 18px bold / ≥ 24px) | 3:1 | axe-core |
       | UI components (borders, icons) | 3:1 | Manual check |
       | Focus indicators | 3:1 against adjacent | Visual inspection |

    2. **Semantic HTML & ARIA:**
       *   Use correct semantic elements: `<button>` for actions, `<a>` for navigation, `<nav>` for nav blocks, `<main>` for primary content.
       *   One `<h1>` per page. Heading levels descend sequentially (h1 → h2 → h3, never skip levels).
       *   Icon-only buttons MUST have `aria-label`. Decorative icons get `aria-hidden="true"`.
       *   Form inputs MUST have associated `<label>` elements (not just placeholders).
       *   Use `role`, `aria-expanded`, `aria-controls`, `aria-live` for dynamic content regions.
    3. **Keyboard Navigation:**
       *   All interactive elements reachable via Tab key.
       *   Visible focus rings (never `outline: none` without replacement).
       *   Escape closes modals and dropdowns, returning focus to the trigger.
       *   Enter/Space activates buttons and checkboxes.
       *   Arrow keys navigate within composite widgets (tabs, menus, listboxes).
    4. **Motion Safety:**
       *   ALL animations wrapped in `@media (prefers-reduced-motion: reduce)`.
       *   Provide instant state changes as fallback.
       *   No flashing content (>3 flashes per second — WCAG 2.3.1).
    5. Use `playwright/browser_evaluate` for programmatic axe-core accessibility audits.
    6. Apply `ckm:ui-styling` for shadcn/ui Radix primitives with built-in ARIA support.

### Phase 5: Perceived Performance & Loading States
*   **Sub-skills:** `ckm:design-system`, `react-best-practices`, `next-best-practices`
*   **Action:**
    1. **The Skeleton Law:** If content takes >300ms to load, show a skeleton screen — not a spinner. Skeletons MUST:
       *   Match the exact dimensions of the final rendered content.
       *   Reflect content hierarchy (title skeleton wider than subtitle skeleton).
       *   Render instantly (< 16ms, before any data fetch begins).
       *   Shimmer left-to-right with a subtle gradient animation.
    2. **Optimistic UI:** For highly-likely-to-succeed actions (toggling favorites, sending messages):
       *   Update the UI immediately, before the API response.
       *   Show visually distinct "pending" state (subtle opacity or pulse).
       *   Auto-rollback if the API responds with an error.
       *   Only use for actions where rollback is trivial and non-destructive.
    3. **Streaming & Progressive Rendering:**
       *   Above-the-fold content streams first.
       *   Below-the-fold content deferred via `Suspense` boundaries.
       *   Independent data blocks load independently (no waterfall fetching).
    4. **Layout Stability (CLS Prevention):**
       *   Reserve explicit `width`/`height` on all images and media.
       *   Skeletons match final content dimensions exactly.
       *   Never inject content above the current viewport position.
       *   Fonts use `font-display: swap` with `size-adjust` for metric compatibility.

### Phase 6: Error, Empty & Edge States
*   **Sub-skills:** `ui-ux-pro-max`, `systematic-debugging`, `ckm:banner-design`
*   **Action:**
    1. **Error State Design (Every error must answer 3 questions):**
       *   **What happened?** — Clear, human-readable title (not "Error 500" or "Something went wrong").
       *   **Why?** — Brief explanation ("Your session expired" / "The server is temporarily unavailable").
       *   **What to do?** — Actionable CTA ("Sign in again" / "Retry" / "Go back").
    2. **Empty State Design:**
       *   Provide an illustration or icon (use `generate_image` or `ckm:banner-design`).
       *   Include a primary action button ("Create your first project" / "Add an item").
       *   Never show a blank white screen with no guidance.
    3. **Edge Cases Checklist:**
       *   [ ] What happens with 0 items? (Empty state)
       *   [ ] What happens with 1 item? (Singular copy: "1 result" not "1 results")
       *   [ ] What happens with 1,000+ items? (Pagination, virtual scrolling, or "Load more")
       *   [ ] What happens with extremely long text? (Truncation with `text-overflow: ellipsis`)
       *   [ ] What happens offline? ("You're offline" banner with cached content below)
       *   [ ] What happens on slow 3G? (Skeletons visible for 3–10 seconds gracefully)
    4. **Network Resilience:**
       *   Graceful error states on network failure — never crash or show raw errors.
       *   Retry buttons visible with exponential backoff.
       *   Clear "You're offline" messaging when connectivity drops.

---

## Form UX Optimization Checklist

- [ ] Focus shifts logically down the form elements.
- [ ] Autofill types match constraints (`autocomplete="email"`, `autocomplete="tel"`).
- [ ] No fields clear themselves when validation fails.
- [ ] Focus remains on the errored input field upon submission validation.
- [ ] Submitting a form displays a loading indicator and disables the CTA button to prevent double-submits.
- [ ] Keyboards displayed on mobile screens match fields (`inputmode="numeric"`, `inputmode="email"`).
- [ ] Text fields offer native autocorrect management (`autocorrect="off"`, `autocapitalize="none"` where necessary).

---

## Dynamic Skeleton UI Boilerplate Template

```html
<!-- Skeleton Wrapper representing a dynamic dashboard card -->
<div class="p-6 bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl space-y-4 shadow-sm w-[350px]">
  <div class="flex items-center space-x-4">
    <!-- Circle Icon Skeleton -->
    <div class="w-12 h-12 bg-zinc-200 dark:bg-zinc-700 rounded-full animate-pulse"></div>
    <div class="space-y-2 flex-1">
      <!-- Title Skeleton -->
      <div class="h-4 bg-zinc-200 dark:bg-zinc-700 rounded-md w-3/4 animate-pulse"></div>
      <!-- Subtitle Skeleton -->
      <div class="h-3 bg-zinc-200 dark:bg-zinc-700 rounded-md w-1/2 animate-pulse"></div>
    </div>
  </div>
  <!-- Body Content Line Skeletons -->
  <div class="space-y-2">
    <div class="h-3 bg-zinc-200 dark:bg-zinc-700 rounded-md w-full animate-pulse"></div>
    <div class="h-3 bg-zinc-200 dark:bg-zinc-700 rounded-md w-5/6 animate-pulse"></div>
  </div>
</div>
```

---

## UX Copywriting & Microcopy Guidelines

*   **Error Messaging:** Use clear, non-guilt-inducing, helpful text.
    *   *Bad:* "Invalid Input: Code must be 6 digits!" (Aggressive, exclamation point)
    *   *Good:* "Please enter a 6-digit confirmation code. You can find this in your SMS message history."
*   **Call-to-Action (CTA):** Action-oriented verbs indicating value.
    *   *Bad:* "Submit" / "Click here" (Vague, lacks scent)
    *   *Good:* "Start Free Trial" / "Save Changes" / "Complete Delivery"
*   **Loading State Copy:** Make waiting interactive and clear. Differentiate static text from dynamic loops.
    *   *Static:* "Loading data..." (Generic)
    *   *Dynamic:* "Verifying security keys..." → "Connecting to box GPS..." → "Syncing local storage..."

---

## Accessibility Bug Signatures & Code Fixes

### 1. Keyboard Navigable Trigger Elements
*   **Bad Code:**
    ```jsx
    // Invisible to tab index and keyboard space/enter activation
    <div onClick={toggleMenu} className="cursor-pointer">
      <MenuIcon />
    </div>
    ```
*   **Good Code:**
    ```jsx
    <button 
      onClick={toggleMenu} 
      aria-label="Toggle Navigation Menu"
      aria-expanded={isOpen}
      className="focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 rounded"
    >
      <MenuIcon aria-hidden="true" />
    </button>
    ```

### 2. Modal Focus Trap Pattern
*   When a modal is opened:
    1. Active keyboard focus MUST be shifted into the modal.
    2. Focus must remain trapped inside the modal (pressing Tab at the last item wraps to the first).
    3. Pressing `Escape` must close the modal and return focus to the trigger element that opened it.

---

## Programmatic Accessibility E2E Test (Playwright / axe-core)

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Compliance Audit', () => {
  test('Page meets WCAG 2.2 AA standards', async ({ page }) => {
    await page.goto('/dashboard');
    
    // Wait for dynamic hydration to settle
    await page.waitForSelector('main');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
```

---

## Touch Target Expansion Patterns

When styling small interactive items (e.g., close buttons, small toggles, arrow links), the visible element may be small, but the interactive tap surface must meet minimum requirements (44px/48px).

### 1. CSS Pseudo-Element Expansion (Web)
```css
/* Visible button is 16x16px, but click area is expanded to 44x44px */
.btn-close-small {
  position: relative;
  width: 16px;
  height: 16px;
}

.btn-close-small::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 44px;
  height: 44px;
  min-width: 44px;
  min-height: 44px;
}
```

### 2. React Native `hitSlop` Configuration (Mobile)
```tsx
// Explicitly define tap padding in pixels around the visible boundary
<TouchableOpacity
  onPress={handleClose}
  hitSlop={{ top: 14, bottom: 14, left: 14, right: 14 }}
  style={{ width: 16, height: 16 }}
>
  <CloseIcon />
</TouchableOpacity>
```

---

## Brand-Integrated UX Patterns (Quick Reference)

| Brand Archetype | Canvas | CTA Shape | Animation Style | Card Radius |
|---|---|---|---|---|
| Apple (Photography-first) | White alternating dark | Pill, Action Blue | Gentle parallax | 16–20px |
| Linear (Developer luxury) | Near-black #010102 | Charcoal pill | Subtle fade-in | 8px |
| Stripe (Fintech editorial) | Deep navy | Pill, indigo | Mesh gradient hero | 8–12px |
| Airbnb (Warm marketplace) | White | Pill, Rausch pink | Card hover lift | 14–16px |
| Vercel (Developer platform) | Near-white | Black pill | Mesh gradient hero | 8px |
| Notion (Workspace) | White | Purple pill, rounded | Slide-in panels | 8px |
| Revolut (Fintech bold) | Black | Cobalt-violet pill | Product mockup reveals | 12–20px |

---

## Anti-Patterns (Reject These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| Full-screen spinner for partial data | Blocks all interaction, feels frozen | Per-section skeleton screens |
| `placeholder` as the only label | Disappears on input, accessibility failure | Always pair with visible `<label>` |
| Color-only error indication | Inaccessible to colorblind users | Add icon + text alongside color |
| Modal on page load | Interrupts task, hostile UX | Use inline banners or toast notifications |
| Infinite scroll without "back to top" | User loses position, frustrating | Add floating "back to top" button |
| Custom scrollbars | Inconsistent cross-platform behavior | Use native scrollbars, style minimally |
| Alert/confirm browser dialogs | Ugly, blocks thread, can't style | Use custom modal with accessible focus trap |

---

## Sub-Skill Checklists & Reference Templates

### 1. Touch & Layout Stability on Mobile (`react-native-skills`)
*   **Virtualization Priority:** Enforce `FlashList` for any list handling more than 50 entries to stabilize frame rates.
*   **Gestures:** Use Reanimated worklets and the `GestureDetector` harness instead of JS thread responders.
*   **Measure Traps:** Avoid manual `measure()` calls in layouts. Use `onLayout` listener callbacks to prevent thread blocks.

### 2. React UI Performance (`react-best-practices` & `composition-patterns`)
*   **Derived UI State:** Never use `useEffect` to synchronise local UI state changes. Derive UI boolean values directly during execution to avoid layout-flickers.
*   **Compound UI Contexts:** Avoid building complex configuration properties for UI components; separate them into semantic subcomponents (e.g. `<Modal.Header>`, `<Modal.Body>`).

### 3. Accessibility Audit Checklist (`web-design-guidelines`)
*   Validate visual contrast ratios across high-priority elements.
*   Verify that interactive components trap keyboard focus correctly when modals/dropdowns are open.

### 4. TTI & Startup Optimization on Mobile (`react-native-best-practices`)
*   **Defer Non-Essential SDKs:** Do not initialize heavy analytics, logging, or third-party tracking scripts during the initial render loop. Defer them using task schedulers (`InteractionManager.runAfterInteractions` or `setTimeout`) to optimize Time-To-Interactive (TTI).
*   **State Hydration:** Display skeletal fallbacks or cached state on first render to prevent blank layouts.

### 5. Navigation Pre-Fetching & State Retention (`next-best-practices`)
*   **Route Prefetching:** Always prefetch pages likely to be visited using `<Link prefetch={true}>` or programmatic prefetching on hover to minimize route transition delays.
*   **Scroll & View State:** Ensure route changes preserve focus states and scroll positions. Return views to their top-most coordinate unless returning to a list, in which case coordinate positions must be cached and restored.

### 6. React Native Reanimated Gestures (`react-native-skills`)
*   **Performance-Safe Gestures:** Animate elements exclusively using Reanimated's UI thread values:
    ```typescript
    import { Gesture, GestureDetector } from 'react-native-gesture-handler';
    import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';
    
    export function SwipeableCard() {
      const translationX = useSharedValue(0);
      
      const panGesture = Gesture.Pan()
        .onChange((event) => {
          translationX.value = event.translationX;
        })
        .onEnd(() => {
          translationX.value = withSpring(0);
        });
        
      const animatedStyle = useAnimatedStyle(() => ({
        transform: [{ translateX: translationX.value }],
      }));
      
      return (
        <GestureDetector gesture={panGesture}>
          <Animated.View style={[animatedStyle, { width: 100, height: 100, backgroundColor: 'blue' }]} />
        </GestureDetector>
      );
    }
    ```

### 7. WCAG Keyboard Focus Trap (`web-design-guidelines`)
*   **Focus Trap Hook:** Prevent keyboard focus from leaking outside modal boundaries:
    ```typescript
    import { useEffect, useRef } from 'react';
    
    export function useFocusTrap() {
      const elRef = useRef<HTMLDivElement>(null);
      
      useEffect(() => {
        const el = elRef.current;
        if (!el) return;
        
        const focusable = el.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        const first = focusable[0] as HTMLElement;
        const last = focusable[focusable.length - 1] as HTMLElement;
        
        const handleKeyDown = (e: KeyboardEvent) => {
          if (e.key !== 'Tab') return;
          if (e.shiftKey) {
            if (document.activeElement === first) {
              last.focus();
              e.preventDefault();
            }
          } else {
            if (document.activeElement === last) {
              first.focus();
              e.preventDefault();
            }
          }
        };
        
        el.addEventListener('keydown', handleKeyDown);
        return () => el.removeEventListener('keydown', handleKeyDown);
      }, []);
      
      return elRef;
    }
    ```

---

## Cross-Cutting Concerns
*   **Frontend:** Chain with `ultimate-frontend-workflow` for full implementation after UX specification.
*   **Research:** Use `tavily-search`, `perplexity-ask`, and `context7/get-library-docs` for WCAG 2.2 standards, platform HIG guidelines, and UX pattern libraries.
*   **Testing:** Use `playwright` MCP for E2E usability testing, screenshot capture, and visual regression across breakpoints.
*   **Memory:** Use `memory` MCP to persist UX audit findings, accessibility issues, and interaction patterns across conversations.
*   **Documentation:** Use `ultimate-documentation-workflow` and `docx` for formal UX audit reports.
*   **Presentation:** Use `ckm:slides` for stakeholder-facing UX review presentations.
*   **Brand:** Reference `Awesome-Design-MD` (all 61 brands) and `ckm:brand` for brand-aligned UX patterns.
*   **Design Tokens:** Use `ckm:design-system` and `theme-factory` for systematic visual quality across components.
