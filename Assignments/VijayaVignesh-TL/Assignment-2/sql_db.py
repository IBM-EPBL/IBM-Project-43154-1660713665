import sqlite3

conn = sqlite3.connect('user.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (email TEXT, password TEXT )')
print("Table created successfully")
conn.close()
