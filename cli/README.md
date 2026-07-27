# Infra Pilot CLI (`ipilot`)

Command-line client for the Infra Pilot orchestration platform.

## Installation

```bash
# From the repo root
pip install ./cli

# Or directly
pip install git+https://github.com/drosemann/infra-pilot.git#subdirectory=cli
```

## Quick Start

```bash
# Configure connection
ipilot config set host orchestrator.example.com:8500
ipilot config set token your-api-token

# List servers
ipilot server list

# Create a server
ipilot server create myapp --type nodejs --memory 1024
```

## Command Groups

| Group | Description |
|-------|-------------|
| `server` | VPS lifecycle (create, list, stats, start, stop, restart, delete) |
| `manifest` | GitOps manifest operations (apply, diff, validate) |
| `org` | Organization management (create, list, members) |
| `project` | Project management within organizations |
| `role` | RBAC role assignment (assign, revoke, list) |
| `billing` | Invoice listing, balance management |
| `scaling` | Auto-scaling rules (create, list, events) |
| `federation` | Multi-datacenter peers (register, list, status) |
| `backup` | Backup lifecycle (create, list, restore) |
| `template` | Instance template management |
| `task` | Scheduled task management |
| `health` | Health check configuration |
| `alert` | Alert rule management |
| `config` | CLI configuration (set, get, list) |

## Authentication

The CLI connects to the Orchestrator Agent's API. Configure via:

```bash
ipilot config set host <host>:<port>
ipilot config set token <federation-api-token>
```

See `wiki/03-Configuration.md` for full details.

## Documentation

Full CLI reference: [wiki/05-CLI-Reference.md](../wiki/05-CLI-Reference.md)
