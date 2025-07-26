def save_to_file(tasks):
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def todo_list():
    tasks = []
    print("📝 Welcome to Your To-Do List")
    print("Commands: add, view, remove, save, exit")

    while True:
        command = input("What do you want to do? ").strip().lower()

        if command == "add":
            task = input("Enter a task: ")
            tasks.append(task)
            print("✅ Task added.")

        elif command == "view":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif command == "remove":
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Enter a valid number.")

        elif command == "save":
            save_to_file(tasks)
            print("💾 Tasks saved to todo_list.txt")

        elif command == "exit":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Unknown command.")

todo_list()
