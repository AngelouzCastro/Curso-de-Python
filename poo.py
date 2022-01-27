# poo
# __init__() es el constructor
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("cliente no encontrado")

    def borrar(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"eliminado")
                return
        print("cliente no encontrado")



#fuera de las clases
hector = Cliente(nombre="Angel",apellidos="martinez",dni="20")
juan = Cliente("222","juan","perez")

empresa = Empresa(clientes=[hector,juan])

print(empresa.clientes)

empresa.mostrar(dni="20")
empresa.borrar("222")

print(empresa.clientes)
                
