import builtins
import json
from typing import Any
import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

_list_type = builtins.list
app = typer.Typer(help="Policy management")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(
    ctx: typer.Context,
    output: str = typer.Option(None, "--output", "-o", help="Output format"),
):
    """List governance policies"""
    client = _get_client(ctx)
    result = client.policy_list()
    data = result if isinstance(result, _list_type) else result.get("policies", result)
    print_output(data, output or ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Policy name"),
    rules: str = typer.Option(..., "--rules", "-r", help="JSON rules"),
):
    """Create a governance policy"""
    client = _get_client(ctx)
    parsed = json.loads(rules)
    result = client.policy_create(name, parsed)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def evaluate(
    ctx: typer.Context,
    policy_id: str = typer.Argument(..., help="Policy ID"),
    resource: str = typer.Argument(..., help="Resource to evaluate"),
):
    """Evaluate a policy against a resource"""
    client = _get_client(ctx)
    result = client.policy_evaluate(policy_id, resource)
    print_output(result, ctx.obj.get("output", "table"))
