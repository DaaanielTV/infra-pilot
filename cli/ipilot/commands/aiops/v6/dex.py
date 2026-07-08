import typer
from ....client import ApiClient
from ....config import load_config
from ....output.formatters import print_output

app = typer.Typer(help="Digital experience")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def monitors(ctx: typer.Context):
    """List monitors"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def regression(ctx: typer.Context):
    """Regression analysis"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def health(ctx: typer.Context):
    """DEX health"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))
