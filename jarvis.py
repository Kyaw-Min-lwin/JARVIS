# Installed libraries:# pyttsx3 is a text to speech library
# speechrecognition is to convert audio into text for further processing.
# wikipedia is a online encyclopedia
# requests is a HTTP library for making API requests
# pywhatkit library for whatsapp, google searches, youtube videos, send emails with attachment

# Functionalities
# Speech recognition
# Text to speech
# Wikipedia search - done
# Weather report - done
# News report- done
# Time report
# Calculator- done
# Dictionary
# Email
# Alarm
# Reminder
# play music
# open youtube- done, whatsapp- done, google- done, facebook, instagram, twitter, snapchat, linkedin, open google maps
# open google search - done
# general knowledge 
# jokes- done
# ability to have conversations with Jarvis

# imports
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# initializing pyttsx3 using sapi5 that is a Microsoft Speech API that helps us use the voices
engine = pyttsx3.init('sapi5')

# setting speech rate
engine.setProperty('rate', 170)

# setting volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
#first voice is male, 2nd female
engine.setProperty('voice', voices[1].id)

#speak function
def speak(text):
    engine.say(text)
    ''' runAndWait() is used to ensure that the program waits until the text queued by say() has been fully
        spoken before proceeding with further code execution.'''
    engine.runAndWait()

# greeting the user based on the current time
def greet():
    # getting the current hour
    hour = datetime.now().hour
    if hour > 6 and hour < 12:
        speak('Good morning sir!')
    elif hour > 12 and hour < 17:
        speak('Good afternoon sir!')
    else:
        speak('Good evening sir!')
    speak(f'I am {BOTNAME}. How may I assist you?')

# taking user speech input and converting it into text
def take_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        print('Listening...')
        # setting how much pause the recognizer should wait before a sentence ends
        recognizer.pause_threshold = 1
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        print("Recognizing...")

    try:
        # Use the recognizer to convert audio to text
        text = recognizer.recognize_google(audio)
        if not 'exit' in text or 'stop' in text:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return '' 
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return ''

    
# greet()
# take_user_input()