num = []
num_ao_quadrado = []

print('Informe dez números:')

for i in range(10):
    valor = float(input(f'Número {i + 1}: '))

    num.append(valor)
    num_ao_quadrado.append(valor ** 2)

print(f'\nO conjunto de números inseridos é:\n{num}')
print(f'\nO conjunto do quadrado de cada número inserido é:\n{num_ao_quadrado}')
