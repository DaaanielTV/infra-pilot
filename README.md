# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A multi-hypervisor cloud orchestration platform with GitOps, RBAC, usage-based billing, auto-scaling, self-healing, and multi-datacenter federation. Manage infrastructure from a CLI, web panel, or Discord bot.

## Table of Contents

- [Architecture](#architecture)
- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Architecture

```
┌─ Clients ──────────────────────────────────────────┐
│ CLI (ipilot)   Web Panel (React)   Discord Bot     │
└────────────────────────┬───────────────────────────┘
                         ▼
┌─ Orchestrator Agent (Python, port 8500) ───────────┐
│  Compute Providers    Manifests / GitOps            │
│  ┌────────────────┐   ┌────────────────────────┐   │
│  │ Docker  Proxmox│   │  YAML → drift detect   │   │
│  │ AWS     GCP   │   │  → reconcile            │   │
│  └────────┬───────┘   └────────────────────────┘   │
│           │                                         │
│  ┌────────▼───────┐   ┌────────────────────────┐   │
│  │  RBAC          │   │  Billing / Metering    │   │
│  │  orgs/projects │   │  usage → invoices      │   │
│  │  teams/roles   │   │  prepaid / postpaid    │   │
│  └────────────────┘   └────────────────────────┘   │
│                                                     │
│  ┌────────────────┐   ┌────────────────────────┐   │
│  │  Healing       │   │  Auto-scaling          │   │
│  │  health checks │   │  CPU/mem thresholds    │   │
│  │  auto-remediate│   │  scale up/down rules   │   │
│  └────────────────┘   └────────────────────────┘   │
│                                                     │
│  ┌────────────────┐   ┌────────────────────────┐   │
│  │  Region/Fed.   │   │  VPS Manager (Docker)  │   │
│  │  multi-DC      │   │  containers, backups   │   │
│  │  peer-to-peer  │   │  snapshots, migration  │   │
│  └────────────────┘   └────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
┌──────────────┐ ┌────────────┐ ┌────────────────┐
│  PostgreSQL  │ │  Redis     │ │  Prometheus/   │
│  (metadata)  │ │  (cache)   │ │  Grafana       │
└──────────────┘ └────────────┘ └────────────────┘
```

## Features

| Area | Capabilities |
|------|-------------|
| **Compute Abstraction** | Plugin-based providers — Docker, Proxmox, AWS, GCP, etc. via `ComputeProvider` ABC |
| **GitOps Declarative** | `InfraFile` YAML manifests, drift detection, auto-reconciliation, Git polling |
| **RBAC** | Organizations → Projects → Teams, built-in roles (owner/admin/operator/developer/viewer/billing), custom roles, fine-grained permissions |
| **Usage Metering & Billing** | Per-instance CPU/RAM/network metering, configurable pricing tiers, invoice generation, prepaid balance with auto-deduction |
| **Self-Healing** | Health checks (ping/port/process/HTTP), configurable remediation policies, auto-restart/recreate/migrate/escalate |
| **Auto-Scaling** | CPU/memory threshold rules, consecutive breach counting, cooldown enforcement, scale up/down via Docker `update()` |
| **Multi-Region Federation** | Region/datacenter models, peer-to-peer REST proxying, health heartbeats, token-authenticated federation API |
| **VPS Lifecycle** | Docker-based containers, create/start/stop/restart/delete, clone, migrate, stats, benchmarks |
| **Backups & Snapshots** | Commit-based backup, retention policies (daily/weekly/monthly), snapshot management, restore |
| **Load Balancing** | Pool management, health-check-aware members, multiple algorithms |
| **DNS & SSL** | Record management (A/AAAA/CNAME/MX), auto-renewal via Let's Encrypt |
| **Monitoring** | Prometheus `/metrics` endpoint, per-container stats, alert thresholds, Grafana dashboards |
| **Task Scheduling** | Cron-based task execution, container commands, one-off and recurring |
| **Resource Quotas** | Per-user CPU/memory/storage/bandwidth limits, soft/hard quotas, increase requests |
| **Templates** | Versioned instance configs, default templates (Ubuntu, Debian, Nginx, Postgres) |
| **Disaster Recovery** | Plans, drills, RTO/RPO tracking, playbook automation |
| **Security Scanning** | Trivy integration, vulnerability allowlists, policy enforcement |
| **Cloud Cost Analysis** | Multi-provider pricing cache, optimization recommendations, anomaly detection |
| **Green Computing** | Carbon-aware scheduling, idle resource optimization |


## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
```

This starts the orchestrator agent, PostgreSQL, Redis, Prometheus, and Grafana.

Install the CLI:

```bash
pip install ./cli
ipilot server list
```

## Usage

```bash
# VPS lifecycle
ipilot server create myapp --type nodejs --memory 1024
ipilot server list
ipilot server stats myapp

# GitOps
ipilot manifest apply infra.yaml
ipilot manifest diff infra.yaml

# RBAC
ipilot org create my-org
ipilot project create my-org my-project
ipilot role assign user@example.com admin my-org

# Billing
ipilot invoice list
ipilot balance add @user 50.00

# Scaling
ipilot scaling rule create --container abc123 --metric cpu_usage --threshold 80
ipilot scaling events

# Healing
ipilot healing policy set abc123 --enable-auto-restart

# Federation
ipilot federation peer register --name remote-dc --url https://dc2.example.com
```

## Documentation

Full documentation is available in the [wiki](wiki/Home.md):

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

## Project Structure

```
infra-pilot/
├── cli/                  # Python CLI (ipilot) — Typer-based
│   └── ipilot/
│       ├── commands/     # Command groups (aiops, billing, federation, etc.)
│       ├── bridge/       # Backward-compat argparse bridge
│       ├── client.py     # API client for orchestrator-agent
│       └── cli.py        # Argparse CLI (legacy)
├── services/
│   ├── orchestrator-agent/   # Core engine (Python, discord.py, aiohttp)
│   │   ├── cogs/             # Discord bot command cogs
│   │   ├── compute/          # Compute provider abstraction
│   │   ├── manifest/         # GitOps manifest engine
│   │   ├── rbac/             # Multi-tenant RBAC
│   │   ├── billing/          # Usage metering & billing
│   │   ├── healing/          # Self-healing & auto-remediation
│   │   ├── region/           # Multi-datacenter region/federation
│   │   ├── scaling/          # Auto-scaling engine
│   │   ├── db.py             # Async PostgreSQL pool
│   │   ├── vps_manager.py    # Docker VPS lifecycle
│   │   └── integration.py    # DB schema & notifications
│   ├── management-panel/ # Web panel (React/TypeScript)
│   └── discord-service/  # Standalone Discord bot (Node.js)
├── infrastructure/       # Prometheus, Grafana configs
├── tests/                # Integration tests
├── wiki/                 # Documentation
├── docker-compose.yml
└── Makefile
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Contributing Guide](wiki/07-Contributing.md).

## License

MIT
