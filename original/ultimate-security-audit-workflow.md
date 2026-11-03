---
name: ultimate-security-audit-workflow
description: "Audit authorized repositories and environments for reachable vulnerabilities, dependency exposure, secrets and control evidence gaps. Verify findings with scoped evidence and safe reproduction."
argument-hint: "[cve-scan | compliance-check | sast-audit | --owasp | --supply-chain]"
---

# Security audit

Record scope, deployed versions, trust boundaries, accounts, exclusions and permitted probe types. Start with read-only review. Use existing tools and applicable standard versions. Keep secrets out of logs and retain redacted scanner evidence.

## Investigate by exposure

- For a dependency advisory, check affected/fixed ranges, deployed presence, configured feature and attacker reachability. Record a distinct disposition for verified exposure, potential exposure, false positive, accepted risk or unavailable evidence. A high scanner score alone does not establish a deploy blocker.
- For application findings, trace source to sink and establish permissions, preconditions, trigger and impact. Test tenant/object authorization, webhook validation, session boundaries and outbound requests as applicable. For SSRF, check parsed URLs, IPv4/IPv6 resolution, redirects and rebinding controls at the actual network boundary.
- For leaked credentials, record only redacted fingerprints, locations and affected scope. Determine who owns remediation. Separate reporting from any authorized rotation or history rewrite.
- For compliance, map applicable controls to actual configuration, procedures and evidence. Report control gaps and unknowns separately from technical vulnerabilities and certification.

Use disposable authorized targets for active probes. Prioritize by attainable impact, exposure, data sensitivity and controls. For each material finding provide evidence, a minimal reproduction or static rationale, remediation and verification. A reachable vulnerable path and an unreachable advisory need different dispositions. Verify fixes against the current target and state any remaining gaps.

## Role and handoffs

**Security assurance auditor.** Own reachability, control evidence, and audit scope. Use [ultimate-security-workflow](../ultimate-security-workflow/SKILL.md) and [ultimate-review-workflow](../ultimate-review-workflow/SKILL.md) when they own the next decision or check, and return the result and evidence to the task owner. Use the [workflow organization](../ultimate-project-workflow/resources/ultimate-organization/role-map.md) for cross-specialty work.

## Representative acceptance case

Compare a reachable advisory with one in an unused path. Verify distinct exposure dispositions, redact sensitive evidence, and keep compliance conclusions within the actual control evidence.
