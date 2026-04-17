# System Architecture Overview

## 📐 Design Philosophy

Gemini follows a **distributed microservices architecture** with clear separation of concerns, enabling independent scaling, deployment, and development of services.

### Core Principles

1. **Modularity** - Each service has a single responsibility
2. **Autonomy** - Services can be deployed independently
3. **Scalability** - Horizontal scaling of individual components
4. **Resilience** - Graceful degradation and fault tolerance
5. **Observability** - Comprehensive logging, metrics, and tracing

---

## 🏛️ System Components

### 1. Management Dashboard
**Language:** TypeScript/React  
**Framework:** Vite, Tailwind CSS, Convex  
**Purpose:** Web-based operations interface

```
┌─────────────────────────┐
│   React Components      │
├─────────────────────────┤
│  - Server Provisioning  │
│  - Status Dashboard     │
│  - User Management      │
│  - Configuration UI     │
└────────────┬────────────┘
             ▼
     ┌───────────────┐
     │ Convex RPC    │
     │ Backend       │
     └───────┬───────┘
             ▼
    Orchestrator Agent API
```

**Responsibilities:**
- User interface for infrastructure operations
- Real-time status updates via WebSocket
- User authentication and RBAC
- Audit logging of all operations

---

### 2. Orchestrator Agent
**Language:** Python 3.9+  
**Frameworks:** aiohttp, Discord.py  
**Purpose:** Core provisioning and orchestration engine

```
┌──────────────────────────┐
│  Event Handlers          │
├──────────────────────────┤
│  - Discord events        │
│  - Webhook events        │
│  - API requests          │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│  Provisioning Logic      │
├──────────────────────────┤
│  - Resource allocation   │
│  - Configuration gen.    │
│  - Workflow engine       │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│  External Integrations   │
├──────────────────────────┤
│  - Pterodactyl API       │
│  - Cloud providers       │
│  - Database ops          │
└──────────────────────────┘
```

**Responsibilities:**
- Handle provisioning requests
- Orchestrate service interactions
- Manage resource allocation
- Execute automation workflows
- Integrate with external APIs

---

### 3. Discord Service
**Language:** Node.js (JavaScript)  
**Framework:** Discord.js  
**Purpose:** Discord bot interface for operations

```
┌─────────────────────────┐
│  Discord Events         │
│  (messages, reactions)  │
└────────────┬────────────┘
             ▼
┌─────────────────────────┐
│  Command Handlers       │
├─────────────────────────┤
│  - /provision           │
│  - /status              │
│  - /configure           │
│  - /billing             │
└────────────┬────────────┘
             ▼
   Orchestrator Agent API
```

**Responsibilities:**
- Parse Discord commands
- Execute infrastructure operations
- Post status updates
- Handle user interactions
- Webhook integration

---

### 4. Service Core
**Language:** Java 8+  
**Build Tool:** Maven  
**Purpose:** Game server lifecycle management

```
┌────────────────────────┐
│  Resource Manager      │
├────────────────────────┤
│  - CPU allocation      │
│  - Memory management   │
│  - Storage provisioning│
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│  Server Lifecycle      │
├────────────────────────┤
│  - Startup/shutdown    │
│  - Monitoring          │
│  - Event logging       │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│  Configuration         │
├────────────────────────┤
│  - Props generation    │
│  - Settings management │
│  - Schema validation   │
└────────────────────────┘
```

**Responsibilities:**
- Manage server resources
- Handle lifecycle events
- Generate configurations
- Report status and metrics
- Coordinate with orchestrator

---

## 🔄 Data Flow Patterns

### Provisioning Flow
```
User (Discord/Dashboard) 
    ▼
Orchestrator Agent
    ▼
Service Core (validate config)
    ▼
Cloud/Infrastructure APIs
    ▼
Infrastructure State Updated
    ▼
Webhook → Discord Service
    ▼
Notification to User
```

### Status Update Flow
```
Service Core (emits metric)
    ▼
Metrics Store (Prometheus)
    ▼
Dashboard (polls metrics)
    ▼
Real-time UI Update
    ▼
User Sees Status
```

### Event-Driven Flow
```
External System (Pterodactyl)
    ▼
Webhook to Orchestrator
    ▼
Process Event
    ▼
Update State
    ▼
Broadcast to Dashboard
```

---

## 🔌 API Boundaries

### Service-to-Service Communication

| From | To | Protocol | Format |
|------|-----|----------|--------|
| Dashboard | Orchestrator | REST/gRPC | JSON |
| Orchestrator | Service Core | REST | JSON |
| Discord Service | Orchestrator | REST | JSON |
| Dashboard | Service Core | REST | JSON |
| External Systems | Orchestrator | Webhook | JSON |

### External Integrations

- **Pterodactyl:** Game server hosting (REST API)
- **Cloud APIs:** AWS, GCP, Azure (REST/SDK)
- **Discord:** Bot webhooks and events (REST)
- **Monitoring:** Prometheus scrape endpoints (HTTP)

---

## 📊 Data Model

### Core Entities

```
┌─────────────────┐
│     Server      │
├─────────────────┤
│ - id            │
│ - name          │
│ - type          │
│ - status        │
│ - resources     │
│ - config        │
└─────────────────┘

┌─────────────────┐
│     User        │
├─────────────────┤
│ - id            │
│ - email         │
│ - role          │
│ - permissions   │
└─────────────────┘

┌─────────────────┐
│  Deployment     │
├─────────────────┤
│ - id            │
│ - server_id     │
│ - status        │
│ - timestamp     │
│ - error_msg     │
└─────────────────┘
```

---

## 🔐 Security Architecture

### Authentication & Authorization

```
User Login
    ▼
Dashboard → Convex Auth
    ▼
JWT Token Generated
    ▼
Token Passed to API Requests
    ▼
Orchestrator Validates
    ▼
RBAC Rules Applied
    ▼
Operation Allowed/Denied
```

### Layers

1. **Transport Layer:** TLS/SSL for all connections
2. **Authentication:** JWT tokens, OAuth2 support
3. **Authorization:** RBAC with granular permissions
4. **Audit Logging:** All operations logged
5. **Secrets Management:** Encrypted config storage

---

## 🚀 Deployment Architecture

### Development
```
Docker Compose
├── Management Dashboard (5173)
├── Orchestrator Agent (8000)
├── Discord Service (-)
├── Service Core (8080)
├── PostgreSQL
└── Redis
```

### Production
```
Kubernetes Cluster
├── Deployment: dashboard
├── Deployment: orchestrator
├── Deployment: discord
├── Deployment: service-core
├── StatefulSet: PostgreSQL
├── StatefulSet: Redis
├── Service: LoadBalancer (ingress)
└── PVC: persistent storage
```

---

## 📈 Scalability Considerations

### Horizontal Scaling

**Stateless Services** (can scale freely)
- Management Dashboard
- Orchestrator Agent
- Discord Service

**Stateful Services** (require special handling)
- Service Core (may cache state)
- Databases (replication/clustering)

### Load Distribution

```
Ingress/LB
    ▼
├── Dashboard pods (N replicas)
├── Orchestrator pods (N replicas)
├── Discord pods (N replicas)
└── Core Service pods (N replicas)

Database Layer (Primary + Replicas)
Cache Layer (Cluster)
```

---

## 🔍 Monitoring & Observability

### Metrics Exposed

- Application metrics (Prometheus format)
- Business metrics (deployments, resources used)
- Infrastructure metrics (CPU, memory, network)

### Logging Strategy

- Service logs → Centralized logging (ELK/Loki)
- Audit logs → Secure storage
- Error tracking → Sentry integration

### Tracing

- Distributed tracing via OpenTelemetry
- Service-to-service correlation IDs
- Performance analysis and bottleneck identification

---

## 🔄 High Availability

### Resilience Patterns

1. **Circuit Breaker** - Fail fast on external failures
2. **Retry Logic** - Exponential backoff
3. **Health Checks** - Readiness/liveness probes
4. **Graceful Degradation** - Partial functionality on component failure

### Recovery

- Automatic pod restart (Kubernetes)
- Database replication
- State recovery from logs
- Backup and restore procedures

---

## 📚 Related Documentation

- [Service Specifications](architecture/)
- [Data Flow Details](architecture/data-flow.md)
- [Integration Patterns](architecture/integration-patterns.md)
- [Deployment Guide](../operations/deployment-guide.md)

---

**Last Updated:** April 2026
