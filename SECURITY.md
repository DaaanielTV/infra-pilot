# Security Policy

## Reporting a Problem

**Do not** post security issues in public. Email the maintainers instead.

Tell us:
- What the problem is
- What parts of the app are affected
- How to reproduce it
- How bad you think it is

**We will:** reply within 48 hours and give you a timeline for the fix.

## Good Security Habits

- Keep your software up to date. Use HTTPS in production.
- Never put passwords or API keys in code. Use environment variables instead.
- Check user input and use parameterized database queries.
- Scan your dependencies for known vulnerabilities.

## Tools We Use

| What | Tools |
|------|-------|
| Python | `bandit`, `safety` |
| JavaScript | `npm audit` |
| Docker | `trivy` |

## Supported Versions

| Version | Support |
|---------|---------|
| Latest release | Full security patches |
| Previous major version | Critical fixes only |
