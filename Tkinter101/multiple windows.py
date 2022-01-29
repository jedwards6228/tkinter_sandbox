from tkinter import *

root = Tk()
root.title('Main Window')
root.geometry('400x400')


def open_window():
    top = Toplevel()
    top.title('Second Window')
    top.geometry('200x200')
    my_label = Label(top, text="wowowowow another window")
    my_label.pack()
    second_button = Button(top, text="Close", command=top.destroy)
    second_button.pack()


my_button = Button(root, text="Open Second Window", command=open_window)
my_button.pack()

if __name__ == '__main__':
    mainloop()
