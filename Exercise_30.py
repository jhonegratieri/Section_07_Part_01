import random

vector_a = [random.randint(0, 20) for i in range(10)]
vector_b = [random.randint(0, 20) for j in range(10)]
intercection_vector = list(set(vector_a).intersection(set(vector_b)))

print(f'The first vector is: {vector_a}')
print(f'The second vector is: {vector_b}')
print(f'The vector with the intersection numbers of the two vectors is: {intercection_vector}')
