import tkinter as tk
# create main window
root = tk.Tk()
root.title("Hello Tkinter")

# button = tk.Button(root,text="click me!!")
# button.place(x=50, y=50)
# add lable widget both shown in middle
# lable = tk.Label(root, text="Welcome") 
lable1 = tk.Label(root, text="Welcome to Tkinter") 
lable2 = tk.Label(root, text="This is me Rishav Shrestha") 
# lable1.pack()
# lable2.pack()
# lable.pack()

lable1.grid(row=0,column=0)
lable2.grid(row=0,column=1,padx=5, pady=5, sticky="w")

button = tk.Button(root,text="click me!!")
button.place(x=50, y=50)
root.geometry("500x400")
root.resizable(True,True)#allow resiing both direction
root.mainloop()


# place(): place widgets at specific coordinate
# grid(): arrange widget in row and column
