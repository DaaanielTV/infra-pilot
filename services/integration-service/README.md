# Integration Service

Cross-platform integration features for Infra Pilot.

## Features

- Unified User Management
- Integrated Monitoring
- Cross-Service Operations
- Shared Configuration
- Unified Logging
- Backup & Reporting

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the service
python src/api.py

# Or run specific modules
python src/integration.py
python src/backup.py
python src/resource_tracker.py
```

## Environment Variables

- `DASHBOARD_URL` - Management dashboard URL
- `DISCORD_API_URL` - Discord service URL
- `SERVICE_CORE_URL` - Service Core URL
- `ORCHESTRATOR_URL` - Orchestrator agent URL
- `DISCORD_WEBHOOK` - Discord webhook URL
- `INTEGRATION_SERVICE_URL` - This service URL

## API Endpoints

- `GET /` - Service info
- `GET /health` - Health check
- `POST /api/users` - Create user
- `GET /api/users/{email}` - Get user profile
- `PUT /api/users/{email}` - Update user
- `POST /api/notifications` - Send notification
- `POST /api/notifications/server-event` - Server event notification
- `GET /api/metrics` - Get metrics
- `GET /api/metrics/dashboard` - Unified dashboard metrics
- `GET /api/config` - Get shared config
- `PUT /api/config` - Update shared config

## Branding
- Cosmic Infra branding is the unified identity used across Infra Pilot. Tokens: Primary #6C5CE7, Secondary #EC4899, Accent #22D3EE.
- Alternate logo variants exist and can be surfaced via branding assets. A simple selector is exposed in the management panel to switch variants at runtime.
- Cosmic Infra branding is the unified identity used across Infra Pilot. Tokens: Primary #6C5CE7, Secondary #EC4899, Accent #22D3EE.
- This service participates in branding across the UI and docs. Logo variants exist and can be surfaced through shared branding assets.
