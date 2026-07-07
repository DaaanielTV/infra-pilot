# Contributing

All contributions welcome — bug fixes, features, docs, or discussions.

## Getting Started

1. Fork the repo, clone your fork
2. Add upstream: `git remote add upstream https://github.com/drosemann/infra-pilot.git`
3. Branch from `main` using naming convention below
4. Make changes, ensure tests pass
5. Push and open a PR against `main`

## Branch Naming

`feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/`, `perf/`, `style/` prefix + hyphenated description.

## Commits

[Conventional Commits](https://www.conventionalcommits.org/):
```
<type>(<scope>): <description>
```
Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`. Scope (optional): `panel`, `orchestrator`, `discord`, `integration`, `cli`, `docs`. Keep summary under 72 chars.

## PR Checklist

- [ ] Branch follows naming convention
- [ ] Commits follow Conventional Commits
- [ ] Tests pass, coverage doesn't decrease
- [ ] No new warnings/errors
- [ ] Documentation updated if behavior changed
- [ ] No secrets committed

## Tests

```bash
pytest tests/
cd services/management-panel && npm test
cd services/orchestrator-agent && pytest
```
