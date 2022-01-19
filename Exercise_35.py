import random

number_a = list(str(random.randint(0, 10000)))
number_a.reverse()

number_b = list(str(random.randint(0, 10000)))
number_b.reverse()

sum_list = []
overflow = 0

while True:
    number_a.append('0')
    if len(number_a) == 5:
        break

while True:
    number_b.append('0')
    if len(number_b) == 5:
        break

for i in range(5):
    number_a[i] = int(number_a[i])
    number_b[i] = int(number_b[i])

    sum_list.append(number_a[i] + number_b[i] + overflow)

    if sum_list[i] >= 10:
        sum_list[i] -= 10
        overflow = 1
    else:
        overflow = 0

while True:
    number_a.pop(len(number_a) - 1)
    if number_a[len(number_a) - 1] != 0:
        break

while True:
    number_b.pop(len(number_b) - 1)
    if number_b[len(number_b) - 1] != 0:
        break

while True:
    sum_list.pop(len(sum_list) - 1)
    if sum_list[len(sum_list) - 1] != 0:
        break

print(f'The vector of the number A is: {number_a}')
print(f'The vector of the number B is: {number_b}')
print(f'The vector of the sum of number A and number B is: {sum_list}')
