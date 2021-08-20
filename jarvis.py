import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecogntion
import pyaudio

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning, Thea")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, Thea")
    elif hour >= 18 and hour < 24:
        speak("Good evening, Thea")
    else:
        speak("Good night, Thea") 
    speak("The current time is")
    time()
    speak("Today is")
    date()
    speak("jarvis at your service. How can I help you?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say again it, please")

        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = command().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'offline' in query:
            quit()    





