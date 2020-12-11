import Expression
import reqDefs as sql

def isEquals(l1,l2, expr):
    """
    Cette fonction prend en paramètre deux listes contenant des sous listes composées d'un nom d'attribut et de son type.
    Elle prend également l'expression sur laquelle on effectue cette vérification
    Elle retourne True si les deux listes sont identiques et False sinon. 
    """
    print(l1)
    print(l2)

    if (len(l1) != len(l2)):
        print("Expression invalide.")
        print(str(expr) + " : le nombres d'attributs de " + str(expr.param1) + " et de " + str(expr.param2) + " sont différents.")
        return False
    else:
        for elem in l1:
            if elem not in l2:
                print("Expression invalide.")
                print("Les schémas sur lesquels on applique l'expression : " + str(expr) + " ne sont pas identiques.")
                print("L'attribut : " + str(elem) + " situé dans le schéma : " + str(expr.param1) + " n'existe pas dans le schéma de : " + str(expr.param2) +".")
                return False
        for elem in l2:
            if elem not in l1:
                print("Expression invalide.")
                print("Les schémas sur lesquels on applique l'expression : " + str(expr) + " ne sont pas identiques.")
                print("L'attribut : " + str(elem) + " situé dans le schéma : " + str(expr.param2) + " n'existe pas dans le schéma de : " + str(expr.param1) +".")
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
        print("on effectue la sélection")
        print(param2)
        Expression.Operation.number += 1
        if isinstance(self.attr, Expression.Cst):
            return sql.selectionSqlCst(param1, self.attr, param2, self.c, Expression.Operation.number)
        else:
            return sql.selectionSqlAttr(param1, self.attr, param2, self.c, Expression.Operation.number)

    def verif(self, param1, param2):
        #On doit vérifier que param1 et attr existent dans le schéma de param2.
        #On doit vérifier que param1 et attr sont du même type.
        attrFinded = False
        param1Finded = False
        attrType = ""
        param1Type= ""
        lColParam2 = param2.getCol(self.c)
        #On cherche param1 et on défini son type
        for t in lColParam2:
            if (str(param1) == t[0]):
                param1Finded = True
                param1Type = t[1]
        #On cherche et on défini le type de attr
        if (isinstance(self.attr, Expression.Cst)):
            attrType = self.attr.getType()
            attrFinded = True
        else:
            for elem in lColParam2:
                if elem[0] == str(self.attr):
                    attrFinded = True
                    attrType = elem[1]
        if(attrFinded == False):
            print("Expression invalide.")
            print("L'attribut " + str(self.attr) + " n'existe pas dans le schéma de l'expression " + str(param2) +".")
            raise Exception
        if (param1Finded == False):
            print("Expression invalide.")
            print("L'attribut " + str(param1) + " n'existe pas dans le schéma de l'expression " + str(param2) +".")
            raise Exception   
        if (attrType == param1Type):
            return self
        else:
            print("Expression invalide.")
            if (isinstance(self.attr, Expression.Cst)):
                print("Le type de la constante " + str(self.attr) + " (" + attrType + ")" + " est différent du type de l'attribut " + str(param1) + " (" + param1Type + ").")
            else:
                print("Le type de l'attribut " + str(self.attr) + " (" + attrType + ")" + " est différent du type de l'attribut " + str(param1) + " (" + param1Type + ").")
            raise Exception 
        

    def getCol(self, c):
        #Le schéma retourné par une opération de Sélection est le schéma de la relation sur laquelle on l'applique.
        #ICI : param2
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
        print("On effectue la projection")
        Expression.Operation.number += 1
        return sql.projectionSql(param1.liste, param2, self.c, Expression.Operation.number)


    def verif(self, param1, param2):
        #On doit vérifier que tous les attributs présent dans la liste param1 existent dans le schéma de param2
        lColParam2 = param2.getCol(self.c)
        param2Attr = []
        for t in lColParam2:
            param2Attr.append(t[0])
        for elem in param1.liste:
            if str(elem) not in param2Attr:
                print("Expression invalide.")
                print("L'attribut : " + str(elem) + " n'existe pas dans le schéma de l'expression : " + str(self.param2) + ".")
                raise Exception
        return self
        
    def getCol(self, c):
        #Le schéma retourné par une opération de Projection est le schéma contenant uniquement les attributs de la liste param1 
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
        print("on effectue la jointure")
        Expression.Operation.number += 1
        return sql.joinSql(param1,param2,self.c, Expression.Operation.number)

    
    def verif(self, param1, param2):
        #Une opération de jointure est toujours valide
        return self

    def getCol(self, c):
        #Le schéma retourné par une opération de Jointure est "l'assemblage" des schéma de ses deux sous expressions
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
        print("on effectue le renommage")
        Expression.Operation.number += 1
        return sql.renameSql(param1, self.newAttr, param2, self.c, Expression.Operation.number)
    
    def verif(self, param1, param2):
        #On doit vérifier que param1 existe dans le schéma de param2
        lCol = param2.getCol(self.c)
        for i in range(len(lCol)):
            if str(param1) == lCol[i][0]:
                return self
        print("expression invalide.")
        print("L'attribut " + str(param1) + " n'est pas présent dans le schéma de la sous expression " + str(param2) + ".")
        raise Exception

    def getCol(self, c):
        #Le schéma retourné par une opération de Renommage est le schéma de l'expression sur laquelle on l'applique en tenant compte de 
        #la modification du nom de l'attribut renommé.
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
        print("on effectue l'union")
        Expression.Operation.number+=1
        return sql.unionSql(param1,param2,self.c, Expression.Operation.number)


    def verif(self, param1, param2):
        #On doit vérifier que les schémas des deux sous-expressions sur lesquelles on applique l'Union sont exactement identiques.
        lParam1 = param1.getCol(self.c)
        lParam2 = param2.getCol(self.c)
        if (isEquals(lParam1,lParam2,self)):
            return self
        else:
            raise Exception

    
    def getCol(self, c):
        #Le schéma retourné par une opération d'Union est le schéma d'une des relations sur lesquelles on l'applique.
        #ICI : param1
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
        print("on effectue la différence")
        Expression.Operation.number+=1
        return sql.diffSql(param1,param2,self.c, Expression.Operation.number)

    def verif(self, param1, param2):
        #On doit vérifier que les schémas des deux sous-expressions sur lesquelles on applique la différence sont exactement identiques.
        lParam1 = param1.getCol(self.c)
        lParam2 = param2.getCol(self.c)
        if (isEquals(lParam1,lParam2,self)):
            return self
        else:
            raise Exception
    
    def getCol(self, c):
        #Le schéma retourné par une opération de Différence est le schéma d'une des relations sur lesquelles on l'applique.
        #ICI : param1
        return self.param1.getCol(self.c)
    
    def __str__(self):
        s = "[ " + str(self.param1) + " " + self.symbol + " " + str(self.param2) + " ]"
        return s
