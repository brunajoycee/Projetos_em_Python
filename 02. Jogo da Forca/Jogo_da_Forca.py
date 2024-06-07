import tkinter as tk
from tkinter import messagebox
import random

class ForcaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")

        self.palavra = self.escolher_palavra()
        self.palavra_oculta = ["_"] * len(self.palavra)
        self.tentativas = 0
        self.max_tentativas = 6
        self.letras_tentadas = []

        self.frame_forca = tk.Frame(master)
        self.frame_forca.pack(pady=20)

        self.label_dica = tk.Label(self.frame_forca, text="Dica: Fruta", font=("Arial", 16))
        self.label_dica.pack()

        self.label_num_letras = tk.Label(self.frame_forca, text=f"Número de letras: {len(self.palavra)}", font=("Arial", 16))
        self.label_num_letras.pack()

        self.label_forca = tk.Label(self.frame_forca, text=self.exibir_forca(), font=("Courier New", 28))
        self.label_forca.pack()

        self.label_palavra = tk.Label(master, text=" ".join(self.palavra_oculta), font=("Arial", 24))
        self.label_palavra.pack()

        self.entry_letra = tk.Entry(master, font=("Arial", 18))
        self.entry_letra.pack(pady=10)

        self.botao_tentar = tk.Button(master, text="Tentar", command=self.tentar, font=("Arial", 18), bg="#1C1C1C", fg="white")
        self.botao_tentar.pack(pady=10)

    def escolher_palavra(self):
        palavras = ["Abacate", "Acerola", "Abacaxi", "Banana", "Carambola"]
        return random.choice(palavras)

    def exibir_forca(self):
        estagios = [
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            """,
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            """
        ]
        return estagios[self.tentativas]

    def tentar(self):
        letra = self.entry_letra.get().lower()

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showinfo("Atenção", "Por favor, insira apenas uma letra.")
            return

        if letra in self.letras_tentadas:
            messagebox.showinfo("Atenção", f"Você já tentou a letra '{letra}'. Tente outra.")
            self.entry_letra.delete(0, tk.END)
            return

        self.letras_tentadas.append(letra)

        if letra in self.palavra.lower():
            for i in range(len(self.palavra)):
                if self.palavra.lower()[i] == letra:
                    self.palavra_oculta[i] = self.palavra[i]
            self.label_palavra.config(text=" ".join(self.palavra_oculta))
            if "_" not in self.palavra_oculta:
                messagebox.showinfo("Parabéns!", "Você ganhou!")
                self.novo_jogo()
        else:
            self.tentativas += 1
            if self.tentativas == self.max_tentativas:
                messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era '{self.palavra}'.")
                self.novo_jogo()
            else:
                messagebox.showinfo("Ops!", "Letra errada.")
                self.label_forca.config(text=self.exibir_forca())

        self.entry_letra.delete(0, tk.END)

    def novo_jogo(self):
        resposta = messagebox.askquestion("Novo Jogo", "Deseja iniciar um novo jogo?")
        if resposta == "yes":
            self.master.destroy()
            main()
        else:
            self.master.destroy()

def main():
    root = tk.Tk()
    
    label_welcome = tk.Label(root, text="Bem-vindo ao Jogo da Forca!", font=("Arial", 22))
    label_welcome.pack(pady=20)

    botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=lambda: iniciar_jogo(root), font=("Arial", 18), bg="#1C1C1C", fg="white")
    botao_iniciar.pack(pady=10)

    root.mainloop()

def iniciar_jogo(root):
    root.destroy()
    root = tk.Tk()
    app = ForcaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
