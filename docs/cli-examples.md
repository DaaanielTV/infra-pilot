# CLI Examples

## Basic Usage

```bash
# Get help
ipilot --help
ipilot server --help
ipilot server list --help

# Check version
ipilot version
```

## Server Management

```bash
# List servers
ipilot server list

# List servers as JSON (pipe-friendly)
ipilot server list --output json

# Filter with jq
ipilot server list --output json | jq '.[].name'

# Create a server
ipilot server create myapp --type nodejs --memory 1024

# Check server status
ipilot server status myapp

# Delete a server
ipilot server delete myapp
```

## Backup & Logs

```bash
# List backups for a server
ipilot backup list myapp

# Create a backup
ipilot backup create myapp

# Fetch logs (last 100 lines)
ipilot logs fetch myapp --lines 100
```

## Edge Computing

```bash
# List edge devices
ipilot edge list

# Register a new edge device
ipilot edge register sensor-01 raspberry_pi aa:bb:cc:dd:ee:ff

# Deploy an edge function
ipilot fn deploy process-video wasm device-01 https://example.com/func.wasm handler

# List ML models
ipilot ml models

# Deploy ML model
ipilot ml deploy model-v2 tflite device-01 2.0

# Generate IoT claim codes
ipilot iot codes --count 20 --ttl 48
```

## Green Computing

```bash
# View current energy consumption
ipilot energy current

# View energy history (last 48 hours)
ipilot energy history --hours 48

# Monthly energy summary
ipilot energy summary --period monthly

# Check carbon footprint
ipilot carbon current

# Get green energy forecast
ipilot green forecast

# Find idle resources
ipilot reclaim scan
```

## Networking

```bash
# List SD-WAN links
ipilot sdwan status

# Create VPN config
ipilot vpn create office-vpn wireguard vpn-server-01

# List DNS zones
ipilot dns zones

# Add DNS record
ipilot dns add-record zone-01 A www 192.168.1.1

# List BGP sessions
ipilot bgp sessions

# Start packet capture
ipilot capture start eth0 --filter "port 443"
```

## Security

```bash
# List OIDC clients
ipilot oidc clients

# Register PAM access request
ipilot pam request prod-server "Deploying hotfix"

# Approve PAM request
ipilot pam approve req-123

# List compliance policies
ipilot policy list

# Run compliance scan
ipilot compliance scan SOC2

# List audit anomalies
ipilot audit anomalies
```

## AIOps

```bash
# Analyze root cause
ipilot rca analyze incident-123

# Create a DEM monitor
ipilot dem create my-site https://example.com --interval 60

# Predict scaling needs
ipilot scaling predict web-service

# Get health forecast
ipilot health-f forecast service-01

# Chat with ops assistant
ipilot assistant message "What's the status of prod?"
```

## FinOps

```bash
# List commitment discounts
ipilot finops commitment list

# Find cost anomalies
ipilot finops anomaly list

# Create a budget
ipilot finops budget create q3-budget --amount 50000 --period monthly

# Get rightsizing recommendations
ipilot finops rightsizing list

# Scan for waste
ipilot finops waste scan
```

## Customer Experience

```bash
# List customer health
ipilot cx health list

# Get customer health details
ipilot cx health get cust-123

# Create support ticket
ipilot cx ticket create cust-123 "Login issue" "User cannot log in" --priority high

# Check NPS score
ipilot cx nps score survey-456
```

## Platform Engineering

```bash
# List developer portal APIs
ipilot devportal list

# Scaffold a new project
ipilot scaffold generate node-express my-api

# List service catalog
ipilot service-catalog list

# Register API in catalog
ipilot api-catalog register payments v1 openapi.yaml
```

## Configuration

```bash
# View current config
ipilot config get

# Set config value
ipilot config set api_url https://api.example.com

# Use a named profile
ipilot --profile prod server list

# Output formats
ipilot server list --output json
ipilot server list --output yaml
ipilot server list --output plain
```

## Advanced

### Interactive Mode
```bash
ipilot interactive
# Then type commands directly:
# server list
# energy current
# exit
```

### Batch Operations
```yaml
# operations.yaml
operations:
  - command: server list
    args: {}
  - command: energy current
    args: {}
  - command: server create
    args:
      name: batch-server
      type: web
      memory: 2048
```

```bash
ipilot batch --file operations.yaml
```

### Piping
```bash
# Get server names only
ipilot server list --output json | jq -r '.[].name'

# Count edge devices
ipilot edge list --output json | jq 'length'

# Export to file
ipilot server list --output json > servers.json
```

### Shell Completion
```bash
# Install completion for current shell
ipilot completion install

# Generate completion script for specific shell
ipilot completion bash --install
ipilot completion zsh --install
ipilot completion fish --install
ipilot completion powershell --install
```

### Documentation Generation
```bash
# Generate CLI reference docs
ipilot docs --output docs/cli-reference.md
```
