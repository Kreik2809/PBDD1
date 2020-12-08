import sqlite.recData.recup_data as rd
import sqlite3
import Expression

cstTemp = 0

def selectionSqlCst(attr, cst, table, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    rd.createTempAs("temp"+str(cstTemp), rd.selectSql("*", table, " WHERE "+ attr.name + "=" + cst.valeur, c), c)
    int(cstTemp) += 1
    return tempTable

def selectionSqlAttr(attr1, attr2, table, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    rd.createTempAs("temp"+str(cstTemp), rd.selectSql("*", table, " WHERE "+ attr1.name + "=" + attr2.name, c), c)
    int(cstTemp) += 1
    return tempTable

def projectionSql(attrlist, table,c):
    where = " GROUP BY "
    attrs = ""
    for i in attrlist:
        attrs += str(i) + " "
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    rd.createTempAs("temp"+str(cstTemp), rd.selectSql(attrlist, table, where+attrs, c), c)
    int(cstTemp) += 1
    return tempTable

def joinSql(table, table2, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    rd.createTempAs("temp"+str(cstTemp), rd.selectSql("*", table.name + " Natural Join " + table2.name, "", c), c)
    int(cstTemp) += 1
    return tempTable

def renameSql(old, new, table, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    where = ""
    sel = rd.selectSql([old.name+" as "+new.name], table.name, where, c)
    rd.createTempAs("temp"+str(cstTemp), sel, c)
    int(cstTemp) += 1
    return tempTable

def unionSql(table, table2, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    sel1 = rd.selectSql("*", table.name, "", c)
    sel2 = rd.selectSql("*", table2.name, "", c)
    rd.createTempAs("temp"+str(cstTemp), sel1 + " UNION " + sel2, c)
    int(cstTemp) += 1
    return tempTable

def diffSql(table, table2, c):
    tempTable = Expression.Relation("temp"+str(cstTemp), c)
    sel1 = rd.selectSql("*", table.name, "", c)
    sel2 = rd.selectSql("*", table2.name, "", c)
    rd.createTempAs("temp"+str(cstTemp), sel1 + " EXCEPT " + sel2, c)
    int(cstTemp) += 1
    return tempTable

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