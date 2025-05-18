import os
import shutil

SOURCE_DIR = "/home/pi/roms_inbox"
TARGET_BASE = "/home/pi/RetroPie/roms"

ROM_TYPES = {
    "nes": [".nes"],
    "snes": [".sfc", ".smc"],
    "gba": [".gba"],
    "gb": [".gb"],
    "gbc": [".gbc"],
    "n64": [".n64", ".z64", ".v64"],
    "psx": [".bin", ".cue", ".img", ".pbp"],
    "megadrive": [".md", ".gen", ".smd"],
    "genesis": [".gen"],
    "mastersystem": [".sms"],
    "segacd": [".iso", ".bin", ".cue"],
    "sega32x": [".32x"],
    "sg-1000": [".sg"],
    "gamegear": [".gg"],
    "arcade": [".zip"],
    "mame-libretro": [".zip"],
    "neogeo": [".zip"],
    "ngp": [".ngp"],
    "ngpc": [".ngc"],
    "pcengine": [".pce"],
    "amstradcpc": [".dsk"],
    "atari2600": [".a26"],
    "atari5200": [".a52"],
    "atari7800": [".a78"],
    "atarilynx": [".lnx"],
    "atari800": [".xex", ".atr", ".rom"],
    "coleco": [".col"],
    "channelf": [".chf"],
    "fds": [".fds"],
    "vectrex": [".vec"],
    "zxspectrum": [".tap", ".tzx", ".z80"],
    "msx": [".rom"],
}

def get_system_by_extension(filename):
    ext = os.path.splitext(filename)[1].lower()
    for system, extensions in ROM_TYPES.items():
        if ext in extensions:
            return system
    return None

def move_roms():
    for file in os.listdir(SOURCE_DIR):
        full_path = os.path.join(SOURCE_DIR, file)
        if os.path.isfile(full_path):
            system = get_system_by_extension(file)
            if system:
                target_dir = os.path.join(TARGET_BASE, system)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(target_dir, file))
                print(f"✅ {file} → {system}")
            else:
                print(f"Unknown Format {file}")

if __name__ == "__main__":
    move_roms()

