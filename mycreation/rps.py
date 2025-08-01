
# #Rock Paper Scissor
# import random

# options = ["rock", "paper", "scissors"]
# user_score = 0
# computer_score = 0
# rounds = 0

# print("🎮 Rock-Paper-Scissors Game")
# print("Type 'exit' anytime to quit.")

# while True:
#     user = input("\nChoose (rock/paper/scissors): ").lower()
#     if user == "exit":
#         break
#     if user not in options:
#         print("❌ Invalid choice. Try again.")
#         continue

#     computer = random.choice(options)
#     print(f"🧠 Computer chose: {computer}")

#     # Determine winner
#     if user == computer:
#         print("⚖️ It's a tie!")
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         print("✅ You win this round!")
#         user_score += 1
#     else:
#         print("❌ Computer wins this round!")
#         computer_score += 1

#     rounds += 1
#     print(f"🏆 Score -> You: {user_score} | Computer: {computer_score}")

# print("\n🎉 Game Over!")
# print(f"Rounds Played: {rounds}")
# if user_score > computer_score:
#     print("🥳 You won the game!")
# elif computer_score > user_score:
#     print("😞 Computer won the game!")
# else:
#     print("🤝 It's a tie!")


import tkinter as tk
import random

# Setup main window
root = tk.Tk()
root.title("🎮 Rock-Paper-Scissors")
root.geometry("400x500")
root.resizable(False, False)

user_score = 0
comp_score = 0
history = []

choices = ["Rock", "Paper", "Scissors"]

# Logic function
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "Draw!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    history.append(f"You: {user_choice} | Computer: {comp_choice} → {result}")
    update_ui(user_choice, comp_choice, result)

def update_ui(user, comp, result):
    lbl_user.config(text=f"Your Choice: {user}")
    lbl_comp.config(text=f"Computer: {comp}")
    lbl_result.config(text=f"Result: {result}")
    lbl_score.config(text=f"Score → You: {user_score} | Computer: {comp_score}")
    txt_history.delete(0, tk.END)
    for item in history[-10:]:  # Show last 10 rounds
        txt_history.insert(tk.END, item)

def reset_game():
    global user_score, comp_score, history
    user_score = 0
    comp_score = 0
    history = []
    lbl_user.config(text="Your Choice: ")
    lbl_comp.config(text="Computer: ")
    lbl_result.config(text="Result: ")
    lbl_score.config(text="Score → You: 0 | Computer: 0")
    txt_history.delete(0, tk.END)

# GUI layout
frame = tk.Frame(root)
frame.pack(pady=20)

lbl_title = tk.Label(frame, text="Rock - Paper - Scissors", font=("Arial", 18, "bold"))
lbl_title.pack()

lbl_user = tk.Label(frame, text="Your Choice: ", font=("Arial", 12))
lbl_user.pack()

lbl_comp = tk.Label(frame, text="Computer: ", font=("Arial", 12))
lbl_comp.pack()

lbl_result = tk.Label(frame, text="Result: ", font=("Arial", 14, "bold"))
lbl_result.pack(pady=10)

lbl_score = tk.Label(frame, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
lbl_score.pack(pady=5)

# Buttons
btns_frame = tk.Frame(root)
btns_frame.pack(pady=10)

tk.Button(btns_frame, text="🪨 Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btns_frame, text="📄 Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btns_frame, text="✂️ Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

tk.Button(root, text="🔄 Reset Game", command=reset_game).pack(pady=10)

# History display
tk.Label(root, text="Match History (Last 10)", font=("Arial", 12)).pack()
txt_history = tk.Listbox(root, height=10, width=45)
txt_history.pack(pady=5)

# Run app
root.mainloop()
