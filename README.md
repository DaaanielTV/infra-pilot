# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **Your infrastructure, one command away.**  
> Manage servers, VPS containers, and deployments from terminal, web dashboard, or Discord.

---

## Overview

Infra Pilot is a CLI-first infrastructure orchestration platform. Define your infrastructure as code, deploy with a single command, and monitor everything from one place.

| Interface | Description |
|-----------|-------------|
| `ipilot` CLI | Python CLI (Typer + Rich) — full control from terminal |
| Web Dashboard | React 19 + Express 5 management panel |
| Discord Bot | AI-powered infrastructure assistant with slash commands |
| Desktop App | Tauri v2 + Zig native build |

---

## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
pip install ./cli
ipilot login   # Log in with your API key from http://localhost:3001/api/setup/status
```

| Service | URL |
|---------|-----|
| Management Panel | http://localhost:5173 |
| API | http://localhost:3001 |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

---

## Architecture

```
┌─ Clients ──────────────────────────────────────────┐
│ CLI (ipilot)   Web Panel (React)   Discord Bot     │
└────────────────────────┬───────────────────────────┘
                         ▼
┌─ Orchestrator Agent (Python, port 8500) ───────────┐
│  Compute Providers · GitOps Engine · RBAC           │
│  Billing & Metering · Self-Healing · Auto-Scaling  │
│  Region/Federation · VPS Manager (Docker)          │
└─────────────────────────────────────────────────────┘
                         │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
┌──────────────┐ ┌────────────┐ ┌────────────────┐
│  PostgreSQL  │ │  Redis     │ │  Prometheus/   │
│  (metadata)  │ │  (cache)   │ │  Grafana       │
└──────────────┘ └────────────┘ └────────────────┘
```

### Services

| Service | Language | Purpose |
|---------|----------|---------|
| Orchestrator Agent | Python | Core engine: VPS, GitOps, RBAC, billing, scaling |
| Management Panel | TypeScript/React 19 | Web dashboard |
| Discord Service | Node.js | Discord bot (legacy) |
| CLI (`ipilot`) | Python (Typer) | Terminal client |

---

## Key Features

- **GitOps (IaC)** — YAML-based: `ipilot gitops apply/plan`
- **SSH Sessions** — Jump hosts, session recording, saved hosts
- **Server Inventory** — Metadata, tags, filtering
- **Secret Store** — Encrypted, versioned, auto-rotation, RBAC
- **Deployment Templates** — Node.js, Python, Docker Compose, Nginx, PostgreSQL, Redis, Traefik
- **Plugin System** — Extensible via `plugins/`, 9 built-in providers
- **Webhooks** — Event-driven HTTP callbacks
- **AI Assistant** — Natural language → plan → confirm → execute
- **Self-Healing** — Automatic remediation on health check failure
- **Auto-Scaling** — Rule-based resource adjustment

---

## Development

```bash
make setup          # Set up development environment
make dev            # Start PostgreSQL + Redis + run panel locally
make dev-services   # Start all Docker services
make test           # Run tests
make lint           # Run linting
```

---

## Documentation

- [Home](wiki/Home.md)
- [Installation](wiki/01-Installation.md)
- [First Deployment](wiki/02-First-Deployment.md)
- [Configuration](wiki/03-Configuration.md)
- [Usage Examples](wiki/04-Usage-Examples.md)
- [CLI Reference](wiki/05-CLI-Reference.md)
- [Architecture](wiki/06-Architecture.md)
- [Contributing](wiki/07-Contributing.md)
- [Security](wiki/08-Security.md)
- [FAQ](wiki/09-FAQ.md)
- [Troubleshooting](wiki/10-Troubleshooting.md)
- [Contributing](CONTRIBUTING.md)

---

## License

MIT — see [LICENSE](LICENSE).
