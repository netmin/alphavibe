from __future__ import annotations

from typing import List, Dict, Type


def run_backtest(strategy_cls: Type, data: List[Dict[str, float]], cash: float = 10_000) -> Dict[str, float]:
    """Stub for backtest."""
    # Placeholder: implement with actual library
    prices = [row["close"] for row in data]
    ret = prices[-1] - prices[0]
    return {"pnl": ret, "sharpe": 0.0, "drawdown": 0.0}
