---
name: ultimate-ux-workflow
description: Audit or implement usable, accessible user flows with platform-aware interaction, clear feedback, state preservation, measured performance and honest automated/manual verification. Preserve existing brand and distinguish standards from design heuristics.
argument-hint: "[flow | component | accessibility | usability-audit]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve established authorization. Research requires all 15 prescribed provider inputs.

# UX and accessibility workflow

Use for requested interaction/flow improvements, usability audits or accessibility work. Inputs: actual user task, audience/platform, current interface/brand, accessibility target, device/browser matrix and authorized implementation scope. An audit is read-only unless changes are authorized. Do not replace an existing design system or force a new component/list/animation library merely to follow this workflow.

## 1. Understand the task and information architecture

Map the primary journey, decisions, terminology, entry/exit points and recovery paths. Observe actual content density and user needs; scanning patterns such as F/Z layouts are optional heuristics, not fixed placement rules. Use clear navigation labels, progressive disclosure where helpful and consistent vocabulary. Validate real task completion, confusion and error recovery; visual polish alone does not establish usability.

Inspect empty/single/many-item states, long or localized text, RTL where supported, missing permissions, expired sessions, offline/slow connections and partial failures. Preserve meaningful user data during validation/retry. Returning navigation should restore appropriate scroll/filter/form state while revalidating data according to freshness, authorization and privacy requirements.

## 2. Choose platform-appropriate interactions

Provide perceptible, prompt feedback and progress for long work; choose skeletons, progress bars, spinners or plain status based on the task and likely duration. 100ms feedback and 300ms loading heuristics are design targets to measure, not universal standards. Avoid fabricated progress phases or invented error causes. Prefer real reasons when known and useful next steps when they are not.

Support cancellation/undo where feasible and describe irreversible consequences. Keep navigation usable during partial loading unless a genuine state constraint requires otherwise. Optimistic updates need a visible pending state and defined reconciliation/rollback; use them only when failed effects are recoverable. Prevent duplicate side effects in the server contract as well as in the UI.

Respect native safe areas, browser history/back gestures, keyboard behavior and platform widget conventions. Gesture conflicts and nesting depend on the actual UI: do not ban every horizontal gesture inside a vertical list. Touch feedback, haptics, shake effects and scaling animations are choices, not required treatments for every action. Respect reduced motion and avoid motion-only feedback.

## 3. Separate standards from larger design targets

For web WCAG 2.2 AA, use the actual applicable success criteria and exceptions. Platform guidance may set larger targets:

| Subject | Requirement/reference | Verification |
|---|---|---|
| Web target size | SC 2.5.8: 24×24 CSS px or its spacing/equivalent/inline/user-agent/essential exceptions | Inspect actual hit areas/spacing; 44×44 is a larger design target rather than the AA minimum |
| iOS / Android targets | Apply current platform guidance for the selected control; 44pt / 48dp are common design references | Check actual target geometry and device interaction |
| Text contrast | Generally 4.5:1; 3:1 for qualifying large text (18pt regular or 14pt bold, approximately 24px/18.67px) | Check actual rendered size, weight, colors and applicable exceptions |
| Non-text contrast | Apply SC 1.4.11 to essential visual information identifying controls/states | Inspect actual boundary/state context, not every decorative border |
| Focus | Visible, logically ordered, not obscured where applicable | Keyboard journey including overlays/sticky UI |
| Reflow / text resize | Apply relevant WCAG criteria at required zoom/viewport conditions | Manual 200–400% checks with meaningful task content |

Use semantic controls and associated labels; decorative icons are hidden from assistive technology and icon-only controls need an accessible name. Do not force a specific aria-label when visible text already labels the control. Choose ARIA only when needed and keep name/role/state synchronized. Proper heading structure matters; a rigid one-h1 count alone does not prove or disprove conformance.

Keyboard patterns depend on widget semantics: Tab between controls, arrows within appropriate composites, Enter/Space according to native control behavior. Modals need contained focus; ordinary dropdowns are not automatically modal traps. Native/browser validation and date inputs can be appropriate; do not disable them solely for styling.

## 4. Dialog focus lifecycle

Prefer a supported native dialog or tested installed accessible primitive. Illustrative DOM integration (not a framework lifecycle or conformance certificate):

```typescript
const dialog = document.querySelector<HTMLDialogElement>('#edit-dialog');
const trigger = document.querySelector<HTMLButtonElement>('#open-edit');
if (!dialog || !trigger) throw new Error('Required dialog elements missing');
trigger.addEventListener('click', () => {
  dialog.showModal(); // native modal semantics/inert background; test support
  const initial = dialog.querySelector<HTMLElement>('[data-initial-focus]');
  initial?.focus(); // choose an appropriate field or tabindex=-1 heading
});
dialog.addEventListener('close', () => {
  if (trigger.isConnected && !trigger.disabled) trigger.focus();
  // If removed, choose the next logical workflow target.
});
```

Provide a programmatically named dialog, suitable initial focus, an explicit close action and inert background behavior. Test Escape/cancel, focus restoration, trigger removal, no-focusable content, dynamic fields, hidden/disabled controls, nested dialogs and scrolling. Remove listeners on component teardown; use framework refs/effects where needed. If the trigger disappears, focus the next logical task target rather than a detached node.

## 5. Loading, resilience and measured performance

Reserve appropriate media/content space to prevent disruptive layout shifts; skeletons should resemble the expected structure without blocking useful content. Use relevant field/lab metrics and device workloads, such as CLS and interaction responsiveness, with project budgets and distributions. Do not promise a skeleton renders within one universal 16ms frame.

Choose virtualization, prefetching, streaming and independent loading boundaries from actual framework support and measured item/network cost. Avoid speculative overfetching on expensive/private routes. List length alone does not mandate FlashList or any package. Make offline state and retry outcomes clear, preserve input on errors, and apply bounded retry behavior rather than automatic duplicate mutations.

Forms need useful labels/autocomplete/input types, understandable constraints and error summaries/focus when appropriate. Disabling submission is not universally better than allowing accessible validation; test discoverability and correction. Long text may require wrapping or expansion rather than silent ellipsis. Avoid color-only state distinctions.

## 6. Verify automated and manual scope

Use actual installed scanner versions and supported rule tags. Illustrative Playwright/axe check below covers only configured machine-testable rules:

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Compliance Audit', () => {
  test('Page has no findings in configured automated WCAG rule tags', async ({ page }) => {
    await page.goto('/dashboard');
    
    // Wait for dynamic hydration to settle
    await page.waitForSelector('main');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
```

Record manual keyboard/assistive-technology name-role-state testing, screen-reader status announcements, focus lifecycle, zoom/reflow, target geometry, reduced motion and meaningful error recovery. No empty axe result can certify all WCAG 2.2 AA criteria. If a tool/browser/device is unavailable, name the unrun check and its consequence; do not substitute a guessed pass.

For implemented changes, run representative user journeys across the agreed viewport/device matrix and inspect screenshots where visual layout matters. Include disabled/pending/loading/error/empty states when they actually apply; not every component needs seven fabricated states. Cross-check actual content, localization, high contrast and permissions where relevant.

## Completion and recovery

Report observed usability/accessibility defects with location, concrete user scenario and effect; distinguish normative violations from measured performance findings and optional design suggestions. Provide changed flows, checks actually run, manual/unavailable limits and unresolved recovery behavior. Preserve existing user work and useful design artifacts. Research into standards or unfamiliar platform contracts follows the mandatory full 15-provider workflow; primary sources resolve version conflicts, not majority vote.
