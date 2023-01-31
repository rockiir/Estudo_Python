"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


# jogo de adivinhação de palavra secreta

palavra_secreta = "banana"
letras_descobertas = ["*" for i in range(len(palavra_secreta))]
num_tentativas = 0
max_tentativas = 3


print("Bem vindo ao jogo de adivinhação de palavra secreta!")

while "*" in letras_descobertas:
    letra = input("Digite uma letra: ")
    letra = letra.lower()
    
    if len(letra) >  1:
        print('Digite apenas uma letra')
        continue
    
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
        print("".join(letras_descobertas))
    else:
        num_tentativas += 1
        print("*")
        
    if num_tentativas == max_tentativas:
        print(f"Você atingiu o limite de { max_tentativas }  tentativas!")
        break

print("Fim do jogo!")


#resolução

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

