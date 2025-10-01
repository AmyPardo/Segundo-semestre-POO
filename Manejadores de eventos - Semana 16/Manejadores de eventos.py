import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("420x420")
        self.root.config(bg="lightpink")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.focus()

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        add_button = tk.Button(button_frame, text="Añadir", command=self.add_task, bg="#E6E6FA")
        add_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(button_frame, text="Completar", command=self.complete_task, bg="#b9ffff")
        complete_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_task, bg="#d8af97")
        delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Lista paralela para estados (False = pendiente, True = completada)
        self.tasks_states = []

        # Atajos de teclado
        # Enter en el entry -> añadir
        self.task_entry.bind('<Return>', self.add_task)

        # Atajos SOLO cuando la listbox tiene foco
        self.task_listbox.bind('<Key-c>', self.complete_task)
        self.task_listbox.bind('<Key-C>', self.complete_task)
        self.task_listbox.bind('<Key-d>', self.delete_task)
        self.task_listbox.bind('<Key-D>', self.delete_task)
        self.task_listbox.bind('<Delete>', self.delete_task)

        # Escape para cerrar (desde cualquier widget)
        self.root.bind('<Escape>', lambda event: self.close_app())

        # Al hacer clic en la lista, darle foco (útil si el usuario usa el ratón)
        self.task_listbox.bind('<Button-1>', lambda e: self.task_listbox.focus_set())

    def add_task(self, event=None):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")
            return
        self.task_listbox.insert(tk.END, task_text)
        self.tasks_states.append(False)  # pendiente
        self.task_entry.delete(0, tk.END)
        # opcional: devolver foco al entry para seguir escribiendo
        self.task_entry.focus_set()

    def complete_task(self, event=None):
        focused = self.root.focus_get()
        sel = self.task_listbox.curselection()
        # Si no hay selección:
        if not sel:
            # Mostrar aviso sólo si la lista tiene el foco
            if focused == self.task_listbox:
                messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")
            return

        idx = sel[0]
        if not self.tasks_states[idx]:
            original = self.task_listbox.get(idx)
            self.tasks_states[idx] = True
            self.task_listbox.delete(idx)
            self.task_listbox.insert(idx, f"✔ {original}")
            self.task_listbox.itemconfig(idx, fg="green")
            # mantener selección en ese índice
            self.task_listbox.selection_set(idx)
            self.task_listbox.activate(idx)
        else:
            messagebox.showinfo("Info", "La tarea ya está completada.")

    def delete_task(self, event=None):
        focused = self.root.focus_get()
        sel = self.task_listbox.curselection()
        if not sel:
            if focused == self.task_listbox:
                messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")
            return

        idx = sel[0]
        del self.tasks_states[idx]
        self.task_listbox.delete(idx)

    def close_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()