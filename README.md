# Jarvis - Python Desktop Assistant

![Jarvis Python Desktop Assistant](assets/jarvis-banner.png)

Jarvis is a terminal-based Python desktop assistant built for quick local tasks. It accepts typed commands, speaks responses using text-to-speech, opens websites, launches Windows apps, opens folders, searches YouTube, opens Google News, tells the time/date, tells programming jokes, and falls back to Google Search for unknown commands.

This version is designed to be reliable on normal desktops and laptops without requiring a microphone, speech recognition, API keys, databases, or paid cloud services.

## Features

- Open popular websites: Google, YouTube, Gmail, Instagram, WhatsApp Web, and GitHub.
- Launch Windows applications: Notepad, Calculator, Paint, and Command Prompt.
- Open common local folders: Desktop, Downloads, Documents, and Pictures.
- Search or play songs through YouTube search results.
- Open Google News top stories.
- Tell the current time and date.
- Tell random programming jokes using `pyjokes`.
- Search Google automatically for unknown commands.
- Speak responses using `pyttsx3`.
- Stop cleanly with `exit`, `quit`, or `stop`.

## Architecture

The project includes a visual architecture page:  
[View Architecture Diagram as Webpage](https://code-with-akki010.github.io/jarvis-python-desktop-assistant/design_plan/architecture.html)

## Supported Commands

| Command | Action |
| --- | --- |
| `open google` | Opens Google |
| `open youtube` | Opens YouTube |
| `open gmail` | Opens Gmail |
| `open instagram` | Opens Instagram |
| `open whatsapp` | Opens WhatsApp Web |
| `open github` | Opens GitHub |
| `open notepad` | Opens Notepad |
| `open calculator` | Opens Calculator |
| `open paint` | Opens Microsoft Paint |
| `open cmd` | Opens Command Prompt |
| `open desktop` | Opens the Desktop folder |
| `open downloads` | Opens the Downloads folder |
| `open documents` | Opens the Documents folder |
| `open pictures` | Opens the Pictures folder |
| `play believer` | Opens YouTube search results for the song |
| `search youtube python tutorial` | Searches YouTube for a topic |
| `news` | Opens Google News top stories |
| `time` | Tells the current time |
| `date` | Tells today's date |
| `joke` | Tells a random programming joke |
| `tell me about virat kohli` | Searches Google for the topic |
| `exit` (CLI only) | Stops Jarvis |
| `quit` (CLI only) | Stops Jarvis |
| `stop` (CLI only) | Stops Jarvis |

## Example Usage (CLI Only: `main.py`)

```text
Type command for Jarvis: open notepad
Jarvis: Opening notepad

Type command for Jarvis: time
Jarvis: The time is 02:30 AM

Type command for Jarvis: joke
Jarvis: [random joke from pyjokes]

Type command for Jarvis: tell me about artificial intelligence
Jarvis: Searching about artificial intelligence
```

## Tech Stack

| Technology | Purpose |
| --- | --- |
| `Python` | Main programming language |
| `pyttsx3` | Offline text-to-speech output |
| `pyjokes` | Random programming jokes |
| `webbrowser` | Opens websites, YouTube searches, Google News, and Google fallback search |
| `subprocess` | Launches Windows desktop applications |
| `os.startfile` | Opens local folders on Windows |
| `pathlib` | Builds user-folder paths |
| `datetime` | Gets current time and date |
| `urllib.parse.quote_plus` | Safely formats search queries for URLs |
| `Thread` | Speaking in Background |
| `asyncio` | Asyncronus function provider |
| `pywin32` | Brighe between python & Windows system functions(windows API) |
| `comtypes` | Python bridge(API) to work with Windows COM components |
| `flet` | Flutter like Modern GUI in Python |
| `pyinstaller` | Packages Python scripts into standalone executables |

## Notes And Limitations

- This project uses typed terminal commands, not microphone input.
- Voice recognition was removed so the assistant can work on systems without a microphone.
- Hugging Face API, NewsAPI, and screenshot features were removed or replaced for reliability.
- App-launching and folder-opening commands are Windows-focused.
- The `play` command opens YouTube search results instead of directly controlling YouTube playback.
- `pyjokes` is optional at runtime; if it is missing, Jarvis tells the user to install it.

## ***Development***

Clone this repository:

```powershell
git clone https://github.com/code-with-akki010/jarvis-python-desktop-assistant.git  

# Nevigate to project directory 
cd jarvis-python-desktop-assistant
```

In case of fork repo replace `your-username` with your GitHub username

### Project Structure

```sh
jarvis-python-desktop-assistant/
├── assets
│   └── jarvis-banner.png
├── design_plan
│   └── architecture.html   # visual structure of app
├── features                # contains helping module 
│   ├── __init__.py
│   ├── get_joke.py
│   ├── process_apps.py
│   ├── process_folder.py
│   ├── process_website.py
├── app.py                  # Main GUI app
├── main.py                 # the CLI (can work individually)
├── speech.py               # process text-to-speech
├── requirements.txt        # contains required python packages
├── README.md
└── LICENSE
```

**Prerequisites:** Python 3.x installed on your system

### Virtual Environment Setup (Best Practices)

It's recommended to use a virtual environment to manage dependencies.  

```bash
# Creating a Virtual Environment:-
python -m venv myenv                
```

Activating the Virtual Environment :-

```powershell
# Command Prompt (cmd) 
myenv\Scripts\activate

# or, PowerShell 
myenv\Scripts\Activate.ps1

# Bash/Zsh (Linux/MacOS)
source myenv/bin/activate
```

**Installing Dependencies**  
Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

### Running The Application

```bash
# Run the CLI app 
python main.py
```

Run the GUI flet app :-

```bash
python app.py
# or 
flet run app.py
```

### Run Flet app with GUI Hot Reload (Development)

```bash
# Watch for changes and auto-reload
flet run -d app.py
```

### Run in Web Mode

```bash
# Run as web app (opens in browser)
flet run -d --web app.py      
```

Now you are ready to bring your ideas to life

### Building the Application

To build the application as a standalone executable (.exe):

```bash
pyinstaller --onefile app.py
```

The executable will be created in the `dist` folder.  

example executable will be : `jarvis-python-desktop-assistant\dist\app.exe`

---

***Note:** Make sure to nevigate to your project directory & activate your virtual environment before **installing** dependencies, **running application** or **building** the application.*

## Future Improvements

- [x] Add a simple graphical user interface.
- [x] Add commands suggations list.
- [ ] Add command history.
- [ ] Add custom user-defined shortcuts.
- [ ] Add support for more Windows applications.
- [ ] Add cross-platform support for macOS and Linux.
- [ ] Add optional voice input only when a microphone is available.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Built as a Python desktop assistant project by `code-with-akki010`.

If you like this project, consider giving it a star on GitHub.
