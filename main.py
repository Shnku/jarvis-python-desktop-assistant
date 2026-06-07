import webbrowser
from datetime import datetime
from urllib.parse import quote_plus

from features.tell_joke import tell_joke
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

    if open_website(command):
        return

    if open_app(command):
        return

    if open_folder(command):
        return

    if command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            response_text = f"Playing {song}"
            speak(response_text)
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(song)}"
            )
        else:
            response_text = "Say song name"
            speak(response_text)

    elif command.startswith("search youtube"):
        query = command.replace("search youtube", "", 1).strip()

        if query:
            response_text = f"Searching YouTube for {query}"
            speak(response_text)
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )
        else:
            response_text = "Say what you want to search on YouTube"
            speak(response_text)

    elif "news" in command:
        response_text = "Opening today's news"
        speak(response_text)
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    elif command in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        response_text = f"The time is {current_time}"
        speak(response_text)

    elif command in ["date", "today date", "what is the date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        response_text = f"Today's date is {current_date}"
        speak(response_text)

    elif "joke" in command:
        response_text = tell_joke()
        speak(response_text)

    elif command.startswith("tell me about"):
        topic = command.replace("tell me about", "", 1).strip()

        if topic:
            response_text = f"Searching about {topic}"
            speak(response_text)
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(topic)}")
        else:
            response_text = "Say the topic name"
            speak(response_text)

    else:
        response_text = "Searching Google"
        speak(response_text)
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
