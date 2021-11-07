list = []

for valor in range(1,11):
  num = int(input("Digite o " + str(valor) + "º número:"))
  list.append(num)
  
print(sum(list))