import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Ejemplos de Técnicas de Programación (POO)/Abstracción.py',
             '1.1':'Ejemplos de Técnicas de Programación (POO)/Encapsulación.py',
             '1.2': 'Ejemplos de Técnicas de Programación (POO)/Herencia.py',
             '1.3': 'Ejemplos de Técnicas de Programación (POO)/Polimorfismo.py',
        '2': 'Comparación de Programación Tradicional y POO/Clima con POO.py',
             '2.1': 'Comparación de Programación Tradicional y POO/Clima con programacion tradicional.py',
        '3': 'EjemplosMundoReal_POO/POO.py',
        '4': 'Calculo_temperaturas/Calculo de temperaturas - semana 5.py',
        '5': 'Clases_Semana_6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Constructores y Destructores - Deber semana 7/Constructores y destructores.py',
        '7': 'Sistema de Gestión de Inventarios Semana 9/Sistema de Gestión de Inventarios.py',
        '8': 'Fundamentos de colecciones - Semana 11/Fundamentos de colecciones.py'
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()