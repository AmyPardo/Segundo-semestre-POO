# El usuario ingresa la temperatura en Celsius y el programa muestra el resultado en Fahrenheit

def convertir_a_fahrenheit(celsius):
    # Fórmula: F = (C * 9/5) + 32
    return (celsius * 9 / 5) + 32


# Pedimos la temperatura al usuario
temperatura_ingresada = input("Ingresa la temperatura en grados Celsius: ")

# Usamos una variable booleana para validar
entrada_valida = True

try:
    temperatura_celsius = float(temperatura_ingresada)

except ValueError:
    print("Debes ingresar un número válido.")
    entrada_valida = False

# Si todo está bien, hacemos la conversión
if entrada_valida:
    temperatura_fahrenheit = convertir_a_fahrenheit(temperatura_celsius)
    print(f"{temperatura_celsius}°C equivale a {temperatura_fahrenheit:.2f}°F")