import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')

cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL,
       email TEXT NOT NULL,
       password TEXT NOT NULL
   )
''')

cursor.execute('''
   CREATE TABLE IF NOT EXISTS posts (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       image TEXT NOT NULL,
       title TEXT NOT NULL,
       description TEXT
   )
''')



conn.commit()
conn.close()
