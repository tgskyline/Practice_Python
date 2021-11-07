carros = ['audi', 'bmw', 'subaru', 'toyota']

for item in carros:
  if item == 'bmw':
    print(item.upper())
  else:
    print(item.title())

a = (15 == 20)
print(a)

idade  = 15
if idade >= 18 and idade <= 69:
  print("Voto obrigatório")
else:
  print("Voto não obrigatório")

frequencia = 20
nota = 80
if nota < 60 or frequencia < 25:
  print("Reprovado")

materiais = ['caneta', 'caderno', 'livro', 'e-book']
valor = 'caneta' in materiais
print(valor)

valor = 'agenda' in materiais
print(valor)

valor = 'caneta' not in materiais
print(valor)

valor = 'agenda' not in materiais
print(valor)

idade = 16
if idade < 14:
  print("Sua entrada custa 0,00")
elif idade > 18:
  print("Sua entrada custa 5,00")
elif idade < 18:
  print("Sua entreda custa 8,00")
else:
  print("Sua entrada custa 10,00")