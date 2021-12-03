a = int(input())
b = int(input())
c = int(input())
d = int(input())
for o in range(c, d + 1):
    print('\t', o,)
for i in range(a, b + 1):
    print('', i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, end='')
    print()
