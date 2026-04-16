# Infra Pilot

Infra Pilot is a multi-component repository for game/server operations tooling, automation bots, and an admin panel prototype.

## Project Overview

This repository currently contains:

- `servermanager/`: Java plugin-style server management module.
- `VPS-MAKER-BOT/`: Python bot for VPS-related automation workflows.
- `discord-bot-hosting-club/`: Node.js Discord bot for server provisioning flows.
- `panel_implementation/`: Convex + Vite React web panel prototype.

## Features / Purpose

- Automate routine infrastructure tasks from Discord and bot workflows.
- Provide a customizable server-management foundation for hosted workloads.
- Experiment with a modern web control panel for configuration and visibility.
- Keep components modular so each can be run independently.

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd infra-pilot
```

Install dependencies per component:

```bash
# Java module (Maven)
cd servermanager && mvn -q -DskipTests package

# Python bot
cd ../VPS-MAKER-BOT && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Node.js Discord bot
cd ../discord-bot-hosting-club && npm install

# Web panel
cd ../panel_implementation && npm install
```

## Usage

Run components independently as needed:

```bash
# Python bot
cd VPS-MAKER-BOT && python3 bot.py

# Node.js Discord bot
cd discord-bot-hosting-club && node index.js

# Web panel (frontend + Convex)
cd panel_implementation && npm run dev
```

## Development Setup

- Use Python 3.10+ for Python bot workflows.
- Use Node.js 18+ for JavaScript/TypeScript components.
- Use Java 17 + Maven for `servermanager`.
- Copy environment templates before local runs:

```bash
cp discord-bot-hosting-club/.env.example discord-bot-hosting-club/.env
```

## Configuration

Key environment variables live in `discord-bot-hosting-club/.env`:

- `DISCORD_TOKEN`
- `PTERODACTYL_API_URL`
- `PTERODACTYL_API_KEY`
- `SERVER_CREATION_CHANNEL_ID`
- `SERVER_CREATOR_ROLE_ID`
- `MAX_SERVERS_PER_USER`

Additional component-specific configuration:

- Java plugin config: `servermanager/src/main/resources/config.yml`
- Convex auth/backend config: `panel_implementation/convex/`

## Build / Run Instructions

Build artifacts should be generated locally, not committed:

```bash
# Java artifact
cd servermanager && mvn package

# Frontend production build
cd ../panel_implementation && npm run build
```

For Debian package content previously committed under `VPS-MAKER-BOT/deb/`, regenerate it from packaging scripts or CI pipelines instead of storing binaries in git.

## Troubleshooting

- **Bot fails to start**: verify required env vars are set and valid.
- **Discord commands not visible**: ensure bot has correct scopes/permissions and command registration completed.
- **Panel cannot load backend data**: verify Convex deployment credentials/config.
- **Maven build errors**: confirm Java 17 is active (`java -version`).

## Open Source Policies

- License: GNU GPLv3 (`LICENSE`)
- Contributing guide: `CONTRIBUTING.md`
- Code of conduct: `CODE_OF_CONDUCT.md`
