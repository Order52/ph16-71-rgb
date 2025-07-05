#!/usr/bin/env python3
import subprocess
import random

# Define effects and their capabilities
effects = {
    "wave":      {"color": False, "speed": True,  "direction": True,  "brightness": True},
    "neon":      {"color": False, "speed": True,  "direction": False, "brightness": True},
    "all":       {"color": True,  "speed": False, "direction": False, "brightness": False},
    "breathe":   {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "ripple":    {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "snake":     {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "heartbeat": {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "snow":      {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "fireball":  {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "stars":     {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "spot":      {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "lightning": {"color": True,  "speed": True,  "direction": False, "brightness": True},
    "rain":      {"color": True,  "speed": True,  "direction": False, "brightness": True},
}


# Predefined colors
colors = [
    "FF0000", "00FF00", "0000FF", "FFFF00",
    "800080", "00FFFF", "FFFFFF", "FF69B4",
    "1A2B3C", "ABCDEF"
]

# Fixed brightness level
brightness_level = "10"

# Randomly select an effect
effect_name, capabilities = random.choice(list(effects.items()))

args = [effect_name]

# Append random color
if capabilities["color"]:
    args.append(random.choice(colors))

# Append random speed
if capabilities["speed"]:
    speed = str(random.randint(1, 11))
    args += ["--speed", speed]

# Always append brightness
if capabilities.get("brightness", False):
    args += ["--level", brightness_level]




# Append random direction if supported
if capabilities.get("direction", False):
    direction = str(random.randint(1, 6))
    args += ["--direction", direction]

# Execute the command
try:
    subprocess.run(["rgbkb"] + args, check=True)
    print(f"Applied: {effect_name} with args {args}")
except subprocess.CalledProcessError:
    print("Failed to run rgbkb command.")

