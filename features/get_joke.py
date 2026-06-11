# from speech import speak


def get_joke():
    response_text = ""
    try:
        import pyjokes
    except ImportError:
        response_text = "Install pyjokes first by running pip install pyjokes"
        return response_text

    response_text = pyjokes.get_joke()
    return response_text
