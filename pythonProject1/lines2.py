a = str(input())
b = 0
c = (len(a))
i = 0
for d in a.upper():
    if d == 'G' or d == 'C':
        b += 1
        i = (b / c) * 100
print(i)

