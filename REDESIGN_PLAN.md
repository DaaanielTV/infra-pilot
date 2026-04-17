# Infra Pilot: Professional Architecture Redesign

**Document Version:** 1.0  
**Status:** Architecture Proposal  
**Date:** April 2026  

---

## TABLE OF CONTENTS

1. [Executive Summary](#executive-summary)
2. [Branding Recommendations](#branding-recommendations)
3. [Module Renaming Guide](#module-renaming-guide)
4. [New Folder Structure](#new-folder-structure)
5. [Architecture Overview](#architecture-overview)
6. [CI/CD Pipeline Strategy](#cicd-pipeline-strategy)
7. [Implementation Roadmap](#implementation-roadmap)

---

## EXECUTIVE SUMMARY

**Infra Pilot** is a polyglot, multi-service infrastructure orchestration platform designed for automated game server and VPS lifecycle management. This redesign modernizes the repository structure, improves clarity, and establishes enterprise-grade documentation standards.

### Key Changes:
- **Structure:** Monorepo with clear service boundaries
- **Naming:** Consistent, descriptive module names following industry conventions
- **Documentation:** Comprehensive `/docs` structure with architecture, operations, and setup guides
- **DevEx:** Unified CI/CD, clear contribution paths, consistent tooling
- **Scalability:** Foundation for multi-region, multi-cloud deployment

---

## BRANDING RECOMMENDATIONS

### Project Identity

| Aspect | Current | **Recommended** | Rationale |
|--------|---------|-----------------|-----------|
| **Project Name** | Infra Pilot | **Gemini** | Modern, memorable, implies duality (control + operations) |
| **Tagline** | Automation bots & ops tools | **"Orchestrate. Automate. Scale."** | Action-oriented, professional |
| **Logo/Color** | None | Blue/Orange spectrum | Tech-forward, accessible contrast |
| **Subtitle** | Multi-component tooling | **Infrastructure Orchestration Platform** | Clear value proposition |

### Product Description

> **Gemini** is an open-source infrastructure orchestration platform enabling teams to automate game server provisioning, VPS lifecycle management, and multi-cloud resource orchestration through Discord, web interfaces, and programmatic APIs.

### Alternatives (Choose 1):
1. **Catalyst** - Implies rapid deployment & transformation
2. **Orion** - Constellation, navigation theme
3. **Conductor** - Orchestration metaphor
4. **Dispatch** - Operations focus

---

## MODULE RENAMING GUIDE

### Current → Recommended Mapping

| Current Name | Recommended | Type | Purpose |
|--------------|-------------|------|---------|
| `servermanager` | `service-core` | Java Plugin | Game server lifecycle & resource management |
| `VPS-MAKER-BOT` | `orchestrator-agent` | Python Bot | Infrastructure provisioning & management |
| `discord-bot-hosting-club` | `discord-service` | Node.js Bot | Discord command interface & webhooks |
| `panel_implementation` | `management-dashboard` | React/TypeScript | Web UI for operations & monitoring |

### Naming Conventions Applied:
- **Kebab-case** for directories
- **Clear intent:** No ambiguous abbreviations
- **Service context:** Each name describes primary function
- **Consistency:** All use "service", "agent", or clear verb

### Why These Names:
1. **service-core** - "Core" implies foundational, "service" shows it's a service module
2. **orchestrator-agent** - "Orchestrator" is infrastructure domain terminology; "agent" clarifies autonomous bot
3. **discord-service** - Clearly bounded to Discord ecosystem
4. **management-dashboard** - Self-documenting purpose

---

## NEW FOLDER STRUCTURE

### Directory Tree

```
gemini/
├── .github/
│   ├── workflows/                          # CI/CD pipelines
│   │   ├── ci-core.yml                     # Java service tests
│   │   ├── ci-orchestrator.yml             # Python bot tests
│   │   ├── ci-discord.yml                  # Node.js tests
│   │   ├── ci-dashboard.yml                # React/TS tests
│   │   └── docker-publish.yml              # Multi-service builds
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       └── security_report.md
│
├── services/                               # Core service modules
│   │
│   ├── service-core/                       # Java server management (renamed)
│   │   ├── pom.xml
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── docs/
│   │   │   ├── API.md
│   │   │   └── CONFIG.md
│   │   └── src/
│   │       └── main/
│   │           ├── java/
│   │           └── resources/
│   │
│   ├── orchestrator-agent/                 # Python VPS automation (renamed)
│   │   ├── requirements.txt
│   │   ├── requirements-dev.txt
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── docs/
│   │   │   ├── API.md
│   │   │   └── DEPLOYMENT.md
│   │   ├── cogs/
│   │   ├── tests/
│   │   └── main.py
│   │
│   ├── discord-service/                    # Node.js Discord bot (renamed)
│   │   ├── package.json
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── docs/
│   │   │   └── COMMANDS.md
│   │   ├── modules/
│   │   ├── tests/
│   │   └── index.js
│   │
│   └── management-dashboard/               # React web UI (renamed)
│       ├── package.json
│       ├── Dockerfile
│       ├── README.md
│       ├── docs/
│       │   ├── API_INTEGRATION.md
│       │   └── DEPLOYMENT.md
│       ├── convex/
│       ├── src/
│       ├── tests/
│       └── vite.config.ts
│
├── infrastructure/                         # Deployment & ops configs
│   ├── docker-compose.yml                 # Local development
│   ├── docker-compose.prod.yml            # Production setup
│   ├── kubernetes/                        # K8s manifests
│   │   ├── namespace.yaml
│   │   ├── configmaps/
│   │   ├── secrets/
│   │   ├── deployments/
│   │   ├── services/
│   │   └── ingress.yaml
│   ├── terraform/                         # IaC for cloud
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── aws/
│   │   ├── gcp/
│   │   └── azure/
│   └── monitoring/
│       ├── prometheus.yml
│       ├── grafana/
│       └── alerting/
│
├── docs/                                   # Root documentation
│   ├── README.md                           # Docs homepage
│   ├── ARCHITECTURE.md                     # System design
│   ├── GLOSSARY.md                         # Terminology
│   │
│   ├── architecture/                       # Detailed architecture
│   │   ├── overview.md
│   │   ├── service-core.md
│   │   ├── orchestrator-agent.md
│   │   ├── discord-service.md
│   │   ├── management-dashboard.md
│   │   ├── data-flow.md
│   │   └── integration-patterns.md
│   │
│   ├── setup/                              # Setup & installation
│   │   ├── local-development.md
│   │   ├── docker-setup.md
│   │   ├── kubernetes-deploy.md
│   │   ├── environment-config.md
│   │   └── ssl-tls-setup.md
│   │
│   ├── operations/                         # Ops & deployment
│   │   ├── deployment-guide.md
│   │   ├── scaling-strategy.md
│   │   ├── monitoring-observability.md
│   │   ├── troubleshooting.md
│   │   ├── backup-recovery.md
│   │   └── security-hardening.md
│   │
│   ├── development/                        # Developer guides
│   │   ├── contributing.md
│   │   ├── development-workflow.md
│   │   ├── testing-strategy.md
│   │   ├── code-standards.md
│   │   └── debugging-tips.md
│   │
│   └── api/                                # API documentation
│       ├── service-core-api.md
│       ├── orchestrator-api.md
│       ├── discord-webhooks.md
│       └── dashboard-api.md
│
├── scripts/                                # Automation scripts
│   ├── setup.sh                            # One-click local setup
│   ├── build.sh                            # Build all services
│   ├── test.sh                             # Run all tests
│   ├── docker-build.sh                     # Build Docker images
│   └── deploy.sh                           # Deploy to target environment
│
├── .devcontainer/                          # VS Code dev container
│   ├── devcontainer.json
│   └── Dockerfile
│
├── tools/                                  # Development tools/helpers
│   ├── migrate-services.sh                 # Migration helpers
│   └── generate-env.sh
│
├── .github/
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md                               # NEW: Professional root README
├── SECURITY.md                             # Security policy
├── docker-compose.yml
└── docker-compose.prod.yml
```

### Key Improvements:
1. **Clear Service Boundaries:** Each service under `/services` with own docs
2. **Infrastructure as Code:** `/infrastructure` for K8s, Terraform, monitoring
3. **Comprehensive Docs:** `/docs` with dedicated sections for setup, ops, dev
4. **Automation:** `/scripts` for common tasks
5. **CI/CD:** `.github/workflows` for GitHub Actions
6. **DevOps Ready:** Dev containers, Docker, K8s configs

---

## ARCHITECTURE OVERVIEW

### System Design (High-Level)

```
┌─────────────────────────────────────────────────────────────────┐
│                      End Users / Teams                          │
└────────┬────────────────────────────────┬──────────────────────┘
         │                                │
    ┌────▼─────────┐          ┌──────────▼──────────┐
    │   Discord    │          │ Management Dashboard│
    │   Service    │          │ (React + Convex)   │
    │  (Node.js)   │          └────────┬────────────┘
    └────┬─────────┘                   │
         │                              │
    ┌────┴──────────────────────────────┴────────┐
    │                                             │
    │        Orchestrator Agent (Python)         │
    │     [Core Logic & Provisioning]            │
    │                                             │
    └────┬──────────────────────────────┬────────┘
         │                              │
    ┌────▼──────────┐          ┌───────▼────────┐
    │  Service Core │          │  External APIs │
    │  (Java Plugin)│          │   & Services   │
    │               │          │                │
    │ - Game Server │          │  - Pterodactyl │
    │ - Resources   │          │  - Cloud APIs  │
    │ - Database    │          │  - Webhooks    │
    └────┬──────────┘          └────────────────┘
         │
    ┌────▼──────────────────┐
    │  Infrastructure Layer  │
    │                        │
    │ - Databases (MySQL)    │
    │ - Cache (Redis)        │
    │ - File Storage         │
    └────────────────────────┘
```

### Data Flow

1. **User Commands (Discord)** → Discord Service → Orchestrator Agent
2. **Web UI Actions** → Management Dashboard → Orchestrator Agent API
3. **Provisioning Logic** → Orchestrator Agent → Service Core
4. **Resource Management** → Service Core → Infrastructure
5. **Monitoring & Webhooks** → All Services → External Systems

---

## CI/CD PIPELINE STRATEGY

### Build Matrix

| Service | Language | Build Tool | Test Framework | Container |
|---------|----------|-----------|-----------------|-----------|
| service-core | Java 8+ | Maven | JUnit | Official Maven image |
| orchestrator-agent | Python 3.9+ | pip | pytest | python:3.9 |
| discord-service | Node.js | npm | Jest | node:18 |
| management-dashboard | TypeScript | Vite | Vitest | node:18 |

### Pipeline Stages

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│  Trigger │→ │  Lint &  │→ │   Test   │→ │  Build   │→ │ Publish  │
│  (Push)  │  │  Format  │  │          │  │ Artifact │  │ Docker   │
└──────────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘
                    ↑                            ↑              ↑
                    │                            │              │
              (Service-specific)         (Matrix builds)   (On tag/main)
```

---

## IMPLEMENTATION ROADMAP

### Phase 1: Structural Migration (Week 1)
- [ ] Create `/services` directory structure
- [ ] Move services to new paths
- [ ] Update import paths and configurations
- [ ] Create `.github/workflows` directory
- [ ] Set up Docker build matrix

### Phase 2: Documentation (Week 2)
- [ ] Create `/docs` structure
- [ ] Write architecture documentation
- [ ] Write setup guides
- [ ] Write API documentation
- [ ] Create troubleshooting guide

### Phase 3: CI/CD Implementation (Week 2-3)
- [ ] Create service-specific workflows
- [ ] Set up docker-publish.yml
- [ ] Configure branch protections
- [ ] Set up PR automation

### Phase 4: DevOps Infrastructure (Week 3-4)
- [ ] Create docker-compose files
- [ ] Create Kubernetes manifests
- [ ] Set up monitoring stack
- [ ] Document deployment procedures

### Phase 5: Testing & Validation (Week 4)
- [ ] Test all pipelines
- [ ] Verify configurations
- [ ] Create migration guide
- [ ] Update CONTRIBUTING.md

---

