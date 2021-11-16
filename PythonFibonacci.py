def fibonacci (n):
    fib = []

    anterior1 = 1
    anterior2 = 1

    fib.append(anterior1)
    fib.append(anterior2)

    for i in range(2,n):
        atual = anterior1 + anterior2
        fib.append(atual)

        anterior1 = anterior2
        anterior2 = atual

    return fib

n = int(input("Digite o número de termos: "))
fib = fibonacci(n)
print(fib)