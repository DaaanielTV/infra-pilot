# Installation

## Full-Stack (Recommended)

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
```

Starts: PostgreSQL 16, Redis 7, Orchestrator, Integration Service, Management Panel, Discord Service.

Optional profiles:
```bash
docker compose --profile monitoring up -d   # Prometheus, Grafana
docker compose --profile cli up -d          # ipilot CLI container
```

## CLI Standalone

```bash
cd cli && pip install -e .
ipilot --version
```

## Requirements

| Component | Version |
|-----------|---------|
| Docker / Compose | 24+ / v2 |
| Python | 3.9+ |
| Node.js | 18+ |

---

*Updated: May 2026*
