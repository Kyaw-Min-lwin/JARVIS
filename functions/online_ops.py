import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import imaplib
import email
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk

PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
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


# def read_email():
#     ORG_EMAIL = "@gmail.com"
#     my_email = "kyawminlwinprogrammer" + ORG_EMAIL
#     password = "vxvf mqsy jttm olgu"

#     imap_server = "imap.gmail.com"
#     SMTP_PORT = 993
#     print("hi")
#     try:
#         mail = imaplib.IMAP4_SSL(imap_server, SMTP_PORT)
#         mail.login(my_email, password)
#         mail.select("inbox")
#         data = mail.search(None, "ALL")
#         mail_ids = data[1]
#         id_list = mail_ids[0].split()
#         first_email_id = int(id_list[0])
#         latest_email_id = int(id_list[-1])
#         for i in range(latest_email_id, first_email_id, -1):
#             data = mail.fetch(str(i), "(RFC822)")
#             for response_part in data:
#                 arr = response_part[0]
#                 if isinstance(arr, tuple):
#                     msg = email.message_from_string(str(arr[1], "utf-8"))
#                     email_subject = msg["subject"]
#                     email_from = msg["from"]
#                     print("From : " + email_from + "\n")
#                     print("Subject : " + email_subject + "\n")

#     except Exception as e:
#         traceback.print_exc()


def download_anime(anime=None):
    if not anime:
        anime = simpledialog.askstring("Anime", "Enter Anime Name")
        print(anime)
    driver.get("https://animension.to/")
    input_element = driver.find_element(By.CSS_SELECTOR, "#s")
    input_element.send_keys(f"{anime}")
    input_element.send_keys(Keys.RETURN)

    # waiting for the anime to appear and then downloading it
    try:
        type_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#searchForm > div.searchOrganizer > div:nth-child(4) > button",
                )
            )
        )
        type_button.click()

        # selecting subbed in radion buttons
        subbed_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#searchForm > div.searchOrganizer > div.filter.dropdown.open > ul > li:nth-child(2) > label",
                )
            )
        )
        subbed_button.click()

        # searching again with subbed anime only
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#searchForm > div.filter.submit.searchButton > button",
                )
            )
        )
        search.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#listupd > div.excstf > div:nth-child(1) > div > a")
            )
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#anime_episodes > ul.episodes-sv-1> li > div.sli-name > a",
                )
            )
        )
        element.click()

        vidcn_download = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#internal-source-selector-modal > a:last-child")
            )
        )

        vidcn_download.click()
        link = vidcn_download.get_attribute("href")
        driver.get(link)
        download_button = driver.find_element(By.CSS_SELECTOR, "#download")
        download_button.click()

    except Exception as e:
        print(e)
        driver.quit()

    time.sleep(1000)
