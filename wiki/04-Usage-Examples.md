# Usage Examples

## Create a Server and View Logs

```bash
ipilot server create --name web-prod --type web --memory 4096
ipilot logs <id> --lines 50 --follow
```

## Backups

```bash
ipilot backup create <id>
ipilot backup list <id>
```

## DNS

```bash
ipilot dns create-zone --domain example.com --ttl 3600
ipilot dns add-record --zone-id <id> --name www --type A --value 192.168.1.1
```

## Green Computing (Energy & Carbon)

```bash
ipilot energy current
ipilot carbon current
ipilot provider rank
```

## FinOps (Cost Optimization)

```bash
ipilot reclaim scan
ipilot shutdown create --name "night-shutdown" --tags "env:staging" --shutdown-hours "20:00-08:00"
```

---

*See [CLI Reference](05-CLI-Reference) for all available commands.*
