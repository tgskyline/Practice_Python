materiais =['lápis', 'caderno', 'borracha', 'caneta']
print(materiais)

materiais.append('mochila')
print(materiais)

materiais.sort()
print(materiais)

print('Tamanho da lista:' + str (len(materiais)))

materiais.remove('caderno')
print(materiais)
print('Tamanho da lista:' + str (len(materiais)))