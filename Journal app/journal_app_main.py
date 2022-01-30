from tkinter import *
import functions

root = Tk()
root.title("Jordan's Journaling App")
root.geometry("800x800+1300+150")

# Canvas
canvas = Canvas(root, bg="#263D42")
canvas.pack(fill="both", expand=True)

# Login prompt
# Create a Frame for un/pw prompt
login_frame = Frame(canvas, bg="grey", width=500, height=300, highlightbackground="black", highlightthickness=1)
login_frame.place(relx=.5, rely=.5, anchor="center")


if __name__ == '__main__':
    root.mainloop()
