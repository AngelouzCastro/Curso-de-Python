#programas de habraham en python
# for i in elemento iterable (listas, cadenas range,etc):

#mayor y menor
numeros = []
numeros2 =[]
conta = []
num =0
pos = 0
pos2=0
lim1 = 0
lim2 = 0
mediana = 0

cant = int(input("dame cantidad de numeros a ingresar: "))


#media
for i in range(cant):
    n = int(input("dame numero: "))
    numeros.append(n)

print("media= ",sum(numeros)/len(numeros))

numeros2 = numeros
numeros = sorted(numeros)
print("lista: ",numeros)

#moda
for i in numeros:
    num = numeros.count(i)
    conta.append(num)
   

#print(conta)
#print(numeros)
cosa = int(len(numeros) )

print(numeros[0:])
print(numeros2[0:])

if numeros[0:] == numeros2[0:]:
    print("la moda es= ", max(numeros))
elif max(conta) == min(conta) and numeros[0:] != numeros2[0:]:
    print("no hay moda")
else:
    print("la moda es= ",numeros[max(conta)-1]," que se repite,",max(conta)," veces")
"""

cc = -1
c = 0
for i in numeros:
    c = 0
    for j in range(cant):
        if numeros[i] == numeros[j]:
            c += 1
    if c > cc:
        moda = numeros[i]
        cc = c

print("la moda es= ",moda)
"""
#mediana

if len(numeros) % 2 == 0:
    pos = len(numeros)/2
    lim1 = int(pos - 1)
    lim2 = int(pos)
    mediana = (numeros[lim1] + numeros[lim2]) / 2
else:
    pos = len(numeros)/2
    pos = int(pos)
    mediana = numeros[pos]
    
print("la mediana es= ",mediana)

