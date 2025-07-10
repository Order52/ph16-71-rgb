import subprocess
import os
import json
from pathlib import Path

# Config paths
CONFIG_DIR = Path.home() / ".config" / "rgbkb"
CONFIG_FILE = CONFIG_DIR / "config.json"
SYSTEMD_SERVICE_NAME = "rgbkb-startup.service"
SYSTEMD_USER_DIR = Path.home() / ".config" / "systemd" / "user"

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

def ensure_systemd_dir():
    SYSTEMD_USER_DIR.mkdir(parents=True, exist_ok=True)

def save_config(effect: str, params: dict):
    ensure_config_dir()
    cfg = {"effect": effect, "params": params}
    CONFIG_FILE.write_text(json.dumps(cfg))

def load_config():
    if not CONFIG_FILE.exists():
        return None
    return json.loads(CONFIG_FILE.read_text())

def create_systemd_service(cfg):
    """Create a systemd user service to run the RGB effect on startup"""
    ensure_systemd_dir()
    
    # Find the full path to rgbkb command
    try:
        result = subprocess.run(["which", "rgbkb"], capture_output=True, text=True, check=True)
        rgbkb_path = result.stdout.strip()
    except subprocess.CalledProcessError:
        # Fallback to common paths
        rgbkb_path = "/usr/local/bin/rgbkb"
        if not Path(rgbkb_path).exists():
            rgbkb_path = "/usr/bin/rgbkb"
    
    # Build the command from saved config
    cmd_parts = [rgbkb_path, cfg["effect"]]
    
    # Add parameters in the correct order
    if cfg["params"]["hexcolor"] is not None:
        cmd_parts.append(cfg["params"]["hexcolor"])
    
    for param, value in cfg["params"].items():
        if value is not None and param != "hexcolor":
            cmd_parts.append(f"--{param}")
            cmd_parts.append(str(value))
    
    # Join command parts with proper escaping
    command = " ".join(cmd_parts)
    
    service_content = f"""[Unit]
Description=RGBKB RGB Keyboard Effect
After=graphical-session.target

[Service]
Type=oneshot
ExecStart={command}
RemainAfterExit=yes
Environment=PATH=/usr/local/bin:/usr/bin:/bin
Environment=HOME={os.getenv('HOME')}

[Install]
WantedBy=default.target
"""
    
    service_file = SYSTEMD_USER_DIR / SYSTEMD_SERVICE_NAME
    service_file.write_text(service_content)
    
    return service_file

def enable_systemd_service():
    """Enable and start the systemd service"""
    try:
        # Reload systemd to recognize the new service
        subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
        
        # Enable the service to start on boot
        subprocess.run(["systemctl", "--user", "enable", SYSTEMD_SERVICE_NAME], check=True)
        
        # Start the service now
        subprocess.run(["systemctl", "--user", "start", SYSTEMD_SERVICE_NAME], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to enable systemd service: {e}")
        return False

def disable_systemd_service():
    """Disable and remove the systemd service"""
    try:
        # Stop the service
        subprocess.run(["systemctl", "--user", "stop", SYSTEMD_SERVICE_NAME], 
                      check=False)  # Don't fail if service doesn't exist
        
        # Disable the service
        subprocess.run(["systemctl", "--user", "disable", SYSTEMD_SERVICE_NAME], 
                      check=False)  # Don't fail if service doesn't exist
        
        # Remove the service file
        service_file = SYSTEMD_USER_DIR / SYSTEMD_SERVICE_NAME
        if service_file.exists():
            service_file.unlink()
        
        # Reload systemd
        subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to disable systemd service: {e}")
        return False

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
        "15": ("remove_startup", {}),
    }

    while True:
        clear_screen()
        print("🎛️  RGBKB Mode Selector\n")
        for key, (label, _) in sorted(menu.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
            if label == "remove_startup":
                print(f" {key}. Remove startup service")
            else:
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
            
            # Build the command args correctly
            cmd_args = [cfg["effect"]]
            if cfg["params"]["hexcolor"] is not None:
                cmd_args.append(cfg["params"]["hexcolor"])
            
            for param, value in cfg["params"].items():
                if value is not None and param != "hexcolor":
                    cmd_args.extend([f"--{param}", str(value)])
            
            # Apply the effect immediately
            run_rgbkb_command(cmd_args)
            print(f"\n✅ Effect '{cfg['effect']}' applied successfully!")
            
            # Ask if user wants to enable on startup
            enable_startup = input("\nEnable this effect on system startup? (y/n) [n]: ").strip().lower()
            if enable_startup == 'y':
                print("Creating systemd service...")
                service_file = create_systemd_service(cfg)
                if enable_systemd_service():
                    print(f"✅ Systemd service created and enabled!")
                    print(f"Effect will now run automatically on system startup.")
                    print(f"Service file: {service_file}")
                else:
                    print("❌ Failed to enable systemd service.")
            
            input("\nPress Enter to return to menu...")
            continue
        
        elif name == "remove_startup":
            if disable_systemd_service():
                print("✅ Startup service removed successfully!")
            else:
                print("❌ Failed to remove startup service.")
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
