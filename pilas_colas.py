#pilas y colas
# pila """no existe como tal la """
# pop siempre saca del fianl
# el pop siempre elimina, hasata en agignaciones

from collections import deque

pila = [3,4,5]
pila.append(6)
pila.append(7)

print(pila)

pila.pop()
n = pila.pop()

print(n)
print(pila,'\n')

#colas
#primeras entradas, primeras salidas

cola = deque()

cola = deque(['hector','juan','miguel'])
print(cola)

cola.append('maria')
print (cola)

cola.popleft()
print(cola)

nextt = cola.popleft()
print(cola)
