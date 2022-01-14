from tkinter import *
from PIL import ImageTk,Image
import os


root = Tk()
root.title('Tkinter 101 Images app')
root.iconbitmap(os.getcwd() + '\Icons\chart_graphic_statistic_icon_208605.ico')

my_img = ImageTk.PhotoImage(Image.open(os.getcwd() + '\Images\stock_photo.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
