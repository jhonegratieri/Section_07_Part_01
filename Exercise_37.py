import random

numbers_list = [random.randint(0, 100) for i in range(11)]
ascending_order = []
descending_order = []

for j in range(0, 11):
    if j <= 5:
        ascending_order.append(numbers_list[j])
    else:
        descending_order.append(numbers_list[j])

ascending_order.sort()
descending_order.sort(reverse=True)

print(f'The original list of numbers is: {numbers_list}')
print(f'The ordered list of numbers is: {ascending_order + descending_order}')
