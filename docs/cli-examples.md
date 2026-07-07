# CLI Examples

```bash
ipilot --help
ipilot server list
ipilot server create myapp --type nodejs --memory 1024
ipilot server delete myapp
ipilot server list --output json | jq '.[].name'
ipilot --profile prod server list
ipilot energy current
ipilot backup create myapp
ipilot edge list
ipilot rca analyze incident-123
ipilot completion install
ipilot interactive
```
