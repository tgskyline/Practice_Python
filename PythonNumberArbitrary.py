def imprime_notas(nome, *notas):
    print("Aluno(a): " + nome)
    for nota in notas:
        print(nota)

imprime_notas('Eddie', 5)
imprime_notas('Alice', 1,2,3,4,5)

def calc_notas(*notas):
    soma = 0
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)

    return soma, media


soma, media = calc_notas(5,5,1,2)
print("Soma: " + str(soma))
print("Média: " + str(media))