import random

vetor = []
num_pares = 0

for i in range(10):
    valor = random.randint(0, 9999999)
    vetor.append(valor)

    if valor % 2 == 0:
        num_pares += 1

print(f'\nDo vetor {vetor}, {num_pares} números são pares.')


"""
Uma outra forma de realizar é inserindo manualmente cada valor

vetor = []
num_pares = 0

print('Informe dez valores inteiros:')

for i in range(10):
    valor = int(input(f'Valor {i + 1}/10: '))
    vetor.append(valor)

for elemento in vetor:
    if elemento % 2 == 0:
        num_pares += 1

print(f'\nVocê inseriu {num_pares} números pares')
"""
