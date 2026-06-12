import webbrowser
from threading import Thread

from speech import speak

WEBSITES = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "github": "https://github.com",
}


def open_website(command):
    for name, url in WEBSITES.items():
        if f"open {name}" in command:
            # speak(f"Opening {name}")
            Thread(target=speak, args=[f"Opening {name}"], daemon=True).start()
            webbrowser.open(url)
            return f"openning {name}"

    return False
