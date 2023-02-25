import speech_recognition as sr
import pyttsx3
from datetime import date
import pywhatkit
import webbrowser

m = pyttsx3.init()

listener = sr.Recognizer()

m.say("Master Jamal what may I do for you today?")
m.runAndWait()


def play():
    with sr.Microphone() as source:
        print("listening")
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
        except:
            print("Cannot recognize!!!")
            return False
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
            m.say("Creating new repo")
            m.runAndWait()
            webbrowser.open_new("https://github.com/new")
        elif "search for" in command:
            s = command.replace("search for", "")
            m.say("searching for" + s)
            m.runAndWait()
            pywhatkit.search(s)
        elif "go offline" in command:
            m.say("Going Offline")
            m.runAndWait()
            return "offline"
        else:
            print("Didnt get that!")
while True:
    keep_playing = play()
    if not keep_playing:
        continue
    if keep_playing == "offline":
        break