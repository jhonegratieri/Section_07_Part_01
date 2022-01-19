import random

vector = []
odd_numbers = []

for i in range(10):
    generated_value = random.randint(0, 50)
    vector.append(generated_value)

    if generated_value % 2 != 0:
        odd_numbers.append(generated_value)

quantity_odd_numbers = len(odd_numbers)

print('The generated vector is:')

for i in range(0, 10, 2):
    print(vector[i], vector[i + 1])

if quantity_odd_numbers != 0:
    print('\nThe vector of odd numbers is:')

    if quantity_odd_numbers % 2 == 0:
        for i in range(0, quantity_odd_numbers, 2):
            print(odd_numbers[i], odd_numbers[i + 1])

    if quantity_odd_numbers % 2 != 0:
        for i in range(0, quantity_odd_numbers - 1, 2):
            print(odd_numbers[i], odd_numbers[i + 1])

        print(odd_numbers[quantity_odd_numbers - 1])

else:
    print('The generated vector does not have odd numbers')
