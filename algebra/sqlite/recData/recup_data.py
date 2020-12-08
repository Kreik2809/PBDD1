import sqlite3
from sqlite3.dbapi2 import Error

def getColAndTypes(table, c):
    """
    Récupère les attributs et types d attributs d une table SQLite

    Attributs :
    -----------
        - table : String
            Prend l emplacement de la table
    Retour :
    --------
        - liste :
            [['attribut1', 'type1'], ['attribut2', 'type2'], ..., ['attributn', 'typen'],]
    Note :
    ------
        - Lance une erreur si la table n existe pas et retourne
        une liste vide.
    """
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

def getTableAr(table, c):
    """
    Récupère l arrité d une table

    Attributs :
    -----------
        - table : String
            Prend le nom de la table
    Retour :
    --------
        - int :
            Entier représentant l arité de la table
    Note :
    ------
        - Lance une erreur si la table n existe pas et retourne 0.
    """
    return len(getColAndTypes(table, c))

def selectSql(attrs, table, where, c):
    """
    Exécute une requête SELECT sur une BDD SQLite

    Attributs :
    -----------
        - attrs : Liste
            Liste d attributs que l on veut sélectionner sur une table
        - table : String
            Prend le nom de la table
        - where : String
            Chaîne de caractères représentant les conditions (on peut utiliser order by aussi)
    Retour :
    --------
        - Retourne liste contenant tuples de la sélection
    Note :
    ------
        - Lance une erreur si la table n existe pas et retourne None.
    """
    try:
        req = "SELECT"
        for i in range(len(attrs)):
            if i == len(attrs)-1:
                req += " " + str(attrs[i]) + " "
            else:
                req += " "+ str(attrs[i]) + ','
        req += "FROM " + str(table)
        if len(where) != 0:
            req += where
        c.execute(req).fetchall()
        return req
    except sqlite3.Error as e:
        print("Erreur :\nMéthode selectSql non-exécutée car :\n",e)

def insertSql(table, values, c):
    """
    Exécute une requête INSERT INTO sur une BDD SQLite

    Attributs :
    -----------
        - table : String
            Prend le nom de la table
        - values : Liste String
            Prend une liste de string contenant les valeurs à ajouter par attribut
    Retour :
    --------
        - Retourne un string contenant la requête exécutée ou None si la requête n'est pas possible
    Note :
    ------
        - Lance une erreur si la table n existe pas et retourne None.
    """
    try:
        req = "INSERT INTO " + str(table) + " VALUES ("
        for i in range(len(values)):
            if i == len(values)-1:
                req += "'" + values[i] + "')"
            else:
                req += "'" + values[i] + "', "
        c.execute(req)
        conn.commit()
        return req
    except sqlite3.Error as e:
        print("Erreur :\nMéthode insertSql non-exécutée car :\n",e)

def modifAttr(table, instruction, props, c):
    """
    Exécute une requête ALTER TABLE sur une BDD SQLite

    Attributs :
    -----------
        - table : String
            Prend le nom de la table
        - instruction : String
            Prend un string représentant l instruction à exécuter comme RENAME COLUMN
        - props : String
            String indiquant sur quoi l instruction doit être exécutée comme id to idVoit dans l'exemple du dessus
    Retour :
    --------
        - Retourne un string contenant la requête exécutée ou None si la requête n'est pas possible
    Note :
    ------
        - Lance une erreur si la table n existe pas et retourne None.
    """
    try:
        req = "ALTER TABLE " + str(table) + " " + str(instruction) + " " + str(props)
        c.execute(req)
        conn.commit()
        return req
    except sqlite3.Error as e:
        print("Erreur :\nMéthode modifAttr non-exécutée car :\n",e)

def createTempAs(name, select, c):
    """
    Permet de créer une table temporaire sur une BDD (avec AS)

    Attributs :
    -----------
        - name : String
            Le nom de la table en String
        - select :
            Requête selectsql()

    Retour :
    --------
        - Créer une table temporaire se terminant à conn.close()
    """
    try:
        if select != "":
            req = "CREATE TEMP TABLE IF NOT EXISTS " + str(name) + " AS " + str(select)
            c.execute(req)
            return req
    except sqlite3.Error as e:
        print("Erreur :\nMéthode createTempAs non-exécutée car :\n",e)

def createTempBasic(name, attrList, c):
    """
    Permet de créer une table temporaire sur une BDD (sans AS)

    Attributs :
    -----------
        - name : String
            Le nom de la table en String
        - attrList :
            Liste de String reprenant les attributs 
            de la nouvelle table ["attr1 type1", "attr2 type2",...]

    Retour :
    --------
        - Créer une table temporaire se terminant à conn.close()
    """
    if len(attrList) == 0:
        print("Veuillez introduire des attributs dans la table temporaire")
    try:
        req = "CREATE TEMP TABLE IF NOT EXISTS " + str(name) + " ("
        if len(attrList) != 0:
            for i in range(len(attrList)):
                if i != len(attrList)-1:
                    req += attrList[i] + ", "
                else:
                    req += attrList[i] + ")"
            c.execute(req)
        return req
    except sqlite3.Error as e:
        print("Erreur :\nMéthode createTempBasic non-exécutée car :\n",e)


if __name__=="__main__":
    #Connexion à la base de donnée et initialisation du curseur pour exécuter les commandes

    conn = sqlite3.connect('../database.db')
    #conn.row_factory = sqlite3.Row
    c = conn.cursor()

    #print(getColAndTypes("dataVoit"))
    #print(getTableAr("dataVoit"))
    #print(insertSql("dataVoit", ["8", "Citroen", "Noire", "2015"]))

    #a = selectSql(["voiture", "couleur", "idVoit", "annee"], "dataVoit", "")
    #print(createTempAs("tempotable", a))
    #print(getColAndTypes("tempotable"))

    #print(modifAttr("dataVoit", "rename column", "id to idVoit"))

    #print(createTempBasic("tableTest", ["attri1 text", "attri2 int"]))
    #print(getColAndTypes("tableTest"))

    print(selectSql(["*"],"Countries", [], c))

    conn.close()