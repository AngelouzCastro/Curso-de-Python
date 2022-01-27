import datetime
import locale

locale.setlocale(locale.LC_ALL,'es-Mx')

dt = datetime.datetime.now() #el ahora
print('normal:',dt)
print('año:',dt.year)
print('mes:',dt.month)
print('dia:',dt.day)
print('hora:',dt.hour)
print('minuto:',dt.minute)
print('segundo:',dt.second)
print('microsegundo:',dt.microsecond)

dt.tzinfo
print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.day,dt.month,dt.year))

dt2 = datetime.datetime(1999,5,20)
dt2.replace(year=2000)
print(dt2.year)
print(dt2.isoformat())

print(dt.strftime("%A %d %B %Y %I:%M"))

print(dt.strftime("%A %d de %B del %Y - %H:%M"))

t = datetime.timedelta(days=15,hours=4,seconds=1001)
dentro_de_dos_semanas = dt + t

print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
