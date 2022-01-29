from tkinter import *
import sqlite3
from pathlib import Path


root = Tk()
root.title('Address Book DB Project')
root.geometry('400x400')
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create directory if needed for the db
p = Path('Databases')
p.mkdir(exist_ok=True)

# Create a db or connect to one
connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')

# Create cursor
cursor = connect.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )''')

# Data entry fields
first_name = Entry(root)
first_name.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky=NSEW)

last_name = Entry(root)
last_name.grid(row=1, column=1, padx=(0, 10), sticky=NSEW)

address = Entry(root)
address.grid(row=2, column=1, padx=(0, 10), sticky=NSEW)

city = Entry(root)
city.grid(row=3, column=1, padx=(0, 10), sticky=NSEW)

state = Entry(root)
state.grid(row=4, column=1, padx=(0, 10), sticky=NSEW)

zipcode = Entry(root)
zipcode.grid(row=5, column=1, padx=(0, 10), sticky=NSEW)

data_entry_list = ['first_name', 'last_name', 'address', 'city', 'state', 'zipcode']

# Create data labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, padx=(0, 20), pady=(10, 0), sticky=E)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0, padx=(0, 20), sticky=E)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0, padx=(0, 20), sticky=E)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0, padx=(0, 20), sticky=E)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0, padx=(0, 20), sticky=E)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0, padx=(0, 20), sticky=E)


# Create submit function
def submit_data():
    # Connect to the db and place the cursor
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        # insert into table
        cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
                       {
                           'first_name': first_name.get(),
                           'last_name': last_name.get(),
                           'address': address.get(),
                           'city': city.get(),
                           'state': state.get(),
                           'zipcode': zipcode.get()
                       },
                       )
        # Commit the change
        connect.commit()
    # Clear the text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query function that opens a new window with the info
def query_db():
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        # Query the database
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()
        # Loop through results
        print_records = ''
        for entry in records:
            print_records += f"{str(entry[0])} {str(entry[1])}\t{str(entry[6])}\n"
        open_window('Name Entries', print_records)


def open_window(title, display):
    top = Toplevel()
    top.title(title)
    top.geometry('400x400')
    my_label = Label(top, text=display)
    my_label.pack()
    second_button = Button(top, text="Close", command=top.destroy)
    second_button.pack()


# Create function to delete a record
def delete_record():
    # Connect to the db and place the cursor
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        # Delete a record
        cursor.execute("DELETE FROM addresses WHERE oid = ?", select_entry_id.get())
        # Commit the change
        connect.commit()
    select_entry_id.delete(0, END)


def edit_record():
    save_button['state'] = NORMAL
    # Pull the entry from the db
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM addresses WHERE oid = ?', select_entry_id.get())
        records = cursor.fetchall()
    # Insert the data into the root window entry fields
    for entry in records:
        for d in zip(data_entry_list, entry):
            data = globals()[d[0]]
            data.delete(0, END)
            data.insert(0, d[1])
    connect.close()


def save_record():
    save_button['state'] = DISABLED
    # Open db connection
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        get_list = []
        for d in data_entry_list:
            d = globals()[d]
            get_list.append(d.get())
        get_list.append(select_entry_id.get())
        sql = """
        UPDATE addresses 
        SET first_name = ? ,
            last_name = ? ,
            address = ? ,
            city = ? ,
            state = ? ,
            zipcode = ?
        WHERE oid = ?
        """
        cursor.execute(sql, get_list)


# Create a delete button
delete_button = Button(root, text='Delete Record', command=delete_record)
delete_button.grid(row=8, column=0, columnspan=2, pady=5, padx=10, sticky=NSEW)

# Create entry for which record to select
select_entry_id = Entry(root, width=20, borderwidth=3)
select_entry_id.grid(row=10, column=1, padx=10, pady=5)

# Create label for select entry field
select_entry_id_label = Label(root, text="Enter ID")
select_entry_id_label.grid(row=10, column=0, padx=(100, 10), pady=5, sticky=E)

# Create a submit button
submit_button = Button(root, text="Add Record To Database", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=(10, 5), padx=10, sticky=NSEW)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query_db)
query_button.grid(row=7, column=0, columnspan=2, pady=5, padx=10, sticky=NSEW)

# Create a button that populates entry fields with editable info
edit_button = Button(root, text="Edit Record", command=edit_record)
edit_button.grid(row=9, column=0, padx=(10, 5), pady=5, sticky=NSEW)
save_button = Button(root, text="Save Changes", command=save_record, state=DISABLED)
save_button.grid(row=9, column=1, padx=(5, 10), pady=5, sticky=NSEW)

# Commit Changes
connect.commit()

# Close Connection
connect.close()

if __name__ == '__main__':
    root.mainloop()
