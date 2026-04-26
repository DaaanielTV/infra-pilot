# AI Assistant Playbook

This playbook defines how AI contributors should work in `infra-pilot` to keep changes safe, maintainable, and easy to review.

## Goals

- Keep infrastructure operations reliable for a small team.
- Favor secure defaults and explicit permission checks.
- Ship small, testable increments instead of sweeping rewrites.
- Preserve existing behavior unless a change request says otherwise.

## Working Agreement

1. **Understand before changing**
   - Inspect the relevant service, docs, and tests first.
   - Verify assumptions in code before proposing API or schema changes.
2. **Choose the smallest safe path**
   - Prefer minimal diffs that solve the root cause.
   - Avoid introducing abstractions that are not currently needed.
3. **Design for operations**
   - Add useful logs for admin actions and failed automation.
   - Handle external service outages and partial failures gracefully.
4. **Build with security in mind**
   - Never hardcode secrets or tokens.
   - Validate authorization for privileged actions.
   - Validate and sanitize all external input.

## Change Checklist

Before opening a PR, confirm:

- [ ] Existing behavior is preserved unless intentionally changed.
- [ ] Inputs are validated at boundaries.
- [ ] Permission checks are present for admin or automation paths.
- [ ] Errors are actionable and do not leak sensitive details.
- [ ] Logs/audit events are adequate for incident response.
- [ ] Tests cover critical path and failure modes.
- [ ] Docs are updated when behavior or configuration changes.

## Preferred Implementation Patterns

### Service Boundaries

- Keep domain logic separate from infrastructure integrations.
- Keep external clients (Discord, VPS APIs, backup providers) behind focused modules.
- Avoid mixing transport concerns with business decisions.

### Reliability

- Prefer idempotent operations when possible.
- Retry only safe operations and cap retries.
- Distinguish user-action errors from platform-health errors.

### Security

- Treat all webhook payloads and chat commands as untrusted.
- Enforce role/permission checks before state mutation.
- Record sensitive admin actions in audit-friendly logs.

## Testing Priorities

Prioritize tests in this order:

1. Critical path behavior.
2. Permission-denied and invalid-input paths.
3. External dependency failure handling (timeouts, downtime, bad responses).
4. Recovery/rollback behavior for automation flows.

## Documentation Expectations

When a feature changes, document:

- What changed and why.
- Required environment/config updates.
- How operators verify healthy behavior.
- Known failure cases and recovery steps.

## Non-Goals

- No broad refactors without a scoped migration plan.
- No hidden behavior changes to existing admin workflows.
- No speculative architecture work without a concrete near-term use case.
