""""
Desempacotament de listas em Python
"""

lista = ['Luzi', 'João', 'Maria', 1,2,3,4,5,6,7,9,100]

n1, n2, n3, *outra_lista = lista

print(n1, n2, outra_lista)
