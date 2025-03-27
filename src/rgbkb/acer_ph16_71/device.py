import argparse
from textwrap import wrap
from usbx import Device, RequestType, Recipient, ControlTransfer, TransferDirection
from rgbkb.acer_ph16_71.commands import ARGUMENTS_TO_COMMANDS, EffectNames
from rgbkb.acer_ph16_71.keys import KeyNames, GroupNames
from rgbkb.kb import RgbKeyboard, KeyboardCommand

class OrderedArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 'ordered_args' in namespace:
            setattr(namespace, 'ordered_args', [])
        previous = namespace.ordered_args
        previous.append((self.dest, values))
        setattr(namespace, 'ordered_args', previous)

def add_parsers_to_cli_subparser(subparsers):
    # effects
    heartbeat_parser = subparsers.add_parser(
        name='heartbeat',
        help=f"help for heartbeat command."
    )
    heartbeat_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    heartbeat_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    heartbeat_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    snow_parser = subparsers.add_parser(
        name='snow',
        help=f"help for snow command."
    )
    snow_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    snow_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    snow_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    fireball_parser = subparsers.add_parser(
        name='fireball',
        help=f"help for fireball command."
    )
    fireball_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    fireball_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    fireball_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    stars_parser = subparsers.add_parser(
        name='stars',
        help=f"help for stars command."
    )
    stars_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    stars_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    stars_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    spot_parser = subparsers.add_parser(
        name='spot',
        help=f"help for spot command."
    )
    spot_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    spot_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    spot_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    lightning_parser = subparsers.add_parser(
        name='lightning',
        help=f"help for lightning command."
    )
    lightning_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    lightning_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    lightning_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    rain_parser = subparsers.add_parser(
        name='rain',
        help=f"help for rain command."
    )
    rain_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    rain_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    rain_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    neon_parser = subparsers.add_parser(
        name='neon',
        help=f"help for neon command."
    )
    neon_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    neon_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    neon_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    ripple_parser = subparsers.add_parser(
        name='ripple',
        help=f"help for ripple command."
    )
    ripple_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    ripple_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    ripple_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    snake_parser = subparsers.add_parser(
        name='snake',
        help=f"help for snake command."
    )
    snake_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    snake_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    snake_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    wave_parser = subparsers.add_parser(
        name='wave',
        help=f"help for wave command."
    )
    wave_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    wave_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    wave_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    breathing_parser = subparsers.add_parser(
        name='breathing',
        help=f"help for breathing command."
    )
    breathing_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    breathing_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    breathing_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    static_color_parser = subparsers.add_parser(
        name='static_color',
        help=f"help for static_color command."
    )
    static_color_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    static_color_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    static_color_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )
    flash_3x_parser = subparsers.add_parser(
        name='flash_3x',
        help=f"help for flash_3x command."
    )
    flash_3x_parser.add_argument(
        'speed',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    flash_3x_parser.add_argument(
        'brightness',
        nargs='?',
        type=str,
        metavar='NUMERIC VALUE'
    )
    flash_3x_parser.add_argument(
        'color',
        nargs='?',
        type=str,
        metavar='COLOR',
        help="Accepts 'random', preset colors , named html colors, colors in the form of RGB ex.:1fe or RRGGBB ex.: 15f0e3"
    )

    # per key
    parser = subparsers.add_parser(
        name='per_key',
        help=f"Set color per group or per key.\n Example: rgbkb per_key  --all black --f_keys red --letters crimson --number_row 0f0 --numpad_numbers sea_green"
    )
    key_groups = parser.add_argument_group('Key Groups')
    for keyword in tuple(group_name.value for group_name in GroupNames):
        key_groups.add_argument(
            f"--{keyword}",
            metavar="COLOR",
            action=OrderedArgs,
            help="Color of this entire group of keys, Accepts: RGB, RRGGBB and named html colors."

        )
    keys = parser.add_argument_group('Individual Keys')
    for keyword in tuple(key_name.value for key_name in KeyNames):
        keys.add_argument(
            f"--{keyword}",
            metavar="COLOR",
            action=OrderedArgs,
            help=f"Set color of {keyword}, Accepts: RGB, RRGGBB and named html colors."
        )


class AcerPredatorPH1671(RgbKeyboard):
    VID = 0x04F2

    PID = 0x0117
    MODEL = "PH16-71"
    NAME = "Acer Predator PH16-71 Keyboard"

    @staticmethod
    def update_subparser(subparsers):
        add_parsers_to_cli_subparser(subparsers)


    @staticmethod
    def parse_arguments(argv: list[str]) -> list[KeyboardCommand]:
        keywords = AcerPredatorPH1671.available_cli_keywords()
        i = 0
        split_arguments = []
        while i < len(argv):
            if argv[i] not in keywords:
                raise ValueError(f'Unknown keyword {argv[i]} on position {i}.')
            split_arguments.append([argv[i]])
            i += 1
            while i < len(argv) and argv[i] not in keywords:
                split_arguments[-1].append(argv[i])
                i += 1
        output = []
        for name, *arguments in split_arguments:
            try:
                command = ARGUMENTS_TO_COMMANDS[name].parse_arguments(arguments)
                output.append(command)
            except KeyError as e:
                raise ValueError(f'Unknown command {name} with arguments {arguments}.') from e
        return output

    @staticmethod
    def available_cli_keywords() -> tuple[str, ...]:
        return tuple(effect_name.value for effect_name in EffectNames) + tuple(
            key_name.value for key_name in KeyNames) + tuple(group_name.value for group_name in GroupNames)

    def __init__(self, device: Device):
        self.device = device

    def send_control_transfer(self, request: int, value: int, index: int, data: bytes, request_type: RequestType,
                              recipient: Recipient):
        transfer = ControlTransfer(request_type, recipient, request, value, index)
        self.device.control_transfer_out(transfer, data)

    def send_commands(self, *commands: bytes):
        self.device.detach_standard_drivers()
        self.device.open()
        self.device.claim_interface(3)
        self.device.clear_halt(4, TransferDirection.OUT)
        for command in commands:
            self.send_control_transfer(9, 0x0300, 3, command, RequestType.CLASS, Recipient.INTERFACE)
        self.device.release_interface(3)
        self.device.close()
        self.device.attach_standard_drivers()

    def color_at_index(self, color: str, index: int):
        self.device.detach_standard_drivers()
        self.device.open()
        self.device.claim_interface(3)
        self.device.clear_halt(4, TransferDirection.OUT)
        self.send_control_transfer(
            9,
            0x0300,
            3,
            bytes.fromhex('12 00 00 08  00 00 00 e5'),
            RequestType.CLASS,
            Recipient.INTERFACE
        )
        payload = '00000000' * 16 * 8
        payload = payload[:index * 8] + '00' + color + payload[index * 8:]
        for chunk in wrap(payload, 64 * 2):
            self.device.transfer_out(4, bytes.fromhex(chunk))
        self.send_control_transfer(
            9,
            0x0300,
            3,
            bytes.fromhex('08 02 33 05  32 08 01 82'),
            RequestType.CLASS,
            Recipient.INTERFACE
        )
        self.device.release_interface(3)
        self.device.close()
        self.device.attach_standard_drivers()
