from __future__ import annotations

import argparse
from datetime import datetime, timedelta

from .fetcher import fetch_ohlcv
from .storage import save_df


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="alphavibe")
    sub = parser.add_subparsers(dest="cmd")

    fetch_p = sub.add_parser("fetch", help="Fetch market data")
    fetch_p.add_argument("symbol")
    fetch_p.add_argument("timeframe")
    fetch_p.add_argument("--days", type=int, default=1)

    args = parser.parse_args(argv)
    if args.cmd == "fetch":
        end = datetime.utcnow()
        start = end - timedelta(days=args.days)
        rows = fetch_ohlcv(args.symbol, args.timeframe, start.isoformat(), end.isoformat())
        save_df(rows, symbol=args.symbol, timeframe=args.timeframe)
        print(f"Fetched {len(rows)} rows")


if __name__ == "__main__":
    main()
