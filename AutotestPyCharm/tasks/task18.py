#Вывести список простых чисел до 1000.
def prime_number():
    list_numb = []
    for i in range(2, 1001):
        for s in range(2, i):
            if i % s == 0:
                break
        else:
            list_numb.append(i)
    return list_numb

'''def prime_number():
    prime = []
    for i in range(2, 1001):
        for s in range(2, i):
            if i % s == 0:
                break
        else:
            prime.append(i)
    return prime'''

'''a = int(input())
b = []
c = 0
for i in range(a + 1):
    if i == 1 or i == 0:
        continue
    for s in range(2, i):
        if i % s == 0:
            c = c + 1
    if c == 0:
        b.append(i)
    else:
        c = 0
print(b)'''




'''a = int(input())
b = []
for i in range(a + 1):
    if i == 1 or i == 0:
        continue
    c = int(i)
    if i == 2:
        b.append(i)
    for s in range(2, c):
        if i % s == 0 or i % s != 0:
            b.append(i)
            break
print(b)



   for s in range(i):
        print(s)
        if i == 1 or i == 0:
            continue
        if i % s != 0 and i % i == 0 and i % 1 == 0:
            b.append(i)
print(b)


a = int(input())
b = []
for i in range(a + 1):
    if i == 1 or i == 0:
        continue
    c = int(i)
    if i == 2:
        b.append(i)
    for s in range(2, c):
        if i % s == 0:
            break
        else:
            b.append(i)
            break
print(b)'''
