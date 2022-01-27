##objetos dentro de objetos

class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se creo la pelicula",self.titulo)


class Catalogo:
    peliculas = []

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self,p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)


p = Pelicula("el padrino",175,1972)
c = Catalogo([p])

c.mostrar()
c.agregar(Pelicula("el padrino: Parte2",202,19))

c.mostrar()
