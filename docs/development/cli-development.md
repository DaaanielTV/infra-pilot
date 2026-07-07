# CLI Development

Add a file in the domain directory:

```python
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output
import typer

app = typer.Typer()

def _get_client(ctx):
    cfg = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(cfg["api_url"], cfg["token"])

@app.command()
def list(ctx: typer.Context):
    print_output(_get_client(ctx).list_examples(), ctx.obj.get("output", "table"))
```

Register in `commands/__init__.py`:

```python
from .infrastructure.example import app as example_app
register("example", "Example commands")(example_app)
```

Add to `client.py`:

```python
def list_examples(self):
    return self._request("GET", "/examples")
```
