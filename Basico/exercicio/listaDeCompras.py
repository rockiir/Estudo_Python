"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
menu = ("inserir","Apagar", "listar")
alimentos = ['Arroz', 'Feijão', 'Pão', 'Frango', 'Carne', 'Peixe', 'Batata', 'Salada', 'Sopa', 'Biscoito']


while True:
    escolha = input("Escolha uma opção: " + str(menu))

    if escolha == "inserir":
        inserir = input("Digite nome do produto a ser adicionado")
        alimentos.append(inserir)
        print("Produto adicionado.")
        for indice, elements in enumerate(alimentos):
            print (indice, elements)

    elif escolha == "apagar":
        print("Selecione um produto para deletar")
        for indice, elements in enumerate(alimentos):
            print(f"{indice}: {elements}")
        deletar = int(input("Digite o índice do produto a ser deletado")) 
        alimentos.pop(deletar)
        print("Produto deletado.")

    elif escolha == "listar":
        print("Lista de alimentos:")
        for indice, elements in enumerate(alimentos):
            print(f"{indice}: {elements}")
    else:
        print("Opção inválida, escolha novamente.")
        
#solução professor

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')













