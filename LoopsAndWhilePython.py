
'''While é útilizado para criar um laço quando não há um limite certo para se repetir'''

# contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1

'''Interrompendo laço While com !='''

# mensagem = ""
# while mensagem != 'sair':
#     mensagem = input("Escreva algo ('sair' para terminar): ")
#     print(mensagem)

'''Interrompendo laço While com lógica bouleana de Flag'''

# flag = True
# while flag:
#     mensagem = input("Escreva algo ('sair' para terminar): ")
#     if mensagem == 'sair':
#         flag = False

#     print(mensagem)

'''Interrompendo laço While com BREAK NÃO É MUITO RECOMENDADO'''

# while True:
#     mensagem = input("Escreva algo ('sair' para terminar): ")
#     if mensagem == 'sair':
#         break
#     else:    
#         print(mensagem)


'''Interrompendo laço While com Continue, ele termina o laço de forma normal enquanto as condições não atendem mais'''

# contador = 0

# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(contador)

materiais =['caneta','caderno', 'livro', 'lápis']
objetos = []

while materiais:
    objeto = materiais.pop()
    objetos.append(objeto)

for objeto in objetos:
    print(objeto.title())
    


