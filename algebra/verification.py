import UserInput as ui
import sqlite.recData.recup_data as rd
import sqlite3

conn = sqlite3.connect('sqlite/database.db')
c = conn.cursor()
#print(rd.selectSql(["*"],"Cities", [], c))
print(rd.getColAndTypes("Test2", c))
print(rd.getColAndTypes("Test1", c))



s = ui.readInput()
expression = None
flag = []

res = ui.analyseInput(s, expression, 0, flag, c)
print("Expression : " + str(res))
#print(type(res.param1))
res.validation()
print(res.getCol(c))
res.compute()
conn.close()
