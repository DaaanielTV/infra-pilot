# Configuration

## CLI Config (`~/.ipilot/config.json`)

This file stores your settings:

```json
{ "api_url": "http://localhost:3001", "api_key": null, "output_format": "table" }
```

```bash
ipilot config set api_url http://localhost:3001
ipilot config set output_format json
```

## Environment File (`.env`)

Copy the example file and fill it in:

```bash
cp .env.example .env
```

Main groups: Discord (`DISCORD_TOKEN`), Database (`DATABASE_URL`), AI/LLM (`AI_API_KEY`, `AI_MODEL`), Security (`JWT_SECRET`, `CORS_ORIGIN`).

Full list: [`.env.example`](https://github.com/drosemann/infra-pilot/blob/main/.env.example)

## Multiple Cloud Providers

The file `infra/naming/provider_map.yaml` maps names to AWS, Azure, Hetzner, etc.

---

*[.env.example](https://github.com/drosemann/infra-pilot/blob/main/.env.example)*
