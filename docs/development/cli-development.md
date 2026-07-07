# CLI Development Guide

## Architecture Overview

```
cli/ipilot/
├── main.py                    # Typer entry point with global commands
├── core/
│   ├── cli.py                 # App factory, legacy bridge, get_client
│   └── command_registry.py    # @register decorator, attach_to_app
├── commands/                  # Organized command modules
│   ├── __init__.py            # Registers all command groups
│   ├── infrastructure/        # server, backup, deploy, logs
│   ├── edge_computing/        # edge, fn, ml, iot, cdn, mesh, gw, pipeline
│   ├── green/                 # energy, carbon, scheduler, reclaim, etc.
│   ├── networking/            # sdwan, vpn, dns, bgp, proxy, etc.
│   ├── security/              # oidc, webauthn, pam, soc, etc.
│   ├── aiops/                 # rca, dem, alert, scaling, etc.
│   ├── finops/                # commitment, spot, budget, etc.
│   ├── cx/                    # health, ticket, nps, etc.
│   ├── marketplace/           # trade, appmarket, plans, etc.
│   ├── platform/              # devportal, scaffold, scorecards, etc.
│   ├── compliance_v2/         # cc, evidence, attest, etc.
│   └── emerging/              # blockchain, quantum, zkp, etc.
├── client.py                  # ApiClient (requests-based HTTP client)
├── config.py                  # Config with profile support
└── output/
    ├── formatters.py          # JSON, YAML, Table, Plain output
    └── styling.py             # Rich terminal output
```

## Adding a New Command

### 1. Create the command module

Create a new file in the appropriate domain directory:

```python
# cli/ipilot/commands/infrastructure/example.py
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Example commands")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def list(ctx: typer.Context):
    """List all examples"""
    client = _get_client(ctx)
    result = client.list_examples()
    print_output(result, ctx.obj.get("output", "table"))
```

### 2. Register the command

In `cli/ipilot/commands/__init__.py`:

```python
from .infrastructure.example import app as example_app
register("example", "Example commands")(example_app)
```

### 3. Add API method to client.py

```python
def list_examples(self):
    return self._request("GET", "/examples")
```

## Best Practices

1. **One command per file** - Each file should be a single Typer app with related commands
2. **Use `_get_client(ctx)` helper** - Avoid repeating connection logic
3. **Use `print_output`** - All output goes through formatters for consistent --output support
4. **Type hints on parameters** - Typer uses them for validation and help text
5. **Descriptive help strings** - Users rely on `--help` output
6. **Handle list responses** - Use `isinstance(result, _list_type)` to normalize API responses
7. **Use the `register` decorator** - Keeps command registration centralized

## Command Naming

- Use `_` in file names, `-` in CLI command names
  - File: `service_catalog.py` → CLI: `service-catalog`
  - File: `backup_sla.py` → CLI: `backup-sla`
- Flat commands should be verbs: `list`, `create`, `delete`, `status`
- Multi-word commands use `-`: `create-zone`, `add-record`

## Testing

```bash
# Run CLI tests
cd cli
pip install -e .
python -m pytest ../../tests/cli/ -v
```

## Legacy Bridge

The legacy bridge (`bridge/`) allows old argparse commands to work alongside new Typer commands. It wraps old `cmd_*` functions. Remove entries from the bridge as commands are natively rewritten.
