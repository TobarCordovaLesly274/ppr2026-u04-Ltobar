#pilares de la POO: Herencia, polimorfismo, encapsulamiento (+,-,#), abstracion

class persona:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre=nombre #atributo nombre
        self.edad=edad #atributo edad

    #metodo para mostrar la informacion
    def saludar (self):
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad}"

#crear un objeto (instancia) de la clase personas (instanciacion)
#nombre del objeto=clase
persona1= persona("juan", 20) #objeto 1
persona2= persona ("maria", 19) #objeto 2

#llamar al metodo del objeto e imprimimos el resultado
print(persona1.saludar())
print(persona2.saludar())