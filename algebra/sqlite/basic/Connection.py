import sqlite3

conn = sqlite3.connect('../database.db')

c = conn.cursor()

#c.execute('''CREATE TABLE Test1 (Name text, Name2 text)''')

#c.execute('''CREATE TABLE Test2 (Name text, Name3 text)''')

#c.execute('''CREATE TABLE data (prenom varchar(255), nom text)''')

"""
c.execute('''CREATE TABLE Cities (Name text, Country text, Population float)''')

c.execute("INSERT INTO Cities VALUES ('Bergen','Belgium',20.3)")
c.execute("INSERT INTO Cities VALUES ('Bergen','Norway',30.5)")
c.execute("INSERT INTO Cities VALUES ('Brussels','Belgium',370.6)")


c.execute('''CREATE TABLE Countries (Name text, Capital text, Population float, Currency text)''')

c.execute("INSERT INTO Countries VALUES ('Belgium','Brussels',10255.6,'EUR')")
c.execute("INSERT INTO Countries VALUES ('Norway','Oslo',4463.2,'NOK')")
c.execute("INSERT INTO Countries VALUES ('Japan','Tokyo',128888.0,'YEN')")



c.execute("INSERT INTO data VALUES ('Pierre-Louis', 'Dagostino')")
c.execute("INSERT INTO data VALUES ('Nicolas', 'Sournac')")
c.execute("INSERT INTO data VALUES ('Jean-Louis', 'Porilo')")
"""


#Permet de sauvegarder les données
conn.commit()

#Fin de la connexion à la base de données
conn.close()