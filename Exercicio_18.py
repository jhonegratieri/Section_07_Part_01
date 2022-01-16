import random

vector = []
multiple_numbers = []
x = random.randint(2, 10)

for i in range(10):
    vector.append(random.randint(0, 24))

    if vector[i] % x == 0 and vector[i] != 0:
        multiple_numbers.append(vector[i])

print(f'The generated vector is: {vector}\n'
      f'The number you want to get the multiples is: {x}')

if len(multiple_numbers) == 0:
    print(f'Vector {vector} has no multiple of {x}')

else:
    print(f'Vector {vector} has {len(multiple_numbers)} multiples of {x}, they are: {multiple_numbers}')
