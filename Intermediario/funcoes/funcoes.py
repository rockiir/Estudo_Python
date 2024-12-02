## python functions

def hello_world():
    print("Hello, World!")

def greet_user(name):
    print(f"Hello, {name}!")

hello_world()
greet_user("Raquel")


## exercicio funçoes 113

def ehPar(num):
    return "Par" if num % 2 == 0 else "Ímpar"
    
print(ehPar(3)) 
################################################################
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao =  multiplicar( 1,2,3,4,5)
print(multiplicacao)












