linguagens = {}

for i in range (0, 3):
    nome = input("Informe o seu nome: ")

    print ("Informe a linguagem de programção dentre as opções (1) C++, (2) Java, (3) Python")

    op = int(input("Digite a sua opção (1, 2 ou 3): "))

    if op == 1:
        linguagens[nome] = 'C++'
    elif op == 2:
        linguagens[nome] = 'Java'
    elif op == 3:
        linguagens[nome] = 'Python'
    
print(linguagens)

c = 0
java = 0
python = 0

for valor in linguagens.values():
    if valor == 'C++':
        c += 1
    elif valor == 'Java':
        java += 1
    elif valor == 'Python':
        python += 1

# O sinal de += siginifica que ele irá somar cada vez que a liguagem determinada for escolhida

print("\nResultado:")

print("C++ " + str(c))
print("Java " + str(java))
print("Python " + str(python))
