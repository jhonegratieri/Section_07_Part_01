vetor = []

print('Informe dez valores inteiros:')

for i in range(10):
    valor = int(input(f'Valor {i + 1}/10: '))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)

print(f'\nO maior valor informado é {maior} e o menor é {menor}')
