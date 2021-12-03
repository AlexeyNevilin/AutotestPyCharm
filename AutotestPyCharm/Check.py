'''def prime_number():
    list_numb = []
    for i in range(2, 1001):
        for s in range(2, i):
            if i % s == 0:
                break
        else:
            list_numb.append(i)
    return list_numb'''

'''def prime_number():
    list_numb = []
    for i in range(2, 1001):
        for s in range(2, i):
            if i % s == 0:
                break
        else:
            list_numb.append(i)
    return list_numb'''
a = 'Неволин Алексей Павлович'
a = a.split()
print(a, type(a))
simv = len(a)
print(simv)