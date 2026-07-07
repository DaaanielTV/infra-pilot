# Security

## LLM Data

If AI features are enabled, server metadata, logs, or config may be sent to the configured LLM API.

**Local mode** (no data leaves the machine):
```env
AI_API_ENDPOINT=http://localhost:1234/v1
AI_API_KEY=not-needed
AI_MODEL=llama3-8b
```

## Telemetry

None. No tracking, analytics, or phone-home. Opt-in only if changed in future.

## Secrets

- `.env` is gitignored — never committed
- Use env vars or a secrets manager (Vault supported)
- TLS for transport, Fernet encryption at rest

## Security Features

JWT auth · RBAC · 2FA/TOTP · WebAuthn/Passkeys · PAM (JIT access) · Audit trail

## Reporting

**Do not** open public issues. Email maintainers (see [`SECURITY.md`](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)). 48h acknowledgment.

---

*[SECURITY.md](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)*
