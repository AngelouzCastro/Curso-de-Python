#listas

numeros = [1,2,3,4]


#se puede hacer listas de diversos tipos de datos
 
datos = [4, "cadena", 3.5, "otra cadena", 2]

 #se puede usar indices

print(datos[1])
print(datos[-1])
print(datos[-2:])
 
#se le puede sumar elementos a  lista

numeros = numeros + [5,6,7,8]

print(numeros[:])

#cambio de elemento de la lista

pares = [0,2,4,5,8,10]
pares[3] = 6
print(pares)

#añadir al final de la lista
#funcion .append()
#se puede realizar operaciones en la función

pares.append(12)

pares.append(7*2)

print(pares)

#modificar conjunto de elmentos en las listas

letras = ['a','b','c','d','e','f']
letras[:3] = ['A','B','C']

print(letras)

#borrar elementos
letras[:3]=[]
print(letras)
#lista vacia  letras = []


#tamaño de lista
print(len(letras))



#################################################################
#listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]
print(r)


#modificacion sublista
#se puede usar en negativo
r[0]        # [1,2,3]  elemento se la lista principal
r[0][0]     # 1 elemeto de la sublista de la lista principal
print(r[1][1]) #5

