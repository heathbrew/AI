import pyttsx3
import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[1].id)




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


if __name__=="__main__":
    wishMe()
    speak("Ayushman is good")