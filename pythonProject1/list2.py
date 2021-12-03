students = ['Ivan', 'Masha', 'Sasha']
students.remove('Sasha')
print(students)

students = ['Ivan', 'Masha', 'Sasha']
del students[0]
print(students)

students = ['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students:
    print('Ivan is here!')
if 'Ann' not in students:
    print('Ann is out')

students = ['Ivan', 'Masha', 'Sasha']
ind = students.index('Sasha')
print(ind)

students = ['Sasha', 'Ivan', 'Masha']
ordered_students = sorted(students)
print(ordered_students)
students.sort()
print(students)
min = min(students)
print(min)
max = max(students)
print(max)

students = ['Sasha', 'Ivan', 'Masha']
students.reverse()
print(students)

reversed(students)
print(students)

print(students[::-1])