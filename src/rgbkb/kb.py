from abc import ABC, abstractmethod
from typing import Iterable


class KeyboardCommand(ABC):
    @staticmethod
    @abstractmethod
    def parse_arguments(argv: Iterable[str]) -> 'KeyboardCommand':
        ...

class RgbKeyboard(ABC):
    """Usb-Connected RGB Keyboard"""

    VID:int
    PID:int
    MODEL:str
    MODEL_NAME:str

    @staticmethod
    @abstractmethod
    def available_cli_keywords()->tuple[str]:
        ...

    @staticmethod
    @abstractmethod
    def update_subparser(subparsers):
        ...

    @staticmethod
    @abstractmethod
    def parse_arguments(argv : Iterable[str]) -> tuple[KeyboardCommand]:
        ...

    @abstractmethod
    def send_commands(self, *commands: bytes) -> None:
        ...

