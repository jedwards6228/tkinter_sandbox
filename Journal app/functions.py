# Functions for the journal app

def register_user():
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
        # Create user
        sql = "INSERT INTO user_credentials VALUES(?, ?)"
        cursor.execute(sql, credentials)
        connection.commit()
        message_label['text'] = "User Created"
    else:
        message_label['text'] = "User name already exists"


def login_user():
    # Get un and pw
    entered_credentials = [(un_entry.get(), pw_entry.get())]
    stored_credentials = find_credentials()
    if entered_credentials == stored_credentials:
        reset_fields(True, True, True)
        message_label['text'] = "Credentials Accepted"
    else:
        reset_fields(False, True, True)
        message_label['text'] = "Incorrect User Name or Password"


# Function to find and store credentials for the un
def find_credentials():
    with connection:
        cursor = connection.cursor()
        sql = "SELECT * from user_credentials WHERE username = ?"
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