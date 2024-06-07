import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")
        self.master.configure(bg="#f0f0f0")

        self.font_style = ("Arial", 12)
        self.button_bg = "#1C1C1C"
        self.button_fg = "white"
        self.entry_bg = "white"

        self.title_label = tk.Label(master, text="Lista de Tarefas", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        self.title_label.grid(row=0, column=0, columnspan=5, pady=(20, 10))

        self.label_task = tk.Label(master, text="Tarefa:", font=self.font_style, bg="#f0f0f0")
        self.label_task.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_task = tk.Entry(master, width=30, font=self.font_style, bg=self.entry_bg)
        self.entry_task.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_date = tk.Label(master, text="Data:", font=self.font_style, bg="#f0f0f0")
        self.label_date.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        self.entry_date = tk.Entry(master, width=15, font=self.font_style, bg=self.entry_bg)
        self.entry_date.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.label_status = tk.Label(master, text="Status:", font=self.font_style, bg="#f0f0f0")
        self.label_status.grid(row=1, column=4, padx=10, pady=5, sticky="w")

        self.status_options = ["Não iniciado", "Em andamento", "Concluído"]
        self.selected_status = tk.StringVar(master)
        self.selected_status.set(self.status_options[0])

        self.status_menu = tk.OptionMenu(master, self.selected_status, *self.status_options)
        self.status_menu.config(width=12, font=self.font_style)
        self.status_menu.grid(row=1, column=5, padx=10, pady=5, sticky="w")

        self.add_button = tk.Button(master, text="Adicionar", command=self.add_task, bg=self.button_bg, fg=self.button_fg, font=self.font_style)
        self.add_button.grid(row=1, column=6, padx=10, pady=5, sticky="we")

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.grid(row=2, column=6, rowspan=3, sticky="ns")
        self.task_list = tk.Listbox(master, width=50, height=10, yscrollcommand=self.scrollbar.set, font=self.font_style, bg=self.entry_bg)
        self.task_list.grid(row=2, column=0, columnspan=6, padx=10, pady=5)
        self.scrollbar.config(command=self.task_list.yview)

        self.remove_button = tk.Button(master, text="Remover Selecionado", command=self.remove_task, bg=self.button_bg, fg=self.button_fg, font=self.font_style)
        self.remove_button.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="we")

    def add_task(self):
        task = self.entry_task.get().strip()
        date = self.entry_date.get().strip()
        status = self.selected_status.get()
        if task and date:
            task_with_date = f"{date} - {task} ({status})"
            self.task_list.insert(tk.END, task_with_date)
            self.entry_task.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha tanto a tarefa quanto a data.")

    def remove_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
