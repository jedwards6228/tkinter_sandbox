from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frame project")

my_frame = LabelFrame(root, text="Options", padx=50, pady=50)
my_frame.pack(padx=50, pady=50)

my_button1 = Button(my_frame, text="Add Topic")
my_button1.grid(row=0, column=0, sticky=W+E)

my_button2 = Button(my_frame, text="Remove Topic")
my_button2.grid(row=1, column=0, sticky=W+E)

my_button3 = Button(my_frame, text="Save")
my_button3.grid(row=2, column=0, sticky=W+E)

root.mainloop()
