#formateo de escritura

v = "texto"
n = 10
print("un texto",v,"un numero",n)

c = "un texto {} y un numero {}".format(v,n)
print (c)

print("un texto '{1}' y un numero '{0}'".format(v,n))

print("un texto '{texto}' y un numero '{numero}'".format(numero = n,texto = v))

print("{v},{v},{v}".format(v=v))

print("{:>30}".format("palabra"))   #alinamiento a la derecha y 30 caracteres

print("{:30}".format("palabra"))    #alinamiento a la izquierda y 30 caracteres

print("{:^30}".format("palabra"))    #alinamiento al centro y 30 caracteres

print("{:.3}".format("palabra"))    #alinamiento cortar palabra

print("{:>30.3}".format("palabra"))    #recortar y alinear



#formateo de numeros enteros, y rellenar con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#formateo de numeros enteros, y rellenar con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:.2f}".format(3.1415926))
print("{:.3f}".format(3.1415926))

print("{:7.2f}".format(3.1415926))
print("{:7.3f}".format(3.1415926))

print("{:07.2f}".format(3.1415926))
print("{:07.3f}".format(3.1415926))
