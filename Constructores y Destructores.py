# Clase Persona usando constructor y destructor

class Persona:
    # Constructor: se llama cuando se crea un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad
        print(f"Persona creada: {self.nombre}, {self.edad} años")

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    # Destructor: se llama cuando el objeto se destruye o el programa termina
    def __del__(self):
        print(f"Persona eliminada: {self.nombre}")


# Crear una persona
persona1 = Persona("Ana", 20)

# Mostrar su información
persona1.mostrar_info()

# El objeto será eliminado automáticamente al final del programa
