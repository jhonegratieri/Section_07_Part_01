import random

vector = []
code_number = 1

for i in range(5):
    vector.append(random.randint(-9999, 10000))

print(f'The generated vector is: {vector}')

while code_number != 0:
    code_number = int(input('\nSELECT A CODE\n'
                            '0 - End the program\n'
                            '1 - Vector in direct order\n'
                            '2 - Vector in reverse order\n'))

    match code_number:
        case 0:
            print('Thank you!')

        case 1:
            print(f'The vector in direct order is: {vector}')

        case 2:
            vector.reverse()
            print(f'The vector in reverse order is: {vector}')

        case _:
            print('Invalid option. Please, try again.')
