from typing import Any, Dict, List, Optional
from rich.console import Console
from rich.table import Table as RichTable
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint
import json

_console = Console()


def get_console():
    return _console


def print_table(data: List[Dict], title: Optional[str] = None):
    if not data:
        _console.print("[yellow](no data)[/yellow]")
        return
    keys = list(data[0].keys())
    table = RichTable(title=title, title_style="bold cyan")
    for key in keys:
        table.add_column(key, style="cyan", no_wrap=True)
    for item in data:
        table.add_row(*[str(item.get(k, "")) for k in keys])
    _console.print(table)


def print_panel(text: str, title: Optional[str] = None, style: str = "green"):
    _console.print(Panel(text, title=title, border_style=style))


def print_json(data: Any):
    _console.print_json(json.dumps(data, default=str))


def print_error(message: str):
    _console.print(f"[red]Error:[/red] {message}")


def print_success(message: str):
    _console.print(f"[green]{message}[/green]")


def print_info(message: str):
    _console.print(f"[blue]{message}[/blue]")


def spinner():
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=_console,
    )