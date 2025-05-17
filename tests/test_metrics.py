import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from alphavibe.metrics import total_return, max_drawdown, sharpe_ratio


def test_total_return():
    prices = [1, 2, 3]
    assert total_return(prices) == 2.0


def test_max_drawdown():
    prices = [3, 2, 1]
    assert max_drawdown(prices) == (3 - 1) / 3


def test_sharpe_ratio():
    returns = [1, -1, 1, -1]
    sr = sharpe_ratio(returns)
    assert abs(sr) < 1e-6
