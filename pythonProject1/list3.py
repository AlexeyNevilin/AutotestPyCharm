a = [1, 'A', 2]
b = a
a[0] = 42
print(a)
print(b)

b[2] = 30
print(b)
print(a)

a = [1, 2, 3]
b = a
print(b)

a[1] = 10
print(b)

b[0] = 20
print(a)

a = [5, 6]
print(b)