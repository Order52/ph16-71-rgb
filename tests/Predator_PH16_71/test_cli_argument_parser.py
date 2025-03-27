import sys

import pytest

from rgbkb.acer_ph16_71.device import AcerPredatorPH1671
from rgbkb.cli import CliParser


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
def test_parser_with_one_command(argv):
    parser = CliParser(AcerPredatorPH1671)
    parsed = parser.parse(argv.split())
    print(parsed)
    assert parsed != ""


@pytest.mark.parametrize(
    "argv, expected",
    [
        ["flash_3x red", [["flash_3x", "red"]]],
        ["wave 33% fast right", [["wave", "33%","fast", "right"]]],
        ["wave .5 bright up", [["wave", ".5", "bright", "up"]]],
        ["static_color blue wasd_keys red", [["static_color", "blue"], ["wasd_keys", "red"]]],
        ["flash_3x magenta", [["flash_3x", "magenta"]]],
        ["static_color yellow", [["static_color", "yellow"]]],
        ["static_color cyan", [["static_color", "cyan"]]],
        ["static_color white", [["static_color", "white"]]],
        ["static_color on", [["static_color", "on"]]],
        ["static_color black", [["static_color", "black"]]],
        ["static_color off", [["static_color", "off"]]],
        ["static_color fff", [["static_color", "fff"]]],
        ["static_color ffffff", [["static_color", "ffffff"]]],
        ["static_color f00", [["static_color", "f00"]]],
        ["snow ff0000", [["snow", "ff0000"]]],
        ["snow crimson", [["snow", "crimson"]]],
        ["static_color white 100%", [["static_color", "white", "100%"]]],
        ["static_color white 10%", [["static_color", "white", "10%"]]],
        ["static_color white 5%", [["static_color", "white", "5%"]]],
        ["static_color white 1", [["static_color", "white", "1"]]],
        ["static_color white 1.0", [["static_color", "white", "1.0"]]],
        ["static_color white 0.1", [["static_color", "white", "0.1"]]],
        ["static_color white .1", [["static_color", "white", ".1"]]],
        ["static_color white 0.05", [["static_color", "white", "0.05"]]],
        ["static_color white .05", [["static_color", "white", ".05"]]],
   ],
)
def test_parser_with_more_commands(argv, expected):
    parser = CliParser(AcerPredatorPH1671)
    parsed = parser.parse(argv.split())
    print(parsed)
    assert parsed == expected


@pytest.mark.parametrize(
    "argv",
    [
        "the_thing red blue white",
        "white static .05",
        "static .5 white",
        "waves red"
    ],
)
def test_parser_should_fail_to_parse(argv):
    parser = CliParser(AcerPredatorPH1671)
    with pytest.raises(ValueError, match=r'Unknown keyword .+ on position \d+.'):
        parser.parse(argv.split())
