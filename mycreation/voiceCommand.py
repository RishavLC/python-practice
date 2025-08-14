import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for voice input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak your calculation:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣 You said: {text}")
        return text
    except:
        print("❌ Could not understand. Try again.")
        return None

# Main calculator logic
def calculate():
    expression = listen()
    if expression:
        try:
            result = eval(expression)
            print(f"✅ Result: {result}")
            speak(f"The answer is {result}")
        except:
            print("❌ Error in calculation.")
            speak("There was an error in calculation.")

if __name__ == "__main__":
    while True:
        calculate()
        again = input("Do you want to calculate again? (y/n): ")
        if again.lower() != 'y':
            break
