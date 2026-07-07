# Infra Pilot

Lets you manage servers from your terminal, a web dashboard, or Discord.

```bash
git clone https://github.com/DaaanielTV/infra-pilot.git
cd infra-pilot
cp .env.example .env
docker compose up -d
```

Then:

```bash
ipilot server list
ipilot server create myapp --type nodejs --memory 1024
ipilot --help
```

MIT
