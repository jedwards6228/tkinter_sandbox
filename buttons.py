from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="Look! I clicked a Button!", fg="red", bg="yellow")
    my_label.pack()


my_button = Button(root, text="Click Me!!", padx=50, pady=50, command=my_click, fg="blue", bg="green")
my_button.pack()


root.mainloop()
