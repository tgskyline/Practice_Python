'''Função que não retorna nada se chama procedimento, quando ela retorna alguma valor ou resultado se chama função'''

def saudação():
    print('Hello Word')

def soma(a,b):
    print("Resultado da soma:" + str(a+b))

def sub(a,b)    :
    print("Resultado da subtração:" + str(a-b))

def calc (a,b,op = 'soma'):
    if op == 'soma':
        print("A soma é:" + str(a+b))
    elif op == 'sub':
        print("A subtração é:" + str(a-b))

def mult(a,b):
    resultado =a*b
    return resultado

saudação()

soma(6,4)
soma(3,3)
soma(2,2)
soma(1,1)

sub(6,4)
sub(3,3)
sub(2,2)
sub(1,1)

sub(a=2, b=1)
soma(a=51 ,b=49)

calc(2,3,'sub')
calc(2,3,'soma')

resultado = mult(2,5)
print("O resultado da multiplicação é: " + str (resultado))