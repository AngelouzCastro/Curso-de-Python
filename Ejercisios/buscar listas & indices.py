clientes= [ {'Nombre':'Angel', 'Apellidos':'Martinez', 'nc':'17010369'},
            {'Nombre':'Josue', 'Apellidos':'Castro', 'nc':'17010370'}
            ]
print(clientes)

def mostrar(clientes, nc):
    for c in clientes:
        if(nc == c['nc']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print("no se encontro")


print(mostrar(clientes, '17010369'))



def borrar(clientes, nc):
    for i,c in enumerate(clientes):
        if(nc == c['nc']):
            del (clientes[i])
            print(str(c), "> borrado")
            return
    


print(borrar(clientes, '17010369'))
