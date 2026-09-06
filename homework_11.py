# text = "Ежевику для ежат Принесли два ежа. Ежевику еле-еле Ежата возле ели съели"
# words = text.lower().replace(".", "").replace(",", "").split()
# count = 0
#
# for word in words:
#     if word.startswith('е'):
#         count += 1
#
# print(f"Количество слов на букву 'е': {count}")

#
# import sqlite3
#
#
# # conn = sqlite3.connect('profile.db')
# # cur = conn.cursor()
# #
# # conn.close()
#
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         summa REAL,
#         date BLOB
#     )''')
#     # cur.execute('DROP TABLE IF EXISTS users')

import sqlite3

# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS person (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB DEFAULT "+79990000000",
#     age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
#     email TEXT UNIQUE NOT NULL
#     )''')

# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     ALTER TABLE person2
#     RENAME COLUMN surname TO home_address
#     ''')


# import sqlite3
#
# with sqlite3.connect('people.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS companies (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER,
#         company_id INTEGER,
#         FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
#     )''')
#
# import sqlite3
#
# with sqlite3.connect('people.db') as connection:
#     cur = connection.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS student (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT,
#         name TEXT,
#         patronymic TEXT,
#         age INTEGER,
#         [group] INTEGER NOT NULL,
#         FOREIGN KEY ([group]) REFERENCES groups (id)
#     )''')
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS groups (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name TEXT
#     )''')
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY (lesson_id) REFERENCES lessons (id)
#         FOREIGN KEY (group_id) REFERENCES groups (id)
#     )''')
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS lessons (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT
#     )''')


import sqlite3


def read_ava(n):
    try:
        with open(f"avatars/{n}.png", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sqlite3.connect('cars.db') as con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.executescript('''CREATE TABLE IF NOT EXISTS users (
          name TEXT,
          ava BLOB,
          score INTEGER 
         )''')

    img = read_ava(1)
    if img:
        binary = sqlite3.Binary(img)
        cur.execute("INSERT INTO users VALUES('Федор', ?, 1000)", (binary,))