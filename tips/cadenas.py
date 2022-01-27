#todo en myusculas
print("hola mundo".upper())
#todo en minusculas 
print("hola mundo".lower())
#solo primera en minuscula
print("hola mundo".capitalize())
#solo primera de cada palabra en mayusculas
print("hola mundo".title())

#contar letras o
print("hola mundo".count('o'))
#contar palabras 'mundo'
print("hola mundo".count('mundo'))
#regresa en donde inicia la palabra mundo
print("hola mundo".find('mundo'))
#regresa donde inicia la ultima palabra mundo
print("hola mundo mundo mundo mundo".rfind('mundo'))


c = "100"
#confirma si una cadena es un digito
print(c.isdigit())
c2 = "ABC10034po"
# confirma si los caracteres son solo letras y numeros
print(c2.isalnum())
# confirma si la cadena es solo letras
print(c2.isalpha())

#coprobar si son mayusculas
hola = "hola mundo"
print(hola.isupper())
#comprobar si son minusculas
print(hola.islower())
#comprobar si es un titulo
print(hola.istitle())

#comprobar si son espacios en blanco
print("    ".isspace())

#comprobar si comienza con una letra, palabra o un numero
print("hola mundo".startswith("hola"))
#comprobar si termina con una letra, palabra o numero
print("hola mundo".endswith("mundo"))


###### Avanzados    ####
hmc = "hola mundo ,cruel"
#separa cadenas palabras
print(hmc.split()[0])
#separa con signo espesifico()
print(hmc.split(',')[1])

#hacer una cadena con comas
print(",".join("hola mundo"))


#borrar solo espacios al inicio y final
print("       hola mundo     ".strip())

#borrar solo signos al inicio y final
print("----hola mundo----".strip('-'))


#replazar letra o por 0
print("hola mundo".strip('o','0'))
#remplaza palabra mundo por marte
print("hola mundo".strip('mundo','marte'))
#remplaza palabra ' mundo' por '' solo los primeros 4
print("hola mundo mundo mundo mundo mundo".replace(' mundo','',4))



