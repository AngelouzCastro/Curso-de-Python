n = int(input("dame numero: "))
n2 = int(input("dame otro numero: "))

def suma(n,n2):
    suma = n + n2
    return suma
    #return n + n2

#r = suma(n,n2)
print(suma(n,n2))

         
### None es un valor nulo o vacio ###

def resta(n=None,n2=None):
    if n == None or n2 == None:
        print("no hago nada primo :(")
        return
    else:
        return n - n2

r = resta()
print(r)


#no se por que no jala
def doble(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doble(ns[:])
print("lol",ns,doble(ns))

### argumentos indeterminados

def indeterminados_posicion(*args):
    print(args)                     #regresa una tupla

indeterminados_posicion(5,"hola",[1,2,3])


def indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(n=6,c="adios",l=[4,5,6])    #regresa un dicionario

def indeterminados_nombre2(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])
indeterminados_nombre2(n=6,c="adios",l=[4,5,6])    #regresa un dicionario

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("sumatorio de indeterinario es",t)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

super_funcion(10,50,-1,1.56,10,20,300,nombre="angel",edad=27)
