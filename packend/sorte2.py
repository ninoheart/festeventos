#importação debiblioteca que manipula janelas
import tkinter as tk
from tkinter import messagebox
#importação de biblioteca de sorteio
import random
#importação de biblioteca que manipula o computador
import os
#importação que verifica o tipo de s.o
import sys
#importação de bilbioteca que manipula o tempo
import time

#criando lista de sites
urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.reddit.org",
    "https://www.pr.senac.br",
]
#função para abrir navegador
def abrir_navegador():
    #loop que vai percorrer cada um dos sites da lista
    for url in urls:
        #abril novegador
        webbrowser.open(url)
        time.slwwp(2)

def jogar():
    #sorteia um número aleatório de 1 a 6
    sorteado = random.randint(1,6)


    def verificar_escolha(numero):
        if numero == sorteado:
            messagebox.shiwerror("Perdeu", "o computados será desligado!😶‍🌫️")
        else:
            messagebox.showinfo("Ufal", "Voçê está seguro por enquanto!🤑")
            jogar()
    janela = tk.Toplevel()
    janela.title("Escolhs um número")


#inicio de Janela principal
root = tk.Tk()
root.title("Jogo do Sorteio")
#define altura e largura da janela
root.geometry(f"{500}x{500}")
tk.Label(root, text="Seja bem-vindo!", font=("Arial", 14)).pack(pady=15)
#botões do menu
tk.Button(root, text="Iniar Jogo", width=20, command=jogar).pack(pady=10)
tk.Button(root, text="Ver Regras", width=20, command=jogar).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=jogar).pack(pady=10)

root.mainloop()
    

