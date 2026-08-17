---
name: ultimate-project-workflow
description: >
  Master workflow for agile project management, scope definition, sprint tracking,
  and walkthrough reporting.
  Coordinates task.md checklists, milestone prioritization, blocker resolution,
  and walkthrough.md generation.
  Triggers on "ultimate project workflow", "/ultimate-project-workflow", or when scoping
  requirements, creating task lists, or documenting final deliverables.
argument-hint: "[task-scoping | sprint-tracking | walkthrough-report]"
---

# Ultimate Project & Task Management Workflow

This workflow drives systematic feature scoping, sprint milestone tracking, blocker resolution, and complete walkthrough reporting to ensure deliverables are clear, prioritized, and fully verified.

---

## The 4-Phase Project Pipeline

### Phase 1: Requirements Scoping & User Stories
*   **Sub-skills:** `superpowers-brainstorm`, `concise-planning`, `sequential-thinking/sequentialthinking`
*   **Action:**
    1. Define the project scope and end goal. List primary constraints, business dependencies, and target audience needs.
    2. Write clear user stories (`As a <role>, I want <feature>, so that <benefit>`).
    3. Establish explicit acceptance criteria for each story before beginning development.
    4. Use `superpowers-brainstorm` for divergent requirement exploration and `concise-planning` for atomic task generation.
    5. Use `sequentialthinking` to trace dependencies between user stories and identify critical path items.

### Phase 2: Milestone Prioritization (MoSCoW)
*   **Sub-skills:** `kaizen`, `ponytail`, `superpowers-plan`
*   **Action:**
    1. Group tasks into logical, incremental milestones (Milestone 1, 2, 3).
    2. Prioritize tasks using the MoSCoW framework:
       *   **Must Have:** Critical tasks that form the Minimum Viable Product (MVP).
       *   **Should Have:** Important but non-blocking tasks.
       *   **Could Have:** Nice-to-have features or polish items.
       *   **Won't Have:** Tasks deferred to future sprints.
    3. Document dependencies between tasks to identify potential blockers early.
    4. Apply `ponytail` YAGNI to ruthlessly prune "Won't Have" items and `kaizen` for continuous scope refinement.
    5. Use `superpowers-plan` for breaking milestones into small, verifiable atomic steps.

### Phase 3: Task Checklist Execution (task.md)
*   **Sub-skills:** `lint-and-validate`, `superpowers-tdd`, `systematic-debugging`
*   **Action:**
    1. Create a dynamic task checklist file at `<appDataDir>/brain/<conversation-id>/task.md` to track execution progress.
    2. Enforce the standard planning-mode notation:
       *   `[ ]` Unstarted task.
       *   `[/]` In-progress task.
       *   `[x]` Completed task.
    3. Update `task.md` continuously at the start and completion of each development task. Keep items atomic (2–10 minutes).
    4. Run `lint-and-validate` after completing each task item.
    5. Apply `superpowers-tdd` for test-driven development on critical path items.
    6. Use `systematic-debugging` for resolving blockers encountered during execution.

### Phase 4: Walkthrough & Deliverables Verification
*   **Sub-skills:** `superpowers-review`, `caveman-review`, `ckm:slides`, `docx`
*   **MCP Tools:** `playwright`, `memory`
*   **Action:**
    1. Conduct a final integration pass against the established acceptance criteria.
    2. Create or update the `walkthrough.md` artifact at `<appDataDir>/brain/<conversation-id>/walkthrough.md` to present results.
    3. Structure the walkthrough to summarize:
       *   **Core Changes:** Exact files modified and new files created.
       *   **Test Results:** Commands run and their outcomes.
       *   **UI/UX Verification:** Embedded screenshots or screen recordings showcasing interface changes.
    4. Use `playwright` MCP for capturing browser screenshots and recording UI verification videos.
    5. Use `superpowers-review` and `caveman-review` for terse, severity-rated final code audit.
    6. Use `ckm:slides` for stakeholder presentation decks and `docx` for formal deliverable documents.
    7. Persist project outcomes and lessons learned to `memory` graph for cross-conversation recall.

---

## Cross-Cutting Concerns
*   **Research:** Use `tavily-search` and `perplexity-ask` for project management methodology research.
*   **Brand:** Use `ckm:brand` for aligning project deliverables with brand guidelines.
*   **Deployment:** Use `ultimate-deployment-workflow` for release engineering integration.
*   **Documentation:** Use `ultimate-documentation-workflow` for maintaining project READMEs and API specs.
