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
    ('send_control_request', 9, 0x0300, 3, bytes.fromhex('0802330532080182')),
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
)

ANIMATIONS_EFFECTS = (
    # For global settings maximum of three commands are neccessary.
    # In most cases (if the desired color is one of the 7), there is only a need for one command.
    # In one case (Wave) this controls the direction 1 to 6 ---------------------,
    # Preset colors, overrides received color if not 1 -----------------------,  |
    # 0,5,9=cyan,1,8=red,2=green,3=yellow,4=blue,6-magenta,7-white            |  |
    # Almost looks like RGB is mapped to bits?  xxxxRBGR                      |  |
    # But there are other checks, anything 9 and over seems to be CYAN        |  |
    # Brightness-----------------------------------------------------------,  |  |
    # Speed------------------------------------------------------------,   |  |  |
    #                                                                  |   |  |  |
    # Blue----------------------------------------,                    |   |  |  |
    # Green------------------------------------,  |                    |   |  |  |
    # Red----------------------------------,   |  |                    |   |  |  |
    #                                      v   v  v                    v   v  v  v
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  ff ff 00 00', '08 02 29 ff  ff 01 01 9b'),  # Heartbeat White

    # Heartbeat: 08 02 29
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest) __ __ __ __  BR __ __ __
    # Preset colors: 01=STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used continuously
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  ff ff 00 00', '08 02 29 ff  ff 01 01 9b'),  # Heartbeat White
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  ff ff 00 00', '08 02 29 ff  01 01 01 9b'),  # Heartbeat White Dim
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  00 00 00 00', '08 02 29 ff  80 01 01 9b'),  # Heartbeat Red Bright
    ('b1 00 00 00  00 00 00 4e', '14 00 00 00  ff 00 00 00', '08 02 29 ff  80 01 01 9b'),  # Heartbeat Green
    (                                                        '08 02 29 01  32 07 00 9b',),  # Heartbeat White Bright Fast
    # Snow: 08 02 28
    # Speed: 1st quad 3rd byte can range from 01 to 0b, 01 being the shortest snowflake melt time and 0b being longest
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Color: 00=RANDOM_FLAKES, 01=STATIC, 02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM_SNOW
    # When color set to 01, the color set with last *14 00 00* will be used
    # Setting color (2nd quad 2nd byte) to 00 makes the color random for each snowflake.
    # Setting color to 08 sets a random color at init, then reuses it for each snowflake
    # When random (00) color selected, the brightness setting is ignored.
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  00 ff 00 00', '08 02 28 ff  80 01 01 9b'),  # Snow Purple
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  00 ff 00 00', '08 02 28 ff  ff 01 01 9b'),  # Snow Purple Bright
    (                                                        '08 02 28 01  32 01 00 9b',), # Snow Fast Bright White
    (                                                        '08 02 28 00  00 00 00 00',), # Snow Default RANDOM
    (                                                        '08 02 28 09  00 00 00 00',), # Snow Fast RANDOM
    (                                                        '08 02 28 01  00 00 00 00',), # Snow Slow RANDOM
    (                                                        '08 04 28 05  16 00 00 00',), # Snow Mid RANDOM Fast
    # Fireball: 08 02 27
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01-STATIC, 02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08-RANDOM
    # When color set to 08, random color wil be selected at init and then used for each fireball
    # When color set to 01, the color set with last *14 00 00* will be used
    ('b1 00 00 00  00 00 00 4e', '14 00 00 00  ff 00 00 00', '08 02 27 ff  80 01 01 9b'),  # Fireball Blue
    (                                                        '08 02 27 01  32 07 00 9b',), # Fireball Fast White
    # Stars: 08 02 26
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=LAST STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 08, random color wil be selected at init and then used for each star
    # When color set to 01, the color set with last *14 00 00* will be used
    ('b1 00 00 00  00 00 00 4e', '14 00 00 dd  80 33 00 00', '08 02 26 00  80 01 01 00'),  # Stars Tan
    (                                                        '08 02 26 01  32 07 00 9b',), # Stars Bright White Fast
    # Spot: 08 02 25
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 08, random color wil be selected at init and then used for each keypress
    # When color set to 01, color set with last *14 00 00* will be used
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ee  50 33 00 00', '08 02 25 00  80 01 01 00'),  # Spot Gold
    ('b1 00 00 00  00 00 00 4e', '14 00 00 66  00 33 00 00', '08 02 25 00  80 01 01 9b'),  # Spot Nice Pink To Purple
    (                                                        '08 02 25 01  32 07 00 9b',), # Spot Bright White Fast
    # Lightning: 08 02 12
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=LAST STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used for each lightning
    ('b1 00 00 00  00 00 00 4e', '14 00 00 cc  cc 00 00 00', '08 02 12 00  00 01 01 9b'),  # Lightning BR<32, then colors again
    (                                                        '08 02 12 01  32 07 00 9b',), # Lightning Bright White Fast
    # Rain: 08 02 0a
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=LAST STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used for each drop
    ('b1 00 00 00  00 00 00 4e', '14 00 00 cc  cc 00 00 00', '08 02 0a 00  16 01 01 9b'),  # Rain Yellow Slow Mid Bright
    ('b1 00 00 00  00 00 00 4e', '14 00 00 cc  00 cc 00 00', '08 02 0a 04  32 01 01 9b'),  # Rain Purple Faster? Bright
    (                                                        '08 02 0a 01  32 07 00 9b',), # Rain Bright White Fast
    # Neon: 08 02 08
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    ('b1 00 00 00  00 00 00 4e',                             '08 02 08 09  32 01 01 9b'),  # Neon Slow Bright speed: 01-09
    ('b1 00 00 00  00 00 00 4e',                             '08 02 08 01  32 01 01 9b'),  # Neon Fast Bright bright: 00-32
    (                                                        '08 02 08 09  32 00 00 00',), # Neon Slow Bright
    # Ripple: 08 02 06
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=LAST STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used for each ripple
    ('b1 00 00 00  00 00 00 4e', '14 00 00 00  ff cc 00 00', '08 02 06 01  32 01 01 9b'),  # Ripple Turq Fast Bright
    ('b1 00 00 00  00 00 00 4e', '14 00 00 cc  ff 00 00 00', '08 02 06 09  16 01 01 9b'),  # Ripple Yellow Slow
    (                                                        '08 02 06 01  32 07 00 00',), # Ripple Fast Bright White
    # Snake: 08 02 05
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # Preset colors: 01=STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used for each run
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  00 cc 00 00', '08 02 05 09  16 01 01 9b'),  # Snake Purple Slow Mid
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  cc cc 00 00', '08 02 05 09  32 01 01 9b'),  # Snake Tan Slow Bright
    (                                                        '08 02 05 01  32 07 00 9b',), # Snake White Fast Mid
    # Wave: 08 02 03
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest)
    # There is no color control with __ __ __ __  __ XX __ __
    # Direction can be controlled with 3rd byte of 2nd quad __ __ __ __  __ XX __ __
    # Direction: 01=left, 02=right, 03=up, 04=down, 05=up, 06=clockwise, 07=counter-clockwise
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 01 9b'),  # Wave Bright Fast Right
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 02 9b'),  # Wave Bright Left
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 03 9b'),  # Wave Bright Fast Up
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 04 9b'),  # Wave Bright Fast Down
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 05 9b'),  # Wave Bright Fast Clockwise
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 01  32 01 06 9b'),  # Wave Bright Fast CounterClockwise
    ('b1 00 00 00  00 00 00 4e',                             '08 02 03 09  32 01 05 9b'),  # Wave Bright Slow Clockwise

    # Breathing: 08 02 02
    # Speed: 01=fast to 0b=slow, rest is default speed
    # Brightness: 2nd quad 1st byte ranges from 00 to 32 (brightest) __ __ __ __  BR __ __ __
    # Preset colors: 01=STATIC COLOR,  02=green, 03=yellow, 04=blue, 05=cyan, 06=magenta, 07=white, 08=RANDOM
    # When color set to 01, color set with last *14 00 00* will be used
    # When color set to 08, random color wil be selected at init and then used continuously
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 01 01 9b'),  # Breathing Red Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 02 01 9b'),  # Breathing Green Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 03 01 9b'),  # Breathing Yellow Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 04 01 9b'),  # Breathing Blue Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 05 01 9b'),  # Breathing Cyan Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 06 01 9b'),  # Breathing Magenta Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 01  32 07 01 9b'),  # Breathing White Fast
    ('b1 00 00 00  00 00 00 4e',                             '08 02 02 09  32 07 01 9b'),  # Breathing White Slow
    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  80 00 00 00', '08 02 02 01  32 01 01 9b'),  # Breathing Custom Orange Fast

    ('b1 00 00 00  00 00 00 4e', '14 00 00 ff  80 00 00 00', '08 02 01 00  08 01 01 9b'),  # Static Custom Orange
    ('b1 00 00 00  00 00 00 4e',                             '08 02 01 00  08 04 01 9b'),  # Static Preset Blue
    ('b1 00 00 00  00 00 00 4e',                             '08 02 01 00  32 02 01 9b'),  # Static BrightPreset Green
    ('08 02 00 00  00 00 00 f5', '14 00 00 00  00 00 00 eb', '08 02 01 00  00 01 01 9b'),  # Static Black?
    ('08 02 00 00  00 00 00 f5',                             '08 02 01 01  00 01 00 9b'),  # Off Also?
    (                                                        '08 02 01 00  00 00 00 9b',), # Off?
    (                                                        '08 02 01 00  32 03 00 9b',), # Static Bright Yellow
    # Working on this one:
    (                                                        '08 02 06 01  32 07 00 00',), # ???
)
# @formatter:on

