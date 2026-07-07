# Infra Pilot

<p align="center">
  <img src="experimental/branding/logo.svg" alt="Infra Pilot Logo" width="120"/>
</p>

<p align="center">

[![CI](https://img.shields.io/github/actions/workflow/status/d5niel-lgtm/infra-pilot/ci-core.yml?branch=main&style=flat-square&label=CI&logo=github)](https://github.com/d5niel-lgtm/infra-pilot/actions/workflows/ci-core.yml)
[![License](https://img.shields.io/github/license/d5niel-lgtm/infra-pilot?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Node](https://img.shields.io/badge/node-18%2B-339933?style=flat-square&logo=nodedotjs)](https://nodejs.org/)
[![React](https://img.shields.io/badge/react-19-61DAFB?style=flat-square&logo=react)](https://react.dev/)
[![Docker](https://img.shields.io/badge/docker-compose-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

</p>

**Infra Pilot** is a developer-first, self-hosted infrastructure orchestration platform — a modern alternative to Pterodactyl.

## CLI-First Architecture

Infra Pilot has been redesigned around a **CLI-first** architecture. The CLI is the single source of truth for all functionality. The Web Dashboard and Discord Bot are wrappers that invoke CLI commands internally, eliminating code duplication.

```
User               CLI (Typer)          API Client         Backend
 |                    |                    |                  |
 |-- ipilot server --|                    |                  |
 |  list --output    |-- ApiClient.list --|                  |
 |  json             |  _servers()        |---- HTTP GET --->|
 |                    |                    |                  |
 |<-- JSON output ---|<-- JSON response --|<-- response -----|
 |                    |                    |                  |
 |    Web Dashboard / Discord Bot          |                  |
 |       (subprocess ipilot ...)          |                  |
```

### Key Design Principles

1. **CLI is Core** — Every feature is accessible via `ipilot <command>`
2. **Web & Discord are Wrappers** — Both call `ipilot ... --output json` via subprocess
3. **Auto-Generated Docs** — CLI reference is generated from code, always in sync
4. **Rich Terminal Output** — Tables, colors, progress bars via Rich library
5. **Shell Completion** — Built-in for bash, zsh, fish, powershell
6. **Type-Safe** — Typer framework uses type hints for validation and IDE support

### Quick Example

```bash
# List servers
ipilot server list

# List servers as JSON (for piping to jq)
ipilot server list --output json | jq '.[].name'

# Create a server
ipilot server create myapp --type nodejs --memory 1024

# Use a config profile
ipilot --profile prod server list

# Check energy consumption
ipilot energy current

# Install shell completion
ipilot completion install

# Enter interactive REPL
ipilot interactive
```

## Core Features

- **Web Dashboard** — React 19 management panel (calls CLI for all operations)
- **CLI Tool** — `ipilot` — 100+ command groups, 500+ subcommands (Typer framework)
- **Discord Bot** — Provision and manage servers directly from Discord (calls CLI)
- **Orchestration** — Health monitoring, backup management, alerting, and task scheduling
- **Container Lifecycle** — Create, start, stop, restart, clone, and snapshot containers
- **Modpack Installer** — One-click game server modpack deployment
- **Multi-Tenant** — Customer workspaces with RBAC and audit trails
- **Monitoring** — Resource metrics, health checks, and Prometheus/Grafana integration

## Quick Start

```bash
git clone https://github.com/DaaanielTV/infra-pilot.git
cd infra-pilot
cp .env.example .env
docker compose up -d     # Starts core (postgres + redis + panel)
```

| Service | URL |
|---------|-----|
| Management Panel | http://localhost:5173 |
| API | http://localhost:3001 |
| Orchestrator Health | http://localhost:8500/health |

## Core Services

| Service | Stack | Purpose |
|---------|-------|---------|
| **management-panel** | React 19 + Express + PostgreSQL | Web dashboard for server and container management |
| **orchestrator-agent** | Python (discord.py) | Server provisioning, health monitoring, and automation |
| **discord-service** | Node.js (discord.js) | Discord bot for server creation and management |
| **cli** | Python | Command-line interface for scripting |

## Extended Features

Extended/experimental features (mobile app, integration gateway, marketplace, data platform, edge computing, FinOps, compliance, and more) are maintained in the [`experimental/`](experimental/) directory.

## Repository Structure

```
core/                    # Core product — strict MVP
├── api/                 # Express REST API
├── frontend/            # React dashboard
├── cli/                 # Python CLI
├── discord/             # Discord bot
└── orchestrator/        # Orchestration agent
experimental/            # Extended features (see experimental/README)
infrastructure/          # Prometheus + Grafana
services/                # Core service implementations
docs/                    # Developer documentation
wiki/                    # User-facing documentation
scripts/                 # Build and setup helpers
```

## Requirements

- Docker & Docker Compose v2
- Node.js 18+ (for local frontend development)
- Python 3.9+ (for CLI/orchestrator development)
- PostgreSQL 16 (handled automatically by Docker Compose)

## Development

```bash
make setup     # Install dependencies
make dev       # Start core services + frontend dev server
make test      # Run test suite
make lint      # Lint codebase
```

## License

MIT
