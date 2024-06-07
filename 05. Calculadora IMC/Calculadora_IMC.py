import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora IMC")
        self.root.configure(bg="#f0f0f0")

        self.label_titulo = tk.Label(root, text="Calculadora IMC", font=("Helvetica", 16, "bold"), bg="#1C1C1C", fg="white")
        self.label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="we")

        self.frame_inputs = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.frame_inputs.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.label_altura = tk.Label(self.frame_inputs, text="Altura (m):", bg="#f0f0f0")
        self.label_peso = tk.Label(self.frame_inputs, text="Peso (kg):", bg="#f0f0f0")
        self.entry_altura = tk.Entry(self.frame_inputs)
        self.entry_peso = tk.Entry(self.frame_inputs)

        self.label_altura.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.label_peso.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_altura.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.entry_peso.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.button_calcular = tk.Button(root, text="Calcular IMC", command=self.calcular_imc, bg="#1C1C1C", fg="white")
        self.button_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="we")

        self.frame_resultado = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.frame_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="we")

        self.label_resultado = tk.Label(self.frame_resultado, text="Resultado:", bg="#f0f0f0")
        self.label_resultado.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_categoria = tk.Label(self.frame_resultado, text="", bg="#f0f0f0")
        self.label_categoria.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    def calcular_imc(self):
        try:
            altura = float(self.entry_altura.get())
            peso = float(self.entry_peso.get())

            if altura <= 0 or peso <= 0:
                raise ValueError("Altura e peso devem ser valores positivos.")

            imc = peso / (altura ** 2)
            self.label_resultado.config(text=f"Resultado: {imc:.2f}")
            self.mostrar_categoria_imc(imc)

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            self.label_resultado.config(text="Resultado:")

    def mostrar_categoria_imc(self, imc):
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            categoria = "Peso normal"
        elif 25 <= imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"

        self.label_categoria.config(text=f"Categoria: {categoria}")

if __name__ == "__main__":
    raiz = tk.Tk()
    app = CalculadoraIMC(raiz)
    raiz.mainloop()
