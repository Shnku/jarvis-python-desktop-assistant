import webbrowser
from datetime import datetime
from threading import Thread
from urllib.parse import quote_plus

from features.get_joke import get_joke
from features.process_apps import open_app
from features.process_folder import open_folder
from features.process_website import open_website
from speech import speak


# ========== COMMAND ==========
def processCommand(command):
    command = command.lower().strip()
    response_text = ""

    if not command:
        return

    if response_text := open_website(command):
        return response_text

    if response_text := open_app(command):
        return response_text

    if response_text := open_folder(command):
        return response_text

    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            response_text = f"Playing {song}"
            Thread(target=speak, args=[response_text], daemon=True).start()
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(song)}"
            )
        else:
            response_text = "Say song name"
            Thread(target=speak, args=[response_text], daemon=True).start()

    elif command.startswith("search youtube"):
        query = command.replace("search youtube", "", 1).strip()

        if query:
            response_text = f"Searching YouTube for {query}"
            Thread(target=speak, args=[response_text], daemon=True).start()
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )
        else:
            response_text = "Say what you want to search on YouTube"
            Thread(target=speak, args=[response_text], daemon=True).start()

    elif "news" in command:
        response_text = "Opening today's news"
        Thread(target=speak, args=[response_text], daemon=True).start()
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    elif command in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        response_text = f"The time is {current_time}"
        Thread(target=speak, args=[response_text], daemon=True).start()

    elif command in ["date", "today date", "what is the date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        response_text = f"Today's date is {current_date}"
        Thread(target=speak, args=[response_text], daemon=True).start()

    elif "joke" in command:
        response_text = get_joke()
        Thread(target=speak, args=[response_text], daemon=True).start()

    elif command.startswith("tell me about"):
        topic = command.replace("tell me about", "", 1).strip()

        if topic:
            response_text = f"Searching about {topic}"
            Thread(target=speak, args=[response_text], daemon=True).start()
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(topic)}")
        else:
            response_text = "Say the topic name"
            Thread(target=speak, args=[response_text], daemon=True).start()

    else:
        response_text = "Searching Google"
        Thread(target=speak, args=[response_text], daemon=True).start()
        query = quote_plus(command)
        webbrowser.open(f"https://www.google.com/search?q={query}")

    return response_text


# ========== MAIN ==========
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        command = input("Type command for Jarvis: ").strip()

        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye")
            break

        processCommand(command)
