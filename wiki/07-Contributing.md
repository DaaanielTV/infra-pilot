# Contributing

## Dev Setup

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot
pip install -r requirements.txt
cd services/management-panel && npm install && cd ../..
cd services/discord-service && npm install && cd ../..
```

## Tests

```bash
pytest tests/
cd services/management-panel && npm test
```

### Test Markers

`unit` · `integration` · `e2e` · `smoke`

## Branch Names

Use a prefix like `feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/` plus a short name.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): description`

## PR Workflow

1. Make a new branch from `main`
2. Commit and push
3. Open a pull request against `main`
4. CI runs tests, lint, and security checks
5. Merge after someone reviews it and all checks pass

---

*See [CONTRIBUTING.md](https://github.com/drosemann/infra-pilot/blob/main/CONTRIBUTING.md) for full details.*
