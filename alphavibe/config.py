from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any, Dict


CONFIG_FILE = Path(__file__).with_name("settings.toml")


def load_config(path: Path | None = None) -> Dict[str, Any]:
    """Load settings from TOML file."""
    cfg_path = path or CONFIG_FILE
    if not cfg_path.exists():
        return {}
    with cfg_path.open("rb") as f:
        return tomllib.load(f)
