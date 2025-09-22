
import tkinter as tk
from tkinter import ttk, messagebox

# Intentamos usar DateEntry de tkcalendar, si no está instalado usamos un Entry
try:
    from tkcalendar import DateEntry
    TIENE_CALENDARIO = True
except:
    TIENE_CALENDARIO = False

class Agenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x500")  # tamaño inicial normal
        self.root.configure(bg='pink')

        # -------- Frame lista de eventos ----------
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(side="left", fill="both", expand=True)

        # Scroll
        scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")

        # -------- Frame de inputs ----------
        frame_inputs = tk.Frame(root)
        frame_inputs.pack(pady=10)

        # Fecha
        tk.Label(frame_inputs, text="Fecha YYYY-MM-DD:").grid(row=0, column=0, padx=5, pady=5)
        if TIENE_CALENDARIO:
            self.entry_fecha = DateEntry(frame_inputs, date_pattern="yyyy-mm-dd")
        else:
            self.entry_fecha = tk.Entry(frame_inputs)

        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_inputs, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_inputs)
        self.entry_hora.insert(0, "08:00")
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(frame_inputs, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(frame_inputs, width=60)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # -------- Frame de botones ----------
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=10)
        tk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_evento).pack(side="left", padx=10)

        tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="left", padx=10)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        desc = self.entry_desc.get()

        if fecha == "" or hora == "" or desc == "":
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos")
            return

        self.tree.insert("", "end", values=(fecha, hora, desc))
        self.entry_hora.delete(0, "end")
        self.entry_desc.delete(0, "end")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Nada seleccionado", "Primero selecciona un evento")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento?")
        if confirmar:
            for item in seleccionado:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = Agenda(root)
    root.mainloop()