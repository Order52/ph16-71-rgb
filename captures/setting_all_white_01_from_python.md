0000   40 74 d2 81 20 9b ff ff 53 02 00 03 01 00 00 00   @t.. ...S.......
0010   97 3e 04 67 00 00 00 00 dd 3c 09 00 8d ff ff ff   .>.g.....<......
0020   08 00 00 00 08 00 00 00 21 09 00 03 03 00 08 00   ........!.......
0030   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0040   12 00 00 08 00 00 00 e5                           ........


Frame 315: 72 bytes on wire (576 bits), 72 bytes captured (576 bits) on interface usbmon1, id 0
    Section number: 1
    Interface id: 0 (usbmon1)
        Interface name: usbmon1
    Encapsulation type: USB packets with Linux header and padding (115)
    Arrival Time: Oct  7, 2024 22:03:35.605405000 CEST
    UTC Arrival Time: Oct  7, 2024 20:03:35.605405000 UTC
    Epoch Arrival Time: 1728331415.605405000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.000495000 seconds]
    [Time delta from previous displayed frame: 0.000495000 seconds]
    [Time since reference or first frame: 3.550735000 seconds]
    Frame Number: 315
    Frame Length: 72 bytes (576 bits)
    Capture Length: 72 bytes (576 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: usb:usbhid]
USB URB
    [Source: host]
    [Destination: 1.3.0]
    URB id: 0xffff9b2081d27440
    URB type: URB_SUBMIT ('S')
    URB transfer type: URB_CONTROL (0x02)
    Endpoint: 0x00, Direction: OUT
        0... .... = Direction: OUT (0)
        .... 0000 = Endpoint number: 0
    Device: 3
    URB bus id: 1
    Device setup request: relevant ('\0')
    Data: present ('\0')
    URB sec: 1728331415
    URB usec: 605405
    URB status: Operation now in progress (-EINPROGRESS) (-115)
    URB length [bytes]: 8
    Data length [bytes]: 8
    [Response in: 316]
    Interval: 0
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
    [bInterfaceClass: HID (0x03)]
Setup Data
    bmRequestType: 0x21
        0... .... = Direction: Host-to-device
        .01. .... = Type: Class (0x1)
        ...0 0001 = Recipient: Interface (0x01)
    bRequest: SET_REPORT (0x09)
    wValue: 0x0300
        ReportID: 0
        ReportType: Feature (3)
    wIndex: 3
    wLength: 8
    Data Fragment: 12000008000000e5
