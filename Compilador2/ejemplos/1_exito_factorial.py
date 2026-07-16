def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

resultado = factorial(5)
print(resultado)

contador = 0
while contador < 3:
    print(contador)
    contador = contador + 1

for i in range(5):
    if i % 2 == 0:
        print(i)
    else:
        continue
