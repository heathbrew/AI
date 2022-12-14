import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as wb
import os
import pyautogui
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
        print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query
if __name__=="__main__":
    #wishMe()
    while True:
        query = takeCommand().lower()
        #print(query)
        # Logic for executing tasks based on query
        if "stop" in query:
            speak("stopping now")
            break
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia:")
            print(results)
            speak(results)
        #website     
        elif "open youtube" in query:
            speak("opening youtube...")
            wb.open("https://www.youtube.com/")
        elif "open google" in query:
            speak("opening google...")
            wb.open("https://www.google.com/")        
        elif "open github" in query:
            speak("opening github...")
            wb.open("https://github.com/heathbrew?tab=repositories")
        elif "play music" in query:
            if "study" in query:
                wb.open("https://music.youtube.com/watch?v=8EeNI0cts4Y&list=PL8uQl6bqhtpP46cpIpBvFLfMV7bltP81h")
                break
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        # elif "the date" or "the day" in query:
        #     strDate = datetime.datetime.now().strftime("%D")
        #     strDay = datetime.datetime.now().strftime("%A")
        #     speak(f"Sir, the date today is {strDate}.")
        #     speak(f"and the day today is {strDay}")
        
        elif "open ai" in query:
            AIpath = "C:\\Users\\Admin\\OneDrive\\Desktop\AI"
            os.startfile(AIpath)
            simplilearn = "https://lms.simplilearn.com/program/masters/117/Artificial%20Intelligence%20Engineer/courses"
            wb.open(simplilearn)
            lmsai = "https://lms.bennett.edu.in/course/view.php?id=3801"
            wb.open(lmsai)
            wb.open("https://music.youtube.com/watch?v=ZeE0ATcbZw0&list=PL8uQl6bqhtpP46cpIpBvFLfMV7bltP81h")
            break
        elif "open coding ninja" in query:
            codingninja = "https://classroom.codingninjas.com/app/cohorts/17193"
            wb.open(codingninja)
            javacompiler = "https://www.onlinegdb.com/online_java_compiler"
            wb.open(javacompiler)
            wb.open("https://music.youtube.com/watch?v=b-I8F0aUGiw&list=PL8uQl6bqhtpP46cpIpBvFLfMV7bltP81h")
            break
        elif "login stud" in query:
            speak("you have 10 sec to select stud wifi")
            pyautogui.sleep(3)
            wb.open("http://10.40.0.1/24online/webpages/client.jsp")
            pyautogui.sleep(10)
            pyautogui.click(545,527)
            pyautogui.write("e21cseu0245")
            pyautogui.click(565,568)
            pyautogui.write("3Cd$5Ul#")
            pyautogui.press("enter")
        elif  "open lms" in query:
            lms = "https://lms.bennett.edu.in/login/index.php"
            wb.open(lms)
            pyautogui.sleep(3)
            pyautogui.moveTo(977, 698)
            pyautogui.click(977,698)
            pyautogui.write("3Cd$5Ul#")
            pyautogui.press("enter")
            break
#apps
        elif "open dragon ball" in query:
            dragonballpath = "steam://rungameid/851850"
            os.startfile(dragonballpath)
            break
        elif "open gotham knights" in query:
            dragonballpath = "steam://rungameid/1496790"
            os.startfile(dragonballpath)
            break
        elif "open pycharm " in query:
            pycharmpath = "D:\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
            os.startfile(pycharmpath)
            
