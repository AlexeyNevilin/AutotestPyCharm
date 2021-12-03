a = input(str())
lett = a[0]
s = 1
result = ''
for i in range(1, len(a)):
    if a[i] == lett:
        s += 1
    else:
        result += lett + str(s)
        s = 1
        lett = a[i]
print(result + lett + str(s))