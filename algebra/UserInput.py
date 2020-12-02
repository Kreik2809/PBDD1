import Expression as e
import Operations as o

def readInput():
    """
    Récupère via la console l'expression tapée par l'utilisateur et la retourne sous forme de String
    """
    s = input("Veuillez entrer votre requête SPJRUD : ")
    return s

def analyseSelect(text, expression, count, flag):
    """
    Analyse une opération de Sélection entrée au clavier.
    Syntaxe attendue : 
        -exemple1 : Select(attr1,Cst(*value*),Rel(name))
        -exemple2 : Select(attr1,attr2,Rel(name))
        Note : Pas d'espace, pas de guillemets, 'Cst' est un mot réservé.
               Une Cst peut être soit un chaîne de caractère, soit un nombre
               Le dernier paramètre peut être autre chose qu'une relation (Ex : une autre expression)
    """
    flag.append(False)
    param1 = None
    attr = None
    param2 = None
    currentExpression = o.Selection(param1, attr, param2)
    #On analyse le param1 (L'attribut que l'on sélectionne)
    count += 1
    nParam1 = ""
    while(text[count] != ","):
        nParam1 += text[count]
        count += 1
    currentExpression.param1 = e.Attribut(nParam1)
    #On analyse attr (Le deuxième élément de l'égalité)
    count += 1
    if(text[count : count +3] == "Cst"):
        #On égalise avec une constante
        count += 4
        vCst= ""
        while(text[count] != ")") :
            vCst += text[count]
            count += 1
        #On détermine le type de la constante
        if (vCst.isalpha() == False):
            vCst = float(vCst)
        currentExpression.attr = e.Cst(vCst)
        count += 1
    else:
        #On égalise avec un attribut
        nAttr =""
        while(text[count] != ","):
            nAttr += text[count]
            count += 1
        currentExpression.attr = e.Attribut(nAttr)
    #On analyse param2 (La relation ou l'expression sur laquelle on applique cette sélection)
    count += 1
    if(text[count:count+3] == "Rel"):
        #C'est une relation, l'expression est donc complète
        flag[-1] = True
        rName = ""
        i = count
        i = i + 4
        while (text[i] != ")"):
            rName += text[i]
            i += 1
        currentExpression.param2=(e.Relation(rName))
    else:
        flag[-1] = False

    if (expression != None):
        #Ce n'est pas la première opération de l'expression : On ajoute l'opération à l'expression existante
        expression.addExpr(currentExpression)
        return expression, flag, count
    else:
        #C'est la première opération de l'expression 
        expression = currentExpression
        return expression, flag, count



def analyseProj(text, expression, count, flag):
    """
    Analyse une opération de Projection entrée au clavier.
    Syntaxe attendue : 
        -exemple1 : Proj([attr1,attr2],Rel(name))
        -exemple2 : Proj([attr1,attr2],Expression)
        Note : Pas d'espace, pas de guillemets.
    """
    flag.append(False)
    listAttr = e.ListeAttribut([])
    param2 = None
    currentExpression = o.Proj(listAttr, param2)
    #On analyse les attributs
    count += 2 
    endAttr = count
    while (text[endAttr] != ']'):
       endAttr+=1

    l = text[count:endAttr].split(",")
    for a in l :
        currentExpression.param1.liste.append(e.Attribut(a))

    count = endAttr

    #On analyse la relation sur laquelle on applique la projection
    count += 2
    if(text[count:count+3] == "Rel"):
        #C'est une relation, l'expression est donc complète
        flag[-1] = True
        rName = ""
        i = count
        i = i + 4
        while (text[i] != ")"):
            rName += text[i]
            i += 1
        currentExpression.param2=(e.Relation(rName))
    else:
        flag[-1] = False

    if (expression != None):
        #Ce n'est pas la première opération de l'expression : On ajoute l'opération à l'expression existante
        expression.addExpr(currentExpression)
        return expression, flag, count
    else:
        #C'est la première opération de l'expression 
        expression = currentExpression
        return expression, flag, count


def analyseJoin(text, expression, count, flag):
    """
    Analyse une opération de jointure entrée au clavier.
    Syntaxe attendue : 
        -exemple1 : Join(Rel(*name*);Rel(*name*))
        -exemple2 : Join(*Expr*;*Expr)
    """
    flag.append(False)
    param1 = None
    param2 = None
    currentExpression = o.Join(param1,param2)
    #On analyse le param1
    count += 1
    if(text[count:count+3] == "Rel"):
        count += 4
        rName = ""
        while(text[count]!=")"):
            rName += text[count]
            count += 1
        currentExpression.param1 = e.Relation(rName)
        rName = ""
        count+=1
    else:
        tempExpr = None
        tempf = []
        i = count
        while(text[i] != ";"):
            i += 1
        #On effectue une seconde récursion pour déterminer le premier paramètre
        tempExpr = analyseInput(text, tempExpr, count, tempf)
        currentExpression.param1 = tempExpr
        count = i
    #On analyse le param2
    count += 1
    if(text[count:count+3] == "Rel"):
        print("hey")
        flag[-1] = True
        count += 4
        rName = ""
        while(text[count]!=")"):
            rName += text[count]
            count += 1
        currentExpression.param2 = e.Relation(rName)
    else:
        flag[-1] = False
    
    if (expression != None):
        #Ce n'est pas la première opération de l'expression : On ajoute l'opération à l'expression existante
        expression.addExpr(currentExpression)
        return expression, flag, count
    else:
        #C'est la première opération de l'expression 
        expression = currentExpression
        return expression, flag, count
        

def analyseRename(text, expression, count,flag):
    pass

def analyseUnion(text, expression, count, flag):
    pass

def analyseDiff(text, expression, count, flag):
    pass


def analyseInput(text,expression, count, flag):
    """
    Analyse récurcivement l'expression sous forme de String passée en paramètre et retourne l'expression de type Expression

    Paramètres :
    ------------
    -text : String
        L'input de l'utilisateur
    -expresison : Expression
        L'expression construite à partir de l'input
    -count : Int
        L'index de la position à partir de laquelle on analyse l'input
    -end : Int
        L'index de fin de l'input
    -flag : Boolean[]
        Un tableau de booléen représentant le fait que l'expression est considérée comme finie ou non.
        Si le dernier élément du tableau est True, alors l'expression est finie et on entre dans le cas de base de la récursion
        Sinon, on continue à analyser l'expression
    """
    if (len(flag)!= 0 and flag[-1] == True):
        return expression
    else:
        op = ""
        count
        while text[count] != '(':
            op += text[count]
            count += 1 
        if (op == "Proj"):
            expr, f, c = analyseProj(text, expression, count, flag)
            return analyseInput(text,expr, c, f)
        elif (op == "Select"):
            expr, f, c = analyseSelect(text, expression, count, flag)
            return analyseInput(text, expr, c, f)
        elif (op == "Join"):
            expr, f, c = analyseJoin(text, expression, count, flag)
            return analyseInput(text, expr, c, f)

           
if __name__ == "__main__":
    s = readInput()
    expression = None
    flag = []
    res = analyseInput(s, expression, 0, flag)
    print(res)
    print(res.compute())
    

