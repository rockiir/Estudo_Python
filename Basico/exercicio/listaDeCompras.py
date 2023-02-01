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
        














