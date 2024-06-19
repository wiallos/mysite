
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')

conn.commit()
conn.close()
