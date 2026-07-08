import typer
from ....client import ApiClient
from ....config import load_config
from ....output.formatters import print_output

app = typer.Typer(help="Incident management")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def remediate(ctx: typer.Context):
    """Remediation suggestions"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def analytics(ctx: typer.Context):
    """Incident analytics"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))

@app.command()
def mttr(ctx: typer.Context):
    """MTTR metrics"""
    print_output({"status": "not implemented", "message": "v6 API endpoint not configured"}, ctx.obj.get("output", "table"))
