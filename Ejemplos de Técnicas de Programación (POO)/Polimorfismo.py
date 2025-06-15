class CuentaVentas:
    def __init__(self):
        self.__ventas = []

    def agregar(self, cant):
        self.__ventas.append(cant)

class Tienda(CuentaVentas):
    def mostrar(self):
        print("Tienda:")
        for v in self._CuentaVentas__ventas:
            print("$", v)

class Online(CuentaVentas):
    def mostrar(self):
        print("Online:")
        for v in self._CuentaVentas__ventas:
            print("$", v)

def mostrar(c):
    c.mostrar()

t = Tienda()
t.agregar(100)
t.agregar(200)

o = Online()
o.agregar(300)
o.agregar(400)

mostrar(t)
mostrar(o)