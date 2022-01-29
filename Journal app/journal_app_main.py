from tkinter import *
import functions

root = Tk()
root.title("Jordan's Journaling App")
root.geometry("800x800+1300+150")

# Canvas
canvas = Canvas(root, bg="#263D42")
canvas.pack(fill="both", expand=True)

# Create a Frame for un/pw prompt
login_frame = Frame(canvas, bg="grey", width=500, height=300, highlightbackground="black", highlightthickness=1)
login_frame.place(relx=.5, rely=.5, anchor="center")









# Function to load previous prompts

# Button to add a prompt

# Button to remove a prompt

# Function to add a prompt

# Function to remove a prompt

# Button to save an entry

# Research and pick a way to organize answers by date and prompt <<<<
# Function to save an entry

if __name__ == '__main__':
    root.mainloop()
