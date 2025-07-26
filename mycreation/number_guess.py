import random

def guessing_game():
    number = random.randint(1, 20)
    attempts = 5

    print("🎲 Guess the Number (1–20)")
    print(f"You have {attempts} attempts.")

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}: Enter your guess: "))
            if guess == number:
                print("✅ Correct! You won the game.")
                break
            elif guess < number:
                print("🔺 Too low.")
            else:
                print("🔻 Too high.")
        except ValueError:
            print("❌ Please enter a number.")

    else:
        print(f"😢 Game Over! The number was {number}")

guessing_game()
