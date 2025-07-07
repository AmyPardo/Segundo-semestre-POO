# Programa sobre animales usando Programación Orientada a Objetos

class Animal:
    def __init__(self, nombre, edad):
        # Encapsulamos el nombre
        self.__nombre = nombre
        self.edad = edad

    # Método para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Método para cambiar el nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método que se puede cambiar en las otras clases
    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Aquí usamos polimorfismo (cambiamos el método hacer_sonido)
    def hacer_sonido(self):
        print(self.get_nombre() + " dice: Guau guau")

# Otra clase que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # También usamos polimorfismo aquí
    def hacer_sonido(self):
        print(self.get_nombre() + " dice: Miau")

# Parte principal del programa
if __name__ == "__main__":
    # Creamos un perro y un gato
    mi_perro = Perro("Toby", 4, "Golden")
    mi_gato = Gato("Eva", 2, "Amarillo, blanco y gris")

    # Mostramos el nombre del perro (usando encapsulación)
    print("Nombre original del perro:", mi_perro.get_nombre())
    mi_perro.set_nombre("Patas")  # Cambiamos el nombre
    print("Nombre nuevo del perro:", mi_perro.get_nombre())

    # Llamamos al método hacer_sonido (polimorfismo)
    mi_perro.hacer_sonido()
    mi_gato.hacer_sonido()
