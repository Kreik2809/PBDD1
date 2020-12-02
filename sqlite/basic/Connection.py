import sqlite3

conn = sqlite3.connect('../ourdatabaseCars.db')

c = conn.cursor()

#c.execute('''CREATE TABLE data (prenom varchar(255), nom text)''')
c.execute('''CREATE TABLE dataVoit (id text, voiture text, couleur text, annee text)''')

c.execute("INSERT INTO dataVoit VALUES ('1','Alpha Romeo','Rouge','2000')")
c.execute("INSERT INTO dataVoit VALUES ('2','Ford','Bleu','2001')")
c.execute("INSERT INTO dataVoit VALUES ('3','Merco','Vert','2002')")
c.execute("INSERT INTO dataVoit VALUES ('4','Peugeot','Noir','2003')")

"""
c.execute("INSERT INTO data VALUES ('Pierre-Louis', 'Dagostino')")
c.execute("INSERT INTO data VALUES ('Nicolas', 'Sournac')")
c.execute("INSERT INTO data VALUES ('Jean-Louis', 'Porilo')")"""

#Permet de sauvegarder les données
conn.commit()

#Fin de la connexion à la base de données
conn.close()