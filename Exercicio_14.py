import random

vector = []
repeated_numbers = []

for i in range(10):
    value = random.randint(0, 6)

    if value in vector:
        repeated_numbers.append(value)

    vector.append(value)

print(f'The generated values are: {vector}')

if len(repeated_numbers) == 0:
    print('There are no repeated numbers')

else:
    print(f'The repeating numbers are: {set(repeated_numbers)}')
