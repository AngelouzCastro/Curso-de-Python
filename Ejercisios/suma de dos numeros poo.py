class Opp:
    """
    n1 = 0
    n2 = 0
    suma = 0
    """
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        self.suma = self.n1 + self.n2

    def imprimir(self):
        print("la suma es = ", self.suma)


###############
n1 = float(input("dame numero"))
n2 = float(input("dame otro numero"))

op = Opp(n1,n2)
op.sumar()
op.imprimir()
