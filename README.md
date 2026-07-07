# Infra Pilot

Developer-first, self-hosted infrastructure orchestrator. A modern alternative to Pterodactyl.

```
ipilot server list
ipilot server create myapp --type nodejs --memory 1024
ipilot server list --output json | jq '.[].name'
```

## Quick Start

```bash
git clone https://github.com/DaaanielTV/infra-pilot.git
cd infra-pilot
cp .env.example .env
docker compose up -d
```

| Service | URL |
|---------|-----|
| Management Panel | http://localhost:5173 |
| API | http://localhost:3001 |

## Services

| Service | Stack | What |
|---------|-------|------|
| `cli` | Python (Typer) | Single source of truth for all operations |
| `management-panel` | React 19 + Express | Web dashboard — wraps CLI |
| `discord-service` | Node.js (discord.js) | Discord bot — wraps CLI |
| `orchestrator-agent` | Python | Server provisioning & health monitoring |

## Development

```bash
make setup     # Install deps
make dev       # Start services + dev server
make test      # Run tests
```

## Requirements

- Docker & Docker Compose v2
- Node.js 18+, Python 3.9+

## License

MIT
