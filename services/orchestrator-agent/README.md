# VPS Automation Bot

Python-based automation bot for VPS lifecycle and host monitoring tasks.

## Features

- Administrative command handlers for VPS operations.
- Resource monitoring helpers.
- Docker-based runtime option.
- Optional anti-crypto abuse helper script (`anti.sh`).

## Installation

### Manual

```bash
pip install -r requirements.txt
docker build -t ubuntu-22.04-with-tmate .
python3 bot.py
```

> Configure your bot token and required runtime settings before startup.

### Automated

Run the local installer script:

```bash
bash install.sh
```

## Supported OS Targets

| Version | Status |
| ------- | ------ |
| Ubuntu 22.04 | ✅ |
| Debian 12 | ✅ |
| Ubuntu 20.04 | ✅ |
| Debian 11 | ✅ |

## Security

If you identify a vulnerability, report it privately to maintainers.

## Branding
- Cosmic Infra branding is the unified identity used across Infra Pilot. Tokens: Primary #6C5CE7, Secondary #EC4899, Accent #22D3EE.
- Alternate logo variants exist and can be surfaced via branding assets. A simple selector is exposed in the management panel to switch variants at runtime.
- Cosmic Infra branding is the unified identity for Infra Pilot. Tokens: Primary #6C5CE7, Secondary #EC4899, Accent #22D3EE. Logo variants available via branding assets.
