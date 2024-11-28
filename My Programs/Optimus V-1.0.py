import speech_recognition as sr
import os
import win32com.client
import pyttsx3
import webbrowser
import datetime
import subprocess
import pyaudio


def say(text):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return text


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning Sir, I am Optimus")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon Sir, I am Optimus")
    else:
        say("Good Evening Sir, I am Optimus")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        r.energy_threshold = 100
        audio = r.listen(source)
        try:
            # print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
    # query = str(input("Enter the command: "))
    # return query


if __name__ == '__main__':
    wish()
    say("I have an Artificial Intelligence")
    while True:
        print("Listening...")
        query = takeCommand()
        print("Recognizing...")
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                 ["wikipedia", "https://www.wikipedia.com"], ]

        if 'open youtube' in query.lower():
            say("Opening youtube, Sir")
            webbrowser.open("https://www.youtube.com")

        if 'open google' in query.lower():
            say("Opening google, Sir")
            webbrowser.open("https://www.google.com")

        if 'open wikipedia' in query.lower():
            say("Opening wikipedia, Sir")
            webbrowser.open("https://www.wikipedia.com")

        if 'what is the time now' in query.lower():
            hor = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            print(datetime.datetime.now().strftime("%H:%M"))
            say(f"The time is {hor} hours and {min} minutes")

        if 'what is the date' in query.lower():
            date = datetime.date.today()
            print(date)
            say(f"Today's Date is {date}")

        if 'open chatgpt' in query.lower():
            say("Opening CharGPT, sir")
            webbrowser.open("https://chat.openai.com")

        if 'open folder' in query.lower():
            say("which folder do you have to open")
            folder = input("which folder do you have to open: ")

            if 'lukhi' in folder.lower():
                os.startfile("C:\\Users\\LUKHI")
                say("opening folder, sir")

            if 'pycharm projects' in folder.lower() or 'pycharm project' in folder.lower():
                os.startfile("C:\\Users\\LUKHI\\PycharmProjects")
                say("opening folder, sir")



        if 'open pycharm' in query.lower():
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
            if os.path.exists(path):
                say("opening PyCharm, sir")
                subprocess.Popen(path)

        if 'open chrome' in query.lower():
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            say("Opening Chrome, Sir")
            subprocess.Popen(path)

