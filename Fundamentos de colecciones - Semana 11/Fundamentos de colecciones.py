import json

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # diccionario con id como clave

    def agregar(self, p):
        if p.id in self.productos:
            print("Ya existe ese ID")
        else:
            self.productos[p.id] = p
            print("Producto agregado")

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado")
        else:
            print("No existe ese ID")

    def actualizar(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad: self.productos[id].cantidad = cantidad
            if precio: self.productos[id].precio = precio
            print("Producto actualizado")
        else:
            print("No existe ese ID")

    def buscar(self, nombre):
        for p in self.productos.values():
            if p.nombre.lower() == nombre.lower():
                print('ID:', p.id, '-', 'Producto:', p.nombre, '-', 'Cantidad:', p.cantidad, '-', 'Precio:', p.precio, '$')
                return
        print("No se encontró ese producto")

    def mostrar(self):
        if not self.productos:
            print("Inventario vacío")
        else:
            for p in self.productos.values():
                print(p.id, p.nombre, p.cantidad, p.precio)

    def guardar(self, archivo="inventario.json"):
        datos = {id: p.__dict__ for id, p in self.productos.items()}
        with open(archivo, "w") as f:
            json.dump(datos, f)
        print("Inventario guardado")

    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                for id, p in datos.items():
                    self.productos[id] = Producto(p["id"], p["nombre"], p["cantidad"], p["precio"])
            print("Inventario cargado")
        except:
            print("No hay inventario guardado")

# Menú
def menu():
    inv = Inventario()
    inv.cargar()

    while True:
        print("\n1.Agregar  2.Eliminar  3.Actualizar  4.Buscar  5.Mostrar  6.Guardar  7.Salir")
        op = input("Opción: ")

        if op == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            inv.agregar(Producto(id, nombre, cant, prec))

        elif op == "2":
            inv.eliminar(input("ID a eliminar: "))

        elif op == "3":
            id = input("ID a actualizar: ")
            c = input("Nueva cantidad (Enter si no): ")
            p = input("Nuevo precio (Enter si no): ")
            inv.actualizar(id, int(c) if c else None, float(p) if p else None)

        elif op == "4":
            inv.buscar(input("Nombre a buscar: "))

        elif op == "5":
            inv.mostrar()

        elif op == "6":
            inv.guardar()

        elif op == "7":
            inv.guardar()
            print("Adiós")
            break

        else:
            print("Opción inválida")

# Programa principal
menu()