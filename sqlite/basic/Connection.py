import sqlite3

conn = sqlite3.connect('ourdatabase.db')

c = conn.cursor()

c.execute('''CREATE TABLE data (prenom text, nom text)''')

c.execute("INSERT INTO data VALUES ('Pierre-Louis', 'Dagostino')")

#Permet de sauvegarder les données
conn.commit()

#Fin de la connexion à la base de données
conn.close()