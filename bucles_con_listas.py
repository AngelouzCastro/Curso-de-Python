#lista en bucles
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while (indice < len(numeros)):
    print(numeros[indice])
    indice+=1
#for

print("\n")

for numero in numeros:
    print(numero)

print("\n")

#for numero in numeros:
#        numeros[indice] *= 10
#        indice+=1
#print(numeros)

for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)

cadena = "hola"
for caracter in cadena:
    print(caracter)

#cdena2 = ""
#for caracter in cadena:
#    cadena2 += caracter * 2
#print(cadena)
#print(cadena2)
print("\n")
for i in range(10):
    print(i)
    
print("\n")
print(list(range(10)))

suma = sum( range(0, 101, 2))
print(suma)
