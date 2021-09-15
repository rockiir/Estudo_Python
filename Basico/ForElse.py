"""
For / Else em python

"""

variavel = [ 'Luiz Otávio', 'joàozinho', 'Maria']

for valor in variavel:
    if valor.startswith('j'):#verifica se o valor da string começa com a letra indicada
        print('começa com j', valor)
    else:
        print('não comeca com J', valor)


#verificando se existe uma palavra com J
variavel = [ 'Luiz Otávio', 'joàozinho', 'Maria']
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print('Existe uma palavra que começa com j', valor)

