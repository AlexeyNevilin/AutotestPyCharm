print(len('Privet, kak dela'))
print('Privet''\n' 'kak dela')  # ИЗИ ЁПТ
print("239" < "30" and 239 < 30, "239" < "30" and 239 > 30, "239" > "30" and 239 < 30, "239" > "30" and 239 > 30)

a = 'string'
b = 'another string'
print(a, b)
print(a + b)
print(a)
print(b)
print(a + '\n' + b)
print('123' + '42')
p = int(input())
print(p % 10)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    print('', i, end='')
    for j in range(c, d + 1):
        print('\t', i*j, end='')
    print()



a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d + 1):
    print('\t', j, end='')
for i in range(a, b + 1):
    print('', i, end='')
    print('\t', i * j, end='')
    print()