from tkinter import *
import sqlite3
from pathlib import Path


root = Tk()
root.title("Login or Register")
root.geometry("300x225")
root.resizable(False, False)

# Create directory for db if needed
p = Path('Databases')
p.mkdir(exist_ok=True)

# Connect to db and create tables if none exist
connection = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\login.db')
with connection:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_credentials (
    username text,
    password text
    )''')
    connection.commit()


# Configure row and column properties
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Label and entry field for username and password
un_label = Label(root, text="User Name:")
un_label.grid(row=0, column=0, pady=(10, 0))
un_entry = Entry(root)
un_entry.grid(row=0, column=1, pady=(10, 0))

pw_label = Label(root, text="Password:")
pw_label.grid(row=1, column=0)
pw_entry = Entry(root, show="*")
pw_entry.grid(row=1, column=1)

message_label = Label(root, text="")
message_label.grid(row=3, column=0, columnspan=2)


def register_user():
    # Get un and pw
    credentials = [un_entry.get(), pw_entry.get()]
    # Reset fields but leave un up
    reset_fields(False, True, True)
    # Check to see if they exist already
    with connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM user_credentials WHERE username = ? "
        cursor.execute(sql, [credentials[0]])
        checking = cursor.fetchall()
        if len(checking) == 0:
            # Create user
            sql = "INSERT INTO user_credentials VALUES(?, ?)"
            cursor.execute(sql, credentials)
            connection.commit()
            message_label['text'] = "User Created"
        else:
            message_label['text'] = "User name already exists"


def login_user():
    return


def reset_fields(username=False, password=False, message=False):
    if username:
        un_entry.delete(0, END)
    if password:
        pw_entry.delete(0, END)
    if message:
        message_label['text'] = ""


# Button to register a new user (if one doesn't exist) or log in
button_width = 20
reg_button = Button(root, text="Register", width=button_width, command=register_user)
reg_button.grid(row=2, column=0, padx=(10, 0), pady=10, sticky=NSEW)
log_button = Button(root, text="Login", width=button_width, command=login_user)
log_button.grid(row=2, column=1, padx=(0, 10), pady=10, sticky=NSEW)


if __name__ == '__main__':
    root.mainloop()
