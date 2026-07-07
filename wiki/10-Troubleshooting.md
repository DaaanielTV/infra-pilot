# Troubleshooting

## CLI & Connection

| Error | Fix |
|-------|-----|
| `Connection refused` | API not running — `docker compose ps`, check URL with `ipilot config get` |
| `Unauthorized` | `ipilot login <api-key>` again |
| `404 Not Found` | Update to latest version |

## Docker Stack

| Problem | Fix |
|---------|-----|
| Container restarting | Missing `.env` vars — copy `.env.example` |
| `port is already allocated` | Stop conflicting containers or override ports |
| PostgreSQL unreachable | Check `docker compose logs postgres` |

## Discord Bot

| Problem | Fix |
|---------|-----|
| Bot not responding | Check `DISCORD_TOKEN` in `.env` |
| Missing Gateway Intents | Enable all 3 intents in Discord Developer Portal |

## AI Features

| Problem | Fix |
|---------|-----|
| AI not responding | Check `AI_API_ENDPOINT` and `AI_API_KEY` |
| "Model not found" | Set `AI_MODEL` to an available model |

## Logs

```bash
docker compose logs --tail=100 -f
docker compose logs orchestrator-agent --tail=50 -f
```

## Support

- [Issues](https://github.com/drosemann/infra-pilot/issues)
- [Discussions](https://github.com/drosemann/infra-pilot/discussions)
- Security: see [SECURITY.md](https://github.com/drosemann/infra-pilot/blob/main/SECURITY.md)
