import random, time, os

dice_faces = {
    1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
}

while True:
    input("\n🎲 Press Enter to roll the dice...")
    print("Rolling", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    rolled = random.randint(1, 6)
    print("\nYou rolled:", dice_faces[rolled])

    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break
