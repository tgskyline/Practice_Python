pessoa = {'nome' : 'Lea' , 'idade' : 21, 'e-mail' : 'lea@gmail.com'}

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['e-mail'])

for chave, valor in pessoa.items():
    print("Chave; " + str(chave))
    print("valor; " + str(valor))
    print()

for a, b in pessoa.items():
    print("Chave; " + str(a))
    print("valor; " + str(b))
    print()

linguagens = {
    'tiago' : 'python',
    'sara' : 'c',
    'eddie' : 'java',
    'phil' : 'python'
}

for nome, linguagem in linguagens.items():
    print(nome.title() + " programa em " + linguagem.title())

for nome in linguagens.keys():
  print(nome.title())

for nome in sorted(linguagens.keys()):
   print(nome.title())

for linguagem in linguagens.values():
   print(linguagem.title())

pessoa1 = {'nome' : 'Lea' , 'idade' : 21, 'e-mail' : 'lea@gmail.com'}
pessoa2 = {'nome' : 'Eddie' , 'idade' : 25, 'e-mail' : 'eddie@gmail.com'}
pessoa3 = {'nome' : 'Phil' , 'idade' : 23, 'e-mail' : 'phil@gmail.com'}

pessoas =[pessoa1, pessoa2, pessoa3]

for pessoa in pessoas:
    print(pessoa)

for pessoa in pessoas:
    print(pessoa['e-mail'])

pessoa = {
    'nome' : 'Lea',
    'curso' : 'computação',
    'linguagens' : ['c', 'python', 'java']
}

for linguagem in pessoa['linguagens']:
    print(linguagem.title())

pessoa1 = {
    'nome' : 'Lea',
    'curso' : 'computação',
    'linguagens' : ['c', 'python', 'java']
}

pessoa2 = {
    'nome' : 'Eddie',
    'curso' : 'Sistemas de Informações',
    'linguagens' : ['ruby', 'java', 'assembler']
}

pessoa3 = {
    'nome' : 'Phil',
    'curso' : 'Engenharia da Computação',
    'linguagens' : ['Java', 'JavaScript', 'C#']
}

pessoas = [pessoa1, pessoa2, pessoa3]
print(pessoas)

for item in pessoas:
    print(item)

for item in pessoas:
    for linguagem in item['linguagens']:
        print(linguagem.title())