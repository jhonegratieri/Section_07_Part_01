vector = []
i = 1

print('Insert 10 different numbers into the vector:')

while len(vector) != 10:
    number = int(input(f'Number {i}/10: '))

    if number in vector:
        print('This number already exists in the vector, enter a different value.')

    else:
        vector.append(number)
        i += 1

print(f'The inserted vector is: {vector}')
