import subprocess
from speech import speak


APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
}


def open_app(command):
    for name, app in APPS.items():
        if f"open {name}" in command:
            speak(f"Opening {name}")
            subprocess.Popen(app)
            return True

    return False
