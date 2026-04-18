# Security Policy

## Reporting Security Vulnerabilities

**Do not open public issues for security vulnerabilities!**

If you discover a security vulnerability in Infra Pilot, please report it responsibly by emailing the maintainers directly instead of using the public issue tracker.

### Reporting Process

1. **Email the maintainers** with details of the vulnerability
2. **Include:**
   - Description of the vulnerability
   - Affected component(s) and version(s)
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if you have one)

3. **Do not include:**
   - Full exploit code in the initial report
   - Unnecessary details that could aid malicious actors
   - Information about other vulnerabilities

### Response

- We will acknowledge receipt of your report within 48 hours
- We'll work on a fix / mitigation with you as necessary
- We'll provide a timeline for a patch release
- We request that you refrain from publicly disclosing the vulnerability until we've had a reasonable time to prepare and deliver a fix

### Security Best Practices

#### For Users

- **Keep software updated** - Always use the latest stable release
- **Use secrets management** - Never hardcode credentials; use environment variables or secret vaults
- **Enable SSL/TLS** - Use HTTPS in production
- **Restrict access** - Use firewalls, VPNs, and proper authentication
- **Monitor logs** - Regularly review application and infrastructure logs
- **Backup data** - Maintain regular backups and test recovery procedures

#### For Developers

- **Validate input** - Always validate and sanitize user input
- **Parameterize queries** - Use parameterized statements / ORMs to prevent SQL injection
- **Use strong auth** - Implement strong authentication and authorization mechanisms
- **Secure credentials** - Never commit secrets; use environment variables
- **Encrypt sensitive data** - Use TLS for transport, encryption at rest for stored data
- **Dependency updates** - Keep dependencies up to date and monitor for vulnerabilities
- **Code review** - Use peer review before merging changes
- **Security testing** - Include security checks in CI/CD pipelines

### Known Security Measures

- **Input Validation:** All API inputs are validated and sanitized
- **Authentication:** JWT-based authentication with secure token handling
- **Authorization:** Role-based access control (RBAC) for operations
- **Secrets:** Environment variable-based secret management
- **Dependencies:** Regular vulnerability scanning with `safety` and `npm audit`
- **CI/CD:** Security checks in GitHub Actions workflows

### Vulnerability Scanning

We use the following tools to identify and prevent vulnerabilities:

- **Python:** `bandit`, `safety`
- **JavaScript:** `npm audit`, ESLint security plugins
- **Java:** Maven plugins for dependency checking
- **Docker:** Image scanning with `trivy` or similar

### Supported Versions

Security updates are provided for:

- **Current Release:** All patches and minor updates
- **Previous Major Version:** Critical security fixes only
- **Older Versions:** No support

### Disclosure Timeline

We follow responsible disclosure practices:

1. **Day 0:** Vulnerability reported
2. **Day 1-2:** Vulnerability confirmed and assessed
3. **Day 3-7:** Fix developed and tested
4. **Day 7-14:** Patch released (depending on severity)
5. **Day 14:** Public disclosure of the fixed vulnerability (after release)

---

**Thank you for helping us keep Infra Pilot secure!**
