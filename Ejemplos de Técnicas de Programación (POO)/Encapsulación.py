class CuentaVentas:
    def __init__(self):
        self.__ventas = []

    def agregar(self, cant):
        self.__ventas.append(cant)

    def promedio(self):
        return sum(self.__ventas) / len(self.__ventas)

    def mostrar(self):
        for v in self.__ventas:
            print("$", v)

c = CuentaVentas()
c.agregar(200)
c.agregar(150)
c.mostrar()
print("Promedio:", c.promedio())
