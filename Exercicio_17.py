import random

vector = []

for i in range(10):
    vector.append(random.randint(-99, 100))

print(f'The generated vector is: {vector}')

for index in range(10):
    if vector[index] < 0:
        vector[index] = 0

print(f'The vector generated with the updated values is: {vector}')
