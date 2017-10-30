import sqlite3 as sql

conn = sql.connect("data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE users")
cursor.execute("DROP TABLE lessons")

cursor.execute("""CREATE TABLE lessons(title text, class text, teacher text, cab text, day int, start time)""")
cursor.execute("""CREATE TABLE users(chatid int, status text, class text)""")