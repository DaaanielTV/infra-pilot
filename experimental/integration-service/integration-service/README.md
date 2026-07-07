# Integration Service

Cross-platform integration features.

## Features

- **Auth:** JWT, OAuth2 (Discord, Minecraft), API keys, 2FA/TOTP
- **Users:** Unified profiles, account linking, role sync
- **Messaging:** Discord↔Minecraft message bridge, webhook support
- **Notifications:** Email, webhook, Telegram; preferences, digests
- **Backups:** Cross-service coordination, atomic restore, verification
- **Resources:** Pool management, allocation tracking, optimization
- **Logging:** Centralized aggregation, search, server log integration
- **Monitoring:** Cross-service view, alert correlation, maintenance windows

## Quick Start

```bash
pip install -r requirements.txt
python src/api.py
```

## Environment

`dashboard_url`, `discord_api_url`, `orchestrator_url`, `jwt_secret`, various service URLs

## API Endpoints

| Group | Endpoints |
|-------|-----------|
| Auth | `/api/auth/login`, `/verify`, `/api-key`, `/oauth2/*`, `/2fa/*` |
| Users | `/api/users/*` — CRUD, profiles, linking, sync |
| Notifications | `/api/notifications/*` — send, preferences, digest |
| Messaging | `/api/messaging/bridge`, `/webhook/*`, `/convert` |
| Backups | `/api/backups/*` — create, restore, verify, cross-service |
| Resources | `/api/resources/*` — allocate, pools, sync, trends |
| Logs | `/api/logs/search`, `/cross-platform`, `/server/*` |
| Config | `/api/config/*` — get, update, rollback, diff, validate |
| Permissions | `/api/permissions/*` — check, grant, revoke, roles |
| Security | `/api/security/events`, `/alert` |
| Metrics | `/api/metrics` — dashboard, prometheus, statistics |
