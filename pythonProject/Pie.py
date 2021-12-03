a = int(input())
b = int(input())
d = 0
while (d % a == 0) and (d % b == 0):
    if a >= b:
        a += b
    else:
        b += a
print(d)
