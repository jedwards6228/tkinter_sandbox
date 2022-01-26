from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Open Files')


def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/Jordan/Pictures", title="Select a File",
                                               filetypes=(("png files", "*.png"),
                                                          ("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()


my_image = None
my_button = Button(root, text="Select an Image to Display", command=open_file)
my_button.pack()


root.mainloop()
