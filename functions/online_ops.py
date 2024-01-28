import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def search_wikipedia(query):
    wikipedia.summary(query, sentences=3)


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+95{number}", message)


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general"
    ).json()
    articles = res["articles"]
    print(articles[:5])
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric"
    ).json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res["slip"]["advice"]


def get_random_joke():
    headers = {"Accept": "application/json"}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def find_my_ip():
    ip_address = requests.get("https://api64.ipify.org?format=json").json()
    return ip_address["ip"]


def dictionary(query):
    query = query.split(" ")
    word = query[-1]
    definition = requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    ).json()[0]["meanings"][0]["definitions"][0]["definition"]
    return definition
