# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> Learning project for operating Docker-backed infrastructure from a Python CLI, a React/Express panel, and an optional Discord integration.

## Components

| Component | Runtime | Default endpoint | Responsibility |
|---|---|---:|---|
| Management panel | React + Express | UI `:5173`, API `:3001` | Container operations, panel APIs, OpenAPI and Swagger UI |
| Orchestrator agent | Python/aiohttp | `:8500` | Health/metrics, GitOps webhook handling, manifest reconciliation, compute-provider and RBAC primitives |
| PostgreSQL / Redis | Docker images | `:5432` / `:6379` | Persistent application data / cache and supporting state |
| Discord service (optional) | Node.js | `:3002` | Discord and Pterodactyl integration; enabled with the `discord` Compose profile |
| Prometheus / Grafana (optional) | Docker images | `:9090` / `:3000` | Metrics collection and dashboards; enabled with `monitoring` |

The panel API offers an OpenAPI document at `http://localhost:3001/api/openapi.json` and Swagger UI at `http://localhost:3001/api/docs`. The orchestrator's API/webhook routes are documented in [the architecture guide](wiki/06-Architecture.md).

## Quick start

### Full local stack

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot
cp .env.example .env
bash scripts/generate-env.sh
docker compose up -d
```

`generate-env.sh` fills empty secret values in `.env`. Do not commit that file. Once Compose reports healthy services, open `http://localhost:5173` and use the panel's setup flow. Check service status with `docker compose ps` and follow logs with `docker compose logs -f management-panel orchestrator-agent`.

### CLI only

```bash
pip install ./cli
ipilot --help
ipilot login <api-key>
```

The CLI targets `http://localhost:3001` by default. Override it with `IPILOT_API_URL`, or configure a profile as described in [Configuration](wiki/03-Configuration.md).

## Common operations

```bash
# Start optional services
docker compose --profile monitoring up -d
docker compose --profile discord up -d

# Local development and checks
make dev                 # PostgreSQL + Redis, then panel dev servers
make test                # repository Python tests
npm run lint --prefix services/management-panel
```

See [Installation](wiki/01-Installation.md), [Configuration](wiki/03-Configuration.md), [Architecture](wiki/06-Architecture.md), [CLI reference](wiki/05-CLI-Reference.md), and the [documentation maintenance guide](docs/DOCUMENTATION.md) for the source-of-truth map.

## Security notes

Compose requires `POSTGRES_PASSWORD`, `GITOPS_WEBHOOK_TOKEN`, and `FEDERATION_API_TOKEN`; generate or set them before starting the stack. Treat Discord, Pterodactyl, webhook, and API tokens as secrets. The optional Discord service mounts the Docker socket and therefore must only run in a trusted environment. See [Security](wiki/08-Security.md).

## Contributing

All PRs, issues, and ideas are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), [wiki/07-Contributing.md](wiki/07-Contributing.md), and [docs/DOCUMENTATION.md](docs/DOCUMENTATION.md) before submitting a change.

## License

MIT — see [LICENSE](LICENSE).
