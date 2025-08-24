# Definicion de la clase producto
class Productos:
    #Inicializacion de los atributos
    def __init__(self, codigo_producto, nombre, cantidad, precio):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo_producto}, {self.nombre}, {self.cantidad}, {self.precio}"

#Archivo txt para guardar los productos
class Inventario:
    def __init__(self, archivo = "Inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_archivo()


    # Manejo de archivos

    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
            print("El inventario ha sido guardado correctamente.")

        #Uso de excepciones para evitar errores de consola
        except PermissionError:
            print("Error: Solicita primero los permisos correspondientes.")
        except Exception as e:
            print(f"Ha ocurrido un error..vuelve a intentarlo, {e}")

    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    codigo_producto,nombre,cantidad,precio = linea.strip().split(",")
                    self.productos.append(
                        Productos(codigo_producto, nombre, int(cantidad), float(precio))
                    )
            print("El inventario ha sido cargado correctamente.")
        except FileNotFoundError:
            print("El archivo no ha sido encontrado, se procerá a crear uno nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    #Operaciones
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_archivo()
        print(f"Producto: {producto.nombre}, agregado correctamente.")

    def actualizar(self, codigo_producto, nueva_cantidad = None, nuevo_precio = None):
        for p in self.productos:
            if str(p.codigo_producto).strip() == str(codigo_producto).strip():
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_archivo()
                print(f"Producto: {p.nombre}, actualizado.")
        print("Producto no encontrado.")

    def eliminar(self, codigo_producto):
        for p in self.productos:
            if str(p.codigo_producto).strip() == str(codigo_producto).strip():
                self.productos.remove(p)
                self.guardar_archivo()
                print(f"Producto {p.nombre}, eliminado.")
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n Iventario actual")
            for p in self.productos:
                print(f"{p.codigo_producto} - {p.nombre},"
                      f" Cantidad: {p.cantidad}, Precio: ${p.precio}")

    #Visualización del programa

def menu():
    inventario = Inventario()

    while True:
        print("\n ----Menú de inventario----")
        print("1. Agregar un producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            codigo_producto = int(input("Ingresa el código del producto: "))
            nombre = str(input("Ingrese el nombre del producto: "))
            cantidad = int(input("Ingrese la cantidad de producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(Productos(codigo_producto, nombre, cantidad, precio))

        elif opcion == 2:
            codigo_producto = int(input("Ingrese el código de producto a actualizar: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad de producto (Enter para no cambiar): "))
            nuevo_precio = float(input("Ingrese el nuevo precio del producto (Enter para no cambiar): "))

            inventario.actualizar(codigo_producto, int(nueva_cantidad) if nueva_cantidad else None, float(nuevo_precio) if nuevo_precio else None)

        elif opcion == 3:
            codigo_producto = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar(codigo_producto)

        elif opcion == 4:
            inventario.mostrar_inventario()

        elif opcion == 5:
            print("Saliendo del programa....")
            break

        else:
            print("Opción no valida.. Intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
