import UserInput as ui
import sqlite.recData.recup_data as rd
import sqlite3

conn = sqlite3.connect('sqlite/database.db')
c = conn.cursor()
#print(rd.selectSql(["*"],"Cities", [], c))
print(rd.getColAndTypes("Test1", c))
print(rd.getColAndTypes("Test2", c))
print(rd.getColAndTypes("Cities", c))


s = ui.readInput()
expression = None
flag = []

res = ui.analyseInput(s, expression, 0, flag, c)
print("Expression : " + str(res))
#print(type(res.param1))
try :
    res.validation()
    res.compute()
except Exception as e:
    print("Veuillez corriger votre expression")

conn.close()
