import sqlite.recData.recup_data as rd
import sqlite3
import Expression

def selectionSql():
    pass

def projectionSql(attrlist, table,c):
    where = ""
    attrs = ""
    for i in attrlist:
        attrs += str(i) + " "
    tempTable = Expression.Relation("temp", c)
    rd.createTempAs("temp", rd.selectSql(attrlist, table, where, c), c)
    return tempTable

def joinSql(table, table2, c):
    req = (rd.createTempAs("temp", rd.selectSql("*", table + " Natural Join " + table2, "", c), c))
    return req

def renameSql(old, new, table, c):
    where = ""
    sel = rd.selectSql([old+" as "+new], table, where, c)
    return (rd.createTempAs("temp", sel, c))

def unionSql(table, table2, c):
    sel1 = rd.selectSql("*", table, "", c)
    sel2 = rd.selectSql("*", table2, "", c)
    return (rd.createTempAs("temp", sel1 + " UNION " + sel2, c))

def diffSql(table, table2, c):
    sel1 = rd.selectSql("*", table, "", c)
    sel2 = rd.selectSql("*", table2, "", c)
    return (rd.createTempAs("temp", sel1 + " EXCEPT " + sel2, c))

def afficher(table, c):
    return (c.execute("SELECT * FROM "+ str(table)).fetchall())

#c.execute('''CREATE TEMP TABLE test (Name TEXT, Voorname TEXT, Denom TEXT, Chiffre REAL)''')

#c.execute('''CREATE TEMP TABLE test2 (prenom TEXT, nom TEXT)''')

#c.execute('''CREATE TEMP TABLE test3 (Pierre TEXT, Name TEXT)''')


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    tab = "Cities"
    c = conn.cursor()

    #print(join("test", "test3", c))
    #print(union("test", "test3", c))
    #print(diff("test", "test3", c))
    #print(projection(["Name", "Denom"], "test", "", c))
    print(rd.getColAndTypes("test",c))
    print(rd.getColAndTypes("test3",c))
    print(rd.getColAndTypes("temp",c))