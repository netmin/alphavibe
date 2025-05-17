import builtins
from io import StringIO
from contextlib import redirect_stdout

from main import main


def test_main_prints_greeting():
    buf = StringIO()
    with redirect_stdout(buf):
        main()
    assert buf.getvalue().strip() == "Hello from alphavibe!"
