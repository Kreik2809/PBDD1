import sqlite3

conn = sqlite3.connect('ourdatabase.db')

c = conn.cursor()

a = c.execute("SELECT * from data")
b = a.fetchall()

print(b)

for i in range(len(b)):
    for j in range(len(b[0])):
        print(b[i][j])

conn.close()