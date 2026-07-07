# Orchestrator Agent

Python Discord bot for VPS management via Docker SDK.

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

## Configuration

All via environment variables in `config.py`:
`discord_bot_token`, `db_host/user/password/name`, `whitelist_ids`, `public_ip`, `ssl_email`

## Architecture

- `main.py` — entry point, loads all cogs
- `config.py` — central config
- `vps_manager.py` — Docker SDK VPS management
- `cogs/*.py` — 35+ Discord command cogs

## Features

- VPS lifecycle (create, start, stop, restart, delete)
- Resource monitoring, billing, auto-scaling
- Backups, snapshots, cloning, migration
- DNS, SSL, load balancing
- Database provisioning, git deployments
- Task scheduler, modpack installer
