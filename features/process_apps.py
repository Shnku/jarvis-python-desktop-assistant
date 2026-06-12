import subprocess
from threading import Thread

from speech import speak

# NOTE: windows only
APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
}


def open_app(command):
    for name, app in APPS.items():
        if f"open {name}" in command:
            # speak(f"Opening {name}")
            Thread(target=speak, args=[f"Opening {name}"], daemon=True).start()
            subprocess.Popen(app)
            return f"Opening {name}"
    return False
