0000   1c 00 a0 99 45 df 84 ae ff ff 00 00 00 00 1b 00   ....E...........
0010   00 01 00 03 00 00 02 10 00 00 00 00 21 09 00 03   ............!...
0020   03 00 08 00 12 00 00 08 00 00 00 e5               ............

Frame 2893: 44 bytes on wire (352 bits), 44 bytes captured (352 bits) on interface \\.\USBPcap1, id 0
    Section number: 1
    Interface id: 0 (\\.\USBPcap1)
        Interface name: \\.\USBPcap1
        Interface description: USBPcap1
    Encapsulation type: USB packets with USBPcap header (152)
    Arrival Time: Oct  6, 2024 00:55:23.728331000 CEST
    UTC Arrival Time: Oct  5, 2024 22:55:23.728331000 UTC
    Epoch Arrival Time: 1728168923.728331000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.013032000 seconds]
    [Time delta from previous displayed frame: 2.278059000 seconds]
    [Time since reference or first frame: 42.595573000 seconds]
    Frame Number: 2893
    Frame Length: 44 bytes (352 bits)
    Capture Length: 44 bytes (352 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: usb:usbhid]
USB URB
    [Source: host]
    [Destination: 1.3.0]
    USBPcap pseudoheader length: 28
    IRP ID: 0xffffae84e00419a0
    IRP USBD_STATUS: USBD_STATUS_SUCCESS (0x00000000)
    URB Function: URB_FUNCTION_CLASS_INTERFACE (0x001b)
    IRP information: 0x00, Direction: FDO -> PDO
        0000 000. = Reserved: 0x00
        .... ...0 = Direction: FDO -> PDO (0x0)
    URB bus id: 1
    Device address: 3
    Endpoint: 0x00, Direction: OUT
        0... .... = Direction: OUT (0)
        .... 0000 = Endpoint number: 0
    URB transfer type: URB_CONTROL (0x02)
    Packet Data Length: 16
    [Response in: 2894]
    Control transfer stage: Setup (0)
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
