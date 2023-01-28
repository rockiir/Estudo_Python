"""
Iterando strings com while
"""
nome = 'Luiz Otávio'  # Iteráveis
tamanho_nome = len(nome)
array_nome = 0
novo_nome =''
print(nome)
print(tamanho_nome)
print(nome[3])


while array_nome < tamanho_nome:
    nome_sep=(nome[array_nome] + '*')
    novo_nome += nome_sep
    array_nome +=1

print(novo_nome)
