import sqlite3

conn = sqlite3.connect("Varan3.db")

cur = conn.cursor()
cur.execute("CREATE TABLE batch(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT,contact TEXT)")
cur.execute("CREATE TABLE train(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT,seat no TEXT)")
cur.execute("INSERT INTO batch VALUES(23,'Shru','21434')")
cur.execute("INSERT INTO train VALUES(1,'Sou','24')")
conn.commit()
conn.close()
