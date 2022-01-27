#herencia multiple
"""
hace referencia a la posibilidad de que una sub clase
herede de varias super clases a la vez

"""

class A:
    def __init__(self):
        print("soy de clase A")
    def a(self):
        print("soy from metodo A")

class B:
    def __init__(self):
        print("soy de clase B")
    def b(self):
        print("soy from metodo B")

# a tiene prioridad por estar primero
class C(A,B):
    def c(self):
        print("soy from metodo C")

c = C()
c.a()
c.b()
c.c()
    
