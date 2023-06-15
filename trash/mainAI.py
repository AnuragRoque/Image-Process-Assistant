import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    speak("Hello Sir Welcome to Image processing Project")

def intro():
    speak("Opening interface")


def takecommand():
    r = sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        #r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio) #Using p for voice recognition.h
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__" :

    greetme()
    intro()
    print("Project-Image Processing")

    while True:
        query = takecommand().lower()
        if 'jarvis you there' in query:
            speak("yes sir")
        elif 'hey jarvis' in query:
            speak("for you sir always")
        elif 'nice' in query:
            speak("My pleasure")
