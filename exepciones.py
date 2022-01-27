#exepciones

#######normal

while(True):
    try:
        n = float(input("dame numero: "))
        m = 5
        print("{}/{}={}".format(n,m,n/m))
        break
    except:
        print("error")
        

#### Bloques de exepciones ###
"""try: sirve para capturar cualquier error dentro de un bloque de instruciones
    except: sirve para definir el codigo excepcional
    else: para definir el codigo que se ejecutara si no ocurre ningun error
    finally: pera definir el codigo que se ejecutara al final haya o no error
"""

while(True):
    try:
        n = float(input("dame numero: "))
        m = 5
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("error")
    else:
        print("todo ha salido bien")
        break
    finally:
        print("fin")

### excepcions con identificadores
"""
Type error: errores de tipos
value error: error de valor
Exception as e: para mostrar el error
"""


try:
    n = float(input("dame numero"))
    m = 5/n
except TypeError:
    print("no se pueden dividir el número por una cadena")
except ValueError:
    print("debes de introducir una cadena que sea un número")
except ZeroDivisionError:
    print("no se puede dividir entre cero")
except Exception as e:
    print( type(e).__name__ )


###     Invocacion de excepciones
### sin el Try & Except manda mensaje a la pantalla del error, pero no detiene crach
def miF(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se puede usar un valor nulo")
    except ValueError:
        print("Error")
miF()
