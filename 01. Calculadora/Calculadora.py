from tkinter import *
from tkinter import ttk

cor_branca = "#FFFFFF"
cor_cinza_claro = "#FFFAFA"
cor_preto = "#000000"
cor_preto_escuro = "#1C1C1C"
fundo_branco = "#FFFAFA"
fundo_preto_escuro = "#1C1C1C"

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.configure(bg=fundo_branco)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_tela = Frame(janela, width=300, height=56, bg=cor_cinza_claro, pady=0, padx=0, relief="flat")
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo_branco, pady=0, padx=0, relief="flat")
frame_quadros.grid(row=2, column=0, sticky=NW)

valor_texto = StringVar()
app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg=fundo_preto_escuro, fg=cor_branca)
app_tela.place(x=0, y=0)

todos_valores = ""

def entrar_valor(evento):
    global todos_valores
    todos_valores += str(evento)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = ""
    except:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")

botao_limpar = Button(frame_quadros, command=limpar_tela, text="C", width=11, height=2, bg=cor_preto, fg=fundo_branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_limpar.place(x=0, y=0)
botao_porcentagem = Button(frame_quadros, command=lambda: entrar_valor('%'), text="%", width=5, height=2, bg=cor_preto, fg=fundo_branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_porcentagem.place(x=118, y=0)
botao_divisao = Button(frame_quadros, command=lambda: entrar_valor('/'), text="/", width=5, height=2, bg=cor_preto_escuro, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_divisao.place(x=177, y=0)

botoes = [
    ('7', 0, 52), ('8', 59, 52), ('9', 118, 52), ('*', 177, 52),
    ('4', 0, 104), ('5', 59, 104), ('6', 118, 104), ('-', 177, 104),
    ('1', 0, 156), ('2', 59, 156), ('3', 118, 156), ('+', 177, 156),
    ('0', 0, 208), ('.', 118, 208), ('=', 177, 208)
]

for (texto, x, y) in botoes:
    if texto == '=':
        botao = Button(frame_quadros, command=calcular, text=texto, width=5, height=2, bg=cor_preto_escuro, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    else:
        largura = 5 if texto != '0' else 11
        cor_fundo = cor_preto if texto not in '*/-+=' else cor_preto_escuro
        cor_texto = fundo_branco if texto not in '*/-+=' else cor_branca
        botao = Button(frame_quadros, command=lambda t=texto: entrar_valor(t), text=texto, width=largura, height=2, bg=cor_fundo, fg=cor_texto, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    botao.place(x=x, y=y)

janela.mainloop()
