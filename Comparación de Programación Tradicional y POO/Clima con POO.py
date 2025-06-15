# Clase para el clima semanal
class ClimaSemana:
    def __init__(self):
        # Nuevas temperaturas semanales
        self.__temperaturas = [19.3, 20.1, 18.7, 21.0, 20.5, 19.8, 22.2]

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"Temperatura promedio: {promedio:.2f}°C")

# Clase hija para funcionalidad extra
class ClimaSemanaAvanzado(ClimaSemana):
    def temperatura_minima(self):
        return min(self._ClimaSemana__temperaturas)

# Función principal
def main():
    print("=== Reporte del Clima en Quito (POO) ===")
    clima = ClimaSemana()
    clima.mostrar_promedio()

main()