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

## Branch Naming

`feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/` prefix + description.

## Commits

[Conventional Commits](https://www.conventionalcommits.org/): `type(scope): description`

## PR Workflow

1. Branch from `main`
2. Commit and push
3. Open PR against `main`
4. CI runs tests, lint, security scans
5. Merge after review + green checks

---

*See [CONTRIBUTING.md](https://github.com/drosemann/infra-pilot/blob/main/CONTRIBUTING.md) for full details.*
