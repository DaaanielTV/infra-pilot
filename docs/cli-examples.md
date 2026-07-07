# CLI Examples

## Basics

```bash
ipilot --help
ipilot server list
ipilot server create myapp --type nodejs --memory 1024
ipilot server delete myapp
```

## Output Formats

```bash
ipilot server list --output json | jq '.[].name'
ipilot server list --output yaml
```

## Profiles & Config

```bash
ipilot --profile prod server list
ipilot config set api_url https://api.example.com
```

## Interactive Mode

```bash
ipilot interactive
# Then type: server list, energy current, etc.
```

## Batch Operations

```yaml
# ops.yaml
- command: server list
- command: energy current
- command: server create --name batch-server --type web --memory 2048
```

```bash
ipilot batch --file ops.yaml
```

## Shell Completion

```bash
ipilot completion install
```

## Common Workflows

```bash
# Check status
ipilot energy current
ipilot health

# Backups
ipilot backup create myapp
ipilot backup list

# Edge & IoT
ipilot edge list
ipilot iot codes --count 20

# Compliance
ipilot compliance scan SOC2
ipilot policy list

# FinOps
ipilot finops commitment list
ipilot finops budget create q3 --amount 50000 --period monthly

# AIOps
ipilot rca analyze incident-123
ipilot scaling predict web-service
```

## Piping

```bash
ipilot server list --output json | jq -r '.[].name'
ipilot edge list --output json | jq 'length'
ipilot server list --output json > servers.json
```
