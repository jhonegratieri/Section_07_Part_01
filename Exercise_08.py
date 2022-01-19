import random

values = []

for i in range(6):
    values.append(random.randint(0, 9999999))

print(f'The values read are: {values}\n'
      f'In reverse order: {values[::-1]}')
