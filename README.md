# JARVIS - Personal Voice Assistant

JARVIS is a Python-based personal assistant designed to automate tasks, retrieve information from the web, and control system operations via voice commands. It integrates various APIs and libraries to perform functions ranging from checking the weather to downloading anime.

## 🚀 Features

JARVIS is equipped with a wide range of functionalities categorized below:

### 🌐 Online Operations
* **Web Search**: Performs Google searches and retrieves Wikipedia summaries.
* **Media**: Plays videos on YouTube and can play music from a local directory.
* **Information**:
    * Retrieves the latest news headlines using NewsAPI.
    * Provides real-time weather reports (temperature and "feels like").
    * Fetches random advice and jokes.
    * Looks up word definitions via DictionaryAPI.
* **Communication**: Sends WhatsApp messages instantly using `pywhatkit`.
* **Anime Downloader**: Automated script using Selenium to search and download anime from "Animension".
* **Location**: Detects current IP address, city, and country.

### 💻 System Operations
* **Application Control**: Opens and closes local applications including Notepad, Command Prompt, Calculator, and Camera.
* **Power Management**: Capable of shutting down, restarting, or putting the system to sleep.
* **Utilities**:
    * **PDF Reader**: Reads PDF files aloud (entire book or specific pages).
    * **Screenshot**: Takes screenshots and saves them with a random filename.
    * **Reminders**: Sets desktop notification reminders.
    * **Date & Time**: verbalizes the current time and date.

## 🛠️ Prerequisites

Ensure you have Python installed. You will need to install the following dependencies found in the project files:

```text
requests
wikipedia
pywhatkit
python-decouple
selenium
plyer
pyautogui
PyPDF2
psutil
```
* **Note: You will also need the jarvis module (referenced in imports) containing greet, speak, and take_user_input functions.**
