import UserInput as ui
import sqlite.recData.recup_data as rd
import sqlite3

conn = sqlite3.connect('sqlite/database.db')
c = conn.cursor()
#print(rd.selectSql(["*"],"Cities", [], c))

s = ui.readInput()
expression = None
flag = []

res = ui.analyseInput(s, expression, 0, flag, c)
print("RES: " + str(res))
res.compute()
conn.close()
