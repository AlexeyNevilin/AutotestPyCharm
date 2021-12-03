# Взято из инета
a = [int(item) for item in input().split()]
a2 = []
for i in range(len(a)):
    if len(a) == 1:
        print(a[0])
        break
    else:
        if i == 0:
            a2.append(a[-1] + a[i + 1])
        elif i > 0 and i != len(a) - 1:
            a2.append(a[i - 1] + a[i + 1])
        else:
            a2.append(a[i - 1] + a[0])
if a2 != 0:
    for i in a2:
        print(i, end=' ')


# Примерно как должно быть
a = [int(i) for i in input().split()]
n = len(a)
if n == 1:
    print(a[0])
else:
    for i in range(n-1):
        print(a[i-1]+a[i+1], end=" ")
    print(a[n-2]+a[0])
