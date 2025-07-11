import tkinter as tk
from tkinter import messagebox, filedialog

def submit_form():
    name = entry_name.get()
    gender = gender_var.get()
    country = country_var.get()
    agree = agree_var.get()
    
    if not name:
        messagebox.showerror("input Error", "name is required")
        return
    
    info = f"Name:{name}\n Gender:{gender}\nCountry:{country}\nAgreed:{agree}"
    messagebox.showinfo("Form submitted", info)
    
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Selected File", f'You selected:\n{file_path}')
        
root = tk.Tk()
root.title("Tkinter GUI example")
root.geometry("400x350")

tk.Label(root,text="Name:").grid(row=0,column=0,padx=5,pady=5,sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0,column=1,padx=5,pady=5)

# radiobutton
tk.Label(root,text="Gender:").grid(row=1,column=0,padx=5,pady=5,sticky="w")
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1,column=1,sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1,column=1,sticky="e")

# dropdown
tk.Label(root,text="Country:").grid(row=2,column=0,padx=5,pady=5,sticky="w")
country_var = tk.StringVar(value="Select a Country")
country_menu = tk.OptionMenu(root, country_var, "Korea", "USA", "UK", "Japan" , "Thailand")
country_menu.grid(row=2,column=1,padx=5,pady=5)

# checkbox
agree_var = tk.IntVar()
tk.Checkbutton(root, text="I Agree to term", variable=agree_var).grid(row=3,column=1,pady=5,sticky="w")

# button
tk.Button(root, text="Submit", command=submit_form).grid(row=4,column=0,padx=5, pady=10)
tk.Button(root, text="Open File", command=open_file).grid(row=4,column=1,pady=10)

# run the application
root.mainloop()

# assignment
# 400*400 ko form , title calculator, 
#  first no: 
#  seconnd no:
# button +-*/
# result button