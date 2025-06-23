# Clase Mascota
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar(self):
        print(f"{self.tipo} llamado {self.nombre}")


# Clase Tienda
class Tienda:
    def __init__(self):
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print("Mascotas disponibles:")
        for m in self.mascotas:
            m.mostrar()


# Código de prueba
if __name__ == "__main__":
    tienda = Tienda()

    m1 = Mascota("Eva", "Gato")
    m2 = Mascota("Sima", "Perro")

    tienda.agregar_mascota(m1)
    tienda.agregar_mascota(m2)

    tienda.mostrar_mascotas()
