"""Constant-time API-key verification without logging credential material."""
from __future__ import annotations

from secrets import compare_digest


def matches_api_key(expected: str | None, presented: str | None) -> bool:
    """Both keys must exist; never accept an unconfigured service."""
    return bool(expected and presented) and compare_digest(expected, presented)
