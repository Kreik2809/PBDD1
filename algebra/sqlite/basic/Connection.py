import sqlite3

conn = sqlite3.connect('../database.db')

c = conn.cursor()

#c.execute('''CREATE TABLE Test1 (Name text, Name2 text)''')

#c.execute('''CREATE TABLE Test2 (Name text, Name3 text)''')

#c.execute('''CREATE TABLE data (prenom varchar(255), nom text)''')

"""
#Table Q1
c.execute('''CREATE TABLE CITIES (Name text, Country text, Population float)''')

c.execute("INSERT INTO CITIES VALUES ('Bergen','Belgium',20.3)")
c.execute("INSERT INTO CITIES VALUES ('Bergen','Norway',30.5)")
c.execute("INSERT INTO CITIES VALUES ('Brussels','Belgium',370.6)")


c.execute('''CREATE TABLE COUNTRIES (Name text, Capital text, Population float, Currency text)''')

c.execute("INSERT INTO COUNTRIES VALUES ('Belgium','Brussels',10255.6,'EUR')")
c.execute("INSERT INTO COUNTRIES VALUES ('Norway','Oslo',4463.2,'NOK')")
c.execute("INSERT INTO COUNTRIES VALUES ('Japan','Tokyo',128888.0,'YEN')")

#Table Q9
c.execute('''CREATE TABLE NAT (Année float, Athlète text, Pays text)''')

c.execute("INSERT INTO NAT VALUES (2004,'M. Phelps','USA')")
c.execute("INSERT INTO NAT VALUES (2004,'T. Yamamoto','JAP')")
c.execute("INSERT INTO NAT VALUES (2004,'S Parry','GBR')")
c.execute("INSERT INTO NAT VALUES (2000,'I. de Bruijn','NED')")
c.execute("INSERT INTO NAT VALUES (2000,'M. Phelps','GBR')")


#Table Q5
c.execute('''CREATE TABLE PODIUM (Année float, GP text, Vainqueur text, Deuxième text, Troisième text)''')

c.execute("INSERT INTO PODIUM VALUES (2001,'Belgique','M. Schumacher', 'J. Trulli', 'R. Barrichello')")
c.execute("INSERT INTO PODIUM VALUES (2003,'Espagne','M. Schumacher', 'F. Alonso', 'R. Barrichello')")
c.execute("INSERT INTO PODIUM VALUES (2003,'Belgique','G. Fisichella', 'K. Räikkönen', 'F. Alonso')")

c.execute('''CREATE TABLE AFFILIATION (Année float, Pilote text, Ecurie text)''')

c.execute("INSERT INTO AFFILIATION VALUES (2001,'M. Schumacher', 'Ferrari')")
c.execute("INSERT INTO AFFILIATION VALUES (2001,'R. Barrichello', 'Ferrari')")
c.execute("INSERT INTO AFFILIATION VALUES (2001,'J. Trulli', 'Jordan')")
c.execute("INSERT INTO AFFILIATION VALUES (2001,'G. Fisichella', 'Benetton')")
c.execute("INSERT INTO AFFILIATION VALUES (2001,'M. Häkkinen', 'McLaren')")

c.execute("INSERT INTO AFFILIATION VALUES (2003,'M. Schumacher', 'Ferrari')")
c.execute("INSERT INTO AFFILIATION VALUES (2003,'R. Barrichello', 'Ferrari')")
c.execute("INSERT INTO AFFILIATION VALUES (2003,'J. Trulli', 'Renault')")
c.execute("INSERT INTO AFFILIATION VALUES (2003,'F. Alonso', 'Renault')")
c.execute("INSERT INTO AFFILIATION VALUES (2003,'G. Fisichella', 'Jordan')")
c.execute("INSERT INTO AFFILIATION VALUES (2003,'K. Räikkönen', 'Jordan')")

c.execute('''CREATE TABLE PARTICIPATIONS (Année float, Pilote text, GP text)''')

c.execute("INSERT INTO PARTICIPATIONS VALUES (2001,'M. Schumacher', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2001,'R. Barrichello', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2001,'J. Trulli', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2001,'G. Fisichella', 'Belgique')")

c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'M. Schumacher', 'Espagne')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'R. Barrichello', 'Espagne')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'F. Alonso', 'Espagne')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'G. Fisichella', 'Espagne')")


c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'M. Schumacher', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'R. Barrichello', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'J. Trulli', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'F. Alonso', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'G. Fisichella', 'Belgique')")
c.execute("INSERT INTO PARTICIPATIONS VALUES (2003,'K. Räikkönen', 'Belgique')")


#Table Q9
c.execute('''CREATE TABLE VILLES (Année float, Ville text)''')
c.execute("INSERT INTO VILLES VALUES (2004,'Athènes')")
c.execute("INSERT INTO VILLES VALUES (2000,'Sydney')")
c.execute("INSERT INTO VILLES VALUES (2008,'Athènes')")
c.execute("INSERT INTO VILLES VALUES (2012,'Londre')")

"""

#Permet de sauvegarder les données
conn.commit()

#Fin de la connexion à la base de données
conn.close()