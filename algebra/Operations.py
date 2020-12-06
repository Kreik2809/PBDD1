import Expression

def isEquals(l1,l2, expr):
    """
    Cette fonction prend en paramètre deux listes contenant des sous listes composées d'un nom d'attribut et de son type.
    Elle prend également l'expression sur laquelle on effectue cette vérification
    Elle retourne True si les deux listes sont identiques et False sinon. 
    """
    if (len(l1) != len(l2)):
        print(str(expr) + " : le nombres d'attributs de " + str(expr.param1) + " et de " + str(expr.param2) + " sont différents")
        return False
    else:
        for i in range(len(l1)):
            if (l1[i][0] != l2[i][0]):
                print("Les schémas sur laquelle on applique l'expression : " + str(expr) + " ne sont pas identiques")
                print("L'attribut : " + l1[i][0] + " situé dans le schéma : " + str(expr.param1) + " n'existe pas dans le schéma de : " + str(expr.param2))
                return False
            elif (l1[i][1] != l2[i][1]):
                print("Le type de l'attribut : " + l1[i][0] + " est différent dans les deux sous expressions de " + str(expr))
                return False
        return True


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

    def __init__(self, param1, param2, attr, c):
        super().__init__(param1,param2, c)
        self.attr = attr
        self.symbol = "σ"
    
    def op(self, param1, param2):
        pass

    def verif(self, param1, param2):
        t = ""
        lColParam2 = param2.getCol(self.c)
        if (isinstance(self.attr, Expression.Cst)):
            t = self.attr.getType()
            for elem in lColParam2:
                if (elem[0] == str(param1)):
                    if (elem[1] == t):
                        print("expression correct")
                        return self
                    else:
                        print("expression incorrect")
                        print("Le type de la constante " + str(self.attr) + " (" + t + ")" + " est différent du type de l'attribut " + str(param1) + " (" + elem[1] + ")")
                        return self
            print("expression incorrect")
            print("L'attribut " + str(param1) + " n'existe pas dans le schéma de l'expression " + str(param2))
            return self      
        else:
            for elem in lColParam2:
                if elem[0] == str(self.attr):
                    t = elem[1]
            if (t == ""):
                print("expression incorrect")
                print("L'attribut " + str(self.attr) + " n'existe pas dans le schéma de l'expression " + str(param2))
            else:
                for elem in lColParam2:
                    if (elem[0] == str(param1)):
                        if (elem[1] == t):
                            print("expression correct")
                            return self
                        else:
                            print("expression incorrect")
                            print("Le type de la constante " + str(self.attr) + " (" + t + ")" + " est différent du type de l'attribut " + str(param1) + " (" + elem[1] + ")")
                            return self

    def getCol(self, c):
        return self.param2.getCol(c)
    

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

    def __init__(self, param1, param2, c):
        super().__init__(param1,param2, c)
        self.symbol = "π"
    
    def op(self, param1, param2):
        s = "projection de : "
        for elem in param1.liste:
            s = s + str(elem) + ", "
        s = s + " sur la relation : " + str(param2)
        return s

    def verif(self, param1, param2):
        lColParam2 = param2.getCol(self.c)
        param2Attr = []
        for t in lColParam2:
            param2Attr.append(t[0])
        for elem in param1.liste:
            if str(elem) not in param2Attr:
                print("Expression incorrect")
                print("L'attribut : " + str(elem) + " n'existe pas dans le schéma de l'expression : " + str(self))
                raise Exception
        print("Expression correct")
        return self
        
    def getCol(self, c):
        lColParam2 = self.param2.getCol(self.c)
        lCol = []
        for elem in self.param1.liste:
            for i in range(len(lColParam2)):
                if(str(elem)==lColParam2[i][0]):
                    lCol.append(lColParam2[i])
        return lCol

    
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

    def __init__(self, param1, param2, c):
        super().__init__(param1,param2, c)
        self.symbol = "x"
    
    def op(self, param1, param2):
        s = "jointure de la relation " + str(param1) + " sur la relation " + str(param2)
        return s
    
    def verif(self, param1, param2):
        print("Expression correct")
        return self

    def getCol(self, c):
        lColParam1 = self.param1.getCol(self.c)
        lColParam2 = self.param2.getCol(self.c)
        lCol = []
        for elem in lColParam1:
            if elem not in lCol:
                lCol.append(elem)
        for elem in lColParam2:
            if elem not in lCol:
                lCol.append(elem)
        return lCol

            
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

    def __init__(self, param1, param2, newAttr, c):
        super().__init__(param1,param2, c)
        self.newAttr = newAttr
        self.symbol = "φ"

    def op(self, param1, param2):
        s = "on renomme : " + str(param1) + " de la relation : " + str(param2) + " en : " + str(self.newAttr)
        return s
    
    def verif(self, param1, param2):
        lCol = param2.getCol(self.c)
        for i in range(len(lCol)):
            if str(param1) == lCol[i][0]:
                print("expression correct")
                return self
        print("expression incorrect")
        print("L'attribut " + str(param1) + " n'est pas présent dans le schéma de la sous expression " + str(param2))
        raise Exception

    def getCol(self, c):
        lCol =self.param2.getCol(self.c)
        for i in range(len(lCol)):
            if (lCol[i][0] == str(self.param1)):
                lCol[i][0] = str(self.newAttr)
        return lCol

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
        super().__init__(param1,param2, c)
        self.symbol = "U"
    
    def op(self, param1, param2):
        pass

    def verif(self, param1, param2):
        lParam1 = param1.getCol(self.c)
        lParam2 = param2.getCol(self.c)
        if (isEquals(lParam1,lParam2,self)):
            print("L'expression est correct")
            return self
        else:
            print("Expression incorrect")
            return self

    
    def getCol(self, c):
        return self.param1.getCol(self.c)
        
    
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

    def __init__(self, param1, param2, c):
        super().__init__(param1,param2, c)
        self.symbol = "-"

    def op(self, param1, param2):
        s = "la différence des relations : " + str(param1) + " et " + str(param2)
        return s

    def verif(self, param1, param2):
        lParam1 = param1.getCol(self.c)
        lParam2 = param2.getCol(self.c)
        if (isEquals(lParam1,lParam2,self)):
            print("L'expression est correct")
            return self
        else:
            print("Expression incorrect")
            return self
    
    def getCol(self, c):
        return self.param1.getCol(self.c)
    
    def __str__(self):
        s = "[ " + str(self.param1) + " " + self.symbol + " " + str(self.param2) + " ]"
        return s
