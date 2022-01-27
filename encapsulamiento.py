"""
publico es como sea
privado empieza con __ (dos guiones bajos)
"""

class Ejemplo:
    __atributo_privado = "soy un atributo inalccanzable desde afuera"

    def __metodo_privado(self):
        print("soy un metodo inalcanzable")

    def metodo_publico(self):
        return self.__metodo_privado()

    def atributo_publico(self):
        return self.__atributo_privado

e = Ejemplo()
e.atributo_publico()
e.metodo_publico()
