student_data = {}

print('\nSTUDENT DATABASE')

for i in range(10):
    student_number = int(input('\nPlease, enter your ID number: '))
    student_data[student_number] = int(input('Please, enter your height (in centimeters): '))

tallest_student = max(student_data, key=student_data.get)
shortest_student = min(student_data, key=student_data.get)

print(f"\nThe tallest student is the student {tallest_student} and his height is "
      f"{student_data[tallest_student]}. "
      f"The shortest student is the student {shortest_student} and his height is "
      f"{student_data[shortest_student]}.")


"""
import random

student_heights = []
student_numbers = []

for i in range(10):
    student_heights.append(round(random.uniform(1.40, 2.10), 2))

while len(student_numbers) != 10:
    number = random.randint(0, 100)

    if number not in student_numbers:
        student_numbers.append(number)

print('\nList of students with their respective heights:\n')

for i in range(10):
    print(f'Student Number: {student_numbers[i]}    Height: {student_heights[i]} meters')

min_height = student_heights.index(min(student_heights))
max_height = student_heights.index(max(student_heights))

print(f'\nStudent {student_numbers[min_height]} is the shortest student, '
      f'he is {min(student_heights)} meters tall.')

print(f'Student {student_numbers[max_height]} is the tallest student, '
      f'he is {max(student_heights)} meters tall.')

"""
