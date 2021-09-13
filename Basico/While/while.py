"""
While
ultilizando para realizar ações
enquanto uma condição for verdadeira

continue, break
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou!')

#tabela
x = 0 #coluna
while x < 10:
    y = 0 # linha

    while y < 5:
        print(f'X vale{x} e Y vale {y}')
        y += 1

    x += 1

print('fim')


#calculadora
while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador:')
    sair = input('sair [S]Sim [N]Nao')

    if sair == 'S' or 's':
        break


    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Voce precisa digitar um numero ")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)



"""
While /Else
contadores 
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')



"""
Iterando strings com While
"""

#conta as letras da frase
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

