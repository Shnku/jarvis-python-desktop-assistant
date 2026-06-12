import os
import platform as pt
import subprocess as sp
from pathlib import Path
from threading import Thread

from speech import speak

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
                say = f"Opening {name.capitalize()}"
                os.startfile(folder) if pt.system == "Windows" else sp.run(
                    ["xdg-open", folder]
                )
            else:
                say = f"{name} folder was not found"
            Thread(target=speak, args=[say], daemon=True).start()
            return say

    return False
