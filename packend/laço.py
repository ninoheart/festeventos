import random

#lista
#              0          1            2         3       4
salgados = [
            "Risoles", "Cola cola", "Coxinha", "kibe", "Suco",
             "Bolo", "mini-churros", "Pão de mel", "Donuts", "Cachorro-quente"]

print(salgados[2]) #coxinha
print("O sorteado foi: ", random.choices(salgados))

#imprimindo todos salgados
#imprima no intervalo do tamanho(len) da lista de salgados
for posicao in range(len(salgados)):
    print(posicao, " - ", salgados[posicao])

contador = 0
while contador < 19:
    print("O Rafael")
    contador = contador + 1

def listar():
    for posicao in range(len(salgados)):
        print(posicao, " _ ", salgados[posicao])

opcao = 0  
while opcao !=3:
        opcao =int(input("Insira a opcao:"))

        if opcao == 1:
            #Efetuando entrada de dados na lista
            item = input("Digite um item para adicionar na lista")
            salgados.append(item)
            listar()
        elif opcao == 2:
            #Removendo item da lista
            item = input("Digite o item que dejeja remover da lista")
            salgados.remove(item)
            listar()
        if opcao == 4:
            listar()
        if opcao == 5:
            break

#listar










