import sqlite3
from sqlite3.dbapi2 import Error

#Connexion à la base de donnée et initialisation du curseur pour exécuter les commandes
conn = sqlite3.connect('../ourdatabaseCars.db')
c = conn.cursor()

#   Cette fonction prend en entrée une table et retourne une liste reprenant les noms de colonnes ainsi que leur type d'attribut
#   sous la forme : [['col1', 'type1'], ['col2', 'type2'], ..., ['coln', 'typen'],]
#   Note : Cette fonction lance une erreur, affiche un message d'erreur et retourne une liste vide
#          lorsqu'aucune table n'a été trouvée.
def getAllColumnsAndTypes(table):
    try:
        c.execute("SELECT * FROM "+table)
    except sqlite3.Error as e:
        print("Aucune table n'a été trouvée, vérifiez à être connecté à la bonne base de données :\n",e)
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

print(getAllColumnsAndTypes("dataVoit"))

conn.close()