import random

vector_1 = []
vector_2 = []
resultant_vector = []

for i in range(10):
    vector_1.append(random.randint(0, 100))
    vector_2.append(random.randint(0, 100))
    resultant_vector.extend([vector_1[i], vector_2[i]])

print(f'The first vector is: {vector_1}\n'
      f'The second vector is: {vector_2}\n'
      f'The resultant vector is: {resultant_vector}')
