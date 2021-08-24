import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecogntion
import pyaudio
import wikipedia # pip install wikipedia
#import smtplib
import webbrowser as wb
import os

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

#def sendEmail(to, content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login("bla@gmail.com", "123")    
#    server.sendmail("bla@gmail.com", to, content)
#    server.close()



if __name__ == "__main__":
    wishme()
    while True:
        query = command().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            search = command().lower()
            wb.get(chromepath).open_new_tab(search+".com")


        elif "logout" in query:
            os.system("shutdown -1")

        elif "shut down" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "C:\Users\Thea\Music\Songs"
            songs = os.list_dir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember" in query:
            speak("What should I remember?")
            data = command()
            speak("You told me to remmember that "+data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that "+remember.read())  



#        elif  'send email' in query:
#            try:
#                speak("what should I say?")
#                content = command()
#                to = "blabla@gmail.com"
#                sendEmail(to, content)
#                speak("Email sent")
#           except Exception as e:
#                print(e)
#                speak("Sorry, something went wrong!")


        elif 'offline' in query:
            quit()





