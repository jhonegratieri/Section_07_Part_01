import random

school_grades = []

for i in range(15):
    school_grades.append(random.randint(0, 11))

print(f'The generated notes were {school_grades}.')
print(f'The grade point average is {(sum(school_grades))/15}.')
