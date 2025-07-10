# RGB Keyboard Control Tool (rgbkb)

A CLI tool to control RGB backlight effects on the Acer Predator PH16-71 keyboard (and potentially other compatible keyboards) on Linux. This tool allows you to customize colors, apply animations, and persist settings across reboots.
    
**Special thanks to:**
- [fuho](https://github.com/fuho) for creating this amazing project!
- [sbstratos79](https://github.com/sbstratos79) for the RGB color implementations!

## Features

- **Static Color**: Set the entire keyboard to a custom HEX color
- **Animations**: Apply effects like:
  - Wave (Supports Directions)
  - Breathing
  - Ripple
  - Snake
  - Heartbeat
  - Snow
  - Fireball
  - Stars
  - Lightning
  - Rain
- **Persistent Settings**: Save your last-used effect and reapply it at startup
- **Customizable Parameters**: Adjust speed, brightness, and direction for supported effects
- **Randomize Effects**: Random effect on execution

## Installation

```bash
# Step 1: Clone the repository
git clone https://github.com/Order52/ph16-71-rgb.git
cd rgbkb
```

# Step 2: Install dependencies
 First install system dependencies
```bash
sudo pacman -S python python-pipx  # or python3/python3-pipx depending on your distro
```

# Core Python dependencies (automatically handled by pip)
 Includes:
 - pyusb
 - click
 - rich
 - packaging

# Step 3: Install the application
 Option 1: Using pipx (recommended)
```bash
# 1. Uninstall existing version (if any)
pipx uninstall rgbkb

# 2. Clone the repository
git clone https://github.com/Order52/ph16-71-rgb.git
cd ph16-71-rgb

# 3. Install the actual package from the subfolder
pipx install --include-deps ~/ph16-71-rgb/

# 4. Inject the missing dependency (click)
pipx inject rgbkb click

# 5. Test it
which rgbkb
rgbkb --help
rgbkb wave --speed 10 --level 0

```

 OR Option 2: Using virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install --editable '.[dev]'
```

# Step 4: Configure USB permissions
```bash
sudo groupadd plugdev
sudo usermod -a -G plugdev $USER
echo 'SUBSYSTEM=="usb", MODE="0660", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-usb-permissions.rules
sudo udevadm control --reload-rules
echo "Please log out and back in for changes to take effect or restart"
```
  
### Then use the rgb_menu.py for more user-friendly usage!
```bash
cd ~/ph16-71-rgb
chmod +x rgb_menu.py
chmod +x rgb_random.py   
python3 ./rgb_menu.py  # RGB Menu
python ./rgb_random.py # The RGB Randomizer
```
