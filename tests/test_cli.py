from alphavibe.cli import main


def test_cli_no_args(capsys):
    try:
        main([])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "usage" in captured.err or captured.out
