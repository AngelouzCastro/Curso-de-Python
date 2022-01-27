c = set()

c.add(1)
c.add(2)
c.add(3)

print(c)

#descartar un elemento
c.discard(1)
print(c)

#copiar conjunto
"""
c = c2
no funciona
si se modifica una se modifican las dos
"""

c2 = c.copy()
c2.discard(2)

print(c,'\n',c2)

#limpiar conhunto
c2.clear()
print(c2)

#comprobar si tienen elementos en comun
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

#distintos
print(c1.isdisjoint(c2))
print(c1.isdisjoint(c4))

#comprobar si todos los elementos de un subconjunto estan en un conjunto
print(c1.issubset(c4))

#varios elementos concuerdan
print(c1.issuperset(c2))

#######avanzados########
#unir conjuntos
print(c1.union(c2) == c4)
#actualizar conjunto
c1.update(c2)
print(c1)

#elementos diferentes del c1 que no estan en c2
print(c1.difference(c2))

# elementos comunes
print(c1.intersection(c2))

#elementos simetricos

print(c1.symmetric_difference(c2))
