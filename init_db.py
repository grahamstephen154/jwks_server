import sqlite3

connection = sqlite3.connect('totally_not_my_privateKeys.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS keys(
    kid INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL,
    exp INTEGER NOT NULL
)
''')

connection.commit()
connection.close()