#dicionarios
""" estos tienen un id """

vacio = {}

print(type(vacio))

# id : regresa

colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green'}


print(colores)

# itroduce el id
print(colores['amarillo'])

numeros = {10:'diez', 20:'veinte'}

print(numeros[10])

#cambiar valor de un dicionario
colores['amarillo'] = 'amarisho'

print(colores['amarillo'])

del(colores['amarillo'])

print(colores)

#sumar a valores

edades = {'angel':21, 'juan':30, 'talia':10}
edades['juan'] += 1
print(edades['juan'])

print(edades['juan'] + edades['angel'],'\n')


#recorrido con for

for idd in edades:
    print(idd)          #por id o clave

print('\n')
for i in edades:
    print(edades[i])    #valor que regresa

#######################################################
"""
b =float(input("dame valor: "))
print('\n')
for i in edades:
    if edades[i] == b:
        print(i,edades[i])
"""
#######################################################

print('\n')
print('\n')
print('\n')
for i,valor in edades.items():
    print(i,valor)

print('\n')
print('\n')
print('\n')
#listas con dicionarios
personajes = []
p = {'nombre':'mario','clase':'mago','raza':'humano'}
personajes.append(p)

p = {'nombre':'bowser','clase':'mounstro','raza':'dragon'}
personajes.append(p)

p = {'nombre':'toad','clase':'normal','raza':'toads'}
personajes.append(p)

print(personajes)

for p in personajes:
    print(p['nombre'],p['clase'],p['raza'],"\n")


for p in personajes:
    if p['nombre'] == 'toad':
        p['nombre'] = 'pepe'
        print(p['nombre'],p['clase'],p['raza'],"\n")


