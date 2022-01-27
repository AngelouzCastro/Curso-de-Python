n = int("10")

f = float('10.5')

c = 'un texto y un numero' + str(10)+ ' ' + str(4.15)

print("int {} float {} string {}".format(n,f,c))

#convierte a Numero Binario
print(bin(10))

#convierte a numero hexadecimal
print(hex(10))

#convierte de binario & hexadecimal a enteros
print(int("0b1010",2))
print(int('0xa',16))

#valor absoluto
print(abs(-10),abs(10),abs(2))

#redondiar
print(round(5.5))
print(round(5.4))

#evaluar expreciones
print(eval('2+5'))

n = 10
print(eval('n*10 - 5'))

#ayuda de python
print(help())

