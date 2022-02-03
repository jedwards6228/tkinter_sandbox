from tkinter import *
import sqlite3
from pathlib import Path

root = Tk()
root.title("Jordan's Journaling App")
root.geometry("800x800+1300+150")

# Create directory for db if needed
p = Path('Databases')
p.mkdir(exist_ok=True)

# Connect to db and create tables if none exist
connection = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Journal app\Databases\login.db')
with connection:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
    username text,
    password text,
    first_name text,
    last_name text
    )''')
    connection.commit()

# Canvas
canvas = Canvas(root, bg="#263D42")
canvas.pack(fill="both", expand=True)

# Login prompt
# Create a Frame for un/pw prompt
frame_bg = "grey"
login_frame = Frame(canvas, bg=frame_bg, width=500, height=300, highlightbackground="black", highlightthickness=1)
login_frame.place(relx=.5, rely=.5, anchor="center")

# Configure row and column properties
login_frame.columnconfigure(0, weight=1)
login_frame.columnconfigure(1, weight=1)

# Label and entry field for username and password
top_label = Label(login_frame, text="Log in or Register", bg=frame_bg, font=("TkDefaultFont", 18, "bold"))
top_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))
un_label = Label(login_frame, text="User Name:", bg=frame_bg)
un_label.grid(row=1, column=0, padx=10, pady=(10, 0))
un_entry = Entry(login_frame)
un_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))

pw_label = Label(login_frame, text="Password:", bg=frame_bg)  # Do this to others and make padding
pw_label.grid(row=2, column=0)
pw_entry = Entry(login_frame, show="*")
pw_entry.grid(row=2, column=1, padx=(0, 10))

message_label = Label(login_frame, text="", bg=frame_bg)
message_label.grid(row=4, column=0, columnspan=2, pady=5)


# New Window to collect additional user info (first/last)
def user_info_window():
    user_window = Toplevel()
    user_window.title("User Info")
    user_window.geometry("300x150")
    user_window.configure(background=frame_bg)
    # Define frame size
    user_window.columnconfigure(0, weight=1)
    user_window.columnconfigure(1, weight=1)

    # Set labels and entry fields
    upper_label = Label(user_window, text="Please Enter New User Info", font=("TkDefaultFont", 14, "bold"), bg=frame_bg)
    upper_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    first_name_label = Label(user_window, text="First Name", bg=frame_bg)
    first_name_label.grid(row=1, column=0, padx=(10, 5))
    first_name_entry = Entry(user_window)
    first_name_entry.grid(row=1, column=1, padx=(10, 5))
    last_name_label = Label(user_window, text="Last Name", bg=frame_bg)
    last_name_label.grid(row=2, column=0, padx=(10, 5))
    last_name_entry = Entry(user_window)
    last_name_entry.grid(row=2, column=1, padx=(10, 5))

    lower_label = Label(user_window, text="", bg=frame_bg)
    lower_label.grid(row=3, column=0, columnspan=2)

    # Save info on button press from user info window
    def save_and_close():
        user_info[0:2] = [first_name_entry.get(), last_name_entry.get()]
        if len(user_info[0]) == 0 or len(user_info[1]) == 0:
            lower_label['text'] = "Please Complete the Form"
        else:
            sql = "UPDATE user SET first_name = ?, last_name = ? WHERE username = ?;"
            values = user_info.copy()
            values.append(current_user)
            cursor.execute(sql, values)
            connection.commit()
            user_window.destroy()

    save_button = Button(user_window, text="Save and Close", command=save_and_close)
    save_button.grid(row=3, column=0, columnspan=2, padx=(10, 5), pady=(15, 10), ipadx=5)


# User info variable
current_user = None
user_info = []


# Register new user
def register_user():
    global current_user
    # Get un and pw
    credentials = [un_entry.get(), pw_entry.get()]
    # Reset fields but leave un up
    reset_fields(False, True, True)
    # Basic pw check
    if len(credentials[1]) < 4:
        message_label['text'] = "Password is too short"
        return
    # Check to see if they exist already
    stored_creds = find_credentials()
    if len(stored_creds) == 0:
        # Pop up user info window to get first/last name NEED TO WAIT ON SQL UNTIL THIS IS DONE OR DO IT SEPARATELY
        user_info_window()
        current_user = credentials[0]
        # Add a user
        # Then Create a table for the user
        sql1 = "INSERT INTO user (username, password) VALUES(?, ?);"
        sql2 = f"""CREATE TABLE IF NOT EXISTS {credentials[0]} (
        date text,
        prompts text);"""
        value1 = credentials.copy()
        cursor.execute(sql1, value1)
        cursor.execute(sql2)
        connection.commit()
        message_label['text'] = "User Created"
    else:
        message_label['text'] = "User name already exists"


def login_user():
    global current_user
    # Get un and pw
    entered_credentials = [(un_entry.get(), pw_entry.get())]
    stored_credentials = find_credentials()
    if entered_credentials == stored_credentials:
        current_user = un_entry.get()
        print(current_user)
        reset_fields(True, True, True)
        message_label['text'] = "Credentials Accepted"
    else:
        reset_fields(False, True, True)
        message_label['text'] = "Incorrect User Name or Password"


# Function to find and store credentials for the un
def find_credentials():
    with connection:
        cursor = connection.cursor()
        sql = "SELECT username, password FROM user WHERE username = ?"
        cursor.execute(sql, [un_entry.get()])
        results = cursor.fetchall()
    return results


# Function for resetting fields on the page
def reset_fields(username=False, password=False, message=False):
    if username:
        un_entry.delete(0, END)
    if password:
        pw_entry.delete(0, END)
    if message:
        message_label['text'] = ""


# Button to register a new user (if one doesn't exist) or log in
button_width = 17
reg_button = Button(login_frame, text="Register", width=button_width, command=register_user)
reg_button.grid(row=3, column=0, padx=(10, 0), pady=(15, 0), sticky=NSEW)
log_button = Button(login_frame, text="Login", width=button_width, command=login_user)
log_button.grid(row=3, column=1, padx=(2, 10), pady=(15, 0), sticky=NSEW)

if __name__ == '__main__':
    root.mainloop()
