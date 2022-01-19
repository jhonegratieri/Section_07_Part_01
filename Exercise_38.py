list_numbers = []

for i in range(10):
    list_numbers.append(int(input(f'Number {i + 1}/10: ')))
    list_numbers.sort()

print(f'The ordered vector is: {list_numbers}')
