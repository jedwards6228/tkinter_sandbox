from tkinter import *

root = Tk()

# Creating a Label Widget
my_label1 = Label(root, text="Hello, World!")
my_label2 = Label(root, text="My Name Is Slim Shady")


my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1)


root.mainloop()
