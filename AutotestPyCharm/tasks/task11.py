#Дано натуральное число N. Надо посчитать его двойной факториал.
a = int(input('Введите натуральное число: '))
b = 1
if a % 2 == 0:
    for i in range(1, a):
        if i % 2 == 0:
            b *= i
    print(int(a*b))
else:
    for i in range(1, a):
        if i % 2 != 0:
            b *= i
    print(int(a*b))
