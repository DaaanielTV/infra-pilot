# CLI Reference

Auto-generated from `ipilot --help`.

## Global Options

```
ipilot [OPTIONS] COMMAND [ARGS]...
```

| Option | Short | Description |
|--------|-------|-------------|
| `--output` | `-o` | Output format: json, table, yaml, or plain |
| `--profile` | `-p` | Configuration profile to use |
| `--no-color` | | Disable colored output |
| `--install-completion` | | Install shell completion |
| `--show-completion` | | Show shell completion script |
| `--help` | | Show help and exit |

## Core Commands

| Command | Description |
|---------|-------------|
| `login <api_key>` | Authenticate with the API |
| `logout` | Clear authentication token |
| `version` | Show CLI version |
| `interactive` | Enter interactive REPL mode |
| `completion [shell]` | Shell completion setup |
| `batch --file <yaml>` | Execute batch operations from YAML file |
| `docs --output <file>` | Generate CLI reference documentation |

## Infrastructure

### server
| Subcommand | Arguments |
|------------|-----------|
| `list` | `[--output]` |
| `create <name>` | `--type, --memory` |
| `delete <server>` | |
| `status <server>` | |

### backup
| Subcommand | Arguments |
|------------|-----------|
| `list [server]` | |
| `create <server>` | |

### deploy
| Subcommand | Arguments |
|------------|-----------|
| `deploy <server> <branch>` | |

### logs
| Subcommand | Arguments |
|------------|-----------|
| `fetch <server>` | `--lines, --follow` |

## Edge & IoT

### edge
| Subcommand | Arguments |
|------------|-----------|
| `list` | `--device-type, --status` |
| `register <name> <device_type> <hardware_id>` | |
| `status <device_id>` | |
| `command <device_id> <command_text>` | |
| `backup <device_id>` | |

### fn
| Subcommand | Arguments |
|------------|-----------|
| `list` | `--device-id` |
| `deploy <name> <runtime> <device_id> <source> <handler>` | |
| `invoke <func_id>` | `--payload` |

### ml
| Subcommand | Arguments |
|------------|-----------|
| `models` | `--device-id` |
| `deploy <name> <model_format> <device_id> <version>` | |
| `infer <model_id>` | |

### iot
| Subcommand | Arguments |
|------------|-----------|
| `codes` | `--count, --ttl` |
| `enroll <code> <device_id>` | |

### cdn, mesh, gw, pipeline
Simple command groups with `stats`, `list`/`create`, `list`, and `stats` subcommands respectively.

## Green Computing

### energy
| Subcommand | Arguments |
|------------|-----------|
| `current` | |
| `history` | `--server-id, --hours` |
| `summary` | `--period` |

### carbon, pue
`current` and `history` subcommands.

### green
`forecast`, `jobs`, `schedule <workload_id> <schedule_type>`, `report`.

### reclaim, shutdown, hardware, provider, offset, efficiency
Resource management with list/scan/create subcommands.

## Networking

| Command | Subcommands |
|---------|-------------|
| `sdwan` | status, apps, create, delete, toggle |
| `vpn` | configs, create, delete, status |
| `dns` | zones, create-zone, delete-zone, records, add-record, delete-record |
| `bgp` | sessions, create, delete, routes |
| `proxy` | rules, create, delete, toggle |
| `segment` | list, create, delete |
| `capture` | list, start, stop |
| `dnsfilter` | status, rules, add, remove |
| `dhcp` | leases |
| `netcost` | show, budget |
| `cell` | networks, register, delete, status, sims, activate, deactivate |

## Security & Identity

| Command | Subcommands |
|---------|-------------|
| `oidc` | clients, register, delete |
| `webauthn` | credentials, remove |
| `session` | list, revoke |
| `pam` | requests, request, approve, deny |
| `breach` | list, report |
| `policy` | list, create, evaluate |
| `compliance` | scan, report, checks |
| `audit` | anomalies, trend, summary |
| `classify` | scan, inventory |
| `vendor` | list, create, assess |
| `soc` | soar, threatintel, decoy, vuln, incident, ueba, cspm, ndr, secrets, training (each with subcommands) |

## Operations

| Command | Subcommands |
|---------|-------------|
| `workflow` | list, create, run |
| `infra-pipeline` | list, run |
| `drift` | scan, list |
| `quota` | list, check |
| `remediate` | rules, history |
| `maintenance` | list, schedule |
| `runbook` | list, use |
| `chaos` | experiments, create, run, stop, faults |
| `heal` | status, history, retrain |

## AIOps

| Command | Subcommands |
|---------|-------------|
| `rca` | analyze, incidents, events, deps |
| `dem` | list, create, check, stats, summary |
| `alert` | ingest, incidents, stats, suppress |
| `scaling` | predict, metrics, policy, summary |
| `health-f` | services, register, forecast, dashboard |
| `assistant` | message, stats |
| `change` | plan, approve, stats |
| `capacity` | recommend, usage, simulate, summary |
| `chatbot` | message, tasks, analytics |
| `alert-corr` (v6) | correlate, sources, suppress, stats |
| `rca-v6` | analyze, impact, timeline, patterns |
| `capacity-v6` | recommend, simulate, forecast, alerts |
| `change-risk` | analyze, trend, ranking |
| `convo` | health, feedback, popular |
| `dex` | monitors, regression, health |
| `health-v6` | forecast, alerts, accuracy |
| `incident` (v6) | remediate, analytics, mttr |
| `ops` | chat, tasks, priorities |
| `scaling-v6` | forecast, alerts, recommend |

## FinOps

```
ipilot finops <subcommand> <action>
```

| Subcommand | Actions |
|------------|---------|
| `commitment` | list, summary, implement, commitments |
| `spot` | list, create, get, instances, savings |
| `uoe` | metrics, record, targets, set-target, violations, overview |
| `anomaly` | list, summary, investigate, resolve, profiles, create-profile |
| `budget` | list, create, get, spend, forecast, scenario, summary |
| `rightsizing` | list, summary, approve, implement, dismiss |
| `waste` | list, summary, scan, approve, cleanup, dismiss |
| `carbon` | list, assets, register, sustainability |
| `arbitrage` | workloads, comparisons, savings |
| `reports` | list, summary, generate |

## Customer Experience

```
ipilot cx <subcommand> <action>
```

| Subcommand | Actions |
|------------|---------|
| `health` | list, get, compute, history, stats |
| `ticket` | list, create, get, status, comment, assign, stats |
| `sla` | list, create |
| `canned` | list, create |
| `sentiment` | analyze, profile, interactions, trends, alerts |
| `adoption` | summary, features, track, recommendations, stats |
| `onboarding` | start, get, step, stats |
| `kb` | list, create, get, update, search, categories, feedback |
| `community` | posts, create, get, vote, comment, comments, requests, categories, leaderboard, stats |
| `comm` | send, batches, batch, maintenance-schedule, maintenance-list, maintenance-complete, templates, template-create |
| `nps` | create, list, get, send, respond, score, trend, detractors, stats |
| `success` | plays, create, status, trigger, executions, stats |

## Marketplace

| Command | Subcommands |
|---------|-------------|
| `trade` | list, create, accept, cancel |
| `appmarket` | list, install, installations |
| `ppu` | metrics, usage, budget |
| `reseller` | list, create, delete, analytics |
| `whitelabel` | settings |
| `sla` | list, create, delete, status |
| `credit` | list, issue |
| `crypto` | wallets, create-wallet, transactions, rates |
| `plans` | list, create, delete, subscriptions |
| `reco` | list, summary, implement, dismiss |
| `tax` | rates, invoices, generate, pay, summary, file |
| `loyalty` | status, badges, rewards, redeem, leaderboard |

## Platform Engineering

| Command | Subcommands |
|---------|-------------|
| `devportal` | list, register, get, summary |
| `scaffold` | list, generate, status, step |
| `service-catalog` | list, register, get, score, summary |
| `scorecards` | list, create, get, update, summary |
| `template-registry` | list, create, get, use, summary |
| `techdebt` | list, report, get, fix, summary |
| `environments` | list, create, get, delete, extend, summary |
| `api-catalog` | list, register, get, summary |
| `docgen` | list, generate, get, summary |
| `pulse` | list, create, respond, results, summary |

## Compliance

| Command | Subcommands |
|---------|-------------|
| `cc` | status, scan, alerts, summary, remediate, drift, compare, report, schedule, weakest |
| `evidence` | list, collect, packages, stats, auto-collect, search, validate, package-create, expired, custody |
| `cac` | list, evaluate, templates, stats, create, gap, test, dry-run, version |
| `attest` | list, generate, sign, stats, approve, verify, compare, schedule, coverage |
| `vcom` | list, register, assess, risk, scorecard, assessments, migrate-tier, categories, discover, remediation |
| `regintel` | changes, detect, sources, stats, impact, matrix, calendar, notify, pending, search |
| `audit-mgmt` | list, schedule, rights, stats, upcoming, overdue, workflow, report, register-right, calendar |
| `dres` | list, register, check, summary, flows, move, audit, violations, compliance-report, asset-search |
| `train` | modules, assign, status, stats, certifications, expiring, search, report, progress, batch-assign |
| `auditor` | sessions, evidence, findings, stats, engagement-create, engagement-complete, finding-create, session-revoke, session-extend, finding-update |

## Emerging Tech

| Command | Subcommands |
|---------|-------------|
| `blockchain` | list, create, status, validators |
| `storage` | list, create, pin, status |
| `quantum` | list, generate, cert, encrypt, decrypt |
| `contracts` | list, deploy, get, events |
| `web3id` | list, create, auth, sessions |
| `confidential` | list, create, attest, secrets |
| `federated` | list, create, status, rounds |
| `zkp` | list, generate, verify, circuits |
| `dcn` | list, submit, status, workers |

## Resiliency

| Command | Subcommands |
|---------|-------------|
| `dr` | list, create, status, failover, readiness, delete, scenarios, versions, notifications, compliance |
| `active-active` | regions, register, status, health, weight, replication, capacity, availability |
| `backup-sla` | list, create, verify, report, policy, storage |
| `chaos-exp` | list, create, run, approve, results, blast-radius, metrics, notifications |
| `res-score` | score, list, summary, alerts, trend, forecast, export |
| `dep-sim` | list, create, run, classify, health, report |
| `rb-exec` | list, create, execute, templates, audit, versions, approve |
| `data-integrity` | list, create, run, schedule, alerts, health, audit |
| `res-pipeline` | list, create, trigger, steps, webhooks, triggers, analytics |
| `bc-dashboard` | show, report, scenarios, subscribe, simulate |

## Examples

```bash
# List all servers (table format)
ipilot server list

# List servers as JSON (for piping)
ipilot server list --output json | jq '.[] | .name'

# Create a server
ipilot server create myapp --type nodejs --memory 1024

# Use a config profile
ipilot --profile prod server list

# Interactive mode
ipilot -i

# Batch operations from YAML
ipilot batch --file ops.yaml

# Install shell completion
ipilot completion install

# Check system health
ipilot health

# Get carbon footprint
ipilot carbon current

# Deploy an edge function
ipilot fn deploy myfunc wasm device-01 https://example.com/func.wasm handler

# Create a FinOps budget
ipilot finops budget create my-budget --amount 5000 --period monthly
```
