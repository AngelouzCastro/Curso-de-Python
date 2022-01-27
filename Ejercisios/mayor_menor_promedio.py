#programas de habraham en python
# for i in elemento iterable (listas, cadenas range,etc):

#mayor y menor

numeros = []
mayor = 0
menor = 0

for i in range(5):
    n = float(input("dame numero: "))
    numeros.append(n)


i = 0
while i < 5:
    if numeros[i] > mayor:
        mayor = numeros[i]
    i += 1

menor = mayor

j=0
while j < 5:
    if numeros[j] < menor:
        menor = numeros[j]
    j += 1

#SON LO MISMO
#for x in numeros:
#    print(x)
#
#for indice,numero in enumerate(numeros):
#    print(numeros[indice])
    
print("mayor: ",mayor)
print("menor: ",menor)

print(sum(numeros[:])/len(numeros))

