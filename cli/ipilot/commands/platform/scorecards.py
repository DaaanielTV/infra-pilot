import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Scorecards")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context):
    """List scorecards"""
    client = _get_client(ctx)
    result = client.scorecards_list()
    import builtins; _list_type = builtins.list
    data = result if isinstance(result, _list_type) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Scorecard name"),
    criteria: str = typer.Argument(help="Scorecard criteria"),
):
    """Create a scorecard"""
    client = _get_client(ctx)
    result = client.scorecards_create(name, criteria)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def get(
    ctx: typer.Context,
    scorecard_id: str = typer.Argument(help="Scorecard ID"),
):
    """Get a scorecard"""
    client = _get_client(ctx)
    result = client.scorecards_get(scorecard_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def update(
    ctx: typer.Context,
    scorecard_id: str = typer.Argument(help="Scorecard ID"),
    criteria: str = typer.Argument(help="New criteria"),
):
    """Update a scorecard"""
    client = _get_client(ctx)
    result = client.scorecards_update(scorecard_id, criteria)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context):
    """Get scorecard summary"""
    client = _get_client(ctx)
    result = client.scorecards_summary()
    print_output(result, ctx.obj.get("output", "table"))
