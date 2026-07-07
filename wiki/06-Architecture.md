# Architecture

Modular microservice architecture. Each service has a clear responsibility.

```
┌─ Clients ─────────────────────┐
│ CLI (ipilot)  Panel  Discord  │
└──────────────┬────────────────┘
               ▼
┌─ Core ────────────────────────┐
│ Orchestrator Agent  (port 8500)│
│ Integration Service (port 9000)│
└──────────────┬────────────────┘
               ▼
┌─ Storage ───┐  ┌─ Monitoring ─┐
│ PostgreSQL  │  │ Prometheus   │
│ Redis 7     │  │ Grafana      │
└─────────────┘  └──────────────┘
```

| Service | Lang | Port | Role |
|---------|------|------|------|
| Management Panel | TS/React/Express | 5173/3001 | Dashboard |
| Orchestrator Agent | Python | 8500 | Provisioning, Discord |
| Integration Service | Python | 9000 | External APIs, webhooks |
| Discord Service | Node.js | 3002 | Discord bot |
| CLI (ipilot) | Python | — | Terminal interface |

## Data Flow

- **AI/LLM features** (optional): can use local LLM (Ollama, LM Studio) — set `AI_API_ENDPOINT=http://localhost:1234/v1`
- **Cloud providers**: Orchestrator sends API requests to AWS, Azure, GCP, Hetzner
- **Protocol**: REST/JSON between services, WebSocket for live metrics

---

*See [Security](08-Security) for data privacy details.*
