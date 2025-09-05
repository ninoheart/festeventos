# Entrada de dados
peso = float(input("Insira o peso (kg): "))
altura = float(input("Insira a altura (m): "))
sexo = input("Insira o sexo: M - para masculino e F para Feminino ")

# Processamento de dados
imc = peso / (altura * altura)

# Saída
print("O IMC calculado é:", imc)
if(sexo == "M" or sexo == "m" or sexo ==  "masculino" ):
    print("Imc Masculino")
elif(sexo == "F" or sexo == "f" or sexo == "feminino" ):
    print("Imc Feminino")
else:
    print("Outro")

# Classificação do IMC
if imc < 18.5:
    print("Abaixo do peso!")
elif imc <= 24.9:
    print("Peso normal.")
elif imc <= 29.9:
    print("Sobrepeso.")
elif imc <= 34.9:
    print("Obesidade grau I.")
elif imc <= 39.9:
    print("Obesidade grau II.")
else:
    print("Obesidade grau III (mórbida).")
