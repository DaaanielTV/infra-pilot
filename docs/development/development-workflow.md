# Development Workflow & Contributing

This guide helps you contribute code and improvements to Infra Pilot.

## 🌳 Git Workflow

### Main Branches

| Branch | Purpose | Protection |
|--------|---------|-----------|
| `main` | Production-ready code | Required PR review, tests pass |
| `develop` | Integration branch | Required tests pass |

### Feature Branches

Name feature branches clearly:
```
feature/user-authentication
fix/server-provisioning-timeout
docs/architecture-overview
chore/upgrade-dependencies
perf/optimize-db-queries
```

---

## 🔄 Development Cycle

### 1. Fork & Clone

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/your-username/infra-pilot.git
cd infra-pilot

# Add upstream remote to stay synchronized
git remote add upstream https://github.com/DaaanielTV/infra-pilot.git
```

### 2. Create Feature Branch

```bash
# Fetch latest from upstream
git fetch upstream

# Create branch from develop
git checkout -b feature/my-feature upstream/develop
```

### 3. Make Changes

```bash
# Edit files in your service
cd services/orchestrator-agent

# Follow code standards (see Code Standards guide)
# Write tests alongside changes
# Commit frequently with clear messages
```

### 4. Test Locally

```bash
# Run service-specific tests
npm run test           # JavaScript
pytest tests/         # Python
mvn test             # Java

# Run linting
npm run lint         # JavaScript

# Type checking
npm run type-check   # TypeScript
```

### 5. Commit & Push

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "feat: add user roles and permissions

- Implement RBAC system
- Add permission checks to API
- Update dashboard UI for role display

Fixes #123"

# Push to your fork
git push origin feature/my-feature
```

### 6. Create Pull Request

On GitHub:
- Title: Clear, descriptive title
- Description: Use PR template
- Reference issues: `Fixes #123`
- Add labels: `type/feature`, `service/orchestrator`

### 7. Respond to Review

```bash
# Address feedback
# Commit additional changes
git commit -m "address review feedback"
git push origin feature/my-feature

# After approval, rebase and merge
git rebase upstream/develop
git push -f origin feature/my-feature
```

---

## 📋 Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style (formatting, semicolons, etc)
- `refactor` - Code refactoring
- `perf` - Performance improvements
- `test` - Adding tests
- `chore` - Build, dependencies, tooling

### Examples

```
feat(orchestrator): add server auto-scaling

Implement auto-scaling policy that monitors CPU and memory usage,
automatically provisioning or decommissioning servers based on thresholds.

- Add scalability service module
- Implement metric collection
- Add scaling rules engine

Closes #456
```

```
fix(dashboard): correct memory leak in WebSocket handler

The connection handler was not properly cleaning up event listeners,
causing memory to grow over time.

Fixes #789
```

```
docs: update architecture documentation with new data flow
```

---

## 🧪 Testing Requirements

### Before Creating PR

### Before Creating PR

1. **Write tests** alongside features
2. **Run full test suite** locally
3. **Verify no regressions** in other areas

### Test Coverage

| Service | Minimum Coverage | Command |
|---------|------------------|---------|
| orchestrator-agent | 80% | `pytest --cov=services/orchestrator-agent` |
| management-dashboard | 70% | `npm run test -- --coverage` |
| discord-service | 70% | `npm run test -- --coverage` |
| service-core | 75% | `mvn test jacoco:report` |

### Running Tests

```bash
# All tests
./scripts/test.sh

# Specific service
cd services/orchestrator-agent && pytest tests/

# Watch mode (JavaScript)
npm run test:watch

# With coverage
pytest --cov=services/orchestrator-agent tests/

# Specific test file
mvn test -Dtest=ServerTest
```

---

## 🎯 Code Quality Standards

### Linting

```bash
# JavaScript/TypeScript
npm run lint
npm run lint -- --fix  # Auto-fix

# Python
pylint services/orchestrator-agent/
black services/orchestrator-agent/  # Format code
```

### Type Checking

```bash
# TypeScript
npm run type-check

# Python (optional, for type hints)
mypy services/orchestrator-agent/
```

### Code Formatting

```bash
# Auto-format all code
npm run format            # JavaScript
black .                    # Python
```

---

## ✅ PR Checklist

Before submitting PR:

- [ ] Code follows project standards
- [ ] Tests added/updated and passing
- [ ] No linting errors (`npm run lint` / `pylint`)
- [ ] Type checking passes (`npm run type-check`)
- [ ] Documentation updated if needed
- [ ] No console warnings/errors
- [ ] Commits are clean and descriptive
- [ ] Tested with related services
- [ ] No breaking changes (or documented)

---

## 🔍 Code Review Process

### What Reviewers Look For

1. **Correctness** - Does it work as intended?
2. **Tests** - Are there adequate tests?
3. **Performance** - Are there performance concerns?
4. **Security** - Are there security issues?
5. **Standards** - Does it follow conventions?
6. **Documentation** - Are changes documented?

### Responding to Review

```bash
# If changes needed
# 1. Make changes
# 2. Commit without force push (if small feedback)
git commit -m "address review feedback"
git push

# 3. Or if rewriting history
git rebase -i upstream/develop
git push -f origin feature/my-feature
```

---

## 📖 Documentation

### When to Update Docs

- Architecture changes → Update [docs/architecture/](../architecture/)
- API changes → Update [docs/api/](../api/)
- Setup changes → Update [docs/setup/](../setup/)
- New feature → Add to [README.md](../../README.md)

### Documentation Style

- Clear, active voice
- Code examples included
- Link to related docs
- Keep up-to-date with code

---

## 🚀 Advanced Topics

### Rebasing & Squashing

```bash
# Rebase on latest develop
git rebase upstream/develop

# If conflicts
git rebase --continue  # After resolving

# Squash commits for cleaner history
git rebase -i upstream/develop
# Mark commits as 's' to squash
```

### Signing Commits

```bash
# Generate GPG key (if not done)
gpg --generate-key

# Configure Git
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true

# Sign commit
git commit -S -m "message"

# Verify commit
git log --show-signature
```

---

## 🎓 Learning Resources

- [System Architecture](../architecture/overview.md)
- [Code Standards](code-standards.md)
- [Testing Strategy](testing-strategy.md)
- [Service Documentation](../architecture/)

---

## 🆘 Getting Help

- **Questions?** Open a discussion on GitHub
- **Bug found?** File an issue with reproduction steps
- **Security issue?** See [SECURITY.md](../../SECURITY.md)

---

**Last Updated:** April 2026
