import webbrowser
from datetime import datetime
from urllib.parse import quote_plus

from features.get_joke import get_joke
from features.process_apps import open_app
from features.process_folder import open_folder
from features.process_website import open_website
from speech import speak


# ========== COMMAND ==========
def processCommand(command):
    command = command.lower().strip()

    if not command:
        return

    if open_website(command):
        return

    if open_app(command):
        return

    if open_folder(command):
        return

    if command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            speak(f"Playing {song}")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(song)}"
            )
        else:
            speak("Say song name")

    elif command.startswith("search youtube"):
        query = command.replace("search youtube", "", 1).strip()

        if query:
            speak(f"Searching YouTube for {query}")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )
        else:
            speak("Say what you want to search on YouTube")

    elif "news" in command:
        speak("Opening today's news")
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    elif command in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif command in ["date", "today date", "what is the date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "joke" in command:
        get_joke()

    elif command.startswith("tell me about"):
        topic = command.replace("tell me about", "", 1).strip()

        if topic:
            speak(f"Searching about {topic}")
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(topic)}")
        else:
            speak("Say the topic name")

    else:
        speak("Searching Google")
        query = quote_plus(command)
        webbrowser.open(f"https://www.google.com/search?q={query}")


# ========== MAIN ==========
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        command = input("Type command for Jarvis: ").strip()

        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye")
            break

        processCommand(command)
