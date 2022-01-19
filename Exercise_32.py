from random import sample

list_numbers1 = sample(range(0, 15), 5)
list_numbers2 = sample(range(0, 15), 5)
sum_list = []
multiplication_list = []

print(f'\nThe first list with 5 unique numbers informed {list_numbers1}.')
print(f'The second list with 5 unique numbers informed {list_numbers2}.')

for i in range(5):
    sum_list.append((list_numbers1[i]) + (list_numbers2[i]))
    multiplication_list.append((list_numbers1[i]) * (list_numbers2[i]))

print(f'Here is the list with the SUM of the numbers in the first list with the numbers in the second list: '
      f'{sum_list}.')
print(f'Here is the list with the MULTIPLICATION of the numbers in the first list with the numbers in the second list: '
      f'{multiplication_list}.')
print(f'Here is the list with the UNION of the numbers in the first list with the numbers in the second list: '
      f'{list(set(list_numbers1).union(set(list_numbers2)))}')
print(f'Here is the list with the INTERSECTION of the numbers in the first list with the numbers in the second list: '
      f'{list(set(list_numbers1).intersection(set(list_numbers2)))}')
print(f'Here is the list with the DIFFERENCE of the numbers in the first list with the numbers in the second list: '
      f'{list(set(list_numbers1).difference(set(list_numbers2)))}')
