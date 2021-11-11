import random

perda = 0
ganho = 0
jogar = True

while jogar:
    op = int(input("Escolha: 0:Cara ou 1:Coroa:"))
    rand = round (random.random()*100)
    if (rand % 2) == op:
        ganho += 1
        if op == 0:
            print("Cara, você ganhou! \n")
        else:
            print("Coroa, você ganhou! \n")
    else:
        perda += 1
        if op == 0:
            print("Cara, você perdeu! \n")
        else:
            print("Coroa, você perdeu! \n")

    mensagem = input("Deseja jogar novamente (S/N): ")
    if mensagem == 'n':
        jogar = False

print("\nRelatório Final:")
print("Número de jogos que você ganhou: " + str(ganho))
print("Número de jogos que perdeu: " + str(perda))