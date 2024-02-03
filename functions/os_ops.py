import os
import subprocess as sp
from plyer import notification
from threading import Timer
import pyautogui, random
import PyPDF2
import sys

sys.path.append("../JARVIS")
from jarvis import speak, take_user_input
from tkinter import filedialog
from tkinter import simpledialog

paths = {
    "notepad": "C:\\Program Files\\Notepad++\\notepad++.exe",
    "calculator": "C:\Windows\System32\calc.exe",
    "command prompt": "C:\Windows\System32\cmd.exe",
}


def open_camera():
    sp.run("start microsoft.windows.camera:", shell=True)


def open_notepad():
    os.startfile(paths["notepad"])


def open_calculator():
    os.startfile(paths["calculator"])


def open_command_prompt():
    os.startfile(paths["command prompt"])


def reminder(title, message, hour, minute):
    seconds = hour * 3600 + minute * 60

    def notify():
        notification.notify(
            title=f"{title}",
            message=f"{message}",
            timeout=1,
        )

    t = Timer(seconds, notify)
    t.start()


def take_screenshot():
    image = pyautogui.screenshot()
    image.save(str(random.randint(0, 10000000000)) + ".png")


def pdf_reader():
    file_path = filedialog.askopenfilename()
    book = open(file_path, "rb")
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speak(f"Sir there are {pages} pages. Do you want me to read the whole thing")
    user_response = take_user_input().lower()
    if "yes" in user_response:
        for page_number in range(1, pages + 1):
            page = pdfReader.pages[page_number]
            text = page.extract_text()
            speak(text)
    else:
        page_number = simpledialog.askinteger("Page", "Enter page number")
        page = pdfReader.pages[page_number]
        text = page.extract_text()
        speak(text)
