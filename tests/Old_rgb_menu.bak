import subprocess
import os
import json
from pathlib import Path

# Config paths
CONFIG_DIR = Path.home() / ".config" / "rgbkb"
CONFIG_FILE = CONFIG_DIR / "config.json"

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

def save_config(effect: str, params: dict):
    ensure_config_dir()
    cfg = {"effect": effect, "params": params}
    CONFIG_FILE.write_text(json.dumps(cfg))

def load_config():
    if not CONFIG_FILE.exists():
        return None
    return json.loads(CONFIG_FILE.read_text())

def clear_screen():
    os.system("clear")

def run_rgbkb_command(args):
    try:
        subprocess.run(["rgbkb"] + args, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to run:", " ".join(["rgbkb"] + args))

def get_input(prompt, default=None, validator=None):
    while True:
        val = input(f"{prompt} [{default}]: ").strip()
        if not val:
            return default
        if validator:
            try:
                return validator(val)
            except Exception:
                print("❌ Invalid input. Please try again.")
        else:
            return val

def get_hex_color():
    preset_colors = {
        "1": ("Red", "FF0000"),
        "2": ("Green", "00FF00"),
        "3": ("Blue", "0000FF"),
        "4": ("Yellow", "FFFF00"),
        "5": ("Purple", "800080"),
        "6": ("Cyan", "00FFFF"),
        "7": ("White", "FFFFFF"),
        "8": ("Pink", "FF69B4"),
        "9": ("Custom hex code", None),
    }

    while True:
        print("\nChoose a color:")
        for k, (name, hexc) in preset_colors.items():
            if hexc:
                print(f" {k}) {name:<7} (# {hexc})")
            else:
                print(f" {k}) {name}")

        choice = input("Select a color number (default 7): ").strip() or "7"

        if choice in preset_colors:
            name, hexcode = preset_colors[choice]
            if hexcode:
                print(f"Selected {name} with hex #{hexcode}")
                return hexcode
            else:
                # Custom hex input
                val = input("Enter custom hex color (6 hex digits, e.g. 1A2B3C): ").strip()
                if len(val) == 6 and all(c in "0123456789abcdefABCDEF" for c in val):
                    return val
                else:
                    print("❌ Invalid hex code. Try again.")
        else:
            print("❌ Invalid choice. Try again.")

def get_speed():
    def validator(x):
        f = float(x)
        if not (1 <= f <= 11):
            raise ValueError()
        return 12 - int(f)  # Reverse mapping: 1 -> 11, 11 -> 1

    val = get_input("Enter speed (1=slow, 11=fast)", "11", validator) 
    print(f"→ Mapped speed: {val} (hardware scale)")
    return val

def get_brightness():
    return get_input(
        "Enter brightness (0-32)", 
        "32", 
        lambda x: int(x) if 0 <= int(x) <= 32 else (_ for _ in ()).throw(ValueError())
    )

def get_direction():
    print("\nChoose a direction:")
    print(" 1) Right")
    print(" 2) Left")
    print(" 3) Up")
    print(" 4) Down")
    print(" 5) Clockwise")
    print(" 6) Counterclockwise")

    while True:
        choice = input("Select a direction number (default 1): ").strip() or "1"
        if choice.isdigit() and 1 <= int(choice) <= 6:
            return choice
        else:
            print("❌ Invalid choice. Try again.")

def apply_effect(name, supports_color=False, supports_speed=False, supports_brightness=False, supports_direction=False):
    clear_screen()
    print(f"Applying effect: {name.capitalize()}\n")

    args = [name]

    if supports_color:
        color = get_hex_color()
        args.append(color)

    if supports_speed:
        speed = get_speed()
        args += ["--speed", str(speed)]

    if supports_brightness:
        level = get_brightness()
        args += ["--level", str(level)]

    if supports_direction:
        direction = get_direction()
        args += ["--direction", str(direction)]

    run_rgbkb_command(args)
    save_config(name, {"hexcolor": args[1] if supports_color else None, "speed": speed if supports_speed else None, "level": level if supports_brightness else None, "direction": direction if supports_direction else None})
    print(f"\n✅ Effect '{name}' applied successfully!")

def main():
    menu = {
        "1": ("wave",        {"color": False, "speed": True, "brightness": True, "direction": True}),
        "2": ("neon",        {"color": False, "speed": True, "brightness": True, "direction": False}),
        "3": ("all",         {"color": True,  "speed": False, "brightness": False, "direction": False}),
        "4": ("breathe",     {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "5": ("ripple",      {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "6": ("snake",       {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "7": ("heartbeat",   {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "8": ("snow",        {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "9": ("fireball",    {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "10":("stars",       {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "11":("spot",        {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "12":("lightning",   {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "13":("rain",        {"color": True,  "speed": True,  "brightness": True, "direction": False}),
        "0": ("exit",        {}),
        "14": ("apply",      {}),
    }

    while True:
        clear_screen()
        print("🎛️  RGBKB Mode Selector\n")
        for key, (label, _) in sorted(menu.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
            print(f" {key}. {label.capitalize()}")
        choice = input("\nChoose an effect number (0 to exit): ").strip()

        if choice == "0":
            clear_screen()
            print("👋 Goodbye!")
            break
        if choice not in menu:
            print("\n❌ Invalid choice. Press Enter to try again.")
            input()
            continue

        name, config = menu[choice]
        if name == "apply":
            cfg = load_config()
            if not cfg:
                print("No saved configuration found.")
                input("\nPress Enter to return to menu...")
                continue
            run_rgbkb_command([cfg["effect"]] + [f"--{k} {v}" for k, v in cfg["params"].items() if v is not None and k != "hexcolor"] + ([cfg["params"]["hexcolor"]] if cfg["params"]["hexcolor"] is not None else []))
            print(f"\n✅ Effect '{cfg['effect']}' applied successfully!")
            input("\nPress Enter to return to menu...")
            continue
        apply_effect(
            name,
            supports_color=config.get("color", False),
            supports_speed=config.get("speed", False),
            supports_brightness=config.get("brightness", False),
            supports_direction=config.get("direction", False),
        )
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

