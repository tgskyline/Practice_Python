
# Dicionarios são criados a partir de chaves {}

pessoa = {'nome' : 'Lea' , 'idade' : 21, 'e-mail' : 'lea@gmail.com'}

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['e-mail'])

print("nome: " + str(pessoa['nome']))

# incluir dados no dicionário

pessoa['curso'] = 'computação'
print(pessoa)

# Posso deletar algum dado dentro do dicionário

del pessoa['curso']
print(pessoa)

linguagens = {
    'tiago' : 'python',
    'sara' : 'c',
    'eddie' : 'java',
    'phil' : 'python'
}

print(linguagens)

print("A linguagem de programação usada por Lea é: " + linguagens['sara'].title())