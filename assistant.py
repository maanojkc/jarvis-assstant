import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit
import wikipedia
import subprocess

engine = pyttsx3.init()
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

def run():
    speak("Hello, I am your assistant")

    while True:
        command = take_command()

        # OPEN APPS (SMART)
        if "open" in command:
            app = command.replace("open", "").strip()
            try:
                subprocess.Popen(app)
                speak(f"Opening {app}")
            except:
                speak("Application not found")

        # BASIC APPS
        elif "chrome" in command:
            os.system("start chrome")

        elif "notepad" in command:
            os.system("notepad")

        elif "calculator" in command:
            os.system("calc")

        elif "cmd" in command:
            os.system("start cmd")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        # SEARCH DIRECT
        elif "search" in command:
            query = command.replace("search", "")
            webbrowser.open(f"https://google.com/search?q={query}")
            speak(f"Searching {query}")

        # YOUTUBE
        elif "youtube" in command:
            query = command.replace("youtube", "")
            pywhatkit.playonyt(query)

        # SYSTEM CONTROL
        elif "shutdown" in command:
            speak("Shutting down")
            os.system("shutdown /s /t 1")

        elif "restart" in command:
            speak("Restarting")
            os.system("shutdown /r /t 1")

        # EXIT
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        # AI-LIKE ANSWER
        elif command != "":
            try:
                speak("Searching for answer")
                result = wikipedia.summary(command, sentences=2)
                speak(result)
            except:
                webbrowser.open(f"https://google.com/search?q={command}")
                speak("I found this on Google")

if __name__ == "__main__":
    run()