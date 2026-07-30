# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> CLI + dashboard for managing a handful of VPS servers – deploy, SSH, secrets, GitOps, backups.

---

## What This Is

A self-hosted toolbox for developers who rent VPS servers and want a unified CLI and web UI to manage them – without logging into Hetzner/DigitalOcean/AWS every five minutes.

| Interface | Status |
|-----------|--------|
| `ipilot` CLI | Working – 15 commands |
| Web Dashboard | Working – management panel on port 3001 |
| Discord Bot | Legacy, not maintained |

---

## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
pip install ./cli
ipilot login   # Log in with your API key from http://localhost:3001/api/setup/status
```

---

## CLI Commands

| Command | What It Does |
|---------|-------------|
| `server` | List, create, delete servers |
| `backup` | Create and list backups |
| `deploy` | Deploy to a server |
| `logs` | Tail server logs |
| `gitops` | YAML-based deployments (`apply`, `plan`) |
| `ssh` | SSH session management, keys, jump hosts |
| `inventory` | Server metadata and tags |
| `secrets` | Encrypted key-value store |
| `plugins` | Install, update, remove plugins |
| `doctor` | Benchmark and diagnose servers |
| `webhooks` | Create, list, test webhooks |
| `apikeys` | API key CRUD |
| `templates` | Deployment blueprints |
| `tui` | Terminal UI mode |
| `rollback` | Undo/rollback changes |

---

## What Works vs What Doesn't

**Works (tested, has backend endpoints):**
- Server CRUD via web panel API
- SSH sessions and keys
- Server inventory tags/metadata
- Secrets store with rotation
- Plugin management
- Webhook management
- API keys
- Deployment templates
- Doctor (benchmark, diagnose)
- Rollback / change history
- GitOps YAML deployments

**Partial / experimental (code exists, backend paths may differ):**
- AI Assistant endpoint exists, quality unknown
- Self-healing / auto-scaling engines exist in orchestrator, not exposed in CLI
- Discord bot is a legacy snapshot
- Multi-tenant RBAC and billing engines exist in orchestrator, untested

---

## Architecture

```
┌─ Clients ────────────────────────┐
│ CLI (ipilot)   Web Panel (React) │
└────────────────┬─────────────────┘
                 ▼
┌─ Management Panel (Express, port 3001) ─┐
│  ~150 REST endpoints, WebSocket          │
│  PostgreSQL + Redis storage              │
└────────────────┬─────────────────────────┘
                 │
                 ▼
┌─ Orchestrator Agent (aiohttp, port 8500) ─┐
│  Compute Providers · GitOps Engine · RBAC  │
│  Billing & Metering · Self-Healing         │
│  Discord Bot integration (legacy)          │
└────────────────────────────────────────────┘
```

---

## Development Status

| Area | Maturity |
|------|----------|
| CLI | Beta – core commands work, path mapping to backend needs alignment |
| Management Panel | Beta – feature-rich, actively extended |
| Orchestrator Agent | Alpha – engine code exists, front-to-back testing is light |
| Tests | Present but coverage is inconsistent |
| Documentation | wiki/ has guides, needs updating to match current scope |

This is a **solo project**. It's being built in the open. Contributions welcome.

---

## License

MIT — see [LICENSE](LICENSE).
