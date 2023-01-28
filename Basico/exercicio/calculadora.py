""" Calculadora com while """
while True:
    num1 = float(input('Digite um valor: '))
    operador = input('Digite o operador (+, -, *, /): ')
    num2 = float(input('Digite outro valor: '))


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



