def cria_pessoa (nome, curso):
    pessoa = {'nome': nome, 'curso': curso}
    return pessoa

pessoa = cria_pessoa('tiago', 'ti')
print(pessoa)

def exibe_usuarios (nomes):
    for nome in nomes:
        print(nome)

nomes = ['Eddie', 'Lea', 'Phil']
exibe_usuarios(nomes)

def altera_notas(notas):
    for i in range(0 ,len(notas)):
        notas[i] += 10

notas = [5,5,6,7,2]
print(notas)

altera_notas(notas[:])
print(notas)

altera_notas(notas)
print(notas)

nova_notas = altera_notas(notas[:])
print(notas)
print(nova_notas)

