a = 100
b = 5
a * b - 2**b >= 20 and not (a % b) != 0

#condiciones
if True:
    print("se cumple la condicion")

if not False:
    print ("not false")

if a == 10:
    print("a vale 10")

if a == 10 and b == 5:
    print("correcto")
else:
    print("no hago nada")

if a == 11:
    print("a es igual a 11")
elif a == 10:
    print ("a es igual a 10")
else:
    print("no se cumple ninguna")

nota = float(input("dame nota del alumno: "))

if nota == 100:
    print("felicidades crack tu calificacion es: ", nota)
elif nota < 100 and nota >= 70:
    print("aprobado con: ",nota)
elif nota > 100 or nota < 0:
    print("valor invalido")
else:
    print("que sad, tu calificacion es: ",nota,"/ de 100")

#saludo = "hola"
saludo = input("dame saludo: ")
if saludo == "hola":
    print("que tal: ")
