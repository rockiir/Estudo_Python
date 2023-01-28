"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um numero inteiro ")
if isinstance(numero, int):
    if (numero%2) == 0:
        print("Par")
    else:
        print("Ímpar")
else:
    print("não é um numero inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora em números inteiros: ')

try:
    hora = int(hora)

    if hora <= 11:
        print("Bom dia")
    elif 17 >= hora >= 12:
        print("Boa tarde")
    else:
        print("Boa noite")

except:
    print("Por favor, digite apenas números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome ")
tamanho=len(nome)
if tamanho <= 4:
    print("Seu nome é curto")
elif 5 <= tamanho <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande.")







