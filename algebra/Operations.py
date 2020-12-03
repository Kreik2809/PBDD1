import Expression

class Selection(Expression.Operation):
    """
    Modélise l'opération de sélection en SPJRUD

    Attributs :
    -----------
    -param1 : Attribut
        L'attribut que l'on sélectionne
    -attr : Attribut OU Cst
        L'attribut ou la constante que l'on utilise pour l'égalité de la sélection
    -param2 : Expression
        La relation sur laquelle on effectue la sélection
    """

    def __init__(self, param1, attr, param2):
        self.param1 = param1
        self.attr = attr
        self.param2 = param2
        self.symbol = "σ"
        self.nbreJUD = 0
    
    def op(self, param1, param2):
        pass
    

    def __str__(self):
        s = "[ " + self.symbol + " ( " + str(self.param1) + " = " + str(self.attr) + " ) " + str(self.param2) + " ]"
        return s


class Proj(Expression.Operation):
    """
    Modélise l'opération de projection en SPJRUD

    Attributs :
    -----------
    -param1 : ListeAttribut
        La liste des attributs sur lesquelles on effectue la projection
    -param2 : Expression
        La relation sur laquelle on effectue la projection
    """

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.symbol = "π"
        self.nbreJUD = 0
    
    def op(self, param1, param2):
        s = "projection de : "
        for elem in param1.liste:
            s = s + str(elem) + ", "
        s = s + " sur la relation : " + str(param2)
        return s
    
    def __str__(self):
        s = "[ " + self.symbol + "( "
        if (len(self.param1.liste) > 1):
            for i in range(len(self.param1.liste) - 1) :
                s = s + str(self.param1.liste[i]) + ", "
        s = s + str(self.param1.liste[-1]) + " ) " + str(self.param2) + " ]"
        return s

class Join(Expression.Operation):
    """
    Modélise l'opération de jointure en SPJRUD

    Attributs :
    -----------
    -param1 : Expression
        La première relation de la jointure
    -param2 : Expression
        La deuxième relation de la jointure
    """

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.symbol = "x"
        self.nbreJUD = 0
    
    def op(self, param1, param2):
        s = "jointure de la relation " + str(param1) + " sur la relation " + str(param2)
        return s
            
    def __str__(self):
        s = "[ "+ str(self.param1) + " x " + str(self.param2) + " ]"
        return s

class Rename(Expression.Operation):
    """
    Modélise l'opération de renommage en SPJRUD

    Attributs :
    -----------
    -newAttr : Attribut
        Le nouvel attribut dont le nom va remplacer celui de l'ancien
    -param1 : Attribut
        L'attribut que l'on renomme
    -param2 : Expression
        La relation sur laquelle on effectue le renommage
    """  

    def __init__(self, newAttr, param1, param2):
        self.newAttr = newAttr
        self.param1 = param1
        self.param2 = param2
        self.symbol = "φ"
        self.nbreJUD = 0    
    def op(self, param1, param2):
        s = "on renomme : " + str(param1) + " de la relation : " + str(param2) + " en : " + str(self.newAttr)
        return s

    def __str__(self):
        s = "[ " + self.symbol + "( " + str(self.newAttr) + "->" + str(self.param1) + " )" + str(self.param2) + " ]"
        return s

class Union(Expression.Operation):
    """
    Modélise l'opération d'union en SPJRUD

    Attributs :
    -----------
    -param1 : Expression
        La première relation de l'union
    -param2 : Expression
        La deuxième relation de l'union
    """
    
    def __init__(self, param1, param2, c):
        self.param1 = param1
        self.param2 = param2
        self.c = c
        self.symbol = "U"
        self.nbreJUD = 0
    
    def op(self, param1, param2):
        #print(param1.getCol(self.c))
        #print(param2.getCol(self.c))
        pass
    
    def getCol(self, c):
        #print("getCol Union")
        pass
    
    def __str__(self):
        s = "[ " +str(self.param1) + " " + self.symbol + " " + str(self.param2) + " ]"
        return s

class Diff(Expression.Operation):
    """
    Modélise l'opération de différence en SPJRUD

    Attributs :
    -----------
    -param1 : Expression
        La première relation de la différence
    -param2 : Expression
        La deuxième relation de la différence
    """

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.symbol = "-"
        self.nbreJUD = 0

    def op(self, param1, param2):
        s = "la différence des relations : " + str(param1) + " et " + str(param2)
        return s
    
    def __str__(self):
        s = "[ " + str(self.param1) + " " + self.symbol + " " + str(self.param2) + " ]"
        return s
