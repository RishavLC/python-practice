import datetime

# File to store mood logs
mood_file = "mood_log.txt"

# Mood options
moods = {
    "1": "😊 Happy",
    "2": "😐 Neutral",
    "3": "😢 Sad",
    "4": "😡 Angry",
    "5": "🤯 Stressed",
    "6": "😴 Tired",
    "7": "❤️ Grateful"
}

def show_mood_menu():
    print("\n📅 Mood Logger")
    print("How are you feeling today?")
    for key, value in moods.items():
        print(f"{key}. {value}")
    print("0. View Mood History")
    print("Q. Quit")

def log_mood(choice):
    now = datetime.datetime.now()
    mood = moods.get(choice)
    with open(mood_file, "a") as file:
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {mood}\n")
    print(f"✅ Mood logged: {mood}")

def show_history():
    print("\n📜 Mood History:")
    try:
        with open(mood_file, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No mood history found.")

# Main loop
while True:
    show_mood_menu()
    user_input = input("Enter your choice: ").strip()

    if user_input.lower() == "q":
        print("👋 Goodbye! Take care.")
        break
    elif user_input == "0":
        show_history()
    elif user_input in moods:
        log_mood(user_input)
    else:
        print("❌ Invalid choice. Try again.")
