class Venta:
    def __init__(self, cant):
        self.cant = cant

    def mostrar(self):
        print("Venta $", self.cant)

v = Venta(100)
v.mostrar()
