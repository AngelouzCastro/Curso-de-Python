import sys

entrada = input()

cadena = entrada.split()

uno = ''.join(reversed(cadena[0]))
dos = ''.join(reversed(cadena[1]))


uno = int(uno)
dos = int(dos)


if uno > dos:
    print(uno)
else:
    print(dos)




