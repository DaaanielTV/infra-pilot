# Contributing to Infra Pilot

Thanks for your interest in contributing.

## Ground Rules

- Be respectful and follow the Code of Conduct.
- Keep pull requests focused and easy to review.
- Avoid unrelated refactors in feature/bugfix PRs.

## Development Workflow

1. Fork the repository and create a branch from `main`.
2. Make your change with clear commits.
3. Run relevant checks/tests locally for the affected component.
4. Update documentation if behavior/configuration changes.
5. Open a pull request with:
   - clear summary
   - testing notes
   - any migration or operational impact

## Commit Guidance

Use concise, imperative commit messages, e.g.:

- `docs: refresh root readme and setup instructions`
- `chore: remove committed build artifacts`
- `fix: correct env var handling in discord module`

## Pull Request Checklist

- [ ] Code builds/runs for touched components
- [ ] Docs updated where needed
- [ ] No generated artifacts or secrets committed
- [ ] `.env` files are not committed (use templates)

## Security

Do not open public issues for sensitive vulnerabilities. Share details privately with maintainers first.
