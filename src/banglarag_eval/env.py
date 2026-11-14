"""Load repository-local environment variables without overriding the shell."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = REPO_ROOT / ".env"


def load_environment() -> None:
    """Load `.env` once, preserving explicitly exported environment values."""
    load_dotenv(ENV_FILE, override=False)


def env_list(name: str, default: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Read a comma-separated environment value as a trimmed non-empty tuple."""
    value = os.environ.get(name)
    if not value:
        return default
    items = tuple(item.strip() for item in value.split(",") if item.strip())
    return items or default


load_environment()
