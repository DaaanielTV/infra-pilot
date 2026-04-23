# Discord Server Creator Bot

Create and provision Pterodactyl servers from Discord workflows.

## Features

- Multiple server templates (Minecraft, Node.js, TeamSpeak, Database, Python).
- User registration and validation flow.
- Automated Pterodactyl user/server creation.
- Optional role assignment after provisioning.
- Configurable per-user server limits.

## Prerequisites

- Node.js 18+
- npm
- A Discord bot application
- A reachable Pterodactyl panel

## Branding
- Cosmic Infra branding is applied across the Infra Pilot UI. Tokens: Primary #6C5CE7, Secondary #EC4899, Accent #22D3EE.
- Logo variants are available, with a simple selector implemented in the management panel to switch between default and alt IP lockup designs.
- UI elements reuse the branding tokens for consistency (buttons, inputs, cards).

## Installation

```bash
npm install
cp .env.example .env
```

Update `.env` with your credentials and IDs.

## Usage

```bash
node index.js
```

Then run `/server create` in your configured channel.

## Configuration

Environment variables include:

- `DISCORD_TOKEN`
- `PTERODACTYL_API_URL`
- `PTERODACTYL_API_KEY`
- `SERVER_CREATION_CHANNEL_ID`
- `SERVER_CREATOR_ROLE_ID`
- `MAX_SERVERS_PER_USER`
- `MINECRAFT_EGG_ID`, `NODEJS_EGG_ID`, `TEAMSPEAK_EGG_ID`, `DATABASE_EGG_ID`, `PYTHON_EGG_ID`
- `LOCATION_ID`

## License

This module is distributed under the repository GPLv3 license.
