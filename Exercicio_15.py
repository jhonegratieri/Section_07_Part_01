import random

vector = []

for i in range(20):
    vector.append(random.randint(0, 11))

print(f'The generated vector is: {vector}\n'
      f'The generated vector without repeated elements is: {set(vector)}')
