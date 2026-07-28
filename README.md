# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A multi-hypervisor cloud orchestration platform with GitOps, RBAC, usage-based billing, auto-scaling, self-healing, and multi-datacenter federation. Manage infrastructure from a CLI, web panel, or Discord bot.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [CLI Usage](#cli-usage)
- [GitOps (Infrastructure as Code)](#gitops-infrastructure-as-code)
- [Deployment Templates](#deployment-templates)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Platform
| Area | Capabilities |
|------|-------------|
| **GitOps (IaC)** | YAML-based infrastructure config, `ipilot gitops apply/plan`, drift detection, export/import |
| **Compute Abstraction** | Plugin-based providers — Docker, Proxmox, AWS, GCP, Hetzner, etc. |
| **RBAC** | Organizations → Projects → Teams, built-in roles, custom roles, fine-grained permissions |
| **Usage Metering & Billing** | Per-instance CPU/RAM/network metering, invoice generation, prepaid balance |
| **Self-Healing** | Health checks, auto-restart/recreate/migrate, escalation policies |
| **Auto-Scaling** | CPU/memory threshold rules, cooldown enforcement, scale up/down |
| **Multi-Region** | Region/datacenter models, peer-to-peer REST proxying, federation API |

### Infrastructure Management
| Area | Capabilities |
|------|-------------|
| **Server Inventory** | Metadata (owner, environment, region, OS, provider, cost), tags, `ipilot inventory list --tag production` |
| **SSH Sessions** | Session connect/record/replay, jump hosts, saved hosts, key management |
| **Secret Store** | Encrypted storage, versioning, auto-rotation, RBAC access control |
| **Backups** | S3/Backblaze support, scheduled backups, snapshot management, restore via CLI |
| **Deployments** | Git branch deployment, template-based, rollback support |
| **Docker Lifecycle** | Containers, images, ports, volumes, environment, compose stacks |

### Deployment Templates
| Template | Type | Description |
|----------|------|-------------|
| `nodejs` | Node.js | Express app with Dockerfile |
| `python` | Python | Flask/Gunicorn app with Dockerfile |
| `docker-compose` | Stack | Multi-service compose file |
| `nginx` | Web Server | Nginx with SSL support |
| `postgresql` | Database | PostgreSQL 15 Alpine |
| `redis` | Cache | Redis 7 Alpine |
| `traefik` | Reverse Proxy | Traefik v3 with auto-SSL |

### Developer Experience
| Command | Description |
|---------|-------------|
| `ipilot doctor --fix` | Comprehensive system diagnostics with auto-fix |
| `ipilot benchmark` | Performance benchmarking (CPU, memory, disk, network) |
| `ipilot diagnose` | Infrastructure issue diagnosis (connectivity, performance, disk) |
| `ipilot tui dashboard` | Text-based terminal UI (Textual) |
| `ipilot rollback` | Undo/rollback infrastructure changes |
| `ipilot gitops plan` | Preview changes before applying |

### Enterprise
| Feature | Description |
|---------|-------------|
| **Plugin System** | Extensible via `plugins/` directory, 9 built-in provider plugins |
| **Webhooks** | Event-driven HTTP callbacks with delivery logs |
| **API Keys** | Role-based programmatic access with expiration |
| **Activity Timeline** | Full audit trail of all user actions |
| **Multi-Tenant** | Organizations with member roles |
| **SSO / OIDC** | Google, GitHub, Microsoft, generic OIDC |
| **GraphQL API** | GraphQL endpoint for flexible queries |
| **Global Search** | Cross-resource search across apps, servers, backups, secrets |

### AI & Automation
| Feature | Description |
|---------|-------------|
| **AI Assistant** | Natural language → analysis → plan → confirm → execute |
| **Runbooks** | Automated workflows: deploy-production, rollback, backup-verify, system-update |
| **Workflow Automation** | Multi-step workflow orchestration |
| **Chaos Engineering** | Fault injection experiments |
| **Discord Bot** | `/deploy`, `/restart`, `/logs`, `/server status` with interactive buttons |

### Monitoring & Observability
| Area | Capabilities |
|------|-------------|
| **Metrics** | CPU, RAM, disk, load, Docker containers, systemd services |
| **Live Dashboard** | Real-time resource monitoring |
| **Prometheus Exporter** | `/metrics` endpoint for scraping |
| **Grafana** | Pre-configured dashboards |
| **Alerting** | Threshold-based alerts with notification channels |
| **Health Checks** | HTTP, TCP, Docker health checks |

### Networking
| Area | Capabilities |
|------|-------------|
| **DNS** | Zone/record management (A, AAAA, CNAME, MX) |
| **VPN** | Multi-protocol VPN configuration |
| **SD-WAN** | Software-defined WAN links |
| **BGP** | BGP session management |
| **Reverse Proxy** | Proxy rule management with toggle |
| **DHCP** | Lease monitoring |

### Security & Compliance
| Area | Capabilities |
|------|-------------|
| **OIDC** | OpenID Connect provider/client management |
| **WebAuthn** | Passkey authentication |
| **PAM** | Privileged Access Management |
| **Compliance Scanning** | CIS benchmark scans |
| **Audit Analytics** | Anomaly detection, trend analysis |
| **Data Classification** | Sensitive data scanning |
| **Vendor Risk** | Vendor assessment management |

## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
```

Install the CLI:

```bash
pip install ./cli
ipilot doctor          # Verify installation
ipilot login <api_key> # Authenticate
```

## CLI Usage

### Authentication
```bash
ipilot login <your-api-key>
ipilot logout
```

### Infrastructure as Code (GitOps)
```bash
# Export current infrastructure as YAML
ipilot gitops export --output infra.yaml

# Preview changes
ipilot gitops plan --file infra.yaml

# Apply configuration
ipilot gitops apply --file infra.yaml --dry-run
ipilot gitops apply --file infra.yaml --auto-approve

# Detect configuration drift
ipilot gitops drift --scan
ipilot gitops drift
```

### Server Inventory
```bash
# List with filters
ipilot inventory list --tag production --environment staging
ipilot inventory list --region us-east --owner alice

# Update metadata
ipilot inventory update web01 --environment production --cost 42.50

# Tag management
ipilot inventory tags --add web01:frontend
ipilot inventory tags --list
```

### SSH Session Management
```bash
# Connect to a server
ipilot ssh connect web01 --user deploy --jump bastion.example.com

# Manage jump hosts
ipilot ssh jump_hosts --create bastion --host bastion.example.com

# SSH keys
ipilot ssh keys --add ~/.ssh/id_rsa.pub --name work

# Session recordings
ipilot ssh list --status active
ipilot ssh record <session-id>

# Saved hosts
ipilot ssh saved --add prod@web01.example.com
ipilot ssh saved --list
```

### Secret Management
```bash
# Store a secret
ipilot secrets set DATABASE_URL "postgresql://..." --rotate --rotation-days 90

# Retrieve
ipilot secrets get DATABASE_URL
ipilot secrets get DATABASE_URL --version 2

# Version history
ipilot secrets versions DATABASE_URL

# Access control
ipilot secrets roles DATABASE_URL --grant developer
ipilot secrets roles DATABASE_URL --revoke viewer
```

### Deployment Templates
```bash
# List available templates
ipilot templates list
ipilot templates list --type node

# Deploy from template
ipilot templates deploy nodejs my-api --server web01
ipilot templates deploy traefik reverse-proxy

# Initialize a local project
ipilot templates init nodejs my-project --output ./apps
```

### Plugins
```bash
# List available plugins
ipilot plugins list

# Install a plugin
ipilot plugins install kubernetes --version 1.0.0
ipilot plugins install aws --source plugins/aws.py

# Plugin management
ipilot plugins update --all
ipilot plugins info docker
ipilot plugins uninstall proxmox
```

### Webhooks
```bash
# Create a webhook
ipilot webhooks create deploy-webhook https://hooks.example.com/deploy --events deploy,backup

# Test delivery
ipilot webhooks test --id <webhook-id> --event deploy

# View logs
ipilot webhooks logs
```

### API Keys
```bash
# Create an API key
ipilot apikeys create ci-cd-key --role readonly --expire 365

# List and revoke
ipilot apikeys list
ipilot apikeys revoke <key-id>
```

### Runbooks
```bash
# List built-in runbooks
ipilot runbook list

# Execute a runbook
ipilot runbook execute deploy-production
ipilot runbook execute backup-verify

# Create custom runbook
ipilot runbook create my-workflow --steps '[{"action":"git_pull","target":"repo"},{"action":"restart","target":"app"}]'
```

### AI Assistant
```bash
# Analyze a request
ipilot assistant analyze "Deploy my test environment"

# Chat with assistant
ipilot assistant chat "What's the status of web01?"
```

### Developer Tools
```bash
# Diagnostics
ipilot doctor
ipilot doctor --fix
ipilot doctor --verbose

# Benchmarks
ipilot benchmark
ipilot benchmark --server web01

# Issue diagnosis
ipilot diagnose --issue connectivity
ipilot diagnose --server web01 --issue performance

# TUI Dashboard
ipilot tui dashboard
ipilot tui monitor web01
ipilot tui logs web01

# Rollback
ipilot rollback list --limit 10
ipilot rollback undo <change-id>
ipilot rollback rollback server web01 --version <version>
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
├── cli/                          # Python CLI (ipilot) — Typer-based
│   └── ipilot/
│       ├── main.py               # Entry point, top-level commands
│       ├── client.py             # HTTP API client for backend
│       ├── config.py             # Config manager (~/.ipilot/config.json)
│       ├── commands/             # All CLI command groups
│       │   ├── gitops/           # Infrastructure as Code (YAML)
│       │   ├── ssh/              # SSH session management
│       │   ├── inventory/        # Server inventory
│       │   ├── secrets/          # Secret management
│       │   ├── plugins/          # Plugin management
│       │   ├── doctor/           # System diagnostics
│       │   ├── webhooks/         # Webhook management
│       │   ├── apikeys/          # API key management
│       │   ├── templates/        # Deployment templates
│       │   ├── tui/              # Terminal UI mode
│       │   ├── rollback/         # Undo/rollback
│       │   ├── infrastructure/   # Server, backup, deploy, logs
│       │   ├── networking/       # DNS, VPN, BGP, etc.
│       │   ├── security/         # OIDC, PAM, compliance, audit
│       │   ├── operations/       # Workflows, runbooks, drift
│       │   ├── aiops/            # Assistant, RCA, alerting
│       │   └── ...               # 50+ command groups
│       ├── core/                 # CLI framework
│       └── output/               # Output formatting (json, table, yaml)
├── plugins/                      # Plugin system (extensible)
├── services/
│   ├── management-panel/         # Web panel (React/TypeScript/Express)
│   │   ├── server/index.ts       # Express API server
│   │   ├── db/schema.sql         # PostgreSQL schema
│   │   └── src/                  # React frontend
│   ├── orchestrator-agent/       # Core engine (Python)
│   └── discord-service/          # Discord bot (Node.js)
├── infrastructure/               # Prometheus, Grafana
├── tests/                        # Integration tests
├── wiki/                         # Documentation
├── docker-compose.yml
└── Makefile
```

## Plugin System

Infra Pilot has a built-in plugin system for extending functionality.

### Available Plugins

| Plugin | Description |
|--------|-------------|
| `kubernetes` | Kubernetes cluster management |
| `docker` | Advanced Docker management |
| `aws` | Amazon Web Services integration |
| `hetzner` | Hetzner Cloud integration |
| `cloudflare` | Cloudflare DNS & CDN integration |
| `proxmox` | Proxmox VE virtualization management |
| `ansible` | Ansible automation integration |
| `nomad` | HashiCorp Nomad orchestration |
| `azure` | Microsoft Azure integration |

### Creating a Plugin

```python
# plugins/myplugin/__init__.py
from plugins import PluginBase

class Plugin(PluginBase):
    name = "myplugin"
    version = "1.0.0"
    description = "My custom plugin"

    def execute(self, **kwargs):
        return {"status": "executed", "input": kwargs}
```

Install: `ipilot plugins install myplugin --source plugins/myplugin`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Contributing Guide](wiki/07-Contributing.md).

## License

MIT
