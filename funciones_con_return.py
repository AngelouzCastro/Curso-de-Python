#### Funciones con retornos ####
def test4():
    return "una cadena"

#mostrar
test4()
print(test4())

c = test4()
print(c)

def lista():
    return [1,2,3,4,5]

print(lista()[-1])

l = lista()
l[-1]

### las funciones pueden regresar multiples varables ###

def test():
    return "cadena",20,[1,2,3]

print(test())

### asignar a variables lo que regresa la funcion ###

c,n,m = test()

print(m,n,c)
