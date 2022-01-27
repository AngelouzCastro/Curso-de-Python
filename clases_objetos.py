#la calase es un molde para crear objetos
"""
class Galleta:
    pass

una_galleta = Galleta()
#otra_galleta = Galleta()

una_galleta.sabor = "chocolate"
una_galleta.color = "marron"

#print(type(una_galleta))
print("el sabor de la galleta es",una_galleta.sabor)
"""

class Galleta():
    chocolate = False
    def __init__(self,sabor = None, forma = None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("se acab de crear una galleta de sabor {} con forma {}".format(sabor,forma))
        else:
            print ("no se a espesificado tu galleta")

    def chocolatear(self):
        self.chocolate = True

    def tiene(self):
        if self.chocolate:
            print("tiene chocolate")
        else:
            print("no tiene chocolate")
            
            

g = Galleta("fresa","redonda")
g.tiene()
g.chocolatear()
g.tiene()

