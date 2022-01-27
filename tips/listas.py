lista = [1,2,3,4]
lista.append(6)

#deja lista vacia
lista.clear()

print(lista)

l1 = [1,2,3,4]
l2 = [5,6,7,8]

#combinar listas

l1.extend(l2)
print(l1)

#contar elementos

print(["hola","mundo","mundo"].count("hola"))

# regresa la posicion del elemento
print(["hola","mundo","mundo"].index("hola"))

l = [1,2,3,4]
#insertar en una posicion (pos, elemento)
l.insert(0,0)

print(l)

l.insert(-1,20)

print(l)

#pop elimina el ultimo elemento de la lista
l.pop()
print(l)
#elimina primer valor igual al parametro
l.remove(3)
print(l)

#revertir
l.reverse()
print(l)


#revertir una cadena
lista = list("hola mundo")
print(lista)
lista.reverse()
print(lista)
cadena = "".join(lista)
print(cadena)

#ordenar letras palabras y numeros
lista.sort()
print(lista)

#ordenar decendente letras palabras y numeros
lista.sort(reverse=True)
print(lista)
