import os
from pathlib import Path
import yaml

_BASE_MAP_PATH = Path(__file__).parent / "provider_map.yaml"


def _load_yaml_file(path: Path) -> dict:
    if not path or not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return yaml.safe_load(f) or {}
        except Exception:
            return {}


def _load_base_map() -> dict:
    return _load_yaml_file(_BASE_MAP_PATH)


def _default_overrides_path() -> Path:
    base = Path(__file__).parent / ".." / "overrides" / "provider_map.yaml"
    return base.resolve()


def _load_overrides_from_path(path: Path) -> dict:
    return _load_yaml_file(path)


def _merge_maps(base: dict, overrides: dict) -> dict:
    merged = dict(base or {})
    for k, v in (overrides or {}).items():
        merged[k] = v
    return merged


def load_map() -> dict:
    base = _load_base_map()
    override_path = None
    env_path = os.environ.get("PROVIDER_CONFIG_OVERRIDE")
    if env_path:
        override_path = Path(env_path)
    else:
        override_path = _default_overrides_path()
    overrides = _load_overrides_from_path(override_path)
    return _merge_maps(base, overrides)


_MAP = load_map()


def refresh_map():
    global _MAP
    _MAP = load_map()


def resolve_provider(token: str) -> str:
    if not token:
        return token
    return _MAP.get(token, token)


def current_env() -> str:
    return os.environ.get("TEST_ENV", "local")