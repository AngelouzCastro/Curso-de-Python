#texro puede ser con doble comilla o comillas simples
print("hola mundo")
print ('hola mundo 2')

#se pueden usar comillas dentro de comillas
print('este texto incluye unas " "')
print("esta 'palabra' se encuentra escrita entre comillas simple")

#para usar las mismas comillas utilizar barra + comillas \+"
print("esta \"palabre\" se encuentra entre comillas dobles")
print('esta \'palabre\' se encuentra entre comillas dobles')

#una tabulacion & salto de linea
print("hola \tAdios")
print ("esto es un \nSalto de linea")

#ignorar atajos de texto
print(r"c:\nombre\directorio\tabla")

#bloques de textoo
print("""uno
dos
tres \ncuatro
""")

#declaracion de variables de texto
#nota se pueden asignar atajos de
#texto pero solo son interpretados por la funcion print
texto = "\thola mundo cruel"
print(texto)

#se pueden sumar los Strings (da saltos de linea automaticos)
print(texto + texto)

#se puede poner dos cadenas en una variable
s = "texto1" "texto2"
print(s)

#se puede multiplicar cadenas de forma directa
nombre = "\nAngel" * 10
print(nombre)
