import json
import os

CONFIG_DIR = os.path.expanduser("~/.ipilot")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "api_url": os.environ.get("IPILOT_API_URL", "http://localhost:8080"),
    "api_key": None,
    "token": None,
    "output_format": "table",
    "profile": None,
}


def ensure_config_dir():
    os.makedirs(CONFIG_DIR, exist_ok=True)


def load_config(profile=None):
    ensure_config_dir()
    config = dict(DEFAULT_CONFIG)

    config_path = _profile_path(None)
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config.update(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass

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

    if os.environ.get("IPILOT_API_URL"):
        config["api_url"] = os.environ["IPILOT_API_URL"]
    if os.environ.get("IPILOT_TOKEN"):
        config["token"] = os.environ["IPILOT_TOKEN"]
    if os.environ.get("IPILOT_OUTPUT"):
        config["output_format"] = os.environ["IPILOT_OUTPUT"]

    return config


def save_config(config):
    ensure_config_dir()
    profile = config.pop("profile", None)
    path = _profile_path(profile)
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    if profile:
        config["profile"] = profile


def get(key, profile=None):
    return load_config(profile=profile).get(key)


def set_key(key, value, profile=None):
    config = load_config(profile=profile)
    config[key] = value
    save_config(config)


def unset_key(key, profile=None):
    config = load_config(profile=profile)
    config.pop(key, None)
    save_config(config)


def list_profiles():
    ensure_config_dir()
    profiles = []
    for fname in os.listdir(CONFIG_DIR):
        if fname.startswith("config-") and fname.endswith(".json"):
            profiles.append(fname[7:-5])
    return profiles


def delete_profile(profile):
    path = _profile_path(profile)
    if os.path.exists(path):
        os.remove(path)


def _profile_path(profile):
    if profile:
        return os.path.join(CONFIG_DIR, f"config-{profile}.json")
    return CONFIG_FILE