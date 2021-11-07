a = int(input("Informe o valor de a: "))
x = int(input("Informe o valor de x: "))
n = int(input("Informe o valor de n: "))

seq =[]

for i in range(1,(n+1)):
  termo = a * (x ** i)
  seq.append(termo)

print(seq)
p = sum(seq)
print("O valor de P: " + str(p))