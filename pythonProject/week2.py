a = 10
while a > 0:
    print(a, end=' ')
    a -= 1

print('\n')

a = 5
while a <= 55:
    print(a, end=' ')
    a += 2

print('\n')

a = 5
while a <= 55:
    if a % 2 == 1:
        print(a, end=' ')
    a += 1

print('\n')

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        print(i, end=' ')

print('\n')

n = int(input())
c = 1
while c <= n:
    print('*' * c)
    c += 1

print('\n')

n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'

print('\n')
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

print('\n')

s = 0
i = int(input())
b = int(input())
while i <= b:
    s += i
    i += 1
print(s)