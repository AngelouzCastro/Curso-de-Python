colores = {"amarillo":"yellow","azul":"blue","verde":"green"}

print(colores.get('amarillo','no se encuentra'))

print('amarillo' in colores)

#solo las llaves
print(colores.keys())

#solo los valores
print(colores.values())

#ambos
print(colores.items())

#solo valores
for c in colores:
    print(colores[c])

#llava y valores
for c,v in colores.items():
    print(c,v)
    
#elimina un valor
colores.pop('amarillo','no se encuentra')
print(colores)

#vaciar dicionario
colores.clear()
print(colores)
