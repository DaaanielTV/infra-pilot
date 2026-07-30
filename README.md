# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> CLI-first infrastructure platform for VPS management, GitOps deployments, and server operations.

---

## Overview

Infra Pilot is a self-hosted platform that unifies server management, deployment, and operations into a single CLI and web dashboard. Stop jumping between cloud provider dashboards, SSH windows, and custom scripts.

---

## Features

| Feature | Description |
|---------|-------------|
| Server Management | Create, delete, monitor VPS servers |
| GitOps | Declarative YAML-based deployments with drift detection |
| SSH | Session management, jump hosts, key management |
| Backup & Restore | Scheduled backups with retention policies |
| Secret Store | Encrypted, versioned, with auto-rotation and RBAC |
| Deployment Templates | Blueprints for Node.js, Python, Docker Compose, Nginx, PostgreSQL, Redis, Traefik |
| Plugin System | 9 built-in providers (Docker, Kubernetes, AWS, Azure, Hetzner, Proxmox, Cloudflare, Ansible, Nomad) |
| Webhooks | Event-driven HTTP callbacks with delivery logs |
| API Keys | Role-based API key management |
| Doctor | Server benchmarking and diagnostics |
| Rollback | Change history with undo/rollback |

---

## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
pip install ./cli
ipilot login
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
┌─ Clients ────────────────────────┐
│ CLI (ipilot)   Web Panel (React) │
└────────────────┬─────────────────┘
                 ▼
┌─ Management Panel (Express) ───────┐
│  REST API · WebSocket · PostgreSQL │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─ Orchestrator Agent (aiohttp) ────┐
│  Compute Providers · GitOps · RBAC │
│  Billing · Self-Healing · Scaling  │
└────────────────────────────────────┘
```

---

## Documentation

- [Installation](wiki/01-Installation.md)
- [First Deployment](wiki/02-First-Deployment.md)
- [Configuration](wiki/03-Configuration.md)
- [CLI Reference](wiki/05-CLI-Reference.md)
- [Architecture](wiki/06-Architecture.md)
- [FAQ](wiki/09-FAQ.md)

---

## License

MIT — see [LICENSE](LICENSE).
