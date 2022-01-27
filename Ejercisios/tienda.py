#tienda xd
import datetime
mientras = True
cuenta = {}
lista = []
modificar = 's'
ahora = datetime.datetime.now()
total = 0
iva = 0
pago = 0
cambio = 0

while mientras:
    opcion = int(input("""
        M E N Ú
        ¿QUE DESEA HACER?
        1. REGISTRAR PRODUCRO.
        2. MODIFICAR PRODUCTO.
        3. ELIMINAR PRODUCTO.
        4. PAGAR E IMPRIMIR TICKET.
        5. SALIR.
    """))


    
    if opcion == 1:
        
        nombre = input("INTRODUCE EL NOMBRE DEL PRODUCTO: ")
        precio = float(input("ITRODUCE EL PRECIO: "))
        cantidad = float(input("INTRODUCE CANTIDAD: "))
        subtotal = precio * cantidad

        cuenta = {'nombre':nombre,'precio':precio,'cantidad':cantidad,'subtotal':subtotal}
        lista.append(cuenta)
        
    elif opcion == 2:

        
        for i in lista:
                print(i['nombre'],i['cantidad'],i['precio'])
        
        while modificar == 's':

            buscado = input("itroduce nombre de articulo a modificar: ")
            
            op2 = int(input("""
                        MENÚ MODIFICAR
                        SELECIONE UNA OPCIÓN
                        1. MODIFICAR NOMBRE.
                        2. MODIFICAR PRECIO.
                        3. MODIFICAR CANTIDAD.
                        4. CANCELAR.[X]
                        """))
                
            

            for i in lista:
                if i['nombre'] == buscado:
                    
                    
                    if op2 == 1:
                        nuevo_nombre = input("introduce nuevo nombre: ")
                        i['nombre'] = nuevo_nombre
                        modificar = input('desea modificar algo más [s/n]:')
                    elif op2 == 2:
                        nuevo_precio = float(input("introduce nuevo precio: "))
                        i['precio'] = nuevo_precio
                        i['subtotal'] = nuevo_precio * i['cantidad']
                        modificar = input('desea modificar algo más [s/n]:')
                    elif op2 == 3:
                        nueva_cant = float(input("introduce cantidad: "))
                        i['cantidad'] = nueva_cant
                        i['subtotal'] = i['precio'] * nueva_cant
                        modificar = input('desea modificar algo más [s/n]:')
                    else:
                        modificar = 'n'
                        break
                        
                    
            
                

    elif opcion == 3:
        for i in lista:
                print(i['nombre'],i['cantidad'],i['precio'])

        eliminado = input("itroduce nombre de articulo a eliminar: ")

        for i in lista:
            if i['nombre'] == eliminado:
                i['nombre'] = ''
                i['precio'] = ''
                i['cantidad'] = ''
                i['subtotal'] = 0
        print("producto eliminado.\n")
                
    elif opcion == 4:
        total = 0
        pago = 0
        print("{:^45}".format("TIENDA MI BODEGA AURRERA"))
        print("{:^20}".format("#N_Venta"),ahora.strftime('%d/%m/%Y - %H:%M'))
        print('\n')
        for i in lista:
            print("{:^20}".format(i['nombre']),"{:^8}".format(i['cantidad']),"{:^8}".format(i['precio']),)

        print('\n')
        for i in lista:
            total += i['subtotal']

        print("{:^20} {:.2f}".format('Subtotal $',total))
        print("{:^20}".format("IVA 16%"))
        iva = total * 1.16
        print("{:^20} {:2}".format("Total:$",iva))

        while pago < iva:
            pago = float(input("introduce pago: "))

            if pago < iva:
                print("saldo insuficiente")
            else:
                cambio = pago - iva
                print("{:^20} {:.2f}".format("Cambio:$",cambio))            

        print("{:^20}".format("vuelva pronto"))

    elif opcion == 5:
        break
    else:
        print('opcion no valida')
        
