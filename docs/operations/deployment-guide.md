# Production Deployment Guide

Deploy Gemini to production environments with confidence.

## 🚀 Deployment Options

### Option 1: Docker Compose (Suitable for small-to-medium deployments)

**Pros:** Simple, all-in-one  
**Cons:** Single point of failure, harder to scale

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Option 2: Kubernetes (Recommended for production)

**Pros:** High availability, auto-scaling, self-healing  
**Cons:** Higher complexity

```bash
kubectl apply -f infrastructure/kubernetes/namespace.yaml
kubectl apply -f infrastructure/kubernetes/deployments/
kubectl apply -f infrastructure/kubernetes/services/
kubectl apply -f infrastructure/kubernetes/ingress.yaml
```

### Option 3: Terraform + Cloud Provider

**Pros:** Infrastructure as code, repeatable, multi-region  
**Cons:** Cloud provider knowledge required

```bash
cd infrastructure/terraform/aws
terraform init
terraform plan
terraform apply
```

---

## 🔐 Pre-Deployment Checklist

- [ ] All tests passing in CI/CD
- [ ] Code reviewed and approved
- [ ] Secrets configured (API keys, tokens)
- [ ] Database backed up
- [ ] SSL/TLS certificates configured
- [ ] Monitoring and alerting set up
- [ ] Rollback plan documented
- [ ] Change logged and approved

---

## 🐳 Docker Compose Production Deployment

### Prerequisites

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Deployment Steps

#### 1. Prepare Server

```bash
# SSH into production server
ssh user@production-server.com

# Create project directory
mkdir -p /opt/gemini
cd /opt/gemini

# Clone repository
git clone https://github.com/DaaanielTV/infra-pilot.git .
```

#### 2. Configure Environment

```bash
# Copy and edit production environment
cp .env.example .env.prod

# Edit configuration
nano .env.prod
```

**Production .env.prod example:**
```env
NODE_ENV=production
DEBUG=false

# Services
DASHBOARD_URL=https://your-domain.com
ORCHESTRATOR_URL=https://api.your-domain.com
SERVICE_CORE_URL=https://core.your-domain.com

# Database (use managed service if possible)
DATABASE_URL=postgresql://user:password@db.your-domain.com:5432/gemini
DATABASE_POOL_SIZE=20
DATABASE_SSL=true

# Redis cluster
REDIS_URL=redis://redis-cluster.your-domain.com:6379

# Secrets
JWT_SECRET=generate-strong-random-key
CONVEX_DEPLOYMENT=production

# External Services
PTERODACTYL_API_KEY=your-key
DISCORD_BOT_TOKEN=your-token
SENTRY_DSN=https://your-sentry-dsn

# Security
ALLOWED_ORIGINS=https://your-domain.com,https://app.your-domain.com
SSL_CERT_PATH=/etc/ssl/certs/your-cert.crt
SSL_KEY_PATH=/etc/ssl/private/your-key.key
```

#### 3. Start Services

```bash
# Pull latest images
docker-compose -f docker-compose.prod.yml pull

# Start services
docker-compose -f docker-compose.prod.yml up -d

# Verify services
docker-compose -f docker-compose.prod.yml ps
```

#### 4. Verify Deployment

```bash
# Check service health
curl https://your-domain.com/health
curl https://api.your-domain.com/health

# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Check resource usage
docker stats
```

---

## ☸️ Kubernetes Deployment

### Prerequisites

```bash
# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Access to Kubernetes cluster (AWS EKS, GCP GKE, Azure AKS, etc)
```

### Deployment Steps

#### 1. Create Namespace

```bash
kubectl create namespace gemini
kubectl label namespace gemini environment=production
```

#### 2. Create Secrets

```bash
# Database credentials
kubectl create secret generic db-credentials \
  --from-literal=username=gemini \
  --from-literal=password=$(openssl rand -base64 32) \
  -n gemini

# API keys and tokens
kubectl create secret generic api-keys \
  --from-literal=jwt-secret=$(openssl rand -base64 32) \
  --from-literal=discord-token=your-token \
  --from-literal=pterodactyl-key=your-key \
  -n gemini

# TLS certificates (if not using cert-manager)
kubectl create secret tls tls-secret \
  --cert=path/to/cert.crt \
  --key=path/to/key.key \
  -n gemini
```

#### 3. Deploy Services

```bash
# Apply all manifests
kubectl apply -f infrastructure/kubernetes/

# Wait for deployments
kubectl rollout status deployment -n gemini

# Check pod status
kubectl get pods -n gemini
```

#### 4. Set Up Ingress

```bash
# If using Nginx Ingress
kubectl apply -f infrastructure/kubernetes/ingress.yaml

# Get LoadBalancer IP
kubectl get svc -n gemini
```

---

## 🌍 Multi-Region Deployment

### Strategy

```
┌─────────────────┐     ┌─────────────────┐
│   Region 1      │     │   Region 2      │
│  (us-east-1)    │     │  (eu-west-1)    │
│   Cluster 1     │     │   Cluster 2     │
└────────┬────────┘     └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     ▼
           ┌─────────────────┐
           │  Global LB      │
           │  (DNS failover) │
           └─────────────────┘
```

### Implementation

```bash
# Deploy to region 1
export KUBECONFIG=~/.kube/config-region1
kubectl apply -f infrastructure/kubernetes/

# Deploy to region 2
export KUBECONFIG=~/.kube/config-region2
kubectl apply -f infrastructure/kubernetes/

# Configure global load balancer (AWS Route53, Azure Traffic Manager, etc)
# Set up DNS failover policies
```

---

## 📊 Monitoring Deployment

### Prometheus

```bash
# Check metrics
kubectl port-forward -n gemini svc/prometheus 9090:9090
# Navigate to http://localhost:9090
```

### Grafana

```bash
# Access Grafana
kubectl port-forward -n gemini svc/grafana 3000:3000
# Navigate to http://localhost:3000
# Default credentials: admin/admin
```

### Logs

```bash
# View service logs
kubectl logs -n gemini deployment/orchestrator-agent -f

# View all logs
kubectl logs -n gemini --all-containers=true -f
```

---

## 🔄 Updates & Rollbacks

### Rolling Update

```bash
# Update image
kubectl set image deployment/orchestrator-agent \
  orchestrator-agent=your-registry/orchestrator:v1.1.0 \
  -n gemini

# Monitor rollout
kubectl rollout status deployment/orchestrator-agent -n gemini

# View history
kubectl rollout history deployment/orchestrator-agent -n gemini
```

### Rollback

```bash
# Rollback to previous version
kubectl rollout undo deployment/orchestrator-agent -n gemini

# Rollback to specific revision
kubectl rollout undo deployment/orchestrator-agent --to-revision=3 -n gemini
```

### Zero-Downtime Deployment

Set in deployment manifest:
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

---

## 🔐 Security Hardening

### Network Policies

```bash
kubectl apply -f infrastructure/kubernetes/network-policies/
```

### Pod Security Policies

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'projected'
    - 'secret'
    - 'downwardAPI'
    - 'persistentVolumeClaim'
  hostNetwork: false
  hostIPC: false
  hostPID: false
  runAsUser:
    rule: 'MustRunAsNonRoot'
  seLinux:
    rule: 'MustRunAs'
  fsGroup:
    rule: 'MustRunAs'
  readOnlyRootFilesystem: false
```

### Resource Limits

```yaml
resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: 1000m
    memory: 1Gi
```

---

## 🆘 Troubleshooting Deployment

### Service Won't Start

```bash
# Check pod status
kubectl describe pod <pod-name> -n gemini

# Check logs
kubectl logs <pod-name> -n gemini

# Check events
kubectl get events -n gemini --sort-by='.lastTimestamp'
```

### Connectivity Issues

```bash
# Test DNS
kubectl run -it --image=busybox:1.28 --restart=Never --rm debug -- nslookup kubernetes.default

# Test network policies
kubectl port-forward service/orchestrator-agent 8000:8000 -n gemini
```

### Database Connectivity

```bash
# Test connection from pod
kubectl run -it --image=postgres:15 --restart=Never --rm -- \
  psql postgresql://user:password@db-host:5432/gemini -c "SELECT 1;"
```

---

## 📈 Performance Tuning

### Database Connection Pooling

```env
DATABASE_POOL_SIZE=20
DATABASE_POOL_IDLE_TIMEOUT=300
DATABASE_MAX_LIFETIME=1800
```

### Cache Configuration

```env
REDIS_POOL_SIZE=10
REDIS_TIMEOUT=5000
```

### Service Replicas

```yaml
replicas: 3  # Increase for higher load
```

---

## 📚 Related Documentation

- [Kubernetes Setup](../setup/kubernetes-deploy.md)
- [Monitoring & Observability](monitoring-observability.md)
- [Scaling Strategy](scaling-strategy.md)
- [Troubleshooting](troubleshooting.md)

---

**Last Updated:** April 2026
