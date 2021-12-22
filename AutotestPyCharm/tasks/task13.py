# Поменять местами самый большой и самый маленький элементы списка 4, 8, 3, -1, -12, 7, 4, 6, 5, 0, 25, 2, 3, 6
a = [4, 8, 3, -1, -12, 7, 4, 6, 5, 0, 25, 2, 3, 6]
b = a.copy()
b.sort()
mn = a.index(b[0])
mx = a.index(b[-1])
a[mn], a[mx] = a[mx], a[mn]
print(a)

#c = [i for i in range(len(a))]
#a[c[mn]], a[c[mx]] = a[c[mx]], a[c[mn]]
#print(a)
#print(b)
#print(b[0], b[-1])
#print(c)
#print(mn, mx)
#print(a[mn], a[mx])

#a = int(input('Введите число "начало" списка: '))
#b = int(input('Введите число "конец" списка: '))
#b = [i for i in range(a, b + 1)]
#b[0], b[-1] = b[-1], b[0]
#print(b)
