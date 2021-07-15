import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

x = datetime.datetime.now()
hour= int(x.hour)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    if hour>=0 and hour< 12:
        speak("Good Morning Sir")
    elif hour>=12 and hour< 18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour< 23:
        speak("Good Evening Sir")
    speak("I am Jarvis, smartest AI on earth. Please tell me how may I help you")

def takecommand():
    r= sr.Recognizer()
#it takes microphone input fromthe userand returns string output
    with sr.Microphone() as source:   
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia... please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "date" in query:
            date = x.strftime("%d")
            month = x.strftime("%B")
            year = x.strftime("%Y")
            speak(f"Sir, today's date is {date} {month} {year}")
            

        elif "which day" in query:
            day = x.strftime("%A")
            speak(f"Sir, today is {day}")
            

        elif "time" in query:
            Hour= x.strftime("%I")
            minute= x.strftime("%M")
            am_pm= x.strftime("%p")
            speak(f"Sir, the time is {Hour} {minute} {am_pm}")
            

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "open zimbra mail" in query:
            webbrowser.open("stud.iitp.ac.in/#1")

        elif "thank you jarvis" in query:
            speak("your most welcome, Sir")

        elif "exit" in query:
            if hour>=3 and hour< 20:
                y= "Have a good day"
            else:
                y= "Good night"
            speak(f"Thankyou Sir, I am exiting in few seconds, {y} Sir")
            sys.exit()
        elif "who are you" in query:
            speak("I am a subconscious computer programme made by the genius Aman Kumar, I am also known by the name artificial intelligence")
        elif "meet" in query:
            speak("Hi Khooshi mam, nice to meet you")
        speak("Sir, what can I do next?")



   