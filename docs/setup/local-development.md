# Local Development Setup

Get the Infra Pilot platform running on your local machine in 15 minutes.

## ⚙️ Prerequisites

### System Requirements

- **OS:** Linux, macOS, Windows (WSL2)
- **Memory:** 4GB minimum (8GB recommended)
- **Disk:** 10GB free space
- **Network:** Internet access

### Software Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| Git | 2.30+ | Version control |
| Docker | 20.10+ | Containerization |
| Docker Compose | 1.29+ | Multi-container orchestration |
| Node.js | 18 LTS | Dashboard & Discord bot |
| Python | 3.9+ | Orchestrator agent |
| Java | 8+ | Service core |
| Maven | 3.6+ | Java build tool |

### Verify Installation

```bash
git --version              # Git 2.30+
docker --version           # Docker 20.10+
docker-compose --version   # Docker Compose 1.29+
node --version             # Node.js 18+
python3 --version          # Python 3.9+
java -version              # Java 8+
mvn --version              # Maven 3.6+
```

---

## 🚀 Quick Start (Docker Compose)

### Option A: Fastest (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/DaaanielTV/infra-pilot.git
cd infra-pilot

# 2. Start all services
docker-compose up -d

# 3. Wait for services to initialize (30-60 seconds)
sleep 60

# 4. Verify services are running
docker-compose ps

# 5. Access services
open http://localhost:5173  # Management Dashboard
```

### Option B: With Log Viewing

```bash
# Start services and view logs
docker-compose up

# In another terminal, view specific service logs
docker-compose logs -f orchestrator-agent
docker-compose logs -f management-dashboard
```

### Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| **Dashboard** | http://localhost:5173 | Web operations UI |
| **Orchestrator API** | http://localhost:8000 | API endpoint |
| **Service Core** | http://localhost:8080 | Server management |
| **PostgreSQL** | localhost:5432 | Database |
| **Redis** | localhost:6379 | Cache |

---

## 🛠️ Manual Setup (Local Development)

If you prefer running services locally without Docker:

### Step 1: Clone Repository

```bash
git clone https://github.com/DaaanielTV/infra-pilot.git
cd infra-pilot
```

### Step 2: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit configuration (adjust as needed)
nano .env
# or
code .env  # If using VS Code
```

**Key variables to configure:**

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/gemini
REDIS_URL=redis://localhost:6379

# Services
DASHBOARD_PORT=5173
ORCHESTRATOR_PORT=8000
SERVICE_CORE_PORT=8080

# External APIs (optional for development)
PTERODACTYL_API_KEY=your-key
DISCORD_BOT_TOKEN=your-token
```

### Step 3: Install Dependencies

#### Management Dashboard

```bash
cd services/management-dashboard
npm install
npm run dev
# Opens at http://localhost:5173
```

#### Orchestrator Agent

```bash
# In new terminal
cd services/orchestrator-agent
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
# Runs at http://localhost:8000
```

#### Discord Service

```bash
# In new terminal
cd services/discord-service
npm install
npm start
# Connects to Discord
```

#### Service Core (Java)

```bash
# In new terminal
cd services/service-core
mvn clean install
mvn spring-boot:run
# Runs at http://localhost:8080
```

### Step 4: Setup Databases

```bash
# Option A: Using Docker containers
docker pull postgres:15
docker run -d --name gemini-postgres \
  -e POSTGRES_USER=gemini \
  -e POSTGRES_PASSWORD=dev \
  -e POSTGRES_DB=gemini \
  -p 5432:5432 \
  postgres:15

docker pull redis:7
docker run -d --name gemini-redis \
  -p 6379:6379 \
  redis:7

# Option B: Install locally (macOS)
brew install postgresql redis
brew services start postgresql
brew services start redis
```

---

## 📝 Configuration

### Environment Variables

Create `.env` file in root directory:

```env
# Application
NODE_ENV=development
DEBUG=true

# Services
DASHBOARD_URL=http://localhost:5173
ORCHESTRATOR_URL=http://localhost:8000
SERVICE_CORE_URL=http://localhost:8080

# Database
DATABASE_URL=postgresql://gemini:dev@localhost:5432/gemini
DATABASE_POOL_SIZE=10

# Cache
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=dev-secret-key-change-in-production
CONVEX_DEPLOYMENT=dev

# External Services
PTERODACTYL_URL=https://panel.example.com
PTERODACTYL_API_KEY=ptl_xxxxx
DISCORD_BOT_TOKEN=your_token_here
DISCORD_WEBHOOK_SECRET=your_secret

# Monitoring
SENTRY_DSN=optional
LOG_LEVEL=debug
```

### Service-Specific Config

**Management Dashboard:** `services/management-dashboard/.env`
```env
VITE_API_URL=http://localhost:8000
VITE_CONVEX_URL=http://localhost:3210
```

**Orchestrator Agent:** `services/orchestrator-agent/.env`
```env
ORCHESTRATOR_PORT=8000
LOG_LEVEL=DEBUG
DATABASE_ECHO=true
```

---

## 🧪 Running Tests

### Test All Services

```bash
./scripts/test.sh
```

### Test Individual Services

```bash
# Dashboard tests
cd services/management-dashboard
npm run test
npm run test:watch  # Watch mode

# Orchestrator tests
cd services/orchestrator-agent
pytest tests/
pytest tests/ -v --cov  # With coverage

# Discord bot tests
cd services/discord-service
npm run test

# Service Core tests
cd services/service-core
mvn test
mvn test -DskipTests=false -Dtest=TestClass  # Specific test
```

---

## 🐛 Development Workflow

### 1. Creating a Feature

```bash
# Create feature branch from main
git checkout -b feature/my-feature

# Make changes in appropriate service
cd services/your-service

# Test locally
npm run test  # or pytest, mvn test

# Commit with clear message
git commit -m "feat: add new provisioning flow"

# Push and open PR
git push origin feature/my-feature
```

### 2. Debugging

#### Docker Containers

```bash
# View logs
docker-compose logs orchestrator-agent

# Enter container shell
docker-compose exec orchestrator-agent bash

# Restart service
docker-compose restart management-dashboard
```

#### Local Services

```bash
# Python debugging
import pdb; pdb.set_trace()

# Node.js debugging
node --inspect-brk=0.0.0.0:9229 main.js
# Connect inspector in Chrome: chrome://inspect

# Java debugging
mvn -Dagentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 spring-boot:run
# Connect in IDE to localhost:5005
```

#### Logs

```bash
# View all logs
docker-compose logs -f

# Filter by service
docker-compose logs -f orchestrator-agent

# Last 50 lines
docker-compose logs --tail=50 management-dashboard

# With timestamps
docker-compose logs -f --timestamps
```

---

## 🔄 Common Tasks

### Update Dependencies

```bash
# Dashboard
cd services/management-dashboard
npm update
npm audit fix

# Orchestrator
cd services/orchestrator-agent
pip list --outdated
pip install --upgrade package-name

# Service Core
cd services/service-core
mvn dependency:tree
mvn versions:display-dependency-updates
```

### Database Operations

```bash
# Connect to PostgreSQL
psql -h localhost -U gemini -d gemini
# Password: dev

# View tables
\dt

# Backup database
pg_dump -h localhost -U gemini -d gemini > backup.sql

# Restore database
psql -h localhost -U gemini -d gemini < backup.sql
```

### Clear Cache & Rebuild

```bash
# Stop all services
docker-compose down

# Remove volumes (careful - deletes data)
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# Start fresh
docker-compose up -d
```

### Monitor Resource Usage

```bash
# Docker stats
docker stats

# System resources
top          # macOS/Linux
Get-Process  # Windows
```

---

## 🆘 Troubleshooting

### Service Won't Start

```bash
# Check port is available
lsof -i :5173      # Dashboard
lsof -i :8000      # Orchestrator
lsof -i :8080      # Service Core
lsof -i :5432      # Database

# Kill process on port
kill -9 $(lsof -t -i:5173)

# Rebuild and restart
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Database Connection Issues

```bash
# Test connection
psql -h localhost -U gemini -d gemini -c "SELECT 1;"

# Reset database
docker-compose down -v
docker-compose up -d
```

### Memory Issues

```bash
# Increase Docker memory
# macOS: Docker > Preferences > Resources > Memory
# Linux: Check available memory: free -h

# Reduce container resource limits in docker-compose.yml
services:
  orchestrator-agent:
    deploy:
      resources:
        limits:
          memory: 1G
```

### API Connection Issues

```bash
# Test API endpoint
curl http://localhost:8000/health

# Check service is running
docker-compose ps

# View logs
docker-compose logs orchestrator-agent
```

---

## 📚 Additional Resources

- [Docker Deployment](docker-setup.md) - Production Docker setup
- [Development Workflow](../development/development-workflow.md) - Contributing guidelines
- [Testing Strategy](../development/testing-strategy.md) - Testing best practices
- [Troubleshooting](../operations/troubleshooting.md) - Advanced troubleshooting

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Dashboard loads at http://localhost:5173
- [ ] Can login to dashboard
- [ ] Orchestrator API responds to `curl http://localhost:8000/health`
- [ ] Can view services in dashboard
- [ ] Database connection works
- [ ] All tests pass: `./scripts/test.sh`

If all checks pass, you're ready to develop! 🎉

---

**Last Updated:** April 2026
