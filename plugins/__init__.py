"""Plugin system for Infra Pilot.

Plugins extend the core functionality of Infra Pilot.
Each plugin is a Python package that exposes an `ipilot_plugin` function
or a class with an `execute` method.

Built-in plugin types:
- kubernetes: Kubernetes cluster management
- docker: Advanced Docker management
- aws: Amazon Web Services integration
- hetzner: Hetzner Cloud integration
- cloudflare: Cloudflare DNS & CDN
- proxmox: Proxmox VE virtualization
- ansible: Ansible automation
- nomad: HashiCorp Nomad
- azure: Microsoft Azure

To create a plugin:
1. Create a directory in plugins/
2. Add __init__.py with a class that has execute() method
3. Register via ipilot plugins install <name>
"""

import importlib
import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))


class PluginBase:
    """Base class for all plugins."""

    name: str = ""
    version: str = "1.0.0"
    description: str = ""

    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the plugin's main functionality."""
        raise NotImplementedError


def discover_plugins() -> Dict[str, PluginBase]:
    """Discover installed plugins."""
    plugins = {}
    for entry in os.listdir(PLUGIN_DIR):
        plugin_path = os.path.join(PLUGIN_DIR, entry)
        if os.path.isdir(plugin_path) and not entry.startswith("_") and not entry.startswith("."):
            try:
                mod = importlib.import_module(f"plugins.{entry}")
                if hasattr(mod, "Plugin"):
                    instance = mod.Plugin()
                    plugins[instance.name or entry] = instance
            except Exception as e:
                logger.warning(f"Failed to load plugin {entry}: {e}")
    return plugins


def list_plugins() -> Dict[str, Dict[str, str]]:
    """List available built-in plugins."""
    return {
        "kubernetes": {"name": "Kubernetes", "description": "Kubernetes cluster management", "version": "1.0.0"},
        "docker": {"name": "Docker", "description": "Advanced Docker management", "version": "1.0.0"},
        "aws": {"name": "AWS", "description": "Amazon Web Services integration", "version": "1.0.0"},
        "hetzner": {"name": "Hetzner", "description": "Hetzner Cloud integration", "version": "1.0.0"},
        "cloudflare": {"name": "Cloudflare", "description": "Cloudflare DNS & CDN integration", "version": "1.0.0"},
        "proxmox": {"name": "Proxmox", "description": "Proxmox VE virtualization management", "version": "1.0.0"},
        "ansible": {"name": "Ansible", "description": "Ansible automation integration", "version": "1.0.0"},
        "nomad": {"name": "Nomad", "description": "HashiCorp Nomad orchestration", "version": "1.0.0"},
        "azure": {"name": "Azure", "description": "Microsoft Azure integration", "version": "1.0.0"},
    }
