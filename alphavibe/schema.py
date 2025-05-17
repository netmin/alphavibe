from __future__ import annotations

from typing import List, Dict

REQUIRED_COLUMNS = {"timestamp", "open", "high", "low", "close", "volume"}


def validate_ohlcv(rows: List[Dict[str, float]]) -> None:
    """Validate OHLCV rows."""
    if not rows:
        raise ValueError("No data")
    for row in rows:
        if set(row) != REQUIRED_COLUMNS:
            raise ValueError("Invalid columns")
        if any(v is None for v in row.values()):
            raise ValueError("NaN detected")
