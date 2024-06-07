import tkinter as tk
from tkinter import messagebox

class AgendaTelefonicaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Agenda Telefônica")
        self.master.configure(bg="#f0f0f0")

        self.font_style = ("Arial", 12)
        self.button_bg = "#363636"
        self.button_fg = "white"
        self.entry_bg = "white"
        self.gray_bg = "#333333"

        self.title_label = tk.Label(master, text="Agenda Telefônica", font=("Helvetica", 24, "bold"), bg=self.gray_bg, fg="white")
        self.title_label.grid(row=0, column=0, columnspan=5, pady=(20, 10), sticky="we")

        self.label_nome = tk.Label(master, text="Nome:", font=self.font_style, bg="#f0f0f0")
        self.label_nome.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_nome = tk.Entry(master, width=30, font=self.font_style, bg=self.entry_bg)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_telefone = tk.Label(master, text="Telefone:", font=self.font_style, bg="#f0f0f0")
        self.label_telefone.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        self.entry_telefone = tk.Entry(master, width=15, font=self.font_style, bg=self.entry_bg)
        self.entry_telefone.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.add_button = tk.Button(master, text="Adicionar Contato", command=self.add_contact, bg=self.button_bg, fg=self.button_fg, font=self.font_style)
        self.add_button.grid(row=1, column=4, padx=10, pady=5, sticky="we")

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.grid(row=2, column=4, rowspan=5, sticky="ns")

        self.contact_list = tk.Listbox(master, width=50, height=10, yscrollcommand=self.scrollbar.set, font=self.font_style, bg=self.entry_bg)
        self.contact_list.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
        self.scrollbar.config(command=self.contact_list.yview)

        self.remove_button = tk.Button(master, text="Remover Selecionado", command=self.remove_contact, bg=self.button_bg, fg=self.button_fg, font=self.font_style)
        self.remove_button.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="we")

        self.search_entry = tk.Entry(master, width=30, font=self.font_style, bg=self.entry_bg)
        self.search_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="we")

        self.search_button = tk.Button(master, text="Pesquisar Contato", command=self.search_contact, bg=self.button_bg, fg=self.button_fg, font=self.font_style)
        self.search_button.grid(row=4, column=0, padx=10, pady=5, sticky="we")

        self.contacts = []

    def add_contact(self):
        nome = self.entry_nome.get().strip()
        telefone = self.entry_telefone.get().strip()
        if nome and telefone:
            contato = f"{nome} - {telefone}"
            self.contacts.append(contato)
            self.contact_list.insert(tk.END, contato)
            self.entry_nome.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha tanto o nome quanto o telefone.")

    def remove_contact(self):
        try:
            index = self.contact_list.curselection()[0]
            del self.contacts[index]
            self.contact_list.delete(index)
        except IndexError:
            messagebox.showwarning("Atenção", "Por favor, selecione um contato para remover.")

    def search_contact(self):
        termo = self.search_entry.get().strip()
        if termo:
            self.contact_list.delete(0, tk.END)
            for contato in self.contacts:
                if termo.lower() in contato.lower():
                    self.contact_list.insert(tk.END, contato)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaTelefonicaApp(root)
    root.mainloop()
