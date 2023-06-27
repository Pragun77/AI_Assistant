import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    print("Recognizing...")
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Unable to recognize speech")
except sr.RequestError as e:
    print("Error:", e)