from functions.os_ops import (
    open_calculator,
    open_camera,
    open_command_prompt,
    open_notepad,
    reminder,
    take_screenshot,
)
from functions.online_ops import (
    get_latest_news,
    get_random_advice,
    get_random_joke,
    get_weather_report,
    search_on_google,
    play_on_youtube,
    search_wikipedia,
    send_whatsapp_message,
    find_my_ip,
    dictionary,
)
from jarvis import greet, speak, take_user_input
import requests
from pprint import pprint
from datetime import datetime
import os, webbrowser, sys
import pywhatkit as kit

if __name__ == "__main__":
    greet()
    while True:
        query = take_user_input().lower()

        if "open notepad" in query:
            open_notepad()

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad++.exe")

        elif "open command prompt" in query or "open cmd" in query:
            open_command_prompt()

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            open_camera()

        elif "close camera" in query:
            os.system("taskkill /f /im camera.exe")

        elif "open calculator" in query:
            open_calculator()

        elif "close calculator" in query:
            os.system("taskkill /f /im calculator.exe")

        elif "ip address" in query:
            ip_address = find_my_ip()
            speak(
                f"Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir."
            )
            print(f"Your IP Address is {ip_address}")

        elif "wikipedia" in query:
            speak("What do you want to search on Wikipedia, sir?")
            search_query = take_user_input().lower()
            results = search_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif "youtube" in query:
            speak("What do you want to play on Youtube, sir?")
            video = take_user_input().lower()
            play_on_youtube(video)

        elif "search on google" in query:
            speak("What do you want to search on Google, sir?")
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak(
                "On what number should I send the message sir? Please enter in the console: "
            )
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        # elif "send an email" in query:
        #     speak("On what email address do I send sir? Please enter in the console: ")
        #     receiver_address = input("Enter email address: ")
        #     speak("What should be the subject sir?")
        #     subject = take_user_input().capitalize()
        #     speak("What is the message sir?")
        #     message = take_user_input().capitalize()
        #     if send_email(receiver_address, subject, message):
        #         speak("I've sent the email sir.")
        #     else:
        #         speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "joke" in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "news" in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep="\n")

        elif "weather" in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(
                f"The current temperature is {temperature}, but it feels like {feels_like}"
            )
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(
                f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}"
            )

        elif "what time" in query or "what's the time" in query:
            speak(f"It's {datetime.now().strftime('%I:%M %p')}")

        elif (
            "what day" in query
            or "what's the date today" in query
            or "what's today's date" in query
        ):
            speak(f"Today is {datetime.now().strftime('%A, %B %d, %Y')}")

        elif "define" in query or "what's the meaning of" in query:
            meaning = dictionary(query)
            speak(f"It means {meaning}")

        elif "make a reminder" in query or "set a reminder" in query:
            speak("Sir, what should be the title of the reminder")
            title = take_user_input()
            speak("What is the body of the reminder?")
            message = take_user_input()
            speak("What hour should be the reminder sir")
            hour = int(take_user_input())
            speak("What minute should the reminder be sir")
            minute = int(take_user_input())
            reminder(title, message, hour, minute)

        elif "play music" in query or "open music" in query:
            music_dir = "C:\\Users\\HP\\Downloads\\yt playlist"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp4"):
                    os.startfile(os.path.join(music_dir, song))

        elif "open youtube" in query or "start youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open facebook" in query or "start facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "open stackoverflow" in query or "start stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif "open google" in query or "search google" in query:
            speak("What do you want to search on Google, sir?")
            search_query = take_user_input().lower()
            webbrowser.open(f"{search_query}")

        elif "play song on youtube" in query:
            speak("What do you want to listen to, sir?")
            song = take_user_input().lower()
            kit.playonyt(f"{song}")

        elif "no thanks" in query:
            sys.exit()

        elif "shutdown the computer" in query:
            os.system("shutdown /s /t 5")

        elif "restart the computer" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "where am i" in query or "where are we" in query:
            try:
                ip = find_my_ip()
                geo_request = requests.get(f"https://get.geojs.io/v1/ip/geo/{ip}.json")
                geo_data = geo_request.json()
                city = geo_data["city"]
                country = geo_data["country"]
                speak(f"Sir we are in {city} and {country}")
            except Exception as e:
                print(e)
                speak("Due to network error, I cannot find the location")

        elif "take screeenshot" in query or "take a screenshot" in query:
            take_screenshot()
            speak("I am done sir, I saved it to the main folder")
