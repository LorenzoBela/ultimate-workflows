---
name: ultimate-architecture-workflow
description: >
  Master workflow for systems architecture design, domain modeling, and technical
  specification.
  Guides the creation of Mermaid diagrams, database schemas, microservice boundaries,
  and Architecture Decision Records (ADRs).
  Triggers on "ultimate architecture workflow", "/ultimate-architecture-workflow", or
  when designing systems, mapping out data models, or drafting ADRs.
argument-hint: "[architecture-diagram | database-model | adr-draft]"
---

# Ultimate Systems Architecture Workflow

This workflow guides the design and documentation of high-level systems, database structures, component boundaries, and key design decisions to ensure scalable, maintainable, and aligned architectures.

---

## The 4-Phase Architecture Pipeline

### Phase 1: Domain Modeling & Bounded Contexts
*   **Action:**
    1. Apply Domain-Driven Design (DDD) principles: identify core domains, subdomains, and support domains.
    2. Define Bounded Contexts and establish clear mapping boundaries for data ownership across subsystems.
    3. Map out user states, triggers, and state transitions.
    4. Use `sequentialthinking` to trace data flow across domain boundaries and identify hidden coupling.
    5. Use `Structured Brainstorming & Architecture Scoping` to evaluate alternative domain decompositions with pros/cons matrices.

### Phase 2: Database Schema & Entity-Relationship Modeling
*   **Action:**
    1. Model data tables, relationships, cardinalities (1:1, 1:N, N:M), and foreign key policies.
    2. Write a comprehensive Entity-Relationship (ER) diagram in Mermaid:
       *   Use quotes for node labels containing special characters.
       *   Avoid HTML tags inside labels.
    3. Document indexes, data types, check constraints, and security requirements (e.g. RLS policies).
    4. For AI/ML search features, design vector embedding schemas using `upstash-vector-js` and full-text search indexes using `upstash-search-js`.
    5. Apply `PostgreSQL & Database Optimization Patterns` for constraint design, indexing strategy, and connection pooling.

### Phase 3: API & Component Interaction Design
*   **Action:**
    1. Define API design specs: resource naming conventions, request/response formats, security requirements, and HTTP statuses.
    2. Draft sequence diagrams (using Mermaid) to trace data flow and call cascades across system components (clients, servers, databases, third-party hooks).
    3. Plan event-driven integrations (e.g. message brokers, event buses, SSE/WebSockets) and state propagation.
    4. For durable multi-step orchestrations, design workflow DAGs using `upstash-workflow-js` with idempotent step definitions.
    5. For async messaging and scheduled tasks, architect delivery pipelines using `upstash-qstash-js`.

### Phase 4: Architecture Decision Records (ADRs)
*   **Action:**
    1. Document significant design decisions in a structured ADR (`docs/adr/000X-title.md`) containing:
       *   **Title:** Sequential number and descriptive title.
       *   **Context:** What is the problem, constraints, and background?
       *   **Decision:** What choice was made and why? What options were rejected?
       *   **Consequences:** What are the pros, cons, and compromises (technical debt) of this choice?
    2. Keep ADRs close to the codebase, ensuring they are version-controlled alongside code.
    3. For formal deliverables, use `docx` skill to generate Word document ADR exports with proper formatting.
    4. Persist architectural decisions to the `memory` graph for cross-conversation recall.

---

## Cross-Cutting Concerns
*   **Research:** Use Web Search, Deep Web Research, `perplexity-ask`, and official library documentation for architecture pattern research.
*   **Caching:** Use `upstash-redis-js` and `ultimate-caching-workflow` for designing caching layers within the architecture.
*   **Security:** Apply `ultimate-security-workflow` and `ultimate-security-audit-workflow` for threat modeling at the architecture level.
*   **Brand Alignment:** For customer-facing architectures, reference `Brand Voice & Identity System` and `Awesome-Design-MD` brand guidelines.
