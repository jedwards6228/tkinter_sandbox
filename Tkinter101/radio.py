from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Radio Buttons Project")

# List with tuples that have text and values in them
modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")


for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack()


# Function that destroys the label and creates it again with a new value
def clicked(value):
    global my_label
    my_label.destroy()
    my_label = Label(root, text=value)
    my_label.pack()


my_label = Label(root, text=pizza.get())
my_label.pack()

mainloop()
