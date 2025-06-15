# Función con temperaturas distintas
def ingresar_temperaturas():
    return [10.2, 20.1, 18.7, 25.0, 20.5, 19.8, 22.2]  # Datos de una semana diferente

# Calcula el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("=== Promedio Climático Semanal de Quito ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"Temperatura promedio: {promedio:.2f}°C")

main()
