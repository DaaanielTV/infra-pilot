# Configuration

## CLI Config (`~/.ipilot/config.json`)

```json
{ "api_url": "http://localhost:3001", "api_key": null, "output_format": "table" }
```

```bash
ipilot config set api_url http://localhost:3001
ipilot config set output_format json
```

## Environment (`.env`)

```bash
cp .env.example .env
```

Key groups: Discord (`DISCORD_TOKEN`), Database (`DATABASE_URL`), AI/LLM (`AI_API_KEY`, `AI_MODEL`), Security (`JWT_SECRET`, `CORS_ORIGIN`).

Full reference: [`.env.example`](https://github.com/drosemann/infra-pilot/blob/main/.env.example)

## Multi-Provider

Provider-neutral mapping at `infra/naming/provider_map.yaml` maps to AWS, Azure, Hetzner, etc.

---

*[.env.example](https://github.com/drosemann/infra-pilot/blob/main/.env.example)*
