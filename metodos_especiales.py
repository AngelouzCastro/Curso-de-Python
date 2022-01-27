class Pelicula:
    #constructor
    def __init__(self,titulo,duracion,fecha):
        self.titulo = titulo
        self.duracion = duracion
        self.fecha = fecha
        print("se creo la pelicula",self.titulo)
    #destructor
    def __del__(self):
        print("se borro la pelicula",self.titulo)

    #redefinir metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos.".format(self.titulo,self.duracion,self.fecha)

    #redefinir metodo lenght
    def __len__(self):
        return self.duracion

p = Pelicula("El Padrino",175,1972)
#del(p)
print(str(p))
print(len(p))

print(str(p))   

print(len("hola"))
