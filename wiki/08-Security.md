# Security

## AI Data

If you turn on AI features, some server data may be sent to the AI.

**Local mode** (data stays on your computer):
```env
AI_API_ENDPOINT=http://localhost:1234/v1
AI_API_KEY=not-needed
AI_MODEL=llama3-8b
```

## Tracking

None. The tool does not track you. No data is sent home.

## Secrets

- `.env` is ignored by git — never commit it
- Use environment variables or a secrets tool (Vault works)
- TLS for sending data. Fernet for stored data.

## Security Features

JWT auth · RBAC · 2FA/TOTP · WebAuthn/Passkeys · PAM (JIT access) · Audit trail

## Reporting Problems

**Do not** open public issues. Email the maintainers (see [`SECURITY.md`](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)). They'll reply in 48 hours.

---

*[SECURITY.md](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)*
