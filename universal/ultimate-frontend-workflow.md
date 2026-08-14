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

# Ultimate Frontend Workflow

This workflow coordinates and executes premium frontend engineering by integrating brand-identity, design token systems, copywriting, assets, styling, animations, and UX validation. It is the definitive pipeline for producing interfaces that feel **alive, premium, and polished**.

---

## Iron Laws

1. **No Placeholder Content.** Never use Lorem ipsum, Unsplash hotlinks, placehold.co, or Picsum URLs. Every image is generated locally via local asset generation or custom SVG. Every copy line is written intentionally.
2. **No Hardcoded Colors.** Zero hex/rgb values in JSX/TSX markup. All color values reference semantic design tokens from CSS variables.
3. **GPU-Only Animations.** Only animate `transform`, `opacity`, `filter`, and `clip-path`. Never animate `width`, `height`, `margin`, `padding`, or any layout-reflowing property.
4. **Server First.** Default all components to React Server Components (RSC). Use `"use client"` only on leaf-level interactive components (inputs, buttons with state, hooks).
5. **Token-Driven Everything.** Spacing, typography, shadows, radii, and colors must come from the design token system. Ad-hoc utility values are rejected.
6. **Zero Cumulative Layout Shift (CLS).** Dimensions must be explicitly defined on all media elements (images, video, iframes) and dynamic component containers.
7. **Strict Anti-Slop Enforcement.** Every component, layout, and style must pass the **Anti-Slop Rulesheet (The 50 Banned AI Tells)** before shipping. Zero AI defaults or vibecoded boilerplate allowed.
8. **Leaf-Level RSC Boundaries.** 100% of routes and layouts must default to React Server Components. `'use client'` is strictly prohibited on route pages, sections, or containers—it may only be declared at leaf-node interactive controls.
9. **Core Web Vitals Invariants.** Target LCP ≤ 2.2s, INP ≤ 150ms, and CLS ≤ 0.05 on mobile 4G. Initial JS bundle must stay under 100 KB gzipped.
10. **WCAG 2.2 Level AA Non-Negotiable.** 100% keyboard navigable, zero focus traps, mandatory `focus-visible` rings, and 4.5:1 text contrast ratio enforced at CI/CD.

---

## Industry-Grade Standards: World-Class Engineering Specs (Linear, Vercel, Stripe)

### 1. The High-Bandwidth Control Surface Philosophy
World-class engineering tools (Linear, Vercel, Stripe) prioritize information density, mathematical precision, and instant responsiveness over decorative fluff.

- **Micro-Borders:** Use barely perceptible borders (`rgba(255, 255, 255, 0.08)` on dark, `rgba(0, 0, 0, 0.08)` on light) to delineate structural regions without adding visual weight.
- **Tabular Data:** Use `font-variant-numeric: tabular-nums tnum` and `font-feature-settings: "cv05", "cv11"` on all numbers, tables, and metric readouts to guarantee zero horizontal shifting during updates.
- **Generous Pacing vs. High Density:**
  - *Marketing Canvas:* Section vertical padding set to `96px–128px` (`py-24` to `py-32`) for expansive confidence.
  - *App/Dashboard Surface:* Compact `12px–24px` spacing for high-density information flow.

### 2. Rendering & State Machine Architecture
- **Server Components by Default:** Fetch data inside Server Components. Never use `useEffect` for client-side data fetching—use TanStack Query or Server Actions for mutations.
- **Partial Prerendering (PPR) & Streaming:** Prerender static layouts at build time; stream dynamic user data via Suspense boundaries wrapped around logical section chunks (e.g., stats row, user feed), avoiding "popcorn" loading pops.
- **Pixel-Matched Skeletons:** Skeleton placeholders must match the exact pixel height and aspect ratio of loaded content to guarantee zero Cumulative Layout Shift (`CLS ≤ 0.05`).
- **Complete Component State Matrix:** Every component must explicitly render all 7 states:
  `Default → Hover → Focus-Visible → Active/Pressed → Loading (Skeleton) → Disabled → Error (With Retry Boundary)`.

### 3. Typography & Micro-Grid Alignment
- **Font Pairing Restraint:** Limit brand systems to a maximum of 2 typeface families.
- **Optical Display Tuning:** Display headlines use tight negative tracking (`-0.02em` to `-0.04em`) with `text-wrap: balance`. Body prose uses standard tracking with `text-wrap: pretty`.
- **Fluid Typography:** Use `clamp()` for responsive display titles instead of abrupt breakpoint font-size jumps:
  ```css
  --text-hero: clamp(2.5rem, 5vw + 1rem, 5.5rem);
  ```

---

## Anti-Slop Rulesheet: The 50 Banned AI-Generated Tells

Any component, layout, or style exhibiting these patterns is rejected as generic AI output ("vibecoded slop").

### Category 1: Color & Palette Bans (1–8)
1. **BAN: AI Blue-to-Indigo Gradient.** `bg-gradient-to-r from-blue-600 to-indigo-700` (or `violet-500`/`blue-500` hue band 200°–290°) is forbidden as a default hero gradient.
2. **BAN: VibeCode Purple Fill.** Filled CTA buttons using default `indigo-600` or violet hues (HSL 240°–295°, ≥35% sat) without a deliberate brand system.
3. **BAN: Gradient Headline Text.** `bg-clip-text text-transparent bg-gradient-to-r` on H1 headlines.
4. **BAN: Colored Ambient Shadow Blur.** Glowing `box-shadow` with ≥24px blur matching the accent color.
5. **BAN: Unmodified Blue Pill Badges.** `bg-blue-100 text-blue-800` or `bg-purple-100 text-purple-800` status chips.
6. **BAN: Pure White/Black Monochromes.** `#ffffff` canvas with `#000000` text without custom warm/cool off-white or off-black scale.
7. **BAN: Secondary AI Default Palette.** Cream `#faf8f4` canvas + sage accent + serif headline (the secondary prompt-engineered AI attractor).
8. **BAN: Low-Contrast Grey Body Text.** Washed-out `gray-400`/`gray-500` text failing WCAG AA (4.5:1) on light surfaces.

### Category 2: Typography & Hierarchy Bans (9–15)
9. **BAN: Default Inter/Geist Monoculture.** Using `Inter`, `Geist`, or `Space Grotesk` as the single font family for 100% of UI copy without a distinct secondary pairing.
10. **BAN: Single Italic Serif Accent.** Placing a single italic word set in `Instrument Serif` inside a sans-serif headline.
11. **BAN: Crushed Display Tracking.** Setting display headlines to tighter than `-0.05em` tracking (`tracking-tight` blindly applied).
12. **BAN: Excessive Body Tracking.** Setting body prose letter-spacing above `+0.05em` (`tracking-wide`).
13. **BAN: Missing Text-Wrap Controls.** Omitting `text-wrap: balance` on display headings and `text-wrap: pretty` on paragraphs.
14. **BAN: Flat Typographic Scale.** Display-to-body font size ratio lower than 2× or having fewer than 3 distinct hierarchy scale steps.
15. **BAN: Uniform Line-Height Defaults.** Applying `leading-normal` or fixed line-heights across display, body, and microcopy indiscriminately.

### Category 3: Layout & Structure Bans (16–24)
16. **BAN: Canonical Section Sequence.** Following `Nav → Hero → 3-Card Features → Testimonials → 3-Tier Pricing → FAQ Accordion → Footer`.
17. **BAN: Centered Hero Boilerplate.** `flex flex-col items-center justify-center text-center py-24` as the default hero stack.
18. **BAN: Floating Eyebrow Pill.** Pill floating above H1 containing `"✨ New: [Feature]"` or `"Now in public beta"`.
19. **BAN: Symmetrical 3-Card Grid.** `grid grid-cols-1 md:grid-cols-3 gap-6` as the feature layout. Use asymmetric grids, `<dl>`, or split layouts instead.
20. **BAN: Rigid Container Wrapper.** Uniformly applying `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` to every section without full-bleed variations.
21. **BAN: Highlighted Middle Pricing Tier.** 3-column pricing card row with the center card offset upwards and highlighted in gradient.
22. **BAN: Generic Bento Grid Wall.** Apple-keynote style bento wall filled with fake stats and generic Lucide icons.
23. **BAN: Standard 4-Column Footer.** Footer partitioned into `Product | Company | Resources | Legal` with identical link lists.
24. **BAN: Uniform Section Padding.** Applying identical `py-20` or `py-24` padding to every section without visual rhythm changes.

### Category 4: Component Primitives Bans (25–33)
25. **BAN: Unmodified shadcn/ui Variables.** Unaltered `--radius: 0.5rem` and `hsl(214.3 31.8% 91.4%)` input borders.
26. **BAN: Universal `rounded-2xl`.** 16px radius applied blindly to buttons, cards, images, badges, inputs, and modals alike.
27. **BAN: Glassmorphic Sticky Header.** Header styled with `backdrop-blur-md bg-background/70 border-b`.
28. **BAN: Terminal Window Mockup.** Mock terminal window with red/yellow/green dots displaying static bash output in the hero.
29. **BAN: Colored Border Accent Stripe.** Cards with a thick chromatic 2px border on top or left edge only.
30. **BAN: Letter-Initial Gradient Avatars.** Testimonial circular avatars containing single capital initial letters on gradient backgrounds.
31. **BAN: Tinted Circle Icon Containers.** Lucide icons placed inside pastel circular containers (`bg-primary/10 text-primary p-3 rounded-full`).
32. **BAN: Emoji-as-Icons.** Raw emojis (`✨`, `🚀`, `⚡`, `🔒`) used directly in JSX as UI icon replacements.
33. **BAN: Schema-less FAQ Accordion.** Generic Radix accordion FAQ missing JSON-LD structured schema markup.

### Category 5: Motion & Micro-interaction Bans (34–40)
34. **BAN: Fade-Up Intersection Observer.** `opacity: 0, y: 20` to `opacity: 1, y: 0` fired indiscriminately on scroll for every section.
35. **BAN: Pricing Card Perma-Pulse.** `animate-pulse` applied to pricing card CTA buttons or highlight badges.
36. **BAN: Linear Stagger Delays.** Fixed linear delay increments (`delay-100`, `delay-200`, `delay-300`) on grid children.
37. **BAN: Hover-Only States.** Interactive elements with hover effects but missing `:active`, `:focus-visible`, or pressed feedback.
38. **BAN: Blanket Ease Transitions.** Overused `transition-all duration-300 ease-in-out` on all interactive surfaces.
39. **BAN: Aurora Background Blobs.** Blurred radial/conic gradient background blobs (`filter blur-3xl opacity-30`) behind heroes.
40. **BAN: Masked Background Grid Lines.** SVG grid pattern overlay with `mask-image: radial-gradient`.

### Category 6: Copywriting & Marketing Bans (41–45)
41. **BAN: Buzzword Headline Formulas.** Headlines using `"X, effortlessly"`, `"Supercharge your Y"`, or `"The ultimate platform for Z"`.
42. **BAN: AI Copywriting Vocabulary.** Prose containing `"delve"`, `"seamless"`, `"robust"`, `"testament"`, or `"elevate"`.
43. **BAN: Excessive Em-Dashes.** Unspaced or overused em-dashes (`—`) in body text and feature bullet lists.
44. **BAN: Antithesis Subheadings.** Subtitles formatted as `"Not just X, it's Y"`.
45. **BAN: Generic CTA Buttons.** Button labels set to `"Get Started"`, `"Start Free Trial"`, or `"Book a Demo"`.

### Category 7: Code & Infrastructure Bans (46–50)
46. **BAN: Stock shadcn Component Tree.** Unmodified `@/components/ui/` primitive exports (`button.tsx`, `card.tsx`).
47. **BAN: Default `cn()` Helper.** `@/lib/utils.ts` exporting standard `clsx` + `tailwind-merge` untouched from starter kit.
48. **BAN: Arbitrary Tailwind Hex Overload.** Inlining arbitrary hex classes (`bg-[#0f172a]`, `w-[350px]`) instead of design tokens.
49. **BAN: AI Builder Loader Script Tags.** Injected head scripts from `gpteng.co`, `framerusercontent.com`, or `tempo` CDNs.
50. **BAN: Unhandled Framework Boundaries.** Missing custom Next.js `error.tsx`, `loading.tsx` skeletons, or custom OpenGraph meta tags.

---

## The 8-Phase Pipeline

### Phase 1: Brand & Aesthetic Alignment
*   **Action:**
    1. Define the brand voice, tone, and visual direction. Choose a brand archetype from the 61 available:
       *   **Fintech/SaaS:** `design-md-stripe` (editorial gradient mesh), `design-md-revolut` (cobalt-violet + heavy Aeonik), `design-md-wise` (lime-green + weight-900 display).
       *   **Developer Tools:** `design-md-linear.app` (near-black + lavender accent), `design-md-vercel` (black-ink + mesh gradient hero), `design-md-cursor` (warm-cream + orange CTA).
       *   **Photography-First:** `design-md-apple` (edge-to-edge tiles, SF Pro Display), `design-md-ferrari` (cinematic Rosso Corsa), `design-md-nike` (towering Futura uppercase).
       *   **AI/ML Brands:** `design-md-claude` (warm cream + coral CTAs), `design-md-cohere` (stark white + green-black bands), `design-md-mistral.ai` (sunset gradients + cream).
       *   **Enterprise:** `design-md-ibm` (Carbon Design flat squares, IBM Blue), `design-md-hashicorp` (per-product accent tokens), `design-md-nvidia` (NVIDIA Green angular).
       *   **Consumer/Marketplace:** `design-md-airbnb` (Rausch pink, Cereal VF), `design-md-uber` (geometric sans, black/white duet), `design-md-pinterest` (masonry grid, warm cream).
    2. Read the selected SKILL.md brand file before writing any CSS. Extract: canvas color, display typeface + weight, body typeface, CTA shape + color, card radius, signature decoration.
    3. Synchronize brand guidelines into `docs/brand-guidelines.md` for team reference.
    4. Choose a distinctive typography pair from the brand file. Never default to Inter or system fonts unless the brand explicitly specifies it.

### Phase 2: Design Token Architecture & CSS Variables
*   **Action:**
    1. Build a **three-layer token hierarchy:**
       *   **Primitive tokens:** Raw values (`--color-blue-500: #3b82f6`, `--space-4: 16px`, `--radius-md: 8px`).
       *   **Semantic tokens:** Intent-mapped (`--color-primary: var(--color-blue-500)`, `--space-section: var(--space-12)`).
       *   **Component tokens:** Scoped (`--button-bg: var(--color-primary)`, `--card-radius: var(--radius-md)`).
    2. Write token definitions to `assets/design-tokens.json` and sync to CSS variables in `assets/design-tokens.css`.
    3. Enforce the spacing scale: `4px → 8px → 12px → 16px → 24px → 32px → 48px → 64px → 80px → 96px → 128px`. No arbitrary values.
    4. Define elevation/shadow scale: `--shadow-xs` through `--shadow-2xl` with consistent blur-spread ratios.
    5. Design light and dark themes **simultaneously**—token values flip, component code stays unchanged.
    6. Use Design Theme Presets for rapid application of 10 pre-set themes (Vercel, Linear, Stripe, etc.).
    7. Apply Modern Component Styling for shadcn/ui Radix-based component theming with Tailwind CSS integration.

### Phase 3: Typography & Iconography System
*   **Action:**
    1. Select font pairing from UI/UX Design Intelligence's 57 curated pairings or from the chosen brand SKILL.md.
    2. Define the type scale: `--text-xs: 12px`, `--text-sm: 14px`, `--text-base: 16px`, `--text-lg: 18px`, `--text-xl: 20px`, `--text-2xl: 24px`, `--text-3xl: 30px`, `--text-4xl: 36px`, `--text-5xl: 48px`, `--text-6xl: 60px`, `--text-7xl: 72px`, `--text-8xl: 96px`.
    3. Set line-heights: display headlines 1.1–1.2, body text 1.5–1.7, UI labels 1.3–1.4.
    4. Set letter-spacing: display headlines -0.02em to -0.04em (tight), body 0em (normal), uppercase labels +0.05em to +0.1em (wide).
    5. Load fonts via `next/font` (Next.js) or `@font-face` with `font-display: swap` for zero-CLS loading.
    6. **Icon system:** Use a single, consistent icon library (Lucide, Phosphor, Radix Icons, or Heroicons). Never mix icon sets. Never use emojis as structural UI icons.
    7. Ensure icon baseline alignment with adjacent text using `vertical-align` or flex centering.

### Phase 4: Copywriting & Asset Generation
*   **Action:**
    1. Write persuasive, intentional copy using proven frameworks:
       *   **AIDA:** Attention → Interest → Desire → Action (best for landing pages).
       *   **PAS:** Problem → Agitate → Solution (best for product explainers).
       *   **FAB:** Features → Advantages → Benefits (best for pricing/feature grids).
       *   **BAB:** Before → After → Bridge (best for transformation narratives).
    2. Generate all visual assets locally using local asset generation or custom SVG tool. Save to `public/images/` or `assets/`.
    3. For hero banners and social graphics, use Hero Graphic & Banner Design (22 styles: minimalist, gradient, bold typography, photo-based, geometric, glassmorphism, 3D, neon, duotone, editorial, collage, retro, illustrated).
    4. For presentation decks, use Data Presentation & Deck Layouts with Chart.js data visualizations.
    5. Every image element must have descriptive `alt` text. Decorative images get `alt=""` and `aria-hidden="true"`.

### Phase 5: Layout Engineering & Component Architecture
*   **Action:**
    1. **Layout Systems:** Go beyond simple card rows. Use:
       *   **Bento Grids:** Asymmetric tile layouts with varied span sizes (2×1, 1×2, 2×2).
       *   **Split Screens:** 50/50 or 60/40 content-image panels.
       *   **Masonry:** Pinterest-style variable-height column grids.
       *   **Overlap/Stack:** Layered cards with z-index depth and offset positioning.
       *   **Full-Bleed Sections:** Edge-to-edge color bands alternating light/dark canvases.
    2. **Component Patterns:** Apply `Component Composition Patterns`:
       *   **Compound Components:** Shared context for complex children (e.g., `<Tabs>`, `<Accordion>`).
       *   **Render Props:** Delegate rendering decisions to consumers.
       *   **Polymorphic Components:** `as` prop for semantic HTML flexibility.
       *   **Slot Pattern:** Named children for flexible content injection.
    3. **Visual Details:** Layer premium surface effects:
       *   Glassmorphism: `backdrop-filter: blur(16px)` + translucent backgrounds.
       *   Noise Textures: Subtle SVG noise overlays for depth.
       *   Gradient Meshes: Multi-stop radial/conic gradients as atmospheric backgrounds.
       *   Liquid Glass: iOS-style frosted glass with saturation boosts.
    4. Use Next.js App Router Best Practices for RSC boundaries, `generateMetadata`, and route-level code splitting.
    5. Use Modular UI Component Architecture for complex multi-component artifacts with state management and routing.

### Phase 6: Fluid Motion & Animation System
*   **Action:**
    1. **Animation Tool Decision Matrix:**

       | Use Case | Tool | Why |
       |---|---|---|
       | Enter/exit/layout | Framer Motion | `AnimatePresence`, layout animations |
       | Scroll-pinned/scrubbed | GSAP ScrollTrigger | Timeline precision, pin control |
       | Hover/focus/press | CSS Transitions | Zero JS overhead, GPU-accelerated |
       | Parallax layers | CSS `transform: translateZ()` | Native 3D perspective, no library |
       | Spring physics | Framer Motion `spring` | Perceptually natural easing |
       | Complex sequences | GSAP Timeline | Frame-level control, callbacks |

    2. **NEVER** mix Framer Motion and GSAP in the same component. Pick one per component boundary.
    3. **GPU-only rule:** Animate only `transform`, `opacity`, `filter`, `clip-path`. Layout-reflowing properties (`width`, `height`, `margin`, `padding`, `top`, `left`) cause jank.
    4. **Timing guidelines:**
       *   Micro-interactions (hover, press): 80–150ms.
       *   Element transitions (enter, exit): 150–300ms.
       *   Page transitions: 200–400ms.
       *   Scroll-driven: tied to scroll position, no fixed duration.
    5. **Reduced motion:** Wrap ALL animations in `prefers-reduced-motion` media query. Provide instant state changes as fallback.
    6. **Cleanup:** Every GSAP `useEffect` must return `() => ctx.revert()`. Every Intersection Observer must `disconnect()`.
    7. For React Native: use Reanimated for 60fps UI-thread animations. Never animate on the JS thread for gestures.

### Phase 7: Responsive & Cross-Platform Engineering
*   **Action:**
    1. **Breakpoint system:** Design mobile-first, then scale up:
       *   `375px` — Mobile (iPhone SE baseline)
       *   `428px` — Large mobile (iPhone 14 Pro Max)
       *   `768px` — Tablet portrait
       *   `1024px` — Tablet landscape / Small desktop
       *   `1280px` — Desktop
       *   `1440px` — Wide desktop
       *   `1920px` — Ultra-wide
    2. **Container queries:** Use CSS container queries (`@container`) for component-level responsiveness when parent width matters more than viewport width.
    3. **Touch targets:** Minimum 44×44pt (iOS) / 48×48dp (Android). Extend small icons with `hitSlop` or padding.
    4. **Safe areas:** Respect notch, Dynamic Island, status bar, home indicator using `env(safe-area-inset-*)`.
    5. For React Native: apply `React Native Architecture Patterns` and `React Native Thread Optimization`.
    6. For Android Native: apply Android Native Standards (Kotlin/Compose) for Jetpack Compose + Material Design 3.

### Phase 8: Quality Gates & Final Review
*   **Action:**
    1. **Accessibility audit:**
       *   WCAG contrast: 4.5:1 body text, 3:1 large text (18px+ bold or 24px+ regular).
       *   Screen reader: `aria-label` on icon-only buttons, correct heading hierarchy (single `<h1>`), semantic HTML5 elements.
       *   Keyboard: visible focus rings, logical tab order, Enter/Space activation on all interactive elements.
       *   Motion: `prefers-reduced-motion` compliance verified.
    2. **State completeness:** Verify every interactive component has ALL states:
       *   Default → Hover → Focus → Active/Pressed → Loading (skeleton/shimmer) → Disabled → Error → Empty/Null.
    3. **Performance audit:**
       *   LCP (Largest Contentful Paint) < 2.5s.
       *   CLS (Cumulative Layout Shift) < 0.1.
       *   FID (First Input Delay) < 100ms.
       *   Heavy libraries (Lottie, GSAP, Three.js, chart libs) are lazy-loaded via `dynamic()` or `React.lazy()`.
    4. **Visual QA:** Use Playwright screenshot tool to capture screenshots at each breakpoint for visual regression.
    5. Run Web Interface & Accessibility Standards (WCAG 2.2) for comprehensive Vercel Web Guidelines compliance.
    6. Run Strict Linting & Type Validation for TypeScript, ESLint, and build verification.
    7. Use Severity-Tiered Code Review (Blocker/Major/Minor/Nit) for severity-rated code audit (Blocker/Major/Minor/Nit).
    8. Use Concise 1-Line Actionable Review for terse one-line findings and Anti-Overengineering & Bloat Audit for over-engineering detection.

---

## Design System Boilerplate (CSS Variables)

```css
:root {
  /* Primitive Colors */
  --color-neutral-50: #fafafa;
  --color-neutral-100: #f5f5f5;
  --color-neutral-900: #171717;
  --color-brand-indigo: #6366f1;
  --color-brand-violet: #8b5cf6;

  /* Semantic Colors */
  --canvas-bg: var(--color-neutral-50);
  --text-primary: var(--color-neutral-900);
  --color-primary: var(--color-brand-indigo);
  --color-accent: var(--color-brand-violet);

  /* Spacing Scale */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;

  /* Border Radii */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}

@media (prefers-color-scheme: dark) {
  :root {
    --canvas-bg: var(--color-neutral-900);
    --text-primary: var(--color-neutral-50);
  }
}
```

---

## RSC vs. Client Component Boundaries Pattern

### Server Component (Data Fetching)
```tsx
// app/dashboard/page.tsx
import { db } from '@/lib/db';
import { UserList } from './user-list'; // Client leaf component

export default async function DashboardPage() {
  const users = await db.select().from('users'); // Server-side execution

  return (
    <main className="p-8 max-w-5xl mx-auto">
      <h1 className="text-4xl font-bold tracking-tight mb-6">User Management</h1>
      <UserList initialUsers={users} />
    </main>
  );
}
```

### Client Leaf Component (Interactions)
```tsx
// app/dashboard/user-list.tsx
"use client";

import { useState } from 'react';

interface User {
  id: string;
  name: string;
}

export function UserList({ initialUsers }: { initialUsers: User[] }) {
  const [users, setUsers] = useState(initialUsers);

  const removeUser = (id: string) => {
    setUsers(prev => prev.filter(user => user.id !== id));
  };

  return (
    <ul className="space-y-4">
      {users.map(user => (
        <li key={user.id} className="flex justify-between items-center p-4 bg-white dark:bg-zinc-800 rounded-lg shadow-sm border border-zinc-200 dark:border-zinc-700">
          <span className="font-medium text-zinc-900 dark:text-zinc-50">{user.name}</span>
          <button 
            onClick={() => removeUser(user.id)}
            className="px-3 py-1.5 text-sm bg-red-600 hover:bg-red-700 text-white rounded transition duration-150"
          >
            Remove
          </button>
        </li>
      ))}
    </ul>
  );
}
```

---

## CSS Grid Bento Layout Setup

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[200px]">
  <!-- Bento Tile 1: Hero Block (Spans 2 columns, 2 rows) -->
  <div class="md:col-span-2 md:row-span-2 p-8 bg-gradient-to-br from-indigo-500 to-purple-600 text-white rounded-2xl flex flex-col justify-end">
    <h2 class="text-3xl font-bold mb-2">Bento Grid Layout</h2>
    <p class="text-indigo-100">Premium visual distribution for modern applications.</p>
  </div>

  <!-- Bento Tile 2: Metric Indicator (Spans 1 column, 1 row) -->
  <div class="p-6 bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-2xl flex flex-col justify-between">
    <span class="text-zinc-500 text-sm font-semibold uppercase tracking-wider">Active Users</span>
    <span class="text-4xl font-extrabold tracking-tight">1,284</span>
  </div>

  <!-- Bento Tile 3: Graph/Chart Block (Spans 1 column, 2 rows) -->
  <div class="md:row-span-2 p-6 bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-2xl flex flex-col justify-between">
    <div>
      <h3 class="font-bold text-lg">Activity History</h3>
      <p class="text-zinc-500 text-xs">Real-time usage metrics</p>
    </div>
    <div class="h-32 bg-zinc-200 dark:bg-zinc-700 rounded-lg animate-pulse"></div>
  </div>

  <!-- Bento Tile 4: Sub-feature Block (Spans 1 column, 1 row) -->
  <div class="p-6 bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-2xl flex items-center justify-center">
    <span class="font-semibold text-zinc-700 dark:text-zinc-300">Settings Config</span>
  </div>
</div>
```

---

## Core Checklists

### Visual Quality
- [ ] No emojis as structural UI icons — use SVG/Phosphor/Radix icons
- [ ] Font baselines and icon baselines aligned
- [ ] Spacing conforms to 4dp/8dp scale — zero arbitrary values
- [ ] Layout graceful at ALL 7 breakpoints (375/428/768/1024/1280/1440/1920)
- [ ] Dark mode tested — no white flashes, no contrast failures
- [ ] Zero hardcoded hex values in component markup

### Interaction & Animation
- [ ] All animations complete within timing guidelines (80ms–400ms)
- [ ] GSAP cleanup logic (`ctx.revert()`) exists in every `useEffect`
- [ ] Press feedback (`scale-[0.98]` or opacity shift) within 80-150ms
- [ ] Scroll content never hidden behind fixed headers/footers
- [ ] `prefers-reduced-motion` wraps ALL motion

### Performance & Code
- [ ] Heavy libraries lazy-loaded via `dynamic()` or `React.lazy()`
- [ ] All images define explicit `width`/`height` (zero CLS)
- [ ] Images use `next/image` with `priority` on above-the-fold hero images
- [ ] Fonts loaded via `next/font` with `display: swap`
- [ ] Bundle analyzed — no duplicate dependencies or unused imports

### Accessibility
- [ ] Color contrast ratios verified (4.5:1 body, 3:1 large)
- [ ] All interactive elements keyboard-navigable with visible focus rings
- [ ] Single `<h1>` per page, correct heading hierarchy
- [ ] Icon-only buttons have `aria-label`
- [ ] Form inputs have associated `<label>` elements

---

## Anti-Patterns (Reject These)

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| `style={{ color: '#ff0000' }}` | Hardcoded colors bypass theming | Use `className` with token-mapped classes |
| `<img src="https://unsplash.com/..."` | External dependency, no control, CLS | Generate locally with local asset generation or custom SVG, use `next/image` |
| `animate={{ width: '100%' }}` | Layout reflow animation causes jank | Animate `transform: scaleX()` instead |
| `delay(300)` before showing content | Artificial delay, feels broken | Use skeleton shimmer during real loading |
| `{isLoading && <Spinner />}` full-page | Blocks all interaction, feels frozen | Use skeleton UI matching final layout dimensions |
| `onClick={() => router.push()}` on `<div>` | Not keyboard-accessible, no semantics | Use `<button>` or `<Link>` component |
| Mixed icon libraries | Visual inconsistency | Pick ONE icon set for the entire project |

---

## Universal Checklists & Reference Architecture

### 1. React Performance Guidelines (`React Architecture Best Practices`)
*   **Eliminating Waterfalls:** Use `Promise.all()` to parallelize independent queries. Start promises early and await them late.
*   **Re-render Optimization:**
    *   Derive state during render rather than sync-updating via `useEffect`.
    *   Use functional updates `setState(prev => ...)` to avoid callback re-creation.
    *   Initialize state lazily: `useState(() => expensiveCalculation())`.
    *   Avoid declaring components inside other components.
*   **RSC Optimization:** Keep client-side serialization boundaries minimal. Hoist static assets (e.g. logos) to module level.

### 2. Component Composition Patterns (`composition-patterns`)
*   **Avoid Boolean Prop Bloat:** Instead of piling boolean flags (e.g., `isBold`, `isHeader`, `hasIcon`), use component composition to wrap internals or construct explicit variants (e.g. `<Button.Primary>`).
*   **Compound Components:** Implement composite UI nodes (such as Tab/Accordion sets) using React Context to share active state implicitly among children.
*   **React 19 Context Use:** Prefer the `use(Context)` hooks pattern. Do not wrap ref-relaying components in `forwardRef` on React 19.

### 3. Mobile list optimizations (`react-native-skills`)
*   Use `FlashList` for heavy list rendering.
*   Avoid inline styles in render items; use memoized stylesheet objects.
*   Only animate properties that compile directly to GPU-level commands (like `transform` and `opacity`).

### 4. Custom Asset Pipeline (Modular UI Component Architecture)
*   **AI Slop Avoidance:** Ensure you do not default to standard purple radial background gradients, centered flex layout overrides, uniform high radii, or Inter typography scales unless explicitly requested.

### 5. Next.js 15+ Async Routing & Fetching (Next.js App Router Best Practices)
*   **Async Parameters:** Dynamic route parameters (`params`) and query filters (`searchParams`) are resolved asynchronously. Always await them before parsing:
    ```typescript
    export default async function ProjectPage({
      params,
      searchParams,
    }: {
      params: Promise<{ slug: string }>;
      searchParams: Promise<{ view?: string }>;
    }) {
      const { slug } = await params;
      const { view } = await searchParams;
      return <Project slug={slug} view={view} />;
    }
    ```
*   **LCP Optimization:** Hero images above the fold must use `next/image` with `priority={true}` and explicit `sizes` configuration to disable lazy-loading and prevent layout shifts.

### 6. React Native Render & Layout Stability (`React Native Performance Best Practices`)
*   **StyleSheet Hoisting:** Never write inline objects `style={{ padding: 10 }}` inside list render loops or dynamic component bodies. Always hoist definitions using `StyleSheet.create` outside the component scope:
    ```typescript
    const styles = StyleSheet.create({
      listItem: {
        padding: 16,
        backgroundColor: '#ffffff',
        borderBottomWidth: 1,
      },
    });
    ```
*   **Layout Calculations:** Use `onLayout` instead of calling `measure()` asynchronously on views, preventing UI blocks.

---

## Automated Anti-Slop Audit Patterns (Code Scanner)

Before declaring a component or page finished, run these static checks against the codebase to catch residual AI boilerplate:

```bash
# 1. Check for AI Blue-Indigo Gradient
grep -rn "from-blue-600 to-indigo-700" ./src ./app

# 2. Check for Universal rounded-2xl Overuse
grep -rn "rounded-2xl" ./src ./app | wc -l

# 3. Check for Perma-Pulse on Pricing Cards
grep -rn "animate-pulse" ./src ./app

# 4. Check for Stock AI Copywriting Clichés
grep -rn -E "delve|seamless|effortlessly|supercharge|testament" ./src ./app

# 5. Check for Hardcoded Hex Colors in JSX
grep -rn -E "bg-\[#|text-\[#|border-\[#" ./src ./app

# 6. Check for AI Builder Loader Tags
grep -rn -E "gpteng\.co|framerusercontent|tempo" ./public ./app ./src
```

---

## Micro-Interaction Physics Matrix (Framer Motion & GSAP)

To prevent stiff or default AI animations, use custom spring physics tuned to specific interaction contexts:

| Interaction Type | Framer Motion Spring Config | Target Experience |
|---|---|---|
| **Primary Button Press** | `{ type: "spring", stiffness: 500, damping: 30, mass: 0.5 }` | Tactile, instant response |
| **Modal / Dialog Entrance** | `{ type: "spring", stiffness: 350, damping: 25, mass: 0.8 }` | Crisp, natural drop-in |
| **Drawer / Slide Panel** | `{ type: "spring", stiffness: 280, damping: 28, mass: 1.0 }` | Smooth, weighted slide |
| **Dropdown Menu Reveal** | `{ type: "spring", stiffness: 450, damping: 32, mass: 0.4 }` | Tight micro-pop |
| **Card Hover Lift** | `{ type: "spring", stiffness: 300, damping: 20, mass: 0.6 }` | Fluid elevation lift |

---

## Performance Budget Protocol
- **JS Bundle Limit:** Core bundle size $< 100\text{ KB}$ gzipped. Total third-party scripts $< 30\text{ KB}$.
- **Layout Shift Prevention:** Every `<img>`, `<video>`, and dynamic iframe MUST specify explicit `width` and `height` attributes or CSS `aspect-ratio` to enforce $0.00$ Cumulative Layout Shift (CLS).
- **Typography & Assets:** Always use Google Fonts `display=swap` or local WOFF2 subsets with preloaded critical fonts.

### Core Web Vitals 2026 p75 Production Baseline
Every frontend build MUST pass the 75th percentile ($p75$) real-user field baseline:
- **LCP (Largest Contentful Paint):** $< 2.5\text{s}$ ($p75$). Enforce `<link rel="preload" as="image">` on hero media and `priority={true}` on Next.js images.
- **INP (Interaction to Next Paint):** $< 200\text{ms}$ ($p75$). Treat responsiveness as main-thread capacity management: offload heavy calculations to Web Workers or `requestIdleCallback`.
- **CLS (Cumulative Layout Shift):** $< 0.1$ ($p75$). Reserve static layout boxes for dynamic ads, toasts, and skeleton loaders.
- **Dynamic Imports:** Heavy components (charts, 3D canvases, rich text editors) strictly wrapped in `dynamic(() => import(...), { ssr: false })`.

---

## Cross-Cutting Concerns
*   **UX Audit:** Chain with `ultimate-ux-workflow` for deep usability testing after implementation.
*   **Research:** Use Web Search, Web Extraction Tool, and official library documentation for component library documentation and animation API references.
*   **Memory:** Use Persistent Project Memory / Scratchpad to persist design decisions, token architecture, and component patterns across conversations.
*   **Database:** Chain with `ultimate-database-workflow` when building data-driven dashboards or table views.
*   **Testing:** Use Playwright / Headless Browser Automation for E2E visual regression testing and `Test-Driven Development (Red-Green-Refactor)` for component unit testing.
*   **Deployment:** Use `ultimate-deployment-workflow` for production build optimization and CDN configuration.
