from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Project")


def popup():
    response = messagebox.askyesno("This is a popup", "Hello, world!")
    if response:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


Button(root, text="popup", command=popup).pack()

mainloop()
