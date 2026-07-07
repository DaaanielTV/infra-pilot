import importlib
import pkgutil
import typer
from pathlib import Path
from typing import Dict, Optional

_registry: Dict[str, typer.Typer] = {}


def register(name: str, help_text: str = ""):
    """Decorator to register a command module with the CLI."""
    def decorator(app: typer.Typer):
        _registry[name] = (app, help_text)
        return app
    return decorator


def discover_commands(package_path: str = "ipilot.commands"):
    """Auto-discover and register all command modules."""
    pkg = importlib.import_module(package_path)
    for importer, modname, ispkg in pkgutil.walk_packages(pkg.__path__, prefix=f"{package_path}."):
        if not ispkg:
            try:
                mod = importlib.import_module(modname)
                if hasattr(mod, "app") and isinstance(mod.app, typer.Typer):
                    parts = modname.split(".")[2:]
                    name = "_".join(parts) if len(parts) > 1 else parts[0]
                    _registry[name] = (mod.app, mod.app.info.help or "")
            except Exception:
                pass


def attach_to_app(app: typer.Typer):
    """Attach all discovered commands to the main app."""
    for name, (sub_app, _) in _registry.items():
        app.add_typer(sub_app, name=name)


def get_registry() -> Dict[str, typer.Typer]:
    return {k: v[0] for k, v in _registry.items()}
