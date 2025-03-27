import binascii
from symtable import Class
from typing import Type
from usbx import Device, usb
from rgbkb.kb import RgbKeyboard
from rgbkb.acer_ph16_71.device import AcerPredatorPH1671

SUPPORTED_DEVICES: tuple[Type[RgbKeyboard]] = (
    AcerPredatorPH1671,
)


def chunkify(s, separator=" ", chunk_size=4):
    # Split the string into chunks of size `chunk_size`
    chunks = [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]
    # Join the chunks with separator and return
    formatted_string = separator.join(chunks)
    return formatted_string


def print_device_info(device: Device):
    print(
        f'VID: 0x{device.vid:04x}, PID: 0x{device.pid:04x}, Serial: {device.serial}, Protocol: {device.protocol_code}, Class: {device.class_code} {device.manufacturer}')
    print(f'Manufacturer: {device.manufacturer} Product: {device.product} Version: {device.device_version}')
    print(f'Configuration value: {device.configuration_value} Configuration descriptor:')
    print(chunkify(chunkify(binascii.hexlify(device.configuration_descriptor).decode('utf-8')), '\n', 80))
    print(f'{len(device.configuration.interfaces)} interfaces:')
    for interface in device.configuration.interfaces:
        print(f'\tInterface {interface.number} (currently selected alternate {interface.current_alternate.number})')
        for alternate in interface.alternates:
            print(
                f"\t\tAlternate {alternate.number} - Class:{alternate.class_code} SubClass:{alternate.subclass_code}"
                f" Protocol: {alternate.protocol_code} number of endpoints: {len(alternate.endpoints)}"
            )
            for endpoint in alternate.endpoints:
                print(
                    f"\t\t\tEndpoint {endpoint.number} Direction: {endpoint.direction.name}"
                    f" Transfer type: {endpoint.transfer_type.name} Max-Packet size: {endpoint.max_packet_size}b"
                )

def is_supported_device(device: Device) -> bool:
    if device is None or not isinstance(device, Device):
        return False
    known_devices = (f"{kb.VID}:{kb.PID}" for kb in SUPPORTED_DEVICES)
    return f"{device.vid}:{device.pid}" in known_devices


def find_supported_devices() -> tuple[RgbKeyboard,...]:
    known_devices = {f"{d.VID}:{d.PID}": d for d in SUPPORTED_DEVICES}
    available_known_devices = tuple(known_devices[f"{d.vid}:{d.pid}"].__call__(d) for d in usb.find_devices(is_supported_device))
    return available_known_devices