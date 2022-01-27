from collections import namedtuple

persona = namedtuple('persona','nombre apellido edad')
p = persona(nombre='angel',apellido='martinez',edad=22)
print(p.nombre)
print(p.edad)
print(p)