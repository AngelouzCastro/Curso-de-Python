#herencia

class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
Referencia \t{}
Nombre\t{}
Pvp\t{}
Descripcion\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion) 
#################################################
class Adorno(Producto):
    pass

#################################################
class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
Referencia \t{}
Nombre\t{}
Pvp\t{}
Descripcion\t{}
Productor\t{}
Distribuidor\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor) 
#################################################
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
Compra de un libro
Referencia \t{}
Nombre\t{}
Pvp\t{}
Descripcion\t{}
Isbn\t{}
Autor\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor) 



a = Adorno(2034,"vaso de adorno",15,"vaso con estampas")

al = Alimento(2035,"botella de aceite de oliva",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = " SA "

li = Libro(2036,"cocina alv",9,"chorizo")
li.isbn = "0-123458"
li.autor = "don crorizote"

#con coleciones, se puede agregar a una lista
produc = [a,al]

produc.append(li)

for p in produc:
    if( isinstance(p, Adorno) ):
        print(p.referencia,p.nombre)
    elif( isinstance(p, Alimento) ):
        print(p.referencia,p.nombre,p.productor)
    elif( isinstance(p, Libro) ):
        print(p.referencia,p.nombre,p.isbn)

def rebaja_producto(p, rebaja):
    """devuelve un producto con un porcentaja de su precio """
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

rebajado = rebaja_producto(al, 10)
print(rebajado)

copia_al = al
copia_al.referencia = 2038

print(al)

"""
import copy
copiaad = copy.copy(ad)
print(copiaad.pvp)



for p in produc:
    print(p,'\n')


print(al)
print(li)
print('\n',a)
"""
        
