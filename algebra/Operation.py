import Expression

class Join(Expression.Operation):
    """Modélise l'opération de jointure en SPJRUD"""

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.symbol = "x"
    
    def op(self, expr1, expr2):
        s = "On effectue la jointure de la relation " + str(expr1) + " sur la relation " + str(expr2)
        return s

    
    def __str__(self):
        s = str(self.expr1) + " x " + str(self.expr2)
        return s

