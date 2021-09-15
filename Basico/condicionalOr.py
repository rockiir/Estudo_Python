""""
Condicional com or reduzindo código
"""
nome = input('Qual o seu nome?')

print(nome or 'Voce não digitou um nome')


#imprime a primeira variavel com valor True
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or f or g
print(variavel)