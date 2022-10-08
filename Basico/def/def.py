'''''
Funções def
'''

def funcao(msg, nome):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg , nome)

funcao('mensagem', 'jonas')
funcao('a', 'gisele')
funcao(nome='João', msg='hi')

