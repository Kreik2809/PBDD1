import Expression as e
import Operations as o

"""
Exemple d'utilisation du package algebra pour créer en python des requêtes SPJRUD
A venir:
    -système de lecture des entrées de l'utilisateur
    -système de récupération de l'entièreté de l'expression dans une forme facile à décoder et à analyser
    -OPTIONNEL:
        -Vérification de la cohérence de l'expression SPJRUD : --> Visitor pattern ?
"""

r1 = e.Relation("Cities")
r2 = e.Relation("CC")

a1 = e.Attribut("Population")
a2 = e.Attribut("Name")
a3 = e.Attribut("Capital")
a4 = e.Attribut("Country")

s1 = o.Selection(a4, e.Cst("Mali"), r2)
r1 = o.Rename(a2, a3, r1)
j1 = o.Join(r1, s1)

listeAttr = e.ListeAttribut([a1])

p1 = o.Proj(listeAttr, j1)

print(p1)
print(p1.compute())