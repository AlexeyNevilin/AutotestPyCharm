#Пришлось подумать
a = int(1261)
b = str(a)
print(int(b[1]) + int(b[2]))

a = input('Введите целое число: ')
b = 0
c = str(a)
d = len(c)
for i in range(0, d):
    b += int(c[i])
print(b)
#Готово