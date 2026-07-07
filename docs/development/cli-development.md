# CLI Development

## Adding a Command

Create a file in the domain directory:

```python
# commands/infrastructure/example.py
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Example commands")

def _get_client(ctx) -> ApiClient:
    cfg = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(cfg["api_url"], cfg["token"])

@app.command()
def list(ctx: typer.Context):
    """List all examples"""
    print_output(_get_client(ctx).list_examples(), ctx.obj.get("output", "table"))
```

Register in `commands/__init__.py`:

```python
from .infrastructure.example import app as example_app
register("example", "Example commands")(example_app)
```

Add API method in `client.py`:

```python
def list_examples(self):
    return self._request("GET", "/examples")
```

## Rules

- One Typer app per file
- Use `_get_client(ctx)` helper
- Use `print_output` for consistent `--output` support
- Use `_` in filenames, `-` in CLI commands: `service_catalog.py` → `service-catalog`
- Flat commands are verbs: `list`, `create`, `delete`, `status`

## Testing

```bash
cd cli
pip install -e .
python -m pytest ../../tests/cli/ -v
```

## Legacy Bridge

Old argparse commands are wrapped in `bridge/` for backward compatibility. Remove entries as commands are natively rewritten.
