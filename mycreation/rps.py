
#Rock Paper Scissor
import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 0

print("🎮 Rock-Paper-Scissors Game")
print("Type 'exit' anytime to quit.")

while True:
    user = input("\nChoose (rock/paper/scissors): ").lower()
    if user == "exit":
        break
    if user not in options:
        print("❌ Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"🧠 Computer chose: {computer}")

    # Determine winner
    if user == computer:
        print("⚖️ It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    rounds += 1
    print(f"🏆 Score -> You: {user_score} | Computer: {computer_score}")

print("\n🎉 Game Over!")
print(f"Rounds Played: {rounds}")
if user_score > computer_score:
    print("🥳 You won the game!")
elif computer_score > user_score:
    print("😞 Computer won the game!")
else:
    print("🤝 It's a tie!")
