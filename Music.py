import sqlite3

con = sqlite3.connect("MusicDB.db")
print("Database opened successfully")

con.execute(
    "create table Music (id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT NOT NULL, Singer TEXT UNIQUE NOT NULL, Genre TEXT NOT NULL, Timeline TEXT NOTN NULL)")

print("Table created successfully")

con.close()
