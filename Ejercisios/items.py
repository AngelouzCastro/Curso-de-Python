from collections import Counter
matriz = []

entrada = input()
lista = entrada.split(' ')
n = int(lista[0])
m = int(lista[1])

diccionario = dict()


for i in range(n):
    matriz.append([])
    for j in range(m):
        item = input()
        matriz[i].append(item.lower())

print(max(set(lista), key=matriz.count))

c = Counter(matriz)
print(max(c, key=c.get))