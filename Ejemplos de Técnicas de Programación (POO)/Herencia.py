class CuentaVentas:
    def __init__(self):
        self.__ventas = []

    def agregar(self, cant):
        self.__ventas.append(cant)

class CuentaVentasOnline(CuentaVentas):
    def mostrar(self):
        for v in self._CuentaVentas__ventas:
            print("Venta online $", v)

o = CuentaVentasOnline()
o.agregar(300)
o.mostrar()
