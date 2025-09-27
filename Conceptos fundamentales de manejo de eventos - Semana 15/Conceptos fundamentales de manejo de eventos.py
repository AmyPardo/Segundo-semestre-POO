import tkinter as tk
from tkinter import messagebox

# Aplicación Lista de Tareas (To-Do List)

def agregar_tarea(event=None):
    """Agrega una nueva tarea a la lista."""
    tarea = entrada_tarea.get().strip()
    if tarea:  # Solo agrega si no está vacío
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Por favor escribe una tarea.")

def marcar_completada():
    """Marca la tarea seleccionada como completada cambiando su estilo."""
    try:
        index = lista_tareas.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        tarea = lista_tareas.get(index)

        # Si ya está marcada como completada, la dejamos igual
        if tarea.startswith("[Tarea realizada] "):
            messagebox.showinfo("Ya completada", "Esa tarea ya está marcada como completada.")
        else:
            lista_tareas.delete(index)
            lista_tareas.insert(index, "[Tarea realizada] " + tarea)  # Añade un prefijo para mostrar completada
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea para marcarla como completada.")

def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea para eliminar.")

def marcar_doble_click(event):
    """Evento opcional: Doble clic en una tarea la marca como completada."""
    marcar_completada()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")
ventana.config(bg="#f5f5f5")

# Widgets principales

# Entrada de texto
entrada_tarea = tk.Entry(ventana, width=30, font=("Arial", 12))
entrada_tarea.pack(pady=10)

# Botones
frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea, bg="#90caf9")
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada, bg="#D1AAF4")
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea, bg="beige")
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Eventos
entrada_tarea.bind("<Return>", agregar_tarea)  # Enter agrega la tarea
lista_tareas.bind("<Double-Button-1>", marcar_doble_click)  # Doble clic marca como completada

# Bucle principal
ventana.mainloop()