import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Net Promoter Score")

def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))

@app.command()
def create(
    ctx: typer.Context,
    name: str = typer.Argument(help="Survey name"),
    targets: str = typer.Argument(help="Target list (JSON)"),
) -> None:
    """Create a survey
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_create(name, targets)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def list(ctx: typer.Context) -> None:
    """List surveys
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def get(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """Get a survey
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_get(survey_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def send(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """Send a survey
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_send(survey_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def respond(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
    score: int = typer.Argument(help="NPS score"),
    comment: str = typer.Option("", "--comment", help="Optional comment"),
) -> None:
    """Respond to survey
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_respond(survey_id, score, comment)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def score(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """Get NPS score
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_score(survey_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def trend(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """NPS trend
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_trend(survey_id)
    print_output(result, ctx.obj.get("output", "table"))

@app.command()
def detractors(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """List detractors
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_detractors(survey_id)
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))

@app.command()
def stats(ctx: typer.Context) -> None:
    """NPS statistics
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.cx_nps_stats()
    print_output(result, ctx.obj.get("output", "table"))