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

# Commit Changes
connect.commit()

# Close Connection
connect.close()

if __name__ == '__main__':
    root.mainloop()

