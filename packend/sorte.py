import random
import os
import sys
import time
import webbrowser

def abrir_janelas():
    url = [
         "https://www.google.com",
         "https://www.youtube.com",
         "https://www.wikipedia.org",
         "https://www.pr.senac.br",
         "https://animekai.com",
    ]
    for i in url:
         webbrowser.open(i)
def jogar():
    opcoes = 6
    escolhido = random.randint(1, opcoes)
    #campo de entreda de número
    try:
        escolha = int(input(f"Escolha um número entre 1 e {opcoes}"))
        if escolha < 1 or escolha > opcoes:
            raise ValueError("Número fora do intervalo permitido!")
    except ValueError as e:
        print("Entrada inválida",e)
        jogar()
    if escolha == escolhido:
        print("bye bye FDP🔞")
        abrir_janelas()
        time.sleep(5)
        if sys.platform == 'win32':
         os.system("shutdown /s /t 1")
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            os.system("shutdown now")
        elif sys.platform == 'darwin':
            os.system("sudo shutdown -h now")
    else:
        print("você esta seguro, por enquanto! 😁")

def menu_principal():
    print("""
    Regrasdo jogo:
    1. Você deve escolher um número entre 1 e 6.
    2. Se você acertaro PC será desligado!
    3. Ao escolher um número deferente, o jogo continuará
""")
          
def menu_principal():
    print("meno Principal")
    print("1.Iniciar Jogo")
    print("2.Ver regras")
    print("3.Sair")

    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        jogar()
    
menu_principal()
          
