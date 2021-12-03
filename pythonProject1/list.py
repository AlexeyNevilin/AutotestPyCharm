student = ['Ivan', 'Masha', 'Sasha']
for student in student:
    print('Hello,' + student + '!')

student = ['Ivan', 'Masha', 'Sasha']
student[1] = 'Oleg'
print(student)

student = ['Ivan', 'Masha', 'Sasha']
student.append('Olga')
print(student)
student += ['Olga']
print(student)
student += ['Boris', 'Sergey']
print(student)

student = ['Ivan', 'Masha', 'Sasha']
student.insert(1, 'Olga')
print(student)

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)