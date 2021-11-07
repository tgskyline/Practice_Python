arquivo = open('pessoas.txt','r')

 # SPLIT da um espaço na leitura dos dados do arquivo

for linha in arquivo:
  print(linha)
  lista = linha.split() 
  print(lista)

arquivo.close()  

materiais = ['caneta', 'caderno', 'lapis', 'livro']

arq = open('materiais.txt', 'w')
for item in materiais:
  arq.write(item + '\n')

arq.close()
  