#!/usr/bin/env python3
"""
A CLI tool to control RGB backlight effects on the Acer PH16-71 keyboard, with persistent settings.

Stores the last-used effect in ~/.config/rgbkb/config.json and provides an `apply` command to re-apply
automatically (e.g. via systemd at boot).
"""
import json
import subprocess
import sys
from pathlib import Path

import click
from usbx import usb

from rgbkb.kb import RgbKeyboard
from rgbkb.utils import find_supported_devices

# USB init packet (preamble)
PREAMBLE_INIT = bytes.fromhex("b1 00 00 00 00 00 00 4e")

# Config paths
CONFIG_DIR = Path.home() / ".config" / "rgbkb"
CONFIG_FILE = CONFIG_DIR / "config.json"


def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def save_config(effect: str, params: dict):
    ensure_config_dir()
    cfg = {"effect": effect, "params": params}
    CONFIG_FILE.write_text(json.dumps(cfg))


def load_config():
    if not CONFIG_FILE.exists():
        return None
    return json.loads(CONFIG_FILE.read_text())


# Utility functions


def map_speed(speed: float) -> int:
    """Map float speed to hardware value: >=1 uses floor, <1 maps to 0 (ultra-fast)."""
    return int(speed) if speed >= 1 else 0


def parse_hex(hexcolor: str) -> tuple[int, int, int]:
    """Convert RRGGBB hex string into (r, g, b) values."""
    hexcolor = hexcolor.lstrip("#")
    if len(hexcolor) != 6:
        raise click.BadParameter("Color must be a 6-digit RRGGBB hex.")
    return tuple(int(hexcolor[i : i + 2], 16) for i in (0, 2, 4))


# Packet builders for each effect


def build_color(r: int, g: int, b: int) -> bytes:
    """Load custom RGB color into keyboard buffer."""
    return bytes([0x14, 0x00, 0x00, r, g, b, 0x00, 0x00])


def build_static_color(r: int, g: int, b: int) -> list[bytes]:
    """Apply last-loaded color as static backlight."""
    # 08 02 01 00 [brightness] 01 01 9b (brightness=32 default)
    return [bytes([0x08, 0x02, 0x01, 0x00, 0x20, 0x01, 0x01, 0x9B])]


def build_breathing(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Breathing pulse effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x02, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_wave(speed: int, brightness: int, direction: int) -> list[bytes]:
    """Color wave effect; direction codes: 1=right,...,6=counterclockwise."""
    return [bytes([0x08, 0x02, 0x03, speed, brightness, 0x01, direction, 0x9B])]


def build_ripple(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Center-originating ripple effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x06, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_snake(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Snake chase animation in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x05, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


# Additional effects


def build_heartbeat(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Heartbeat pulse effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x29, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_snow(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Snowflake fall and melt in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x28, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_fireball(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Fireball burst effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x27, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_stars(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Twinkling stars effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x26, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_spot(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Keypress spot effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x25, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_lightning(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Random lightning flashes in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x12, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_rain(r: int, g: int, b: int, speed: int, brightness: int) -> list[bytes]:
    """Raindrop fall effect in custom color."""
    return [
        build_color(r, g, b),
        bytes([0x08, 0x02, 0x0A, speed, brightness, 0x01, 0x01, 0x9B]),
    ]


def build_neon(speed: int, brightness: int) -> list[bytes]:
    """Pulsing neon glow effect (no custom color)."""
    return [bytes([0x08, 0x02, 0x08, speed, brightness, 0x01, 0x01, 0x9B])]


# Common CLI group
@click.group(help="Control RGB backlight effects on Acer PH16-71 keyboard.")
def cli():
    pass


# Apply last saved settings
@cli.command()
def apply():
    """Apply the last saved RGB effect (loads from config)."""
    cfg = load_config()
    if not cfg:
        click.echo("No saved configuration found.", err=True)
        sys.exit(1)
    effect = cfg["effect"]
    params = cfg["params"]
    cmd = ["rgbkb", effect]
    for k, v in params.items():
        if k == "hexcolor":
            cmd.append(v)
        elif k == "direction":
            cmd += ["--direction", str(v)]
        elif k == "speed":
            cmd += ["--speed", str(v)]
        elif k in ("brightness", "level"):
            cmd += ["--level", str(v)]
    subprocess.run(cmd, check=True)
    click.echo(f"Applied saved effect: {effect}")


# Static color
@cli.command(name="all", short_help="Set keyboard to a custom HEX color")
@click.argument("hexcolor", metavar="HEX", required=True)
def all_mode(hexcolor):
    """Load and apply a static color to the entire keyboard."""
    r, g, b = parse_hex(hexcolor)
    devs = find_supported_devices()
    if not devs:
        click.echo("No compatible keyboard found.", err=True)
        sys.exit(1)
    kb = devs[0]
    cmds = [PREAMBLE_INIT, build_color(r, g, b)] + build_static_color(r, g, b)
    kb.send_commands(*cmds)
    save_config("all", {"hexcolor": hexcolor})
    click.echo(f"Set all keys to #{hexcolor}")


# Breathing effect
@cli.command(short_help="Start breathing effect with custom color")
@click.argument("hexcolor", metavar="HEX", required=True)
@click.option(
    "--speed",
    default=1.0,
    type=float,
    help="Breathing speed (>=1 hardware 1–11, <1 ultra-fast)",
)
@click.option(
    "--level",
    "--brightness",
    "brightness",
    default=32,
    type=int,
    help="Breathing brightness (0–32)",
)
def breathe(hexcolor, speed, brightness):
    """Begin breathing animation in a specified color."""
    r, g, b = parse_hex(hexcolor)
    hw = map_speed(speed)
    devs = find_supported_devices()
    if not devs:
        click.echo("No compatible keyboard found.", err=True)
        sys.exit(1)
    kb = devs[0]
    cmds = [PREAMBLE_INIT] + build_breathing(r, g, b, hw, brightness)
    kb.send_commands(*cmds)
    save_config("breathe", {"hexcolor": hexcolor, "speed": hw, "level": brightness})
    click.echo(f"Started breathing #{hexcolor} @ speed={hw} bright={brightness}")


# Wave effect
@cli.command(short_help="Run wave animation (no color argument)")
@click.option(
    "--speed",
    default=1.0,
    type=float,
    help="Wave speed (>=1 hardware 1–11, <1 ultra-fast)",
)
@click.option(
    "--level",
    "--brightness",
    "brightness",
    default=32,
    type=int,
    help="Wave brightness (0–32)",
)
@click.option(
    "--direction",
    default=1,
    type=click.IntRange(1, 6),
    help="Wave dir: 1=right,2=left,3=up,4=down,5=clockwise,6=counter",
)
def wave(speed, brightness, direction):
    """Initiate continuous wave animation across keyboard."""
    hw = map_speed(speed)
    devs = find_supported_devices()
    if not devs:
        click.echo("No compatible keyboard found.", err=True)
        sys.exit(1)
    kb = devs[0]
    cmds = [PREAMBLE_INIT] + build_wave(hw, brightness, direction)
    kb.send_commands(*cmds)
    save_config("wave", {"speed": hw, "level": brightness, "direction": direction})
    click.echo(f"Wave effect speed={hw} bright={brightness} dir={direction}")


# Neon effect
@cli.command(short_help="Run neon glow effect (no color argument)")
@click.option(
    "--speed",
    default=1.0,
    type=float,
    help="Neon speed (>=1 hardware 1–11, <1 ultra-fast)",
)
@click.option(
    "--level",
    "--brightness",
    "brightness",
    default=32,
    type=int,
    help="Neon brightness (0–32)",
)
def neon(speed, brightness):
    """Initiate pulsing neon glow across keyboard."""
    hw = map_speed(speed)
    devs = find_supported_devices()
    if not devs:
        click.echo("No compatible keyboard found.", err=True)
        sys.exit(1)
    kb = devs[0]
    cmds = [PREAMBLE_INIT] + build_neon(hw, brightness)
    kb.send_commands(*cmds)
    save_config("neon", {"speed": hw, "level": brightness})
    click.echo(f"Started neon speed={hw} bright={brightness}")


# Helper to register custom-color effects


def register_color_effect(name, builder, short_help):
    @cli.command(name=name, short_help=short_help)
    @click.argument("hexcolor", metavar="HEX", required=True)
    @click.option(
        "--speed",
        default=1.0,
        type=float,
        help=f"{name.capitalize()} speed (>=1 hw speed, <1 ultra-fast)",
    )
    @click.option(
        "--level",
        "--brightness",
        "brightness",
        default=32,
        type=int,
        help=f"{name.capitalize()} brightness (0–32)",
    )
    def _cmd(hexcolor, speed, brightness, _builder=builder, _name=name):
        """Start {} effect in a specified color.""".format(_name.capitalize())
        r, g, b = parse_hex(hexcolor)
        hw = map_speed(speed)
        devs = find_supported_devices()
        if not devs:
            click.echo("No compatible keyboard found.", err=True)
            sys.exit(1)
        kb = devs[0]
        cmds = [PREAMBLE_INIT] + _builder(r, g, b, hw, brightness)
        kb.send_commands(*cmds)
        save_config(name, {"hexcolor": hexcolor, "speed": hw, "level": brightness})
        click.echo(f"Started {_name} #{hexcolor} speed={hw} bright={brightness}")

    return _cmd


# Registering custom-color effects
register_color_effect(
    "ripple", build_ripple, "Center-originating ripple with custom color"
)
register_color_effect("snake", build_snake, "Snake chase animation with custom color")
register_color_effect("heartbeat", build_heartbeat, "Heartbeat pulse in custom color")
register_color_effect("snow", build_snow, "Snowflake fall effect with custom color")
register_color_effect("fireball", build_fireball, "Fireball burst in custom color")
register_color_effect("stars", build_stars, "Twinkling stars in custom color")
register_color_effect("spot", build_spot, "Keypress spot effect with custom color")
register_color_effect("lightning", build_lightning, "Random lightning in custom color")
register_color_effect("rain", build_rain, "Raindrop fall effect with custom color")


main = cli

if __name__ == "__main__":
    cli()
