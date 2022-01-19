import random

list_numbers = [random.randint(0, 10000) for i in range(10)]

print(f'The original vector is: {list_numbers}')

list_numbers.sort()

print(f'The ordered vector is: {list_numbers}')
