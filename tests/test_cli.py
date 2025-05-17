import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alphavibe.cli import main


def test_cli_no_args(capsys):
    try:
        main([])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "usage" in captured.err or captured.out
