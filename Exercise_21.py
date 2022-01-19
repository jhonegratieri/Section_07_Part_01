import random

vector_A = []
vector_B = []
vector_C = []

for i in range(10):
    vector_A.append(random.randint(0, 100))
    vector_B.append(random.randint(0, 100))
    vector_C.append(vector_A[i] - vector_B[i])

print(f'The vector A is: {vector_A}\n'
      f'The vector B is: {vector_B}\n'
      f'The vector C is: {vector_C}')