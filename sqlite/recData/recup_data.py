import sqlite3
from sqlite3.dbapi2 import Error

#Connexion à la base de donnée et initialisation du curseur pour exécuter les commandes
conn = sqlite3.connect('../ourdatabaseCars.db')
#conn.row_factory = sqlite3.Row
c = conn.cursor()


#   Cette fonction prend en entrée une table et retourne une liste reprenant les noms de colonnes ainsi que leur type d'attribut
#   sous la forme : [['col1', 'type1'], ['col2', 'type2'], ..., ['coln', 'typen'],]
#   Note : Cette fonction lance une erreur, affiche un message d'erreur et retourne une liste vide
#          lorsqu'aucune table n'a été trouvée.
def getColAndTypes(table):
    try:
        c.execute("SELECT * FROM "+table)
    except sqlite3.Error as e:
        print("Erreur :\nMéthode getColAndTypes non-exécutée car :\n",e)
    z = (c.execute("PRAGMA table_info("+table+");")).fetchall()
    listes = []
    listes2 = []

    for i in range(len(z)):
        listes.append(z[i][1])
        count=0
        for j in range(len(listes)):
            if i == j:
                listes.insert(i+count+1,z[i][2])
            count +=1

    counter = 0
    for k in range(len(listes)//2):
        listes2.insert(k, listes[counter:counter+2])
        counter += 2

    return listes2

#   Prend en entrée une table et retourne son arité
#   Note : Cette fonction lance une erreur, affiche un message d'erreur et retourne une liste vide
#          lorsqu'aucune table n'a été trouvée.

def getTableAr(table):
    return len(getColAndTypes(table))

#   Prend en entrée : list(attrs), str(table), str(where):
#   Retourne liste contenant tuples de la sélection

def selectSql(attrs, table, where):
    req = "SELECT"
    for i in range(len(attrs)):
        if i == len(attrs)-1:
            req += " " + str(attrs[i]) + " "
        else:
            req += " "+ str(attrs[i]) + ','
    req += "FROM " + str(table)
    if len(where) != 0:
        req += " WHERE " + where
    return (c.execute(req)).fetchall()

#   Permet d'insérer une ligne dans une table
#   prend en entrée une table et des values string (ATTENTION : Bien respecter l'insertion
#   en mettant toutes les valeurs et tout en STRING)
#   Retourne sous string la requête et l'exécute dans la base de données.

def insertSql(table, values):
    req = "INSERT INTO " + str(table) + " VALUES ("
    for i in range(len(values)):
        if i == len(values)-1:
            req += "'" + values[i] + "')"
        else:
            req += "'" + values[i] + "', "
    c.execute(req)
    conn.commit()
    return req

def modifAttr(table, instruction, props):
    req = "ALTER TABLE " + str(table) + " " + str(instruction) + " " + str(props)
    c.execute(req)
    conn.commit()
    return req

"""
- Créer sous-bdd
"""

#print(getColAndTypes("dataVoit"))
#print(getTableAr("dataVoit"))

#print(insertSql("dataVoit", ["6", "Mercedes", "Blanche", "2019"]))
#print(selectSql(["voiture", "couleur", "id", "annee"], "dataVoit", ""))

print(modifAttr("dataVoit", "rename column", "id to idVoit"))

print(getColAndTypes("dataVoit"))

conn.close()