import sqlite3

entries = []
connection = sqlite3.connect('data.db')

def create_table():
    with connection: # context manager, this is how we automatically commit
        connection.execute('CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);')

def add_entry(content, date):
    with connection:
        # instead of f strings, we do it this way to avoid SQL injection attack
        connection.execute('INSERT INTO entries VALUES (?,?);', (content, date))

def get_entries():
    cursor = connection.execute('SELECT * FROM entries;')
    return cursor

