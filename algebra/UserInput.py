import Expression as e
import Operations as o

def readInput():
    """
    Récupère via la console l'expression tapée par l'utilisateur et la retourne sous forme de String
    """
    s = input("Veuillez entrer votre requête SPJRUD : ")
    return s


def analyseRel(text, count):
    """
    Cette fonction permet d'analyse de manière générale le nom d'une relation.
    Retourne le nom de la relation (rName : String)
    ------------
    """
    count += 4
    rName = ""
    while(text[count]!=")"):
        rName += text[count]
        count += 1
    return rName

def analyseAttr(text, count):
    """
    Cette fonction permet d'analyser de manière générale le nom d'un attribut
    Retourne le nom de l'attribut ( : String), et l'endroit où l'analyse s'est arrêtée
    """
    aName = ""
    while(text[count] != ","):
        aName += text[count]
        count += 1
    return aName, count

def analyseLen(text, count):
    """
    Cette fonction permet retourner la taille du premier paramètre d'une expression JUD en prenant compte des potentiels autres opérations
    JUD qui la composent.
    """
    startCount = count
    nbreJUD = 1
    x = 0
    while(x < nbreJUD):
        if text[count] == ";":
            x += 1
        if text[count:count+5] == "Union":
            nbreJUD += 1
        elif text[count:count+4] == "Diff" or text[count:count+4] == "Join":
            nbreJUD += 1
        count += 1
    l = count - startCount
    return l-1


def analyseSelect(text, expression, count, flag, c):
    """
    Analyse une opération de Sélection entrée au clavier.
    Syntaxe attendue : 
        -exemple1 : Select(attr1,Cst(value),Rel(name))
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
    attr, j = analyseAttr(text,count)
    count = j
    currentExpression.param1 = e.Attribut(attr)
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
        attr, j = analyseAttr(text,count)
        count = j
        currentExpression.attr = e.Attribut(attr)
    #On analyse param2 (La relation ou l'expression sur laquelle on applique cette sélection)
    count += 1
    if(text[count:count+3] == "Rel"):
        #C'est une relation, l'expression est donc complète
        flag[-1] = True
        currentExpression.param2=(e.Relation(analyseRel(text, count), c))
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



def analyseProj(text, expression, count, flag, c):
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
    #On analyse la liste d'attributs
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
        currentExpression.param2=(e.Relation(analyseRel(text, count), c))
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

def analyseJUD(text, expression, count, flag, OP, c):
    """
    Analyse une opération de jointure entrée au clavier.
    Le paramètre OP spécifie le type de l'Opération à créer:
        1) OP = "J" => Join
        2) OP = "U" => Union
        ") OP = "D" => Diff 
    Syntaxe attendue : 
        -exemple1 : Join(Rel(name);Rel(name))
        -exemple2 : Join(*expr1*;*expre2*)
        -exemple3 : Union(*expr1*;*expre2*)
        -exemple4 : Diff(*expr1*;*expre2*)
        Note : expr1 et expr2 sont des expressions SPJRUD entrée au clavier en respectant la syntaxe.
    """
    flag.append(False)
    param1 = None
    param2 = None
    if(OP == "J"):
        currentExpression = o.Join(param1,param2)
    elif (OP == "U"):
        currentExpression = o.Union(param1,param2, c)
    elif (OP == "D"):
        currentExpression = o.Diff(param1,param2)
    #On analyse le param1
    count += 1
    if(text[count:count+3] == "Rel"):
        currentExpression.param1=(e.Relation(analyseRel(text, count), c))
        while(text[count] != ";"):
            count += 1
    else:
        tempExpr = None
        tempf = []
        #On effectue une seconde récursion pour déterminer le premier paramètre
        l = analyseLen(text, count)
        print(l)
        tempExpr = analyseInput(text, tempExpr, count, tempf, c)
        currentExpression.param1 = tempExpr
        #On calcule l'indice de début du param2
        count += l
    #On analyse le param2
    count += 1
    if(text[count:count+3] == "Rel"):
        flag[-1] = True
        currentExpression.param2=(e.Relation(analyseRel(text, count), c))
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
        

def analyseRename(text, expression, count,flag, c):
    """
    Analyse une opération de Renommage entrée au clavier.
    Syntaxe attendue : 
        -exemple1 : Rename(newName,oldName,Rel(name))
    """
    flag.append(False)
    newAttr = None
    param1 = None
    param2 = None
    currentExpression = o.Rename(newAttr, param1, param2)
    #On analyse newAttr
    count += 1
    nAttr, j = analyseAttr(text, count)
    currentExpression.newAttr = e.Attribut(nAttr)
    count = j
    #On analyse le param1
    count += 1
    nParam1, j = analyseAttr(text, count)
    currentExpression.param1 = e.Attribut(nParam1)
    count = j
    #On analyse le param2
    count += 1
    if(text[count:count+3] == "Rel"):
        flag[-1] = True
        currentExpression.param2=(e.Relation(analyseRel(text, count), c))
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



def analyseInput(text,expression, count, flag, cursor):
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
    -cursor : Cursor
        Le curseur sur la base de donnée à laquelle on applique l'expression
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
            expr, f, c = analyseProj(text, expression, count, flag, cursor)
            return analyseInput(text,expr, c, f, cursor)
        elif (op == "Select"):
            expr, f, c = analyseSelect(text, expression, count, flag, cursor)
            return analyseInput(text, expr, c, f, cursor)
        elif (op == "Join"):
            expr, f, c = analyseJUD(text, expression, count, flag, "J", cursor)
            return analyseInput(text, expr, c, f, cursor)
        elif (op == "Rename"):
            expr, f, c = analyseRename(text, expression, count, flag, cursor)
            return analyseInput(text, expr, c, f, cursor)
        elif (op == "Union"):
            expr, f, c = analyseJUD(text, expression, count, flag, "U", cursor)
            return analyseInput(text, expr, c, f, cursor)
        elif (op == "Diff"):
            expr, f, c = analyseJUD(text, expression, count, flag, "D", cursor)
            return analyseInput(text, expr, c, f, cursor)

           
if __name__ == "__main__":
    s = readInput()
    expression = None
    flag = []
    #res = analyseInput(s, expression, 0, flag)
    #print(res)
    #print(res.compute())
    

