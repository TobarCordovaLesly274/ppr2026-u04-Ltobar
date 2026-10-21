class animal:
    def __init__(self, nombre):
        self.nombre=nombre

    def hacersonido(self):
        return f"Hola soy {self.nombre} y hago sonido generico"

class perro(animal):
    def hacersonido(self):
        return f"Hola soy {self.nombre} y hago Guauu!"

class pato(animal):
    def hacersonido(self):
        return f"Hola soy {self.nombre} y hago cuac cuac!"

#instanciar
perrito=animal("rocky")
print(perrito.hacersonido())

#objeto perro 2
perrito2=perro("bambi")
print (perrito2.hacersonido())

#objeto pato 
patito=pato("tiago")
print (patito.hacersonido())