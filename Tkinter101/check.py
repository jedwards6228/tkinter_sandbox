from tkinter import *


root = Tk()
root.title('Checkbox Project')
root.geometry('400x400')


def update_status():
    global my_label
    my_label.destroy()
    my_label = Label(root, text=var.get())
    my_label.pack()


var = StringVar()

check_box = Checkbutton(root, text="Check Me OUT!", variable=var, command=update_status, onvalue="On", offvalue="Off")
check_box.deselect()
check_box.pack()

my_label = Label(root, text=var.get())
my_label.pack()


root.mainloop()
