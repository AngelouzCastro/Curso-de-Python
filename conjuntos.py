#conjuntos
#colecion desordenadas
conjunto = set()
print(conjunto)

conjunto = {1,2,3}
print(conjunto)

conjunto.add(4)
print(conjunto)

conjunto.add(4)
print(conjunto)



conjunto.add(0)
print(conjunto)

#se pude usar "in" para buscar en grupos
grupo = {'angel','victor','roger'}
print('angel' in grupo)


#si el elemento en el grupo esta repetido este se elimina
test = {'pedro','pedro','pedro'}
print(test)

#pasar lista un conjunto
lista = [1,2,3,3,2,1,1]
print("lista",lista)

c = set(lista)
print(c)

#pasar conjunto a una lista
lista = list(c)
print("nueva lista ",lista)

#elimina de una lista datos repetidos y los ordena
lista2 = [1,2,3,3,2,1,1,16,10]
lista2 = list( set(lista2) )
print("lista2: ",lista2)

#se pude usar conjuntos con strings
s = "pepe pecas pica papas"
print(set(s))
