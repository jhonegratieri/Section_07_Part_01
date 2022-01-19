import random

vector = [random.randint(0, 10) for i in range(15)]

print(f'The read vector is: {vector}')

while 0 in vector:
    vector.remove(0)

print(f'The vector read in its compressed form is: {vector}')
