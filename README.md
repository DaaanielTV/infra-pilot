# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Your infrastructure, one command away.**

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
pip install ./cli
ipilot login <your-api-key>
```
