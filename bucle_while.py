#bucle while
c = 0
while c <= 5:
    c+=1
    print("c vale",c)
    if c == 2:
        #break
        continue #sirve para saltar
    print("cc vale",c)
else:
    print("no se para que sirve esto")


print("M E N U")
while(True):
    print(""""elige opcion:
    1) saludar
    2) sumar dos numeros
    3) salir""")
    opcion = input()
    if opcion == '1':
        print("hola")
    elif opcion == '2':
        n1 = float(input("dame numero 1: "))
        n2 = float(input("dame numero 2: "))
        print ("suma es = ", n1 + n2)
    else:
        break
