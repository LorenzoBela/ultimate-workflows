---
name: ultimate-security-workflow
description: >
  Workflow for application security hardening, zero-trust architectures,
  cryptographic protection, input sanitization, automated CORS/CSP headers, Upstash rate limiting,
  and database Row-Level Security (RLS).
  Triggers on "ultimate security workflow", "/ultimate-security-workflow", or when
  handling authentication, user data, cryptographic functions, or production hardening.
argument-hint: "[security-audit | auth-flow | rls-policy | --hardening | --zero-trust]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Ultimate Application Security Workflow

## Inputs, threat model and scope

Identify requested feature/control, trust boundaries, sensitive data, user/tenant roles, exposure, identity provider and existing requirements. Preserve stack/provider and inherited authorization. Prioritize concrete abuse cases/assets; feature work does not authorize intrusive tests or unrelated full audit.

Map attacker capabilities and authorization invariants to controls and observable checks. Discover tools/versions; vendor products are examples, not architecture prerequisites.

## Boundary and authorization

Validate payload shape/type/range/size on server. Normalization is context-specific, not universal sanitization. Parameterize database values; allowlist dynamic identifiers. Encode output for actual HTML/URL/script context; rich HTML needs a maintained sanitizer. Address applicable upload type/content/size, path traversal, SSRF destination/redirect/DNS and resource exhaustion risks.

Authenticate before sensitive work; authorize each object/property using trusted identity. Roles alone do not establish ownership. Client tenant IDs, prices and privileges are untrusted. Apply least privilege to database roles, services, storage and queues; test actual serving credentials.

Applicable relational designs use RLS plus grants/WITH CHECK, considering owner/service bypass, views/functions. Other stores need equivalent rules. Verify tenant isolation through reads/writes, reassignment, bulk/export/search and indirect paths.

## Sessions and browser behavior

Prefer established secure session/identity design. HttpOnly/Secure cookies reduce script access; choose SameSite based on login/cross-site needs. Strict can break OAuth/redirect flows. Cookie-authenticated mutations need framework-appropriate CSRF defense: token and/or trusted Origin checks with documented exceptions. CORS is neither CSRF defense nor server authorization.

Define expiry, refresh rotation/reuse detection, revocation/logout, session management and concurrent refresh where relevant. Native/public clients have different secure storage/redirect requirements; don't force browser cookies onto them. Avoid browser-persistent bearer secrets when safer architecture is available; document unavoidable tradeoffs.

Use step-up auth for sensitive account/payout changes and recovery. Consider supported phishing-resistant MFA. Test recovery, enumeration resistance and abuse limits, not only successful login.

## Cryptography, webhooks and secrets

Use vetted platform/library primitives. Password hashing parameters follow current guidance and measured capacity; prefer Argon2id where supported, migrate legacy hashes carefully and avoid timeless fixed bcrypt cost rules. Authenticated encryption requires nonce uniqueness, protected/versioned keys, rotation and recovery; naming an algorithm is insufficient.

Never commit credentials or log tokens/private payloads. Scope secrets to environment/runtime role; define rotation and leak response. Deleting the current file does not revoke leaked keys or erase history.

Verify webhook with provider's actual scheme/SDK and raw-body requirements; not all use HMAC. Check timestamp tolerance, audience/endpoint, rotation and size. Authenticate before effects; durably deduplicate trusted event/operation identity and reconcile uncertainty. Forgery rejection and valid duplicate handling are distinct checks.

## Network and operations

Use HTTPS and appropriate headers. Stage CSP report-only where needed then enforce compatible nonces/hashes. HSTS includeSubDomains/preload requires every affected subdomain's readiness and deliberate rollout; do not preload blindly. Frame policy must allow legitimate embeds where required.

Use threat/workload-based rate/concurrency limits with trusted proxy handling, tenant/principal keys, outage policy and cost caps. No specific Redis provider is required.

Audit meaningful events with actor/action/target/outcome/correlation; redact sensitive fields, restrict access and set retention. An append-only SQL table is not tamper-proof against administrators; choose integrity/remote storage for the threat model.

## Validation, recovery and evidence

Run focused negative cases in authorized disposable environments: cross-tenant/object access, CSRF, expired/revoked session, privilege change, modified/stale/replayed webhook, injection, SSRF/redirect and upload abuse when applicable. Verify legitimate OAuth returns and key rotation still work. Check logs for secrets and dependency-failure deny behavior.

Return control/threat mapping, actual results and unresolved risks without certification claims. Keep tested rollback/rotation/revocation path and migration compatibility. Escalate only concrete unresolved decisions while preserving authorized scope.

Sources: [OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html), [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [Stripe signature verification](https://docs.stripe.com/webhooks/signature).
