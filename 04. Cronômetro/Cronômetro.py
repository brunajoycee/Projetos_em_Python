import tkinter as tk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Digital")

        self.rodando = False
        self.tempo = 0

        self.label = tk.Label(self.root, font=("Arial", 48), fg="white", bg="#1C1C1C", relief="solid", bd=2, text="00:00:00")
        self.label.pack(fill="both", expand=True)

        self.botao_frame = tk.Frame(self.root)
        self.botao_frame.pack(pady=20)

        self.botao_iniciar = tk.Button(self.botao_frame, text="Iniciar", command=self.iniciar, font=("Arial", 18), relief="solid", bd=2)
        self.botao_iniciar.grid(row=0, column=0, padx=(0, 20))

        self.botao_parar = tk.Button(self.botao_frame, text="Parar", command=self.parar, font=("Arial", 18), relief="solid", bd=2, state="disabled")
        self.botao_parar.grid(row=0, column=1)

        self.botao_resetar = tk.Button(self.botao_frame, text="Resetar", command=self.resetar, font=("Arial", 18), relief="solid", bd=2)
        self.botao_resetar.grid(row=0, column=2, padx=(20, 0))

        self.atualizar_tempo()

    def atualizar_tempo(self):
        if self.rodando:
            self.tempo += 1
            minutos = self.tempo // 60
            segundos = self.tempo % 60
            horas = minutos // 60
            minutos %= 60
            self.label.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
        self.root.after(1000, self.atualizar_tempo)

    def iniciar(self):
        self.rodando = True
        self.botao_iniciar.config(state="disabled")
        self.botao_parar.config(state="normal")

    def parar(self):
        self.rodando = False
        self.botao_iniciar.config(state="normal")
        self.botao_parar.config(state="disabled")

    def resetar(self):
        self.rodando = False
        self.tempo = 0
        self.label.config(text="00:00:00")
        self.botao_iniciar.config(state="normal")
        self.botao_parar.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
