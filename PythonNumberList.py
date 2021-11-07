materiais =['lápis', 'caderno', 'borracha', 'caneta']
print(materiais)

# Lista de 1 a 10
numeros = list(range(1,11))
print(numeros)

for valor in numeros:
  print(valor)

  quadrados = []

for item in range(1,11):
  quadrado = item ** 2
  quadrados.append(quadrado)

print(quadrados)

print(min(numeros))
print(max(numeros))
print(sum(numeros))

print(materiais[0:3])

mat = [1,2,3,4]
# Quando utilizo a atribuição de variável com [:] estou fazendo uma cópia da lista
obj = mat[:] 
obj.append(5)
print(mat)
print(obj)