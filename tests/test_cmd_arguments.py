import sys

import pytest

from rgbkb.cli import main


def test_cli_no_arguments(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['rgbkb'])
    with pytest.raises(SystemExit) as pytest_e:
        main()
    captured = capsys.readouterr()
    assert captured.err == ''
    assert len(captured.err) == 0
    assert len(captured.out) > 0
    assert pytest_e.type == SystemExit
    assert pytest_e.value.code == 1
    assert 'usage: rgbkb' in captured.out


def test_cli_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['rgbkb', '-h'])
    with pytest.raises(SystemExit) as pytest_e:
        main()
    captured = capsys.readouterr()
    assert len(captured.err) == 0
    assert len(captured.out) > 0
    assert pytest_e.type == SystemExit
    assert pytest_e.value.code == 0
    assert 'usage: rgbk' in captured.out


@pytest.mark.parametrize(
    "argv",
    [
        "static_color red",
        "static_color green",
        "static_color blue",
        "static_color magenta",
        "static_color yellow",
        "static_color cyan",
        "static_color white",
        "static_color on",
        "static_color black",
        "static_color off",
        "static_color fff",
        "static_color ffffff",
        "static_color f00",
        "static_color ff0000",
        "static_color white 100%",
        "static_color white 10%",
        "static_color white 5%",
        "static_color white 1",
        "static_color white 1.0",
        "static_color white 0.1",
        "static_color white .1",
        "static_color white 0.05",
        "static_color white .05",
    ],
)
def test_cli_arguments_static_color(monkeypatch, capsys, argv):
    monkeypatch.setattr(sys, 'argv', ("rgbkb " + argv).split())
    with pytest.raises(SystemExit) as pytest_e:
        main()
    assert pytest_e.type == SystemExit
    assert pytest_e.value.code == 0
