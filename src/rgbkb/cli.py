import argparse
import inspect
from collections.abc import Iterable
from typing import Type

from rgbkb.acer_ph16_71.commands import color, static_color
from rgbkb.utils import find_supported_devices
from rgbkb.kb import RgbKeyboard


def print_help():
    print(inspect.cleandoc("""
    usage: rgbkb [-h,--help] [-g GROUP GROUP] [-k KEY KEY] [color] effect [effect ...]
    RGB Keyboard Control (Written for a Acer Predator PH16-71, but might work for others too.
    Lives on GitHub @ https://github.com/fuho/rgbkb

    positional arguments:
      color                 Whole keyboard, one color
      effect                Animated effect, can have up to 4 sub-arguments

    options:
      -h, --help            show this help message and exit
      -g GROUP GROUP, --group GROUP GROUP
                            Group of keys, `-g function red` or `-g keypad 00ccff`
      -k KEY KEY, --key KEY KEY
                            One single key; `-k f_key white`

    I'd REALLY appreciate any feedback, especially devices you tried to use and if it worked or not.
    """))


class CliParser:
    def __init__(self, kb: Type[RgbKeyboard]):
        self.keywords = kb.available_cli_keywords()

    def parse(self, argv) -> Iterable[Iterable[str]]:
        i = 0
        commands = []
        while i < len(argv):
            if argv[i] not in self.keywords:
                raise ValueError(f'Unknown keyword {argv[i]} on position {i}.')
            commands.append([argv[i]])
            i += 1
            while i < len(argv) and argv[i] not in self.keywords:
                commands[-1].append(argv[i])
                i += 1
        return commands


def main():
    available_keyboards = find_supported_devices()
    argparser = argparse.ArgumentParser(
        prog='rgbkb',
        description='Controls keyboard backlight, specifically Acer Predator Helios 16',
        epilog="And that's the way the cookie crumbles."
    )
    group = argparser.add_mutually_exclusive_group()
    group.add_argument(
        '-l',
        '--list',
        nargs='?',
        type=bool,
        const=True,
        default=False,
        help='List all found compatible keyboards.'
    )
    group.add_argument(
        '-s',
        '--select',
        # metavar='DEVICE',
        nargs='?',
        type=int,
        const=0,
        default=0,
        choices=[i for i, _ in enumerate(available_keyboards)],
        help=f'Choose an ID from available supported keyboards: {','.join(f"{i}: {kb.MODEL}" for i, kb in enumerate(available_keyboards))}'
    )

    for kb in available_keyboards:
        kb.update_subparser(argparser.add_subparsers(dest="command"))
    ns = argparser.parse_args()
    print(ns)
    if ns.list:
        index = 0
        for kb in available_keyboards:
            print(f'{index} :  {kb.NAME} Model: {kb.MODEL} Vendor ID: {kb.VID:04x} Product ID: {kb.PID:04x}')
        return
    else:
        kb = available_keyboards[ns.select]

    # if len(sys.argv) <= 1:
    #     print_help()
    #     sys.exit(1)
    # elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    #     print_help()
    #     sys.exit(0)
    # else:
    #     parser = CliParser(AcerPredatorPH1671)
    #     parsed = parser.parse(sys.argv[1:])
    #     pprint(parsed)
    #     sys.exit(0)

    kb.send_commands(color(255, 255, 255), static_color(1, 32, 1, 0))
    # kb.send_commands(color(200, 100, 50), flash3x(0, 16, 1, 0))
    # kb.send_commands(flash3x(0, 16, 2, 1))
    # kb.send_commands('b1 00 00 00  00 00 00 4e','14 00 00 ff ff ff 00 ee', '08 02 29 ff 30 01 01 9b')
    # kb.send_commands('08 02 08 0b  19 01 00 00')
