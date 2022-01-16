import random

numbers = []

for i in range(5):
    numbers.append(random.randint(0, 100))

print(f'The generated vector is: {numbers}\n'
      f'The highest value read is:: {max(numbers)}\n'
      f'The smallest value read is: {min(numbers)}\n'
      f'The arithmetic mean of the values read is: {sum(numbers) / 5}')
