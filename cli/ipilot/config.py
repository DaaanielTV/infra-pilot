import json
import os
from typing import Any, Dict, Optional

CONFIG_DIR = os.path.expanduser("~/.ipilot")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG: Dict[str, Any] = {
    "api_url": os.environ.get("IPILOT_API_URL", "http://localhost:8080"),
    "api_key": None,
    "token": None,
    "output_format": "table",
    "profile": None,
}


def ensure_config_dir():
    os.makedirs(CONFIG_DIR, exist_ok=True)


def load_config(profile: Optional[str] = None) -> Dict[str, Any]:
    """Load config, optionally merging a named profile."""
    ensure_config_dir()
    config = dict(DEFAULT_CONFIG)

    # Load base config
    config_path = _profile_path(None)
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config.update(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass

    # Merge profile if specified
    profile = profile or config.get("profile")
    if profile:
        profile_path = _profile_path(profile)
        if os.path.exists(profile_path):
            try:
                with open(profile_path, "r") as f:
                    config.update(json.load(f))
                config["profile"] = profile
            except (json.JSONDecodeError, IOError):
                pass

    # Override from env
    if os.environ.get("IPILOT_API_URL"):
        config["api_url"] = os.environ["IPILOT_API_URL"]
    if os.environ.get("IPILOT_TOKEN"):
        config["token"] = os.environ["IPILOT_TOKEN"]
    if os.environ.get("IPILOT_OUTPUT"):
        config["output_format"] = os.environ["IPILOT_OUTPUT"]

    return config


def save_config(config: Dict[str, Any]):
    ensure_config_dir()
    profile = config.pop("profile", None)
    path = _profile_path(profile)
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    if profile:
        config["profile"] = profile


def get(key: str, profile: Optional[str] = None) -> Any:
    return load_config(profile=profile).get(key)


def set_key(key: str, value: Any, profile: Optional[str] = None):
    config = load_config(profile=profile)
    config[key] = value
    save_config(config)


def unset_key(key: str, profile: Optional[str] = None):
    config = load_config(profile=profile)
    config.pop(key, None)
    save_config(config)


def list_profiles() -> list:
    """List all saved configuration profiles."""
    ensure_config_dir()
    profiles = []
    for fname in os.listdir(CONFIG_DIR):
        if fname.startswith("config-") and fname.endswith(".json"):
            profiles.append(fname[7:-5])
    return profiles


def delete_profile(profile: str):
    path = _profile_path(profile)
    if os.path.exists(path):
        os.remove(path)


def _profile_path(profile: Optional[str]) -> str:
    if profile:
        return os.path.join(CONFIG_DIR, f"config-{profile}.json")
    return CONFIG_FILE
