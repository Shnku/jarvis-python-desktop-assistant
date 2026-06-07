from speech import speak


def tell_joke():
    try:
        import pyjokes
    except ImportError:
        speak("Install pyjokes first by running pip install pyjokes")
        return

    return pyjokes.get_joke()
