from tkinter import *
from PIL import ImageTk,Image
import os


root = Tk()
root.title('Tkinter 101 Image Viewer app')
root.iconbitmap(os.getcwd() + '\Icons\chart_graphic_statistic_icon_208605.ico')

# Setting min/max window size
root.minsize(300, 300)
root.maxsize(1900, 1300)


# Function for changing to next or previous picture
def picture_changer(command):
    global image_index

    my_label.grid_forget()
    if command == 'next':
        image_index += 1
    if command == 'previous':
        image_index -= 1
    display_picture()
    button_state_changer()
    return


# Function to display the selected image
def display_picture():
    global image_index
    global my_label
    global my_img

    my_img = ImageTk.PhotoImage(Image.open(os.getcwd() + f'\Images\{image_list[image_index]}').resize((1900, 1080)))
    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    return


# Function to enable or disable buttons, and display them
def button_state_changer():
    global image_index

    if image_index == 0:
        forward_button = Button(root, text="Next", command=lambda: picture_changer('next'))
        back_button = Button(root, text="Previous", state=DISABLED)
    elif image_index == len(image_list) - 1:
        forward_button = Button(root, text="Next", state=DISABLED)
        back_button = Button(root, text="Previous", command=lambda: picture_changer('previous'))
    else:
        forward_button = Button(root, text="Next", command=lambda: picture_changer('next'))
        back_button = Button(root, text="Previous", command=lambda: picture_changer('previous'))

    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    return


# Make list of all images in a folder
image_list = [str(x) for x in os.listdir('Images')]
image_index = 0
display_picture()

# Buttons that go forward and backward
button_state_changer()

# Button that exits the program
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)


root.mainloop()
