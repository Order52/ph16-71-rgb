# RGB Keyboard (rgbkb)

Program to control RGB backlight of a computer keyboard on linux

Specifically, Acer Predator PH16-71, but likely there are other compatible marketing victims.

### Reasons
I couldn't find any way to control the keyboard backlight from linux. The settings do not carry 
over from Windows as the keyboard is reset on each reboot. This would not be a problem if Acer decided
to use sane default backlight settings. Unfortunately, likely due to their need to differentiate themselves from 
all the other displayed laptop units on the shop floor by showing that this particular laptop has individually
addressable rgb key backlight, the default keyboard setting is a cyan rendition of a night sky. Cyan likely because
["At lower light levels, where only the rod cells function, the sensitivity is greatest at a blueish-green
wavelength."](https://en.wikipedia.org/wiki/Cone_cell#Function) And starry sky because ["Flicker fusion thresholds
decline towards the periphery, but do that at a lower rate than other visual functions; so the periphery has a relative
advantage at noticing flicker."](https://en.wikipedia.org/wiki/Peripheral_vision#cite_ref-StrasburgerRentschler2011_1-5).
I love ([marketing](https://en.wikipedia.org/wiki/Marketing)...  

This, in addition to the already strange physical layout (arrow keys nestled under Enter and Shift), kind of makes the
laptop unpleasant to use since the keys essentially try to escape and move right under your fingers when you type (in linux).
This is a shame because the keyboard is the interface between the fleshy sack of blood and bones sitting in front of
it and the oh so awesome hardware inside (32 core CPU, 12GB VRam RTX4080, 64GB RAM in 2 dims, 2 NVMe sockets).

TODO: Here, maybe add a GIF, because it really is silly.

I tried to use OpenRGB, but it crashes during device lookup, tried to rebuild from source and limit
the system search to no avail.

### Method
Disassembly of windows libraries leads to nothing because I am not very smart. I did find out that the laptop drivers
shipped with `openrgb.exe` executable hidden inside and used it in its server mode. Their UI was then sending commands
to the server and `openrgb.exe` was doing the work (while looking at how it was run I found some concerning mentions
of kubernetes networks). At this point, I still didn't know if it communicated with the backlight using WMI or if it
was a USB device or something else altogether. I learned that the Turbo/Mode Select button is controlled using WMI in
logs but nothing regarding the keyboard.  
After installing the OpenRGB app it automatically found and connected to the `openrgb.exe --server` that
was started by PredatorSense with an open port. Thanks to this, I saw two identified devices, one for
the keyboard and the second one for the RGB light on the back of the laptop (let's not care about this). 
Then I used Wireshark to collect all the USB traffic while changing effects and colors in PredatorSense and later using
the OpenRGB GUI (which least allows me to save/export the key color settings, unlike PredatorSense).  
Then I combed through the captured USB packets and started learning about USB :) After a couple of days, 
I managed to find a way to stop the 'starry night animation' and managed to set all the keys to white. This was the
breakthrough I needed. Then I mapped where each key lies in the stream of data being sent to the
keyboard, so I could control individual keys. This was a lot of fun and not repetitive at all (did I mention this is
a 102-key keyboard with numpad?). Funnily enough, this individual key control is the most
involved way to set all keys to a single color as I later learned. After this, I started looking into
the animation effect of the keyboard and reverse engineered all of those. And that brings us to now...  

Now it "just" needs to be converted into a library/program that others can use....that should be easy...


# Issues with USB access
Your user will need to have access to USB devices.
The way I solved it for myself was to create a group `plugdev`, then telling `udevadm` to give that group access
using a cutom rule file and then adding my user to that group:
```bash
# Create group 'plugdev"
sudo groupadd plugdev

# Adding my user to plugdev group
sudo usermod -a -G plugdev $USER

# Creaate udev rule thst gives members of plugdev access to USB devices
sudo echo 'SUBSYSTEM=="usb", MODE="0660", GROUP="plugdev"' > /etc/udev/rules.d/00-usb-permissions.rules

# Reload udevadm so it can pick up the new rule
sudo udevadm control --reload-rules

#Now you have to log out and log in again
```

---
# Development
This is mostly for me to remember how to get this project running again... next time...  after months of inactivity.
Install it as editable (run from repo root, also run this to reinstall and/or on dependency changes):

`python -m pip install --upgrade --force-reinstall --editable '.[dev]'`

building distribution packages:
```shell
# Install build and distribute dependencies
python3 -m pip install --upgrade build twine

# Build the project
python3 -m build

# Test upload to testpypi
python3 -m twine upload --repository testpypi dist/*

# If all went well upload to PyPi
python3 -m twine upload --repository pypi dist/*
```  

# TODO
 - [ ] Add command that checks if user has access to usb
 - [ ] Add command to give user access to USB devices 