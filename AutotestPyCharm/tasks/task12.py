#Для каждого числа от 1 до 100, вывести список чисел меньше текущего и кратного 5
a = int(input('Введите число: '))
for i in range(1, a + 1):
    b = []
    for s in range(5, i, 5):
        b.append(s)
    print(i, '-', b)
