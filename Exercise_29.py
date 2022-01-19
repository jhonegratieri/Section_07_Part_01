import random

odd_numbers = []
even_numbers = []

for i in range(6):
    generated_number = random.randint(0, 100)

    if generated_number % 2 == 0:
        even_numbers.append(generated_number)

    else:
        odd_numbers.append(generated_number)

print(f'The even numbers entered are {even_numbers}, their sum is {sum(even_numbers)}')
print(f'{len(odd_numbers)} odd numbers were entered, they are {odd_numbers}')
