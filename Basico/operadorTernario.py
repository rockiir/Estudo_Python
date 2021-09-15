"""
Operadores ternarios
"""

logged_user = False
if logged_user:
    msg = 'Usuario logado'
else:
    msg = 'Deslogado'

print(msg)

#forma2

logged_user = False
msg = 'Usuario logado' if logged_user else 'usuario deslogado'

print(msg)



idade = 18

if idade >= 18:
    print('Pode acessar')
else:
    print('não pode acessar')


#forma3
idade = input('Qual a sua idade?')
idade = int(idade)
e_de_maior = (idade>= 18)
msg = 'pode acessar' if e_de_maior else 'Nao pode acessar'
print(msg)
