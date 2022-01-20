import random

number_a = list(str(random.randint(0, 10000)))
number_a.reverse()

number_b = list(str(random.randint(0, 10000)))
number_b.reverse()

sum_list = []
overflow = 0


while len(number_a) != 5 or len(number_b) != 5:

    if len(number_a) != 5:
        number_a.append('0')

    if len(number_b) != 5:
        number_b.append('0')


for i in range(5):
    sum_list.append(int(number_a[i]) + int(number_b[i]) + overflow)

    if sum_list[i] >= 10:
        sum_list[i] -= 10
        overflow = 1
    else:
        overflow = 0


while number_a[len(number_a) - 1] == '0' or number_b[len(number_b) - 1] == '0' or sum_list[len(sum_list) - 1] == 0:

    if number_a[len(number_a) - 1] == '0':
        number_a.pop(len(number_a) - 1)

    if number_b[len(number_b) - 1] == '0':
        number_b.pop(len(number_b) - 1)

    if sum_list[len(sum_list) - 1] == 0:
        sum_list.pop(len(sum_list) - 1)


print(f'The vector of the number A is: {number_a}')
print(f'The vector of the number B is: {number_b}')
print(f'The vector of the sum of number A and number B is: {sum_list}')
