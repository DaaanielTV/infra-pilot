# Security Policy

## Reporting a Vulnerability

**Do not** post security issues in public. Email the maintainers instead.

Please include:
- What the problem is
- What parts of the app are affected
- How to reproduce it
- How severe you think it is

**We will:** reply within 48 hours and provide a timeline for the fix.

## Security Best Practices

- Keep your software up to date. Use HTTPS in production.
- Never put passwords or API keys in code. Use environment variables instead.
- Validate user input and use parameterized database queries.
- Scan your dependencies for known vulnerabilities.

## Tools

| Language    | Tools              |
|-------------|--------------------|
| Python      | `bandit`, `pip-audit` |
| JavaScript  | `npm audit`        |
| Docker      | `trivy`            |

## Supported Versions

| Version          | Support                |
|------------------|------------------------|
| Latest release   | Full security patches  |
| Previous major  | Critical fixes only    |
