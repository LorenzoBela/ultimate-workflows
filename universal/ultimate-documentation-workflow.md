---
name: ultimate-documentation-workflow
description: >
  Write implementation-grounded READMEs, validated OpenAPI references, ADRs, onboarding and operational runbooks. Use for repository and engineering documentation with actual check evidence.
argument-hint: "[readme | api-spec | onboarding | runbook]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Technical documentation grounded in implementation

Use for repository READMEs, API references, onboarding and operational runbooks. Preserve the project's stack, package manager and supported shells. Documentation must distinguish working commands, illustrative placeholders and unrun instructions.

## Inputs

Inspect actual manifests/scripts, configuration, public interfaces, setup requirements and intended readers. Define supported versions/platforms and the document's purpose. Discover existing documentation and ownership rather than generating parallel contradictory guides. Do not expose real credentials in `.env.example` or command transcripts.

## Repository README and onboarding

Cover purpose, supported environment, prerequisites, exact setup/configuration, run/check commands, architecture overview, common failures and links to detailed docs. Use real repository commands; do not promise a five-minute setup without timing a clean supported environment. Explain external account requirements and expected local side effects.

Use fences longer than embedded fences when showing a Markdown template:

````markdown
## Quickstart

```text
Replace this block with commands verified against the actual repository.
Declare prerequisites, supported shell, environment variables and expected result.
```
````

This is a template, not a runnable quickstart. For actual commands, test a clean disposable checkout with documented prerequisites, record environment/results and mark unavailable external checks. Keep secrets in a separate manager; document required/optional variables, defaults and environments with safe placeholders.

## Complete OpenAPI example

The following self-contained example demonstrates OpenAPI 3.1 syntax; adapt its behavior to the actual API. It is a specification, not a live implemented endpoint. Headers on requests belong in operation `parameters`, and every operation defines responses.

```yaml
openapi: 3.1.0
info:
  title: Example Charges API
  version: 1.0.0
paths:
  /api/v1/charges:
    post:
      operationId: createCharge
      summary: Create a charge using an operation-scoped idempotency key
      parameters:
        - name: Idempotency-Key
          in: header
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 128
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChargeRequest'
      responses:
        '201':
          description: Charge created, or the original successful result replayed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Charge'
        '400':
          description: Invalid input or missing idempotency key
        '409':
          description: Same operation key was already used with a different payload
components:
  schemas:
    ChargeRequest:
      type: object
      additionalProperties: false
      required: [amountInCents, currency]
      properties:
        amountInCents:
          type: integer
          minimum: 1
        currency:
          type: string
          pattern: '^[A-Z]{3}$'
    Charge:
      type: object
      additionalProperties: false
      required: [id, amountInCents, currency]
      properties:
        id:
          type: string
        amountInCents:
          type: integer
          minimum: 1
        currency:
          type: string
          pattern: '^[A-Z]{3}$'
```

Document actual security schemes/authorization, all material status/error schemas, examples, pagination and compatibility for the target endpoint. The sample omits authentication to stay focused on syntax; do not infer it is suitable for an unauthenticated billing service. Validate with an available pinned OpenAPI validator, resolve all references, and compare operations with the implemented route inventory. For structured HTTP errors use the project's supported current Problem Details contract; do not copy obsolete RFC references blindly.

## Architecture and operations

Record significant choices in ADRs with context, evidence, alternatives, decision, status/date, consequences and revisit trigger. Link superseding records. Keep diagrams synchronized with actual boundaries; a changed label is not proof the deployment changed.

A runbook states symptom, prerequisites/permissions, read-only diagnosis, scoped action, expected outcome, stop/escalation conditions, recovery and owner. Separate production-changing commands from inspection. Include idempotency and uncertain-result reconciliation for retryable operations; never recommend a blind destructive reset.

## Verification and completion

Validate syntax/references, render Markdown where layout matters, exercise real quickstart/snippets in a disposable supported environment and check env/interface drift. Report exactly which checks ran, their versions and unrun limitations. Include ownership/version or last-verified revision so future readers can assess staleness. A lint pass proves syntax, not live endpoint behavior or onboarding speed.
