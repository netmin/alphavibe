from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).with_name("data")


def save_df(rows: List[Dict[str, float]], *, symbol: str, timeframe: str) -> Path:
    """Save rows to CSV file."""
    exchange = "binance"
    path = DATA_DIR / exchange / symbol / f"{timeframe}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def load_df(symbol: str, timeframe: str, start: str | None = None, end: str | None = None) -> List[Dict[str, float]]:
    """Load rows from CSV file."""
    exchange = "binance"
    path = DATA_DIR / exchange / symbol / f"{timeframe}.csv"
    with path.open() as f:
        reader = csv.DictReader(f)
        data = [
            {k: float(v) if k != "timestamp" else int(v) for k, v in row.items()}
            for row in reader
        ]
    return data
