from tkinter import *


root = Tk()
root.title('Slider project')
root.geometry("400x400")


def slide():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


# Creates a vertical slider
vertical = Scale(root, from_=200, to=400)
vertical.pack()

# Creates a horizontal slider
horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL)
horizontal.pack()

my_button = Button(root, text="Click Me!", command=slide)
my_button.pack()


root.mainloop()
