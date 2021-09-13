"""
Listas
fatiamento
append, insert, pop, del, cleaner,
extend
min, max
range
"""
lista = ['A', 'B', 'C', 'D', 'E']

print(lista[1]) #imprime o valor selecionado
print(lista[:3]) # imprime até o valor selecionado
print(lista[-1]) # imprime até o ultimo valor selecionado
print(lista[::2]) # imprime de 2 em 2
print(lista[::-1]) # imprime de forma invertida

# Extend, apend , insert,
l1 = [ 1, 2, 3]
l2 = [ 4, 5, 6]
print( max(l2) ) #imprime ultimo
print( min(l2) ) # imprime inicial

l1.extend(l2) # Une as listas
print(l2)
l2.append('b') #adiciona valor
print(l2)
l2.insert(0, 'banana') # adiciona valor na posição indicada
print(l2)
l2.pop()# remove ultimo elemento
print(l2)
del(l2[3:5]) # deleta selecionados
print(l2)
# Soma todos os valores da lista
l3 = list(range(10,20))
soma = 0
for valor in l3:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)
print(l1)
print(l2)
print(l3)

#exibe o tipo de cada elemento da lista
l4 = ['String', True, 10, -20.5]
for elem in l4:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')


