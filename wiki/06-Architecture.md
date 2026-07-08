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

| Service | Language | Port | What It Does |
|---------|------|------|------|
| Management Panel | TS/React/Express | 5173/3001 | The web page you see |
| Orchestrator Agent | Python | 8500 | Runs servers, talks to Discord |
| Integration Service | Python | 9000 | Talks to other services |
| Discord Service | Node.js | 3002 | The Discord bot |
| CLI (ipilot) | Python | — | The command line tool |

## How Data Moves

- **AI stuff** (optional): You can use a local AI like Ollama or LM Studio. Set `AI_API_ENDPOINT=http://localhost:1234/v1`
- **Cloud stuff**: The Orchestrator sends requests to AWS, Azure, GCP, Hetzner
- **Talking between parts**: REST/JSON is used normally. WebSocket is used for live data.

---

*See [Security](08-Security) for data privacy details.*
