""" Calculadora com while """
while True:

    num1 = float(input('Digite um valor: '))
    operador = input('Digite o operador (+-/*): ')
    num2 = float(input('Digite outro valor: '))

    numeros_validos = None

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print('Operador inválido')
        continue

    print('Resultado:', resultado)

    sair = input('Quer sair? [s]: ').lower().startswith('s')
    if sair:
        break



