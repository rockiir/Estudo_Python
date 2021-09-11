"""'
Formatando valores com modificadores

:s Texto (strings)
:d Inteiro(int)
:f Numeros de ponto flutuante (float)
:. (numero) f - quantidade de casas deciamais (float)
: (Caractere) (> ou < ou ^) ( QUANTIDADE(TIPO -s, d ou f)

> Esquerda
< direita
^ centro

"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{: f}'.format(divisao))