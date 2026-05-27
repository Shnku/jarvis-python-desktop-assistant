import pyttsx3
import time

engine = pyttsx3.init("espeak")
engine.setProperty("rate", 130)
engine.setProperty("volume", 200)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Initializing Jarvis")
time.sleep(1)
speak("I am your desktop assistant. How can I help you?")
speak("You can ask me to open apps, folders, websites, tell jokes, and much more.")
speak("Just type your command and I will do my best to assist you.")
speak(
    "For example, you can say 'open notepad', 'open desktop', 'open google', 'play some music', 'search youtube for cat videos', 'what is the time', 'tell me a joke', etc."
)
speak("I am always here to help you. Just let me know what you need.")
speak("I hope you have a great day with Jarvis!")
speak("Let's get started. What can I do for you?")
