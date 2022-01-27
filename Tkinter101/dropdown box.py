from tkinter import *


root = Tk()
root.title('Dropdown Project')
root.geometry('400x400')


def show():
    global my_label
    my_label.destroy()
    my_label = Label(root, text=clicked.get())
    my_label.pack()


# Dropdown Boxes

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text="Show Selection", command=show)
my_button.pack()

my_label = Label(root, text=clicked.get())
my_label.pack()


if __name__ == '__main__':
    root.mainloop()
