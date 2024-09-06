import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else :
        speak("Good Evening!")  

    speak("Hello! Sir, I am 47. Please tell me how may I help you")       

def takeCommand():
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results =wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")   

        elif 'open lab' in query:
            webbrowser.open("https://dld.srmist.edu.in/srmktretelab2021/#/")
            
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com")
            
        elif 'open AWS' in query:
            webbrowser.open("https://aws.amazon.com/console/")
            
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")    
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}") 
                
        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com//results?search_query={query}")    
            
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5") 
             
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")    
            
        
