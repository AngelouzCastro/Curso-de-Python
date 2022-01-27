from io import open

numeros=[]
numeros2=[]
mayor = 0

fichero = open('numeros.csv','r')
numeros = fichero.readlines()
fichero.close()

for i in range(len(numeros)):
    numeros2.append(float(numeros[i]))
    i+=1


for i in range(len(numeros2)):
    if numeros2[i] >  mayor:
        mayor = numeros2[i]

menor = mayor

for i in range(len(numeros2)):
    if numeros2[i] < menor:
        menor =  numeros2[i]
        
print(mayor)
print(menor)
print(sum(numeros2)/len(numeros2))
