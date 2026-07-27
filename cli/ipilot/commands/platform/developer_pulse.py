import typer
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="Pulse surveys")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def list(ctx: typer.Context) -> None:
    """List surveys
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.pulse_list()
    data = result if isinstance(result, list) else result.get("key", result)
    print_output(data, ctx.obj.get("output", "table"))


@app.command()
def create(
    ctx: typer.Context,
    title: str = typer.Argument(help="Survey title"),
    questions: str = typer.Argument(help="Questions (JSON)"),
) -> None:
    """Create
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.pulse_create(title, questions)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def respond(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
    answers: str = typer.Argument(help="Answers (JSON)"),
) -> None:
    """Respond
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.pulse_respond(survey_id, answers)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def results(
    ctx: typer.Context,
    survey_id: str = typer.Argument(help="Survey ID"),
) -> None:
    """Results
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.pulse_results(survey_id)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def summary(ctx: typer.Context) -> None:
    """Summary
    
    Args:
        ctx: Typer context for accessing config and output format.
    
    Returns:
        None (output is printed via print_output).
    """
    client = _get_client(ctx)
    result = client.pulse_summary()
    print_output(result, ctx.obj.get("output", "table"))