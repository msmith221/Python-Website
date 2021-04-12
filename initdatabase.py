import sqlite3 as sql

def create_database():
    conn = sql.connect("database.db")
    conn.execute("CREATE TABLE students (name TEXT, address TEXT, city TEXT, pin TEXT)")
    conn.close()

create_database()

conn = sql.connect('database.db')
print("Opened database successfully!");

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully");
conn.close()