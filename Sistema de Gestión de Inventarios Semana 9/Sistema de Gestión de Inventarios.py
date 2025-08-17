# Esta clase es para los productos
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # aquí guardamos los datos del producto
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        # cuando imprimimos el producto se ve así
        return f"{self.id} - {self.nombre} - {self.cantidad}unidades - ${self.precio}"

# Esta clase es para manejar todo el inventario
class Inventario:
    def __init__(self):
        self.productos=[]  # aquí se guardan todos los productos

    # agregar producto
    def agregar(self, producto):
        # verificamos que no se repita el ID
        if any(p.id==producto.id for p in self.productos):
            print("ID repetido")
        else:
            self.productos.append(producto)
            print("Agregado")

    # eliminar producto
    def eliminar(self, id_producto):
        for producto in self.productos:
            if producto.id==id_producto:
                self.productos.remove(producto)
                print("Eliminado")
                return
        print("No encontrado")

    # actualizar cantidad o precio
    def actualizar(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id==id_producto:
                if nueva_cantidad!=None: producto.cantidad=nueva_cantidad
                if nuevo_precio!=None: producto.precio=nuevo_precio
                print("Actualizado")
                return
        print("No encontrado")

    # buscar producto por nombre (puede ser parcial)
    def buscar(self, nombre):
        resultados=[p for p in self.productos if nombre.lower() in p.nombre.lower()]
        print(*resultados if resultados else ["No encontrado"], sep="\n")

    # mostrar todos los productos
    def mostrar(self):
        print(*self.productos if self.productos else ["Inventario vacío"], sep="\n")

# Menú para que el usuario pueda usar el sistema
def menu():
    inventario=Inventario()
    while True:
        print('\n1.Agregar','\n2.Eliminar' '\n3.Actualizar' '\n4.Buscar' '\n5.Mostrar' '\n6.Salir')
        opcion=input("Opción: ")
        if opcion=="1":
            # pedimos los datos del producto
            producto=Producto(input("ID: "), input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: ")))
            inventario.agregar(producto)
        elif opcion=="2":
            inventario.eliminar(input("ID: "))
        elif opcion=="3":
            # si el usuario no escribe nada en cantidad o precio, no cambia
            id_producto=input("ID: ")
            cantidad=input("Cantidad: ")
            precio=input("Precio: ")
            inventario.actualizar(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion=="4":
            inventario.buscar(input("Nombre: "))
        elif opcion=="5":
            inventario.mostrar()
        elif opcion=="6":
            break
        else:
            print("Inválido")

# aquí se ejecuta el programa
menu()