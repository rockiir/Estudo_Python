"""
For in em Python
Iterando strings com for
Função range (strat=0, stop, step=1)

"""
# enumera texto
texto = 'Python'

for n,  letra in enumerate(texto):
    print(n, letra)

#contagem regressiva
for n in range(20,10, -1):
    print(n)

# numeros de 8 em 8 até 100
print('##############')
for n in range(100):
    if n % 8 == 0:
        print(n)

# letra T e H em Maiuscula
texto = 'Python'
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra =='h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)







