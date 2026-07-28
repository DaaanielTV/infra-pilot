"""Developer experience - doctor, benchmark, diagnose, health checking."""

import os
import shutil
import subprocess
import sys
from typing import Any, Dict, List, Optional

import typer

from ... import __version__
from ...client import ApiClient
from ...config import load_config
from ...output.formatters import print_output

app = typer.Typer(help="System diagnostics and health checks")


def _get_client(ctx: typer.Context) -> ApiClient:
    config = load_config(profile=ctx.obj.get("profile"))
    return ApiClient(config.get("api_url", "http://localhost:8080"), config.get("token"))


@app.command()
def doctor(
    ctx: typer.Context,
    fix: bool = typer.Option(False, "--fix", help="Attempt to auto-fix issues"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed output"),
):
    """Run comprehensive system diagnostics."""
    checks: List[Dict[str, Any]] = []

    checks.append({"check": "Python Version", "status": "ok" if sys.version_info >= (3, 10) else "warn", "detail": sys.version})

    ipilot_path = shutil.which("ipilot")
    checks.append({"check": "ipilot CLI", "status": "ok" if ipilot_path else "fail", "detail": ipilot_path or "not found in PATH"})

    docker_path = shutil.which("docker")
    checks.append({"check": "Docker", "status": "ok" if docker_path else "warn", "detail": docker_path or "not found (optional)"})

    git_path = shutil.which("git")
    checks.append({"check": "Git", "status": "ok" if git_path else "warn", "detail": git_path or "not found (optional)"})

    ssh_path = shutil.which("ssh")
    checks.append({"check": "SSH", "status": "ok" if ssh_path else "warn", "detail": ssh_path or "not found (optional)"})

    config = load_config()
    if config:
        checks.append({"check": "Config", "status": "ok", "detail": f"profile: {config.get('profile', 'default')}"})
    else:
        checks.append({"check": "Config", "status": "warn", "detail": "no config found, run 'ipilot login'"})

    api_url = config.get("api_url", "http://localhost:8080") if config else "http://localhost:8080"
    token = config.get("token") if config else None
    if token:
        try:
            client = ApiClient(api_url, token)
            health = client.health_check()
            if isinstance(health, dict) and health.get("status") == "ok":
                checks.append({"check": "API Connection", "status": "ok", "detail": api_url})
            else:
                checks.append({"check": "API Connection", "status": "warn", "detail": f"{api_url} - unhealthy"})
        except Exception as e:
            checks.append({"check": "API Connection", "status": "fail", "detail": f"{api_url} - {e}"})
    else:
        checks.append({"check": "API Connection", "status": "warn", "detail": "not authenticated, run 'ipilot login'"})

    if os.path.exists(os.path.expanduser("~/.ssh")):
        key_count = len([f for f in os.listdir(os.path.expanduser("~/.ssh")) if f.endswith(".pub")])
        checks.append({"check": "SSH Keys", "status": "ok" if key_count > 0 else "warn", "detail": f"{key_count} public key(s) found"})
    else:
        checks.append({"check": "SSH Keys", "status": "warn", "detail": "~/.ssh not found"})

    print_output(checks, ctx.obj.get("output", "table"))

    failed = [c for c in checks if c["status"] == "fail"]
    warnings = [c for c in checks if c["status"] == "warn"]

    if failed:
        typer.echo(f"\n{'!'*40}")
        typer.echo(f"Found {len(failed)} issue(s) that need attention:")
        for f in failed:
            typer.echo(f"  - {f['check']}: {f['detail']}")
        if fix:
            typer.echo("\nAttempting fixes...")
            for f in failed:
                if f["check"] == "ipilot CLI":
                    typer.echo("  Reinstall ipilot: pip install -e .")
                elif f["check"] == "API Connection":
                    typer.echo("  Ensure the API server is running and reachable")
        typer.echo(f"{'!'*40}")
    elif warnings:
        typer.echo(f"\n{'*'*40}")
        typer.echo(f"{len(warnings)} warning(s) found (non-critical)")
        for w in warnings:
            typer.echo(f"  - {w['check']}: {w['detail']}")
        typer.echo(f"{'*'*40}")
    else:
        typer.echo("\nAll checks passed!")


@app.command()
def benchmark(
    ctx: typer.Context,
    server: Optional[str] = typer.Option(None, "--server", "-s", help="Server to benchmark"),
    duration: int = typer.Option(10, "--duration", "-d", help="Benchmark duration in seconds"),
):
    """Run performance benchmarks."""
    client = _get_client(ctx)
    if server:
        result = client.benchmark_server(server, duration=duration)
    else:
        result = client.benchmark_system(duration=duration)
    print_output(result, ctx.obj.get("output", "table"))


@app.command()
def diagnose(
    ctx: typer.Context,
    server: Optional[str] = typer.Option(None, "--server", "-s", help="Server to diagnose"),
    issue: Optional[str] = typer.Option(None, "--issue", "-i", help="Specific issue to diagnose (connectivity, performance, disk)"),
):
    """Diagnose infrastructure issues."""
    client = _get_client(ctx)
    if server:
        result = client.diagnose_server(server, issue=issue)
    else:
        result = client.diagnose_system(issue=issue)
    print_output(result, ctx.obj.get("output", "table"))
