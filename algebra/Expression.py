import sqlite.recData.recup_data as rd
"""
Exemple d'utilisation du package algebra pour créer en python des requêtes SPJRUD


if __name__ == "__main__":
    r1 = Relation("Cities")
    r2 = Relation("CC")

    a1 = Attribut("Population")
    a2 = Attribut("Name")
    a3 = Attribut("Capital")
    a4 = Attribut("Country")

    s1 = o.Selection(a4, Cst("Mali"), r2)
    r1 = o.Rename(a2, a3, r1)
    j1 = o.Join(r1, s1)

    listeAttr = ListeAttribut([a1])

    p1 = o.Proj(listeAttr, j1)

    print(p1)
    print(p1.compute())
"""

class Expr():
    """
    Super classe représentant une expression algébrique
    """

    def __init__(self):
        pass

    def compute(self):
        #méthode abstraite définie dans la sous classe Operation
        pass
    
    def __str__(self):
        #méthode abstraite définie dans les sous classe d'Operation
        return ""


class Operation(Expr):
    """
    Modélise une opération avec deux paramètre de type Expression
    
    Note:
    -----
    -Un objet de cette classe ne sera jamais instancié.
    -nbreJUD est un nombre temporaire que l'on incrémente afin de calculuer l'index du début du param2 dans une expression J/U/D
    """

    def __init__(self, param1, param2, c):
        self.param1 = param1
        self.param2 = param2
        self.symbol = "?"
        self.c = c

    def op(self, expr1, expr2):
        #la méthode op est définie dans les sous classes modélisant des opérations concrètes
        return 0
    
    def verif(self, expr1, expr2):
        """
        Cette méthode effectue la vérification de l'expression
        """
        #la méthode vérif est définie dans les sous classes modélisant des opérations concrètes
        return 0
    
    def getCol(self, c):
        #la méthode getCol est définie dans les sous classes modélisation des opérations concrètes
        #cette fonction retourne la schéma des attributs de l'expression en la parcourant de manière récursive
        return 0
    
    def addExpr(self, expression):
        """Ajoute une sous-expression"""
        if (self.param2 == None):
            self.param2 = expression
        else:
            self.param2.addExpr(expression)
    
    def compute(self):
        """Calcul de manière récursive le résultat de l'expressions"""
        return self.op(self.param1.compute(), self.param2.compute())
    
    def validation(self):
        """Effectue la validation de l'expression de manière récursive"""
        return self.verif(self.param1.validation(), self.param2.validation())
    

class Attribut(Expr):
    """
    Modélise un attribut d'une table
    """

    def __init__(self, name):
        self.name = name

    def compute(self):
        return self
    
    def validation(self):
        return self
    
    def __str__(self):
        return self.name


class ListeAttribut(Expr):
    """
    Modélise une liste d'attributs d'une table
    
    Attribut :
    ----------
    -liste : Liste 
        Cette liste contient un ou plusieurs attributs
    """

    def __init__(self, liste):
        self.liste = liste

    def compute(self):
        return self
    
    def validation(self):
        return self
    
    def __str__(self):
        s = "[ "
        if (len(self.liste)>1):
            for i in range(len(self.liste) - 1):
                s = s + str(self.liste[i]) + ", "
        s = s + str(self.liste[-1]) + " ]"
        return s



class Relation(Expr):
    """
    Modélise une table d'une base de donnée relationnelle
    
    """
    def __init__(self, name, c):
        self.name = name
        self.c = c

    def compute(self):
        return self
    
    def validation(self):
        return self

    def getCol(self, c):
        return rd.getColAndTypes(self.name, c)
    
    def __str__(self):
        return self.name

class Cst(Expr):
    """
    Modélise une constante utilisable dans une expression SPJRUD
    
    """

    def __init__(self, valeur):
        self.valeur = valeur
    
    def compute(self):
        return self.valeur
    
    def getType(self):
        if type(self.valeur) == float:
            return "float"
        else:
            return "text"
    
    def __str__(self):
        return str(self.valeur)

