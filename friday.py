import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newvoicerate = 200
engine.setProperty('rate', newvoicerate)
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I hours: %M minutes :%S seconds ")
    speak("the current time is ")
    speak(Time)
    
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir")
    hour =  datetime.datetime.now().hour
    
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    elif hour >= 17 and hour < 24:
        speak("Good Evening")
    
    speak("Friday at Your service. How Can I help? ")
    
    
def takecommand():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =  r.listen(source)
    
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio)
        print(query)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        speak("Say That again please....")
    except sr.RequestError as e:
        print("Error:", e)
        speak("Say That again please....")
        
        return "None"
    return query

def sende_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com', '25626717')
    server.sendmail('test@gmail.com', to , content)

if __name__ == "__main__":
    wishme()
    
    while True:
        query2 = takecommand().lower()
        print(query2)
        
        if "time" in query2:
            time()
        elif "date" in query2:
            date()
        elif "offline" in query2:
            quit()    
        elif "wikipedia" in query2:
            speak("Searching...")
            query2 = query2.replace("wikipedia", "")
            result = wikipedia.summary(query2, sentences = 2)
            speak(result)
        elif "send email" in query2:
            try:
                speak("What should I say")
                content = takecommand()
                to = 'test_2@gmail.com'
                sende_mail(to, content)
                speak("The mail was sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send this mail")
        elif "search in chrome" in query2:
            speak("What should I search")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            # wb.register('chrome', None,wb.BackgroundBrowser(chromepath),1)
            search = takecommand()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query2:
            os.system("shutdown - 1")
        elif "shutdown" in query2:
            os.system("shutdown /s /t 1")
        elif "restart" in query2:
            os.system("shutdown  /r /t 1")