import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Hi! I am your assistant.")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("🎤 Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print("You said:", command)
        engine.say("You said " + command)
        engine.runAndWait()
except:
    print("❌ Error in recognition.")
