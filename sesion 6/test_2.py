"""POO polimorfismo"""

class Vaca():
    def sonido(self):
        print("muuuu")

class Gato():
    def sonido(self):
        print("miaauu")

class Perro():
    def sonido(self):
        print("guauuu")


gato=Gato()
perro=Perro()
vaca=Vaca()

lista_animales=[perro,gato,vaca]

def canto(animales):
    for animal in animales:
        animal.sonido()

canto(lista_animales)
