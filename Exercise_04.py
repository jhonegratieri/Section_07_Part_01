print('Informe oito elementos de um vetor e duas posições, será retornada a soma dos elementos dessas posições:')

numeros = []

for i in range(8):
    valor = float(input(f'Número {i + 1}: '))

    numeros.append(valor)

X = int(input('\nInforme uma posição entre 1 e 8: '))
Y = int(input('Informe uma outra posição entre 1 e 8: '))

print(f'\nA soma dos elementos das posições informadas é {numeros[X - 1] + numeros[Y - 1]}')
