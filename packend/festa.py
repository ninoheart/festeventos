idade = 17
#booleano - tipo de dado que pode ser Verdadeiro ou falso
estudante = True
temConvite = False

#Pode enrtrar
#Se a pessoa tem mais de 17 anos e tem convite
#Ou se a pessoa é menos de 18 anos e é estudante

if(idade >= 17 and temConvite) or (idade < 18 and estudante):
    print("Pode entrar 🔞")
else:
    print("Não pode entrar! 😒")