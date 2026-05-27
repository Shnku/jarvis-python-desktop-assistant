import webbrowser

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
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True

    return False
