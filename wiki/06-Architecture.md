# Architecture

Think of it like a factory. Each part does one job.

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

| Service            | Language     | Port          | Purpose               |
|--------------------|--------------|---------------|-----------------------|
| Management Panel   | TS/React/Express | 5173/3001 | Web interface         |
| Orchestrator Agent | Python       | 8500          | Server orchestration  |
| Integration Service| Python       | 9000          | External integrations |
| Discord Service    | Node.js      | 3002          | Discord bot           |
| CLI (ipilot)       | Python       | —             | Command line tool     |

## Data Flow

- **AI** (optional): Use a local AI like Ollama or LM Studio. Set `AI_API_ENDPOINT=http://localhost:1234/v1`
- **Cloud**: The Orchestrator sends requests to AWS, Azure, GCP, Hetzner
- **Inter-service**: REST/JSON is used normally. WebSocket is used for live data.

---

*See [Security](08-Security) for data privacy details.*
