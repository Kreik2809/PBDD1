class Expression():
    """Super classe représentant une expression algébrique"""

    def __init__(self):
        pass

    def compute(self):
        #méthode abstraite définie dans la sous classe Operation
        pass
    
    def __str__(self):
        #méthode abstraite définie dans la sous classe Operation
        pass


class Operation(Expression):
    """Modélise une opération avec deux paramètre de type Expression"""

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.symbol = "?"

    def op(self, expr1, expr2):
        #la méthode op est définie dans les sous classe modélisant des opérations concrètes
        return 0
    
    def compute(self):
        """Calcul de manière récursive le résultat de l'expressions"""
        return self.op(self.expr1.compute(), self.expr2.compute())

    def __str__(self):
        s = repr(self.expr1) + " " + self.symbol + " " + repr(self.expr2)
        return s


class Attribut(Expression):
    """Modélise un attribut de table dans une base de donnée relationnelle"""

    def __init__(self, name):
        self.name = name

    def compute(self):
        return self
    
    def __str__(self):
        return self.name

class Relation(Expression):
    """Modélise une relation d'une base de donnée relationnelle"""

    def __init__(self, name):
        self.name = name
    
    def compute(self):
        return self
    
    def __str__(self):
        return self.name
