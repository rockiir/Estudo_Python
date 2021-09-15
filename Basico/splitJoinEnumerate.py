"""
Split, join, Enumerate
* Split - dividir uma string # str
* join -juntar a lista # str
* Enumerate - Enumerar elementos da lista # itineraveis
"""
#Conta quantas vezes cada palavra apareceu na frase
string = "O Brasil é o pais do futebol, O Brasil é o pais da musica"
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu { lista_1.count(valor)}x na frase')


#contagem de palavras2
string = "O Brasil é o pais do futebol, O Brasil é o pais da musica"
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_2:
    qtd_vezes = lista_2.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes é {palavra} ({contagem}x) ')

#imprime frases separadas
string = "O Brasil é o pais do futebol, O Brasil é o pais da musica"
lista_1 = string.split(' ')
lista_2 = string.split(',')


for valor in lista_2:
    print(valor.strip().capitalize())#strip tira espaço


#Separa
string = 'O brasil é penta. '
lista = string.split(' ')
string2 = ' '.join(lista)

print(lista)
print(string)
print(string2)


#Enumera
string = 'O brasil é penta. '
lista = string.split(' ')

for indice , valor in enumerate(lista):
    print(indice, valor)
