import os
import subprocess as sp

paths = {
    'notepad' : "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator' : "C:\Windows\System32\calc.exe",
    'command prompt' : "C:\Windows\System32\cmd.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    os.startfile(paths['calculator'])

def open_command_prompt():
    os.startfile(paths['command prompt'])