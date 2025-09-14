import tkinter as tk
from tkinter import messagebox

# Aplicación GUI Básica con Tkinter

# Función para agregar datos a la lista
def agregar():
    dato = entrada.get()  # Obtener el texto ingresado
    if dato.strip():  # Verificar que no esté vacío
        lista.insert(tk.END, dato)  # Insertar al final de la lista
        entrada.delete(0, tk.END)   # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar un campo vacío.")

# Función para limpiar selección o lista
def limpiar():
    seleccion = lista.curselection()  # Obtener elemento seleccionado
    if seleccion:  # Si hay uno seleccionado
        lista.delete(seleccion)
    else:  # Si no hay selección, limpiar toda la lista
        lista.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica - Gestión de Datos")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Componentes GUI

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón Agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar, bg="pink", fg="white", font=("Arial", 11))
btn_agregar.pack(pady=5)

# Lista para mostrar los datos
lista = tk.Listbox(ventana, width=40, height=8, font=("Arial", 11))
lista.pack(pady=10)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="purple", fg="white", font=("Arial", 11))
btn_limpiar.pack(pady=5)

# Bucle principal
ventana.mainloop()