import sqlite3


# Function to create the table if not exists
def create_table():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            CellNumber TEXT NOT NULL,
            Email TEXT
        )
    ''')

    connection.commit()
    connection.close()


# Function to insert data into the table
def insert_data(name, cell_number, email):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)
    ''', (name, cell_number, email))

    connection.commit()
    connection.close()


# Function to fetch all data from the table and display them
def fetch_and_display_data():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM contacts
    ''')

    data = cursor.fetchall()

    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Cell#: {row[2]}, Email: {row[3]}")

    connection.close()


# Create table if not exists
create_table()

# Insert 5 rows of data
insert_data("John Doe", "1234567890", "john.doe@example.com")
insert_data("Jane Smith", "9876543210", "jane.smith@example.com")
insert_data("Alice Johnson", "5555555555", "alice.johnson@example.com")
insert_data("Bob Brown", "7777777777", "bob.brown@example.com")
insert_data("Charlie Davis", "9999999999", "charlie.davis@example.com")

# Fetch and display all data
fetch_and_display_data()
