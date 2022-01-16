import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 99999999))

print(f'\nGeramos uma lista de 10 números. \nSão eles {lista}. \nO maior número gerado foi {max(lista)} e ele está na '
      f'posição: {lista.index(max(lista)) + 1}.')
