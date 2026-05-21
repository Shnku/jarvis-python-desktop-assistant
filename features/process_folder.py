import os
from pathlib import Path
from main import speak

FOLDERS = {
    "desktop": Path.home() / "Desktop",
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "pictures": Path.home() / "Pictures",
}


def open_folder(command):
    for name, folder in FOLDERS.items():
        if f"open {name}" in command:
            if folder.exists():
                speak(f"Opening {name}")
                os.startfile(folder)
            else:
                speak(f"{name} folder was not found")
            return True

    return False
