from __future__ import annotations

from typing import List


def total_return(prices: List[float]) -> float:
    if not prices:
        return 0.0
    return (prices[-1] - prices[0]) / prices[0]


def max_drawdown(prices: List[float]) -> float:
    peak = prices[0]
    drawdowns = []
    for p in prices:
        if p > peak:
            peak = p
        drawdowns.append((peak - p) / peak)
    return max(drawdowns)


def sharpe_ratio(returns: List[float]) -> float:
    if not returns:
        return 0.0
    avg = sum(returns) / len(returns)
    var = sum((r - avg) ** 2 for r in returns) / len(returns)
    std = var ** 0.5
    if std == 0:
        return 0.0
    return (avg / std) * (len(returns) ** 0.5)
