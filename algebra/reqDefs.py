import sqlite.recData.recup_data as rd
import sqlite3
import Expression


def selectionSqlCst(attr, cst, table, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    rd.createTempAs("temp"+str(n), rd.selectSql("*", table, " WHERE "+ attr.name + "='" + str(cst.valeur)+"'", c), c)
    return tempTable

def selectionSqlAttr(attr1, attr2, table, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    rd.createTempAs("temp"+str(n), rd.selectSql("*", table, " WHERE "+ attr1.name + "=" + attr2.name, c), c)
    return tempTable

def projectionSql(attrlist, table,c, n):
    where = " GROUP BY "
    attrs = ""
    for i in attrlist:
        attrs += str(i) + " "
    rd.createTempAs("temp"+str(n), rd.selectSql(attrlist, table, where+attrs, c), c)
    tempTable = Expression.Relation("temp"+str(n), c)
    return tempTable

def joinSql(table, table2, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    rd.createTempAs("temp"+str(n), rd.selectSql("*", table.name + " Natural Join " + table2.name, "", c), c)
    return tempTable

def renameSql(old, new, table, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    where = ""
    sel = rd.selectSql([old.name+" as "+new.name], table.name, where, c)
    rd.createTempAs("temp"+str(n), sel, c)
    return tempTable

def unionSql(table, table2, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    sel1 = rd.selectSql("*", table.name, "", c)
    sel2 = rd.selectSql("*", table2.name, "", c)
    rd.createTempAs("temp"+str(n), sel1 + " UNION " + sel2, c)
    return tempTable

def diffSql(table, table2, c, n):
    tempTable = Expression.Relation("temp"+str(n), c)
    sel1 = rd.selectSql("*", table.name, "", c)
    sel2 = rd.selectSql("*", table2.name, "", c)
    rd.createTempAs("temp"+str(n), sel1 + " EXCEPT " + sel2, c)
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