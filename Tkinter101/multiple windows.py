from tkinter import *

root = Tk()
root.title('Main Window')


def open_window():
    top = Toplevel()
    top.title('Second Window')
    my_label = Label(top, text="wowowowow another window")
    my_label.pack()
    second_button = Button(top, text="Close", command=top.destroy)
    second_button.pack()


my_button = Button(root, text="Open Second Window", command=open_window)
my_button.pack()


mainloop()
