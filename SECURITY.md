# Security Policy

## Reporting

Do **not** open public issues. Email maintainers with:
- Description of vulnerability
- Affected components/versions
- Steps to reproduce
- Impact assessment

**Response:** 48h acknowledgment, fix timeline provided.

## Best Practices

- Keep software updated, use HTTPS in production
- Never hardcode credentials — use env vars or vaults
- Validate input, parameterize queries
- Scan dependencies regularly

## Scanning

| Ecosystem | Tools |
|-----------|-------|
| Python | `bandit`, `safety` |
| JavaScript | `npm audit` |
| Docker | `trivy` |

## Supported Versions

Current release: all patches. Previous major: critical fixes only.
