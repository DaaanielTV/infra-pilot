# Infra Pilot

[![CI](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml/badge.svg)](https://github.com/drosemann/infra-pilot/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-0%25-brightgreen)](https://github.com/drosemann/infra-pilot)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A tool to manage your servers from terminal, web, or Discord.

## Table of Contents

- [Quick Start](#quick-start)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

```bash
git clone https://github.com/drosemann/infra-pilot.git
cd infra-pilot && cp .env.example .env
docker compose up -d
```

## Usage

```bash
ipilot server list
ipilot server create myapp --type nodejs --memory 1024
```

## Documentation

Full documentation is available in the [wiki](wiki/Home.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
