import pyttsx3
import datetime
import speech_recognition as sr
#import pyaudio
import wikipedia
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning sir")
    elif hour>= 12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("I am Jarvis, How may i help you sir ?")
def takeCommand():
    """
    It take microphone input from the user and return a
    string output
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        #print("User said: {query}\n")
        print("User said: {}\n".format(query))
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)
        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia:")
            print(results)
            speak(results)
        if "stop" in query:
            query = query.replace("stop")
            break
    
