from tkinter import *


root = Tk()
root.geometry("400x400")


for r in range(0, 3):
    root.rowconfigure(r, weight=1)
    for c in range(0, 3):
        root.columnconfigure(r, weight=1)
        button = Button(root, text=f'{r} x {c}')
        button.grid(row=r, column=c, sticky=NSEW)

if __name__ == '__main__':
    root.mainloop()
