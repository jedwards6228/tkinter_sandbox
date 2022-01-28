from tkinter import *
import sqlite3
from pathlib import Path


root = Tk()
root.title('Database Project')
root.geometry('400x400')

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
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create data labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10, 0))

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


# Create function to delete a record
def delete_record():
    # Connect to the db and place the cursor
    connect = sqlite3.connect(r'C:\Users\Jordan\PycharmProjects\Tkinter Sandbox\Tkinter101\Databases\address_book.db')
    with connect:
        cursor = connect.cursor()
        # Delete a record
        cursor.execute(f'DELETE from addresses WHERE oid = {delete_entry_id.get()}')
        # Commit the change
        connect.commit()
    delete_entry_id.delete(0, END)


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
                       })
        # Commit the change
        connect.commit()
    # Clear the text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query function
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

        query_label = Label(root, text=print_records)
        query_label.grid(row=11, column=0, columnspan=2)


# Create a delete button
delete_button = Button(root, text='Delete Record', command=delete_record)
delete_button.grid(row=8, column=0, columnspan=2,pady=10,padx=10, ipadx=129)

# Create entry for which record to delete
delete_entry_id = Entry(root, width=20, borderwidth=3)
delete_entry_id.grid(row=9, column=1)

# Create label for delete entry field
delete_entry_id_label = Label(root, text="Enter ID to Delete")
delete_entry_id_label.grid(row=9, column=0)

# Create a submit button
submit_button = Button(root, text="Add Record To Database", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query_db)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Commit Changes
connect.commit()

# Close Connection
connect.close()

if __name__ == '__main__':
    root.mainloop()
