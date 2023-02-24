import speech_recognition as sr
import pyttsx3
from datetime import date
import pywhatkit
import webbrowser
import os
import pyjokes
import subprocess


m = pyttsx3.init()

listener = sr.Recognizer()

m.say("Master Jamal what may I do for you today?")
m.runAndWait()


def play():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            todays_date = date.today()
            if "swagger" in command:
                m.say("Yes?")
                m.runAndWait()
            elif "date" in  command:
                m.say(todays_date)
                m.runAndWait()  
            elif "play" in command:
                video = command.replace("play", "")
                m.say("playing" + video)
                pywhatkit.playonyt(video)
            elif "google" in command:
                m.say("opening google")
                m.runAndWait()
                webbrowser.open_new("https:/google.com")
            elif "i want to code" in command:
                webbrowser.open_new("https://github.com/new")
            elif "search for the" in command:
                s = command.replace("search for the", "")
                m.say("searching for" + s)
                m.runAndWait()
                pywhatkit.search(s)
            else:
                print("Didnt get that!")
                play()
    except Exception:
        play()
while True:
    play()