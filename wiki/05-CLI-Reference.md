# CLI Reference

## How to Use

```bash
ipilot [global-flags] <command> [subcommand] [flags]
```

Global flags: `--version`, `--output`/`-o` (json, table, yaml, plain)

## Core

`login <api_key>` · `logout` · `health` · `config get [key]` · `config set <key> <value>`

## Server Management

`server list` · `server create --name --type --memory` · `server delete <id>` · `server status <id>`
`logs <id> --lines --follow` · `backup list/create <id>` · `deploy <id> <branch>`

## Networking

`dns zones/create-zone/records/add-record` · `vpn create` · `proxy create` · `bgp create` · `segment create`

## Edge & IoT

`edge list/register` · `fn deploy` · `iot codes` · `mesh create`

## Green Computing

`energy current/history` · `carbon current/history` · `green schedule` · `offset quote` · `provider rank` · `reclaim scan`

## FinOps

`finops commitment/spot/anomaly/rightsizing/waste/budget`

## Security & Compliance

`vuln cves/scan` · `cspm scan` · `compliance scan` · `secrets findings` · `soar playbooks`

## Resilience

`dr create/failover` · `chaos create` · `heal status`

## Platform Engineering

`environments create` · `scaffold generate` · `scorecards create` · `techdebt list`

> 200+ commands total. Use `ipilot <command> --help` for details.

---

*[Source: cli/ipilot/cli.py](https://github.com/drosemann/infra-pilot/blob/main/cli/ipilot/cli.py)*
