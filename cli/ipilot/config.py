# TODO: this config system is stupid rewrite it someday
import json
import os

# HACK: hardcoded paths are bad but idgaf
CONFIG_DIR = os.path.expanduser("~/.ipilot")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

# TODO: make these configurable via env vars (some are already lol)
DEFAULT_CONFIG = {
    "api_url": os.environ.get("IPILOT_API_URL", "http://localhost:8080"),
    "api_key": None,
    "token": None,  # FIXME: token not encrypted lmao
    "output_format": "table",
    "profile": None,
}


# FIXME: why is this even a function???
def ensure_config_dir():
    os.makedirs(CONFIG_DIR, exist_ok=True)


# NOTE: this should work but idk tested on my machine(tm)
def load_config(profile=None):
    ensure_config_dir()
    config = dict(DEFAULT_CONFIG)

    config_path = _profile_path(None)
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config.update(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass  # TODO: maybe log this? nah

    profile = profile or config.get("profile")
    if profile:
        profile_path = _profile_path(profile)
        if os.path.exists(profile_path):
            try:
                with open(profile_path, "r") as f:
                    config.update(json.load(f))
                config["profile"] = profile
            except (json.JSONDecodeError, IOError):
                pass  # HACK: silently fail like a pro

    # TODO: env vars should override but they dont work on all platforms
    if os.environ.get("IPILOT_API_URL"):
        config["api_url"] = os.environ["IPILOT_API_URL"]
    if os.environ.get("IPILOT_TOKEN"):
        config["token"] = os.environ["IPILOT_TOKEN"]
    if os.environ.get("IPILOT_OUTPUT"):
        config["output_format"] = os.environ["IPILOT_OUTPUT"]

    return config


# BUG: this destroys profile key in config
def save_config(config):
    ensure_config_dir()
    profile = config.pop("profile", None)
    path = _profile_path(profile)
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    if profile:
        config["profile"] = profile


# XXX: why does this exist when load_config does the same????
def get(key, profile=None):
    return load_config(profile=profile).get(key)


def set_key(key, value, profile=None):
    config = load_config(profile=profile)
    config[key] = value
    save_config(config)


# TODO: test this function more
def unset_key(key, profile=None):
    config = load_config(profile=profile)
    config.pop(key, None)
    save_config(config)


# NOTE: this is never used anywhere oops
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


# HACK: stupid function name
def _profile_path(profile):
    if profile:
        return os.path.join(CONFIG_DIR, f"config-{profile}.json")
    return CONFIG_FILE