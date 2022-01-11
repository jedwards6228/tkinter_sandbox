from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="white", bg="gray")
e.pack()
e.insert(0, "Enter Your Name: ")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="Enter Your Name", padx=50, pady=50, command=my_click, fg="blue", bg="green")
my_button.pack()

root.mainloop()
