import random

values = []

for i in range(6):
    values.append(random.randrange(0, 9999999, 2))

print(f'The even values read are: {values}\n'
      f'In reverse order: {values[::-1]}')
