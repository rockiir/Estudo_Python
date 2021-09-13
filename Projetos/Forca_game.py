secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra =input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ah isso não vale digite a proxima letra')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhul a letra"{letra}" existe')
    else:
        print(f'Aff a letra"{letra}" não existe na palavra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'QUe legal voce GANHOU!! a palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavre secreta está assim {secreto_temporario}')

    print(secreto_temporario)

    if letra not in secreto:
        chances -= 1

    print(f'voce ainda tem {chances} chances')



