##indices de texto

#   +---+---+---+---+---+---+
#     |  p |  y |  t  |  h | o |  n |
#   +---+---+---+---+---+---+
#pos: 0    1   2    3   4    5
#neg:-6  -5  -4  -3  -2  -1

#las cadenas son inmutables

palabra = "python"
print(palabra[0]) # p
print(palabra[3]) # h

print(palabra[-1]) # n
print(palabra[-3]) # h

#multi indice
# [inicio : fin -1]

print(palabra[0:2]) # py
print(palabra[0:])  #python
print(palabra[:5])  #pytho
print(palabra[:])   #python
  
#se puede sumar
print(palabra[:2] + palabra[2:]) #py + thon
print(palabra[:99])              #python
print (palabra[99:])             #''

#se puede sumar concatenar

palabra = "N" + palabra[1:]
print (palabra)

#tamaño de las cadenas #    len()
print(len(palabra))

