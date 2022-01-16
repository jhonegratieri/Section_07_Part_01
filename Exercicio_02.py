print('Informe 6 números:')

numeros = []

for i in range(6):
    numeros.append(int(input()))

print('Os números informados são:')

for elemento in numeros:
    print(elemento, end='  ')
