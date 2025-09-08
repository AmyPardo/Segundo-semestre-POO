# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # titulo y autor no cambian
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} ({self.categoria}, ISBN:{self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # aquí van los libros que tiene el usuario
    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # isbn -> libro
        self.usuarios = {}  # id -> usuario
        self.ids = set()  # para que no se repitan los ids

    # añadir libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Ese libro ya estaba guardado.")
        else:
            self.libros[libro.isbn] = libro
            print("Libro agregado.")

    # quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            self.libros.pop(isbn)
            print("Libro eliminado.")
        else:
            print("No se encontró el libro.")

    # registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids:
            print("Ese usuario ya existe.")
        else:
            self.ids.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print("Usuario registrado.")

    # dar de baja usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids:
            self.ids.remove(id_usuario)
            self.usuarios.pop(id_usuario)
            print("Usuario eliminado.")
        else:
            print("No existe ese usuario.")

    # prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids:
            print("Ese usuario no está registrado.")
            return
        if isbn not in self.libros:
            print("El libro no está disponible.")
            return
        libro = self.libros.pop(isbn)
        self.usuarios[id_usuario].libros_prestados.append(libro)
        print(f"Se prestó el libro {libro.info[0]} a {self.usuarios[id_usuario].nombre}.")

    # devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.ids:
            print("Ese usuario no está registrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print("Libro devuelto.")
                return
        print("Ese usuario no tenía ese libro.")

    # buscar libro
    def buscar_libro(self, tipo, valor):
        encontrados = []
        for libro in self.libros.values():
            if (tipo == "titulo" and valor.lower() in libro.info[0].lower()) or \
                    (tipo == "autor" and valor.lower() in libro.info[1].lower()) or \
                    (tipo == "categoria" and valor.lower() in libro.categoria.lower()):
                encontrados.append(libro)
        if encontrados:
            print("Se encontraron estos libros:")
            for l in encontrados:
                print(l)
        else:
            print("No se encontró nada.")

    # listar libros prestados
    def listar_prestados(self, id_usuario):
        if id_usuario not in self.ids:
            print("Ese usuario no existe.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for l in usuario.libros_prestados:
                print(l)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")

#MENÚ INTERACTIVO
def menu():
    biblio = Biblioteca()
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        op = input("Elige una opción: ")

        if op == "1":
            t = input("Título: ")
            a = input("Autor: ")
            c = input("Categoría: ")
            i = input("ISBN: ")
            biblio.agregar_libro(Libro(t, a, c, i))

        elif op == "2":
            i = input("ISBN del libro a quitar: ")
            biblio.quitar_libro(i)

        elif op == "3":
            n = input("Nombre: ")
            idu = input("ID: ")
            biblio.registrar_usuario(Usuario(n, idu))

        elif op == "4":
            idu = input("ID del usuario: ")
            biblio.dar_baja_usuario(idu)

        elif op == "5":
            idu = input("ID del usuario: ")
            i = input("ISBN del libro: ")
            biblio.prestar_libro(idu, i)

        elif op == "6":
            idu = input("ID del usuario: ")
            i = input("ISBN del libro: ")
            biblio.devolver_libro(idu, i)

        elif op == "7":
            tipo = input("¿Por que opcion quiere buscar el libro? (titulo/autor/categoria): ")
            val = input("Introduzca el (titulo/autor/categoria): ")
            biblio.buscar_libro(tipo, val)

        elif op == "8":
            idu = input("ID del usuario: ")
            biblio.listar_prestados(idu)

        elif op == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# correr el programa
if __name__ == "__main__":
    menu()