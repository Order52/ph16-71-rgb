0000   c0 72 4b cd 22 9b ff ff 53 01 04 03 01 00 2d 00   .rK."...S.....-.
0010   a5 3c 04 67 00 00 00 00 6d 66 09 00 8d ff ff ff   .<.g....mf......
0020   40 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00   @...@...........
0030   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0040   00 ff ff ff 00 ff ff ff 00 ff ff ff 00 ff ff ff   ................
0050   00 ff ff ff 00 ff ff ff 00 ff ff ff 00 ff ff ff   ................
0060   00 ff ff ff 00 ff ff ff 00 ff ff ff 00 ff ff ff   ................
0070   00 ff ff ff 00 ff ff ff 00 ff ff ff 00 ff ff ff   ................


Frame 431: 128 bytes on wire (1024 bits), 128 bytes captured (1024 bits) on interface usbmon1, id 0
    Section number: 1
    Interface id: 0 (usbmon1)
        Interface name: usbmon1
    Encapsulation type: USB packets with Linux header and padding (115)
    Arrival Time: Oct  7, 2024 21:55:17.616045000 CEST
    UTC Arrival Time: Oct  7, 2024 19:55:17.616045000 UTC
    Epoch Arrival Time: 1728330917.616045000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.000173000 seconds]
    [Time delta from previous displayed frame: 0.000173000 seconds]
    [Time since reference or first frame: 10.408551000 seconds]
    Frame Number: 431
    Frame Length: 128 bytes (1024 bits)
    Capture Length: 128 bytes (1024 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: usb:usbhid]
USB URB
    [Source: host]
    [Destination: 1.3.4]
    URB id: 0xffff9b22cd4b72c0
    URB type: URB_SUBMIT ('S')
    URB transfer type: URB_INTERRUPT (0x01)
    Endpoint: 0x04, Direction: OUT
        0... .... = Direction: OUT (0)
        .... 0100 = Endpoint number: 4
    Device: 3
    URB bus id: 1
    Device setup request: not relevant ('-')
    Data: present ('\0')
    URB sec: 1728330917
    URB usec: 616045
    URB status: Operation now in progress (-EINPROGRESS) (-115)
    URB length [bytes]: 64
    Data length [bytes]: 64
    [Response in: 432]
    [bInterfaceClass: HID (0x03)]
    Unused Setup Header
    Interval: 1
    Start frame: 0
    Copy of Transfer Flags: 0x00000000
        .... .... .... .... .... .... .... ...0 = Short not OK: False
        .... .... .... .... .... .... .... ..0. = ISO ASAP: False
        .... .... .... .... .... .... .... .0.. = No transfer DMA map: False
        .... .... .... .... .... .... ..0. .... = No FSBR: False
        .... .... .... .... .... .... .0.. .... = Zero Packet: False
        .... .... .... .... .... .... 0... .... = No Interrupt: False
        .... .... .... .... .... ...0 .... .... = Free Buffer: False
        .... .... .... .... .... ..0. .... .... = Dir IN: False
        .... .... .... ...0 .... .... .... .... = DMA Map Single: False
        .... .... .... ..0. .... .... .... .... = DMA Map Page: False
        .... .... .... .0.. .... .... .... .... = DMA Map SG: False
        .... .... .... 0... .... .... .... .... = Map Local: False
        .... .... ...0 .... .... .... .... .... = Setup Map Single: False
        .... .... ..0. .... .... .... .... .... = Setup Map Local: False
        .... .... .0.. .... .... .... .... .... = DMA S-G Combined: False
        .... .... 0... .... .... .... .... .... = Aligned Temp Buffer: False
    Number of ISO descriptors: 0
HID Data: 00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff00ffffff
