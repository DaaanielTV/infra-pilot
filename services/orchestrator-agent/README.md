# Orchestrator Agent

The core orchestration engine. A Python async service that manages Docker-based VPS instances, evaluates GitOps manifests, enforces RBAC, meters usage, runs billing cycles, heals unhealthy instances, auto-scales resources, and federates across datacenters. Exposes a Discord bot and an aiohttp webhook/API server.

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env
python main.py
```

The server listens on port 8500 for health/metrics/webhook endpoints.

## Configuration

All via environment variables, loaded by `config.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `DISCORD_BOT_TOKEN` | `""` | Discord bot token (omit to run headless) |
| `DB_HOST` | `localhost` | PostgreSQL host |
| `DB_PORT` | `5432` | PostgreSQL port |
| `DB_USER` | `infra_pilot` | PostgreSQL user |
| `DB_PASSWORD` | `CHANGE_ME` | PostgreSQL password |
| `DB_NAME` | `infra_pilot` | PostgreSQL database |
| `GITOPS_WEBHOOK_PORT` | `8500` | Webhook/API server port |
| `FEDERATION_API_TOKEN` | `""` | Shared secret for federation peers (required in production; `/api/` fails closed without it) |
| `AUTO_SCALE_COOLDOWN_MINUTES` | `5` | Minutes between auto-scale actions |
| `AUTO_SCALE_CPU_THRESHOLD` | `80.0` | CPU % threshold for auto-scaling |
| `AUTO_SCALE_MEMORY_THRESHOLD` | `80.0` | Memory % threshold for auto-scaling |
| `ORCHESTRATOR_AGENT_DISABLED` | `true` | Set `false` to enable the Discord bot |
| `PUBLIC_IP` | `""` | Public IP for SSH commands |
| `WHITELIST_IDS` | `""` | Comma-separated allowed user IDs |
| `SERVER_LIMIT` | `1` | Max VPS per user |
| `SSL_EMAIL` | `admin@example.com` | Email for Let's Encrypt |

## Modules

### compute/ — Compute Provider Abstraction

Plugin architecture for hypervisor back-ends. Define new providers by implementing `ComputeProvider`:

- `base.py` — Abstract base class, `InstanceSpec`, `InstanceInfo`, `InstancePowerState`
- `registry.py` — `ProviderRegistry` singleton, register/lookup providers by name
- `docker_provider.py` — Wraps `VPSManager` as a `ComputeProvider` (reference implementation)

Usage:
```python
from compute.registry import ProviderRegistry
prov = ProviderRegistry.get("docker")
instances = await prov.list()
await prov.create(spec)
```

### manifest/ — GitOps Manifest Engine

Declarative infrastructure as code using YAML manifests:

- `schema.py` — `InfraFile` data model with `InfraInstance`, `InfraNetwork`, `InfraStorage`, `HealthCheckSpec`
- `engine.py` — `ManifestEngine`: load YAML, detect drift (diff desired vs actual), reconcile (create/update/delete)
- `watcher.py` — `ManifestWatcher`: polls Git repos on a timer, triggers reconciliation on changes

Manifest example (`infra.yaml`):
```yaml
api_version: v1
kind: InfraFile
metadata:
  name: prod-web
  region: us-east-1
spec:
  instances:
    - name: web-01
      image: nginx:latest
      cpu: 1
      memory_mb: 512
      ports: {"80/tcp": "8080"}
  networks:
    - name: internal
      cidr: 10.0.0.0/24
  storage:
    - name: data-volume
      size_gb: 50
```

### rbac/ — Multi-Tenant RBAC

Hierarchical access control:

- `models.py` — `Org`, `Project`, `Team`, `Role`, `Permission` enum (38 fine-grained permissions), built-in role templates
- `engine.py` — `RBACEngine`: CRUD for orgs/projects/teams, permission checks at org & project scope, role assignment with optional expiry

Built-in roles: `owner`, `admin`, `operator`, `developer`, `viewer`, `billing`.

### billing/ — Usage Metering & Billing

Usage-based billing engine:

- `meter.py` — `UsageMeter`: polls compute providers for CPU/RAM/network/storage usage, records to `usage_records` table
- `billing_engine.py` — `BillingEngine`: aggregates usage records into invoices, applies pricing tiers, generates totals

Pricing is configurable per-org via `pricing_tiers` table. Prepaid balances are handled by `cogs/prepaid_billing.py`.

### healing/ — Self-Healing & Auto-Remediation

Monitors instance health and automatically recovers:

- `engine.py` — `HealingEngine`: health check configs, remediation policies, action handlers (restart, recreate, migrate, scale_up, notify, escalate), rate limiting, health check loop

Handlers can be overridden per-action:
```python
engine.register_handler(RemediationAction.RESTART, my_custom_handler)
engine.set_scaling_engine(scaling_engine)  # connects SCALE_UP
```

### region/ — Multi-Datacenter Region & Federation

Physical location tracking and cross-region management:

- `region.py` — `Region`, `Datacenter` data models with capacity tracking and utilization %
- `federation.py` — `Federation` class: peer registration, REST-proxied instance operations, heartbeat monitoring

Peers authenticate via Bearer tokens validated by the `federation_auth_middleware` in `main.py`.

### scaling/ — Auto-Scaling

Resource-based auto-scaling:

- `engine.py` — `ScalingEngine`: evaluates `scaling_rules` DB table, queries live stats via `VPSManager.get_vps_stats()`, scales CPU/memory via `update_vps_config()`, consecutive breach counting, cooldown enforcement

Rules are managed via the `AutoScaler` Discord cog (`/scaling-rules`, `/scaling-rule-create`, etc.).

### Core Infrastructure

| File | Purpose |
|------|---------|
| `main.py` | Entry point: Discord bot setup, cog loading, webhook/API server, auto-scale & healing wiring |
| `config.py` | Central config from environment variables |
| `vps_manager.py` | `VPSManager` — Docker container lifecycle, stats, backups, snapshots, health checks, benchmarks |
| `db.py` | `DatabasePool` — asyncpg connection pool, sync psycopg2 helpers |
| `integration.py` | `init_database_tables()` — creates all 50+ tables, notification proxying |

### Discord Cogs (`cogs/`)

| Cog | Slash Commands | Purpose |
|-----|---------------|---------|
| `vps_commands` | /vpscreate, /vpsstart, /vpsstop, /vpsrestart, /vpsdelete, /vpsstats, /vpslist | VPS lifecycle |
| `vps_pricing` | /vpscost, /purchasevps | Cost calculation & one-time payment |
| `vps_billing` | — | Hourly billing loop against player_economy |
| `prepaid_billing` | /balance, /balance add, /balance history, /balance cost | Prepaid balance & hourly deduction |
| `monitoring` | /stats, /containerstats | Per-container stats, alerting |
| `bot_commands` | /servers, /create, /start, /stop, /restart | Legacy text commands |
| `health_checks` | /health, /health-check | Health check management |
| `backup_manager` | /backup, /backups, /restore | Backup lifecycle |
| `resource_manager` | /resources, /pool | Resource pool management |
| `template_manager` | /template, /templates | Versioned instance templates |
| `task_scheduler` | /task, /tasks | Cron-based task scheduling |
| `alert_manager` | /alert, /alerts | User-defined alert rules |
| `cleanup` | /cleanup | Idle resource reclamation |
| `database_manager` | /db-create, /db-delete, /db-list | MySQL/MariaDB database provisioning |
| `modpack_installer` | /modpack | Minecraft modpack installer |
| `update_manager` | /update, /updates | Container update management |
| `auto_scaler` | /scaling-rules, /scaling-rule-create, /scaling-rule-delete, /scaling-rule-toggle, /scaling-events | Auto-scaling rule management |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check (no auth) |
| GET | `/metrics` | Prometheus metrics (no auth) |
| GET | `/api/v1/federation/status` | Federation peer status (requires `FEDERATION_API_TOKEN`) |
| POST | `/webhook/github/{deploy_id}` | GitHub webhook receiver |
| POST | `/webhook/gitops` | GitOps sync webhook |

## Database

50+ tables across these domains:
- **Core**: `vps_containers`, `vps_statistics`, `vps_peak_statistics`
- **RBAC**: `organizations`, `projects`, `teams`, `team_members`, `roles`, `role_assignments`
- **Billing**: `usage_records`, `invoices`, `invoice_line_items`, `pricing_tiers`
- **Region**: `regions`, `datacenters`, `federation_peers`
- **Scaling**: `scaling_rules`
- **Health**: `health_checks`, `health_check_results`
- **Backups**: `backup_rotation`, `snapshots`
- **DNS/SSL**: `dns_records`, `ssl_certificates`
- **Load Balancing**: `load_balancer_pools`, `lb_pool_members`
- **Automation**: `scheduled_tasks`, `recovery_playbooks`, `recovery_executions`, `runbooks`, `runbook_executions`
- **Templates**: `templates`
- **DR**: `dr_plans`, `dr_drills`
- **Monitoring**: `synthetic_checks`, `synthetic_check_results`, `alerts`
- **Security**: `scan_results`, `scan_policies`, `scan_allowlist`
- **K8s/Edge/FaaS**: `k8s_clusters`, `edge_nodes`, `faas_functions`
- **Cloud**: `cloud_pricing_cache`
- **Optimization**: `optimization_recommendations`, `threat_incidents`, `capacity_forecasts`, `gitops_sync_state`

## Testing

```bash
pytest tests/unit/ -v
pytest tests/smoke/ -v
```
