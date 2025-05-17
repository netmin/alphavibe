from __future__ import annotations

import json
import urllib.request
from datetime import datetime
from typing import List, Dict

API_URL = (
    "https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start}&endTime={end}&limit=1000"
)


def _ts_to_ms(ts: str | int) -> int:
    if isinstance(ts, int):
        return ts
    dt = datetime.fromisoformat(ts)
    return int(dt.timestamp() * 1000)


def fetch_ohlcv(symbol: str, timeframe: str, since: str | int, until: str | int) -> List[Dict[str, float]]:
    """Fetch OHLCV data from Binance public API."""
    start_ms = _ts_to_ms(since)
    end_ms = _ts_to_ms(until)
    url = API_URL.format(symbol=symbol.upper(), interval=timeframe, start=start_ms, end=end_ms)
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode())
    result = []
    for item in data:
        result.append(
            {
                "timestamp": int(item[0]) // 1000,
                "open": float(item[1]),
                "high": float(item[2]),
                "low": float(item[3]),
                "close": float(item[4]),
                "volume": float(item[5]),
            }
        )
    return result
