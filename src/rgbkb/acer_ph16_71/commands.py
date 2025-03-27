from enum import Enum

from rgbkb.kb import KeyboardCommand


class EffectNames(Enum):
    HEARTBEAT = 'heartbeat'
    SNOW = 'snow'
    FIREBALL = 'fireball'
    STARS = 'stars'
    SPOT = 'spot'
    LIGHTNING = 'lightning'
    RAIN = 'rain'
    NEON = 'neon'
    RIPPLE = 'ripple'
    SNAKE = 'snake'
    WAVE = 'wave'
    BREATHING = 'breathing'
    STATIC_COLOR = 'static_color'
    FLASH_3X = 'flash_3x'


effect_command = lambda identifier, *args: bytes.fromhex(identifier) + bytes((*args, 0))

color = lambda *args: effect_command('14 00 00', *args, 0)
heartbeat = lambda *args: effect_command('08 02 29', *args)
snow = lambda *args: effect_command('08 02 28', *args)
fireball = lambda *args: effect_command('08 02 27', *args)
stars = lambda *args: effect_command('08 02 26', *args)
spot = lambda *args: effect_command('08 02 25', *args)
lightning = lambda *args: effect_command('08 02 12', *args)
rain = lambda *args: effect_command('08 02 0a', *args)
neon = lambda *args: effect_command('08 02 08', *args)
ripple = lambda *args: effect_command('08 02 06', *args)
snake = lambda *args: effect_command('08 02 05', *args)
wave = lambda *args: effect_command('08 02 03', *args)
breathing = lambda *args: effect_command('08 02 02', *args)
static_color = lambda *args: effect_command('08 02 01', *args)
flash3x = lambda *args: effect_command('08 03 22', *args)

# @formatter:off
ALL_KEYS_WHITE = (
    ('send_control_request', 9, 0x0300, 3, bytes.fromhex('12 00 00 08  00 00 00 e5')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff')),
    ('send_interrupt_transfer', 3, 4, bytes.fromhex('00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff0000000000000000')),
    ('send_control_request', 9, 0x0300, 3, bytes.fromhex('08 02 33 05  32 08 01 82')),
)
# @formatter:on

# @formatter:off
FLASH_KEYS = (
    # Captured
    ('14 00 01 2e  09 c7 00 ec', '08 03 22 05  32 02 01 98'),  # 3 flash blue
    ('14 00 01 c7  00 ff 00 24', '08 03 22 05  32 02 01 98'),  # 3 flash purple
    # Synthesised
    # 14 00 01 RR  GG BB 00 24
    ('14 00 01 ff  00 00 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash red
    ('14 00 01 ff  ff 00 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash yellow
    ('14 00 01 00  ff 00 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash green
    ('14 00 01 00  ff ff 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash cyan
    ('14 00 01 00  00 ff 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash blue
    ('14 00 01 ff  00 ff 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash purple
    ('14 00 01 ff  ff ff 00 00', '08 03 22 05  32 02 01 98'),  # 3 flash white
    (                            '08 03 22 01  00 00 01 00',),  # 3 flash cyan
    (                            '08 03 22 00  00 00 00 ff',),  # 3 flash cyan
    (                            '08 03 22 00  00 00 00 00',),  # 3 flash cyan
    (                            '08 03 22 ff  ff 00 ff ff',),  # 3 flash cyan
    (                            '08 03 22 00  00 02 00 00',),  # 3 flash red
    (                            '08 03 22 ff  ff 02 ff ff',),  # 3 flash red
    (                            '08 03 22 00  00 03 00 00',),  # 3 flash yellow
    (                            '08 03 22 ff  ff 03 ff ff',),  # 3 flash yellow
    (                            '08 03 22 ff  ff 04 ff ff',),  # 3 flash last set color
    (                            '08 03 22 00  00 04 00 00',),  # 3 flash last set color
    (                            '08 03 22 00  00 05 00 00',),  # 3 flash last set color
    (                            '08 03 22 00  00 06 00 00',),  # 3 flash last set color
    (                            '08 03 22 00  00 07 00 00',),  # 3 flash last set color
    (                            '08 03 22 ff  ff ff ff ff',),  # 3 flash last set color
    (                            '08 03 22 00  00 01 00 ff',),  # 3 flash last set color
    (                            '08 03 22 00  00 04 00 ff',),  # 3 flash last static color?
    (                            '08 03 22 00  00 05 00 ff',),  # 3 flash last static color?
    # Working on this one
    (                            '08 03 22 00  00 18 00 00',),  # 3 flash last set color
)

BRIGHTNESS_MAX = 0x32
SPEED_MAX = 0x1b

class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red % 256
        self.green = green % 256
        self.blue = blue % 256

class ColorPreset(Enum):
    STATIC = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 3
    CYAN = 4
    MAGENTA = 5
    WHITE = 6
    RANDOM = 7

class HtmlColors(Enum):
    ALICE_BLUE = "f0f8ff"  # White
    ANTIQUE_WHITE = "faebd7"  # White
    AQUA = "00ffff"  # Blue
    AQUA_MARINE = "7fffd4"  # Blue
    AZURE = "f0ffff"  # White
    BEIGE = "f5f5dc"  # White
    BISQUE = "ffe4c4"  # Brown
    BLACK = "000000"  # Gray
    BLANCHED_ALMOND = "ffebcd"  # Brown
    BLUE = "0000ff"  # Blue (one of preset colors)
    BLUE_VIOLET = "8a2be2"  # Purple
    BROWN = "a52a2a"  # Brown
    BURLY_WOOD = "deb887"  # Brown
    CADET_BLUE = "5f9ea0"  # Blue
    CHARTREUSE = "7fff00"  # Green
    CHOCOLATE = "d2691e"  # Brown
    CORAL = "ff7f50"  # Orange
    CORN_FLOWER_BLUE = "6495ed"  # Blue
    CORNSILK = "fff8dc"  # Brown
    CRIMSON = "dc143c"  # Red
    CYAN = "00ffff"  # Blue
    DARK_BLUE = "00008b"  # Blue
    DARK_CYAN = "008b8b"  # Green
    DARK_GOLDEN_ROD = "b8860b"  # Brown
    DARK_GRAY = "a9a9a9"  # Gray
    DARK_GREEN = "006400"  # Green
    DARK_KHAKI = "bdb76b"  # Yellow
    DARK_MAGENTA = "8b008b"  # Purple
    DARK_OLIVE_GREEN = "556b2f"  # Green
    DARK_ORANGE = "ff8c00"  # Orange
    DARK_ORCHID = "9932cc"  # Purple
    DARK_RED = "8b0000"  # Red
    DARK_SALMON = "e9967a"  # Red
    DARK_SEA_GREEN = "8fbc8f"  # Green
    DARK_SLATE_BLUE = "483d8b"  # Purple
    DARK_SLATE_GRAY = "2f4f4f"  # Gray
    DARK_TURQUOISE = "00ced1"  # Blue
    DARK_VIOLET = "9400d3"  # Purple
    DEEP_PINK = "ff1493"  # Pink
    DEEP_SKY_BLUE = "00bfff"  # Blue
    DIM_GRAY = "696969"  # Gray
    DODGER_BLUE = "1e90ff"  # Blue
    FIRE_BRICK = "b22222"  # Red
    FLORAL_WHITE = "fffaf0"  # White
    FOREST_GREEN = "228b22"  # Green
    FUCHSIA = "ff00ff"  # Purple
    GAINSBORO = "dcdcdc"  # Gray
    GHOST_WHITE = "f8f8ff"  # White
    GOLD = "ffd700"  # Yellow
    GOLDEN_ROD = "daa520"  # Brown
    GRAY = "808080"  # Gray
    GREEN = "008000"  # Green
    GREEN_YELLOW = "adff2f"  # Green
    HONEY_DEW = "f0fff0"  # White
    HOT_PINK = "ff69b4"  # Pink
    INDIAN_RED = "cd5c5c"  # Red
    INDIGO = "4b0082"  # Purple
    IVORY = "fffff0"  # White
    KHAKI = "f0e68c"  # Yellow
    LAVENDER = "e6e6fa"  # Purple
    LAVENDER_BLUSH = "fff0f5"  # White
    LAWN_GREEN = "7cfc00"  # Green
    LEMON_CHIFFON = "fffacd"  # Yellow
    LIGHT_BLUE = "add8e6"  # Blue
    LIGHT_CORAL = "f08080"  # Red
    LIGHT_CYAN = "e0ffff"  # Blue
    LIGHT_GOLDENROD_YELLOW = "fafad2"  # Yellow
    LIGHT_GRAY = "d3d3d3"  # Gray
    LIGHT_GREEN = "90ee90"  # Green
    LIGHT_PINK = "ffb6c1"  # Pink
    LIGHT_SALMON = "ffa07a"  # Orange
    LIGHT_SEA_GREEN = "20b2aa"  # Green
    LIGHT_SKY_BLUE = "87cefa"  # Blue
    LIGHT_SLATE_GRAY = "778899"  # Gray
    LIGHT_STEEL_BLUE = "b0c4de"  # Blue
    LIGHT_YELLOW = "ffffe0"  # Yellow
    LIME = "00ff00"  # Green
    LIME_GREEN = "32cd32"  # Green
    LINEN = "faf0e6"  # White
    MAGENTA = "ff00ff"  # Purple
    MAROON = "800000"  # Brown
    MEDIUM_AQUA_MARINE = "66cdaa"  # Green
    MEDIUM_BLUE = "0000cd"  # Blue
    MEDIUM_ORCHID = "ba55d3"  # Purple
    MEDIUM_PURPLE = "9370d8"  # Purple
    MEDIUM_SEA_GREEN = "3cb371"  # Green
    MEDIUM_SLATE_BLUE = "7b68ee"  # Blue
    MEDIUM_SPRING_GREEN = "00fa9a"  # Green
    MEDIUM_TURQUOISE = "48d1cc"  # Blue
    MEDIUM_VIOLET_RED = "c71585"  # Pink
    MIDNIGHT_BLUE = "191970"  # Blue
    MINT_CREAM = "f5fffa"  # White
    MISTY_ROSE = "ffe4e1"  # White
    MOCCASIN = "ffe4b5"  # Yellow
    NAVAJO_WHITE = "ffdead"  # Brown
    NAVY = "000080"  # Blue
    OLD_LACE = "fdf5e6"  # White
    OLIVE = "808000"  # Green
    OLIVE_DRAB = "6b8e23"  # Green
    ORANGE = "ffa500"  # Orange
    ORANGE_RED = "ff4500"  # Orange
    ORCHID = "da70d6"  # Purple
    PALE_GOLDEN_ROD = "eee8aa"  # Yellow
    PALE_GREEN = "98fb98"  # Green
    PALE_TURQUOISE = "afeeee"  # Blue
    PALE_VIOLET_RED = "db7093"  # Pink
    PAPAYA_WHIP = "ffefd5"  # Yellow
    PEACH_PUFF = "ffdab9"  # Yellow
    PERU = "cd853f"  # Brown
    PINK = "ffc0cb"  # Pink
    PLUM = "dda0dd"  # Purple
    POWDER_BLUE = "b0e0e6"  # Blue
    PURPLE = "800080"  # Purple
    RED = "ff0000"  # Red
    ROSY_BROWN = "bc8f8f"  # Brown
    ROYAL_BLUE = "4169e1"  # Blue
    SADDLE_BROWN = "8b4513"  # Brown
    SALMON = "fa8072"  # Red
    SANDY_BROWN = "f4a460"  # Brown
    SEA_GREEN = "2e8b57"  # Green
    SEA_SHELL = "fff5ee"  # White
    SIENNA = "a0522d"  # Brown
    SILVER = "c0c0c0"  # Gray
    SKY_BLUE = "87ceeb"  # Blue
    SLATE_BLUE = "6a5acd"  # Purple
    SLATE_GRAY = "708090"  # Gray
    SNOW = "fffafa"  # White
    SPRING_GREEN = "00ff7f"  # Green
    STEEL_BLUE = "4682b4"  # Blue
    TAN = "d2b48c"  # Brown
    TEAL = "008080"  # Green
    THISTLE = "d8bfd8"  # Purple
    TOMATO = "ff6347"  # Orange
    TURQUOISE = "40e0d0"  # Blue
    VIOLET = "ee82ee"  # Purple
    WHEAT = "f5deb3"  # Brown
    WHITE = "ffffff"  # White
    WHITE_SMOKE = "f5f5f5"  # White
    YELLOW = "ffff00"  # Yellow
    YELLOW_GREEN = "9acd32"  # Green

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    CLOCKWISE = 5
    COUNTER_CLOCKWISE = 6

def parse_color(value: str, skip_preset = False) -> Color | ColorPreset:
    try:
        if not skip_preset and value.upper() in ColorPreset.__members__:
            return ColorPreset[value.upper()]
        if value.upper() in HtmlColors.__members__:
            return Color(
                int(HtmlColors[value.upper()][:2], 16) % 256,
                int(HtmlColors[value.upper()][2:4], 16) % 256,
                int(HtmlColors[value.upper()][4:], 16) % 256
            )
        elif len(value) == 6:
            return Color(
                int(value[0:2], 16) % 256,
                int(value[2:4], 16) % 256,
                int(value[4:6], 16) % 256
            )
        elif len(value) == 3:
            return Color(
                int(value[0] * 2, 16) % 256,
                int(value[1] * 2, 16) % 256,
                int(value[2] * 2, 16) % 256
            )
        else:
            raise ValueError(f"Can not construct Color from  '{value}'.")
    except Exception as _:
        raise ValueError(f"Can not construct Color from  '{value}'.")

def parse_numeric(value: str, lower_bound: int, upper_bound: int) -> int:
    try:
        if value[-1] == '%':
            percentage = int(value[:-1])
            if not 0 <= percentage <= 100:
                raise ValueError(f"Percentage value '{value}' is out of range.")
            return round(lower_bound + (percentage * (upper_bound - lower_bound) / 100))
        elif '.' in value:
            float_value = float(value)
            if 0 <= float_value <= 1.0:
                return round(lower_bound + (float_value * (upper_bound - lower_bound)))
            elif 1.0 < float_value <= 100.0:
                return round(lower_bound + (float_value / 100 * (upper_bound - lower_bound)))
            else:
                raise ValueError(f"Float value '{value}' is out of range.")
        else:
            raise ValueError(f"Value '{value}' does not end with '%' and is not a float.")
    except Exception as e:
        raise ValueError(f"Cannot construct numeric value from '{value}': {str(e)}")

def parse_brightness(value: str) -> int:
    try:
        return parse_numeric(value, 0, 1 + BRIGHTNESS_MAX)
    except Exception as _:
        raise ValueError(f"Can not construct brightness from  '{value}'.")

def parse_speed(value: str) -> int:
    try:
        return parse_numeric(value, 0, 1 + SPEED_MAX)
    except Exception as _:
        raise ValueError(f"Can not construct speed from  '{value}'.")

def parse_direction(value: str) -> Direction:
    try:
        return Direction[value.upper()]
    except Exception as _:
        raise ValueError(f"Can not construct direction from  '{value}'.")


class CmdStaticColor(KeyboardCommand):
    name = EffectNames.STATIC_COLOR

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdStaticColor instance, if it's possible to parse the input
        
        Valid options are:
        static_color {color: color}
        static_color {color: color} {brightness: quantity}
        If brightness not supplied 100% is assumed
        """
        if len(argv) == 1:
            color = parse_color(argv[0])
            return CmdStaticColor(color)
        elif len(argv) == 2:
            color = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdStaticColor(color, brightness)
        else:
            raise ValueError(f'Can not construct CmdStaticCommand from arguments {argv}.')

    def __init__(self, color: Color | ColorPreset, brightness: int = BRIGHTNESS_MAX):
        self.color = color
        self.brightness = brightness

class CmdFlash3x(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdFlash3x instance, if it's possible to parse the input
        
        Valid options are:
        flash_3x {color: color}
        flash_3x {color: color} {brightness: quantity}
        If brightness not supplied 100% is assumed.
        This command doesn't support preset colors because the device doesn't interpret them
        in a standard fashion. Therefore, this command will always send two USB transfers.
        """
        if len(argv) == 1:
            c = parse_color(argv[0], skip_preset = True)
            return CmdFlash3x(c)
        elif len(argv) == 2:
            c = parse_color(argv[0], skip_preset = True)
            brightness = parse_brightness(argv[1])
            return CmdFlash3x(c, brightness)
        else:
            raise ValueError(f'Can not construct CmdFlash3x from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX):
        self.color = color
        self.brightness = brightness

class CmdBreathing(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdBreathing instance, if it's possible to parse the input.

        Valid options are:  
        breathing {color: color}  
        breathing {color: color} {brightness: quantity}  
        breathing {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdBreathing(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdBreathing(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdBreathing(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdBreathing from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdWave(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdWave instance, if it's possible to parse the input.

        Valid options are:  
        wave {brightness: quantity}  
        wave {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if not argv:
            return CmdWave()
        elif len(argv) == 1:
            brightness = parse_brightness(argv[0])
            return CmdWave(brightness)
        elif len(argv) == 2:
            brightness = parse_brightness(argv[0])
            speed = parse_speed(argv[1])
            return CmdWave(brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdWave from arguments {argv}.')

    def __init__(self, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdNeon(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdNeon instance, if it's possible to parse the input.

        Valid options are:  
        neon {brightness: quantity}  
        neon {brightness: quantity} {speed: quantity}  
        neon {brightness: quantity} {speed: quantity} {direction: quantity}
        If brightness or speed is not supplied, 100% is assumed.
        I speed is not supplied 'right' is assumed.
        """
        if not argv:
            return CmdNeon()
        elif len(argv) == 1:
            brightness = parse_brightness(argv[0])
            return CmdNeon(brightness)
        elif len(argv) == 2:
            brightness = parse_brightness(argv[0])
            speed = parse_speed(argv[1])
            return CmdNeon(brightness, speed)
        elif len(argv) == 3:
            brightness = parse_brightness(argv[0])
            speed = parse_speed(argv[1])
            direction = parse_speed(argv[2])
            return CmdNeon(brightness, speed, direction)
        else:
            raise ValueError(f'Can not construct CmdNeon from arguments {argv}.')

    def __init__(self, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX, direction: Direction = Direction.RIGHT):
        self.brightness = brightness
        self.speed = speed
        self.direction = direction

class CmdSnake(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdSnake instance, if it's possible to parse the input.

        Valid options are:  
        snake {color: color}  
        snake {color: color} {brightness: quantity}  
        snake {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdSnake(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdSnake(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdSnake(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdSnake from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdRipple(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdRipple instance, if it's possible to parse the input.

        Valid options are:  
        ripple {color: color}  
        ripple {color: color} {brightness: quantity}  
        ripple {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdRipple(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdRipple(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdRipple(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdRipple from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdRain(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdRain instance, if it's possible to parse the input.

        Valid options are:  
        rain {color: color}  
        rain {color: color} {brightness: quantity}  
        rain {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdRain(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdRain(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdRain(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdRain from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdLightning(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdLightning instance, if it's possible to parse the input.

        Valid options are:  
        lightning {color: color}  
        lightning {color: color} {brightness: quantity}  
        lightning {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdLightning(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdLightning(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdLightning(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdLightning from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdSpot(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdSpot instance, if it's possible to parse the input.

        Valid options are:  
        spot {color: color}  
        spot {color: color} {brightness: quantity}  
        spot {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdSpot(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdSpot(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdSpot(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdSpot from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdStars(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdStars instance, if it's possible to parse the input.

        Valid options are:  
        stars {color: color}  
        stars {color: color} {brightness: quantity}  
        stars {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdStars(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdStars(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdStars(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdStars from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdFireball(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdFireball instance, if it's possible to parse the input.

        Valid options are:  
        fireball {color: color}  
        fireball {color: color} {brightness: quantity}  
        fireball {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdFireball(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdFireball(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdFireball(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdFireball from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdSnow(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdSnow instance, if it's possible to parse the input.

        Valid options are:  
        snow {color: color}  
        snow {color: color} {brightness: quantity}  
        snow {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdSnow(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdSnow(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdSnow(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdSnow from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

class CmdHeartbeat(KeyboardCommand):
    name = EffectNames.FLASH_3X

    @staticmethod
    def parse_arguments(argv: list[str]) -> 'KeyboardCommand':
        """
        :param argv:  Subsection of arguments from command line
        :return: CmdHeartbeat instance, if it's possible to parse the input.

        Valid options are:  
        heartbeat {color: color}  
        heartbeat {color: color} {brightness: quantity}  
        heartbeat {color: color} {brightness: quantity} {speed: quantity}  
        If brightness or speed is not supplied 100% is assumed.
        This might send one or two USB transfers depending on the choice of color.
        If it is one of the few preset colors, or a random one is requested, only one transfer
        is required.
        """
        if len(argv) == 1:
            c = parse_color(argv[0])
            return CmdHeartbeat(c)
        elif len(argv) == 2:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            return CmdHeartbeat(c, brightness)
        elif len(argv) == 3:
            c = parse_color(argv[0])
            brightness = parse_brightness(argv[1])
            speed = parse_speed(argv[2])
            return CmdHeartbeat(c, brightness, speed)
        else:
            raise ValueError(f'Can not construct CmdHeartbeat from arguments {argv}.')

    def __init__(self, color: Color, brightness: int = BRIGHTNESS_MAX, speed: int = SPEED_MAX):
        self.color = color
        self.brightness = brightness
        self.speed = speed

ARGUMENTS_TO_COMMANDS = {
    EffectNames.STATIC_COLOR.value: CmdStaticColor,
    EffectNames.FLASH_3X.value: CmdFlash3x,
    EffectNames.BREATHING.value: CmdBreathing,
    EffectNames.WAVE.value: CmdWave,
}
