import random

numbers = []
positive_number_sum = 0
negative_numbers = 0

for i in range(10):
    value = random.randint(-99, 100)
    numbers.append(value)

    if value < 0:
        negative_numbers += 1
    else:
        positive_number_sum += value

print(f'The generated vector is: {numbers}\n'
      f'The sum positive numbers is: {positive_number_sum}\n'
      f'The vector has {negative_numbers} negative numbers')
