#curp
import random
nombre1 = ""
nombre2 = ""
apellidopa = ""
apellidoma = ""
anio = ""
dia = ""
mes = ""
estado = ""
sexo = ""
curp = ""


cantnom = input("cuantos nombres tienes: ")
cantnom = int(cantnom)

if cantnom == 1:
    nombre1 = input("introduce tu nombre: ")
else:
    nombre1 = input("introduce tu primer nombre: ")
    nombre2 = input("introduce tu segundo nombre: ")
    
apellidopa = input("apellido paterno: ")
apellidoma = input("apellidos materno: ")

curp = curp + apellidopa[0]


for i in range(len(nombre1)):
    if nombre1[i] == "a"or nombre1[i] == 'e' or nombre1[i] == 'i' or nombre1[i] == 'o' or nombre1[i] == 'u':
        curp = curp + nombre1[i]
        break

curp = curp + apellidoma[0]
curp = curp + nombre1[0]

curp = curp.upper()

anio = input("dame año: ")
curp = curp + anio [2:]

mes = input ("dame mes: ")
dia = input ("dame dia: ")

if len(mes) == 1:
    curp = curp + "0" + mes
else:
    curp = curp + mes

if len(dia) == 1:
    curp = curp + "0" + dia
else:
    curp = curp + dia

sexo = input("sexo [H/M]: ")

curp = curp + sexo[0]

estado = input("introduce tu estado: ")
estado = estado.upper()

if estado == 'AGUASCALIENTES':
    curp = curp + "AS"
elif estado == 'BAJA CALIFORNIA':
    curp = curp + 'BC'
elif estado == 'BAJA CALIFORNIA SUR':
    curp = curp + 'BS'
elif estado == 'CAMPECHE':
    curp = curp + 'CC'
elif estado == 'CHIAPAS':
    curp = curp + 'CS'
elif estado == 'CIHUAHUA':
    curp = curp + 'CH'
elif estado == 'CIUDAD DE MEXICO':
    curp = curp + 'DF'
elif estado == 'COAHUILA':
    curp = curp + 'CL'
elif estado == 'COLIMA':
    curp = curp + 'CM'
elif estado == 'DURANGO':
    curp = curp + 'DG'
elif estado == 'GUANAJUATO':
    curp = curp + 'GT'
elif estado == 'GUERRERO':
    curp = curp + 'GR'
elif estado == 'HIDALGO':
    curp = curp + 'HG'
elif estado == 'JALISCO':
    curp = curp + 'GC'
elif estado == 'MEXICO' or estado == 'MÉXICO':
    curp = curp + 'MC'
elif estado == 'MICHOACAN' or estado == 'MICHOACÁN':
    curp = curp + 'MN'
elif estado == 'MORELOS':
    curp = curp + 'MS'
elif estado == 'NAYARIT':
    curp = curp + 'NT'
elif estado == 'NUEVO LEON':
    curp = curp + 'NL'
elif estado == 'OAXACA':
    curp = curp + 'OC'
elif estado == 'PUEBLA':
    curp = curp + 'PL'
elif estado == 'QUERETARO':
    curp = curp + 'QO'
elif estado == 'QUINTANA ROO':
    curp = curp + 'QR'
elif estado == 'SAN LUIS POTOSI' or estado == 'SAN LUIS POTOSÍ':
    curp = curp + 'SP'
elif estado == 'SINANLOA':
    curp = curp + 'SL'
elif estado == 'SONORA':
    curp = curp + 'SR'
elif estado == 'TABASCO':
    curp = curp + 'TC'
elif estado == 'TAMAULIPAS':
    curp = curp + 'TS'
elif estado == 'TLAXCALA':
    curp = curp + 'TL'
elif estado == 'VERACRUZ':
    curp = curp + 'VZ'
elif estado == 'YUCATAN':
    curp = curp + 'YN'
elif estado == 'ZACATECAS':
    curp = curp + 'ZS'
else:
    curp == curp + 'NE'


exap = "" + apellidopa[1:]
exam = "" + apellidoma[1:]
exn1 = "" + nombre1[1:]

for i in range(len(exap)):

    if exap[i] == 'a':
        continue
    elif exap[i] == 'e':
        continue
    elif exap[i] == 'i':
        continue
    elif exap[i] == 'o':
        continue
    elif exap[i] == 'u':
        continue
    else:
        curp = curp + exap[i]
        break
    
for i in range(len(exam)):

    if exam[i] == 'a':
        continue
    elif exam[i] == 'e':
        continue
    elif exam[i] == 'i':
        continue
    elif exam[i] == 'o':
        continue
    elif exam[i] == 'u':
        continue
    else:
        curp = curp + exam[i]
        break

for i in range(len(exn1)):

    if exn1[i] == 'a':
        continue
    elif exn1[i] == 'e':
        continue
    elif exn1[i] == 'i':
        continue
    elif exn1[i] == 'o':
        continue
    elif exn1[i] == 'u':
        continue
    else:
        curp = curp + exn1[i]
        break
    
anio2 = int(anio)


if anio2 < 2000:
    curp = curp + "0"
    
else:
    curp = curp + "A"


print(listaza)
    
print(curp.upper(),random.randint(0,9))
    


                   
