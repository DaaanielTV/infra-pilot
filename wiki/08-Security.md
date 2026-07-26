# Security

## AI Data

If you enable AI features, some server data may be sent to the AI provider.

**Local mode** (data stays on your machine):

```env
AI_API_ENDPOINT=http://localhost:1234/v1
AI_API_KEY=not-needed
AI_MODEL=llama3-8b
```

## Tracking

None. The tool does not track you. No data is sent home.

## Secrets Management

- `.env` is ignored by git — never commit it
- Use environment variables or a secrets tool (Vault works)
- TLS for data in transit. Fernet for data at rest.

## Security Features

JWT auth · RBAC · 2FA/TOTP · WebAuthn/Passkeys · PAM (JIT access) · Audit trail

## Reporting Issues

**Do not** open public issues. Email the maintainers (see [`SECURITY.md`](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)). Expect a reply within 48 hours.

---

*See [SECURITY.md](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md) for the full security policy.*
