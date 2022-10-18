''''
Funções def- args Kwargs
aula 16
'''

def func(*args): #args enpacontamento
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    for V in args:
        print(V)


lista = [1,2,3,4,5]
n1, n2, *n = lista # printa pelo indice 1 e 2 e o restante da lista
print(n1, n2, n)
print(*lista, sep='_')#separação da lista

func(1,2,3,4,5)








