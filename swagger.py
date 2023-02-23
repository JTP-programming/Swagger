import speech_recognition as sr
import pyttsx3
from datetime import date
import pywhatkit
import webbrowser

m = pyttsx3.init()

listener = sr.Recognizer()

m.say("Hello I am Swagger. What Can I do for you.")
m.runAndWait()

def play():
    with sr.Microphone() as source:
        print("listening")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        todays_date = date.today()
        if "swagger" in command:
            m.say("What do you want")
            m.runAndWait()
        elif "date" in  command:
            m.say(todays_date)
            m.runAndWait()  
        elif "play" in command:
            video = command.replace("play", "")
            m.say("playing" + video)
            pywhatkit.playonyt(video)
        elif "*" in command:
            m.say(10)
            m.runAndWait()
        elif "google" in command:
            m.say("opening google")
            m.runAndWait()
            webbrowser.open_new("https:/google.com")
while True:
    play()