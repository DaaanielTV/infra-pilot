import typer

from .core.cli import create_app, legacy_bridge
from .core.command_registry import discover_commands, attach_to_app

app = create_app()

import ipilot.commands
from .core.command_registry import attach_to_app
attach_to_app(app)


@app.command()
def login(
    ctx: typer.Context,
    api_key: str = typer.Argument(..., help="Your API key"),
):
    """Log in to the API."""
    from .client import ApiClient
    from .config import load_config
    from .output.formatters import print_output
    config = load_config(profile=ctx.obj.get("profile"))
    client = ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))
    result = client.login(api_key)
    if "token" in result:
        from .config import set_key
        set_key("token", result["token"], profile=ctx.obj.get("profile"))
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def logout(ctx: typer.Context):
    """Log out and clear your token."""
    from .config import unset_key
    unset_key("token", profile=ctx.obj.get("profile"))
    from .output.formatters import print_output
    print_output({"status": "Logged out"}, ctx.obj.get("output", "table"))


@app.command()
def version():
    """Show CLI version."""
    from . import __version__
    typer.echo(f"ipilot v{__version__}")


@app.command()
def interactive():
    """Open interactive mode."""
    _run_interactive()


@app.command()
def completion(
    shell: str = typer.Argument("auto", help="Shell type: bash, zsh, fish, powershell"),
    install: bool = typer.Option(False, "--install", help="Install completion"),
):
    """Set up shell completion."""
    if install:
        from typer._completion import install as install_completion
        install_completion()
        typer.echo(f"Completion installed for {shell}")
    else:
        from typer._completion import show_callback
        show_callback(shell)


@app.command()
def batch(
    ctx: typer.Context,
    file: str = typer.Option(..., "--file", "-f", help="YAML batch operations file"),
):
    """Run many commands from a YAML file."""
    import yaml
    with open(file) as f:
        ops = yaml.safe_load(f)
    for op in ops.get("operations", []):
        cmd = op.get("command", "")
        args = op.get("args", {})
        typer.echo(f"Running: ipilot {cmd} {args}")


@app.command()
def docs(
    output: str = typer.Option("docs/cli-reference.md", "--output", "-o", help="Output file"),
):
    """Generate CLI reference docs."""
    _generate_docs(output)


def _run_interactive():
    from rich.prompt import Prompt
    from rich.console import Console
    console = Console()
    console.print("[bold cyan]Infra Pilot CLI[/bold cyan] - Interactive mode")
    console.print("Type commands directly, or 'exit' to quit.\n")
    while True:
        try:
            cmd = Prompt.ask("[bold]ipilot[/bold]")
            if cmd in ("exit", "quit", "q"):
                break
            if cmd.strip():
                from typer.testing import CliRunner
                runner = CliRunner()
                result = runner.invoke(app, cmd.split())
                console.print(result.output)
        except (KeyboardInterrupt, EOFError):
            break


def _generate_docs(output_path: str):
    lines = ["# CLI Reference\n", "Auto-generated from `ipilot --help`.\n", "## Global Options\n"]
    from typer.testing import CliRunner
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    lines.append("```\n" + result.output + "```\n")

    import os
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    typer.echo(f"Docs generated: {output_path}")