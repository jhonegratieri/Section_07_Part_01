import random

numbers = []

for i in range(5):
    numbers.append(random.randint(0, 100))

print(f'The generated vector is: {numbers}\n'
      f'The position of the highest value read is position {numbers.index(max(numbers)) + 1}\n'
      f'The position of the lowest value read is position {numbers.index(min(numbers)) + 1}')
