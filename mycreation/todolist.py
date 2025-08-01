# def save_to_file(tasks):
#     with open("todo_list.txt", "w") as file:
#         for task in tasks:
#             file.write(task + "\n")

# def todo_list():
#     tasks = []
#     print("📝 Welcome to Your To-Do List")
#     print("Commands: add, view, remove, save, exit")

#     while True:
#         command = input("What do you want to do? ").strip().lower()

#         if command == "add":
#             task = input("Enter a task: ")
#             tasks.append(task)
#             print("✅ Task added.")

#         elif command == "view":
#             print("\nYour Tasks:")
#             for i, task in enumerate(tasks, 1):
#                 print(f"{i}. {task}")

#         elif command == "remove":
#             try:
#                 index = int(input("Enter task number to remove: ")) - 1
#                 if 0 <= index < len(tasks):
#                     removed = tasks.pop(index)
#                     print(f"🗑️ Removed: {removed}")
#                 else:
#                     print("❌ Invalid task number.")
#             except ValueError:
#                 print("❌ Enter a valid number.")

#         elif command == "save":
#             save_to_file(tasks)
#             print("💾 Tasks saved to todo_list.txt")

#         elif command == "exit":
#             print("👋 Goodbye!")
#             break

#         else:
#             print("❌ Unknown command.")

# todo_list()

import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load saved tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"text": task, "done": False})
        save_tasks()
        entry.delete(0, tk.END)
        refresh_list()
    else:
        messagebox.showwarning("Empty", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Select Task", "Select a task to delete.")

# Toggle task done/undone
def toggle_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = not tasks[selected]["done"]
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Select Task", "Select a task to mark as done.")

# Refresh listbox
def refresh_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✅" if t["done"] else "❌"
        listbox.insert(tk.END, f"{status} {t['text']}")

# Main window
root = tk.Tk()
root.title("📝 Advanced To-Do List")
root.geometry("400x500")

tasks = load_tasks()

# Entry + Buttons
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root, text="Add Task", width=15, command=add_task).pack(pady=2)
tk.Button(root, text="Mark Done/Undone", width=15, command=toggle_done).pack(pady=2)
tk.Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=2)

# Task List
listbox = tk.Listbox(root, height=20, width=45, font=("Arial", 12))
listbox.pack(pady=10)

refresh_list()
root.mainloop()
