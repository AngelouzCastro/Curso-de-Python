class Opp:
    
    """
    n1 = 0
    n2 = 0
    suma = 0
    
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    """
    def __init__(self):
        n1 = 0
        n2 = 0
        suma = 0
    def setn1(self,n1):
        self.n1 = n1

    def setn2(self,n2):
        self.n2 = n2        
        

    def sumar(self):
        self.suma = self.n1 + self.n2

    def getn1(self):
        return self.n1

    def getn2(self):
        return self.n2

    def getsuma(self):
        return self.suma

#######
class Interfaz:

    def pedir_n1(self):
        self.n1 = float(input("dame numero 1: "))
    
    def pedir_n2(self):
        self.n2 = float(input("dame numero 2: "))
    
    def imprimir(self,suma):
        print("la suma es: ",suma)

    def getn1(self):
        return self.n1

    def getn2(self):
        return self.n2

#######
class main:

    def run(self):
        mInterfaz = Interfaz()
        mOpp = Opp()

        mInterfaz.pedir_n1()
        mInterfaz.pedir_n2()

        mOpp.setn1(mInterfaz.getn1())
        mOpp.setn2(mInterfaz.getn2())

        mOpp.sumar()
        mInterfaz.imprimir(mOpp.getsuma())
####

mMain = main()
mMain.run()
mMain.run()






