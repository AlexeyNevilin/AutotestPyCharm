my_list = [42, 'смысл всего', 'hello']
print(type(my_list))

my_list2 = []
print(type(my_list2))

my_list3 = [1, 3.5, 'string', [2, 'список']]
print(type(my_list3))

a = list('Тензор')
print(a)

a = list([1, 2, 3, 4])
print(a)

a = list([1, 2, 3, 4, 5])
print(a[:2])
print(a[3:])
print(a[-4:1:2])
print(a[-5:4:2])

a = list([1, 2, 3, 4])
print(a[1])
print(a[1:2])
print(type(a[1]))
print(type(a[1:2]))

a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(a * 3)
a.append(4)
print(a)
a.append(5)
print(a)
a.append([6, 7, 8])
print(a)
print(len(a))
b.extend(a)
print(b)
print(len(b))

our_list = list('Тензо')
our_list.insert(5, 'р')
print(our_list)
our_list.insert(99, '!')
print(our_list)

a = ['Камень', 'Ножницы', 'Бумага']
# a.remove(2) нужно передавать именно значение, а не индекс
a.remove('Камень')
print(a)

a = ['ниф-ниф', 'наф-наф', 'нуф-нуф']
a.pop(2)
# a.pop('наф-наф') нужно передавать индекс, а не значение
print(a)
a = ([1, 2, 3, 4, 5])
a.pop()  # Если не указывать индекс, то удалится последнее значение
print(a)

a = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си', 'до']
print(a.index('ре'))
print(a.index('до'))
#print(a.index('фи')) выдась ошибку так как такого значения нет
#print(a.index('до', 3, 7)) #Диапазон поиска, последний не включа, выдаст ошибку так как значение вне диапазона
print(a.index('до', 3, 8))

a = ['Орел', 'Решка', 'Орел', 'Орел'] #Передаёт количество найденых значений в списке
print(a.count('Решка'))
print(a.count('Орел'))
print(a.count('Ребро'))

a = [1, 2, 3, 4, 6, 5, 7, 0, -1]
a.sort() #Сортировка списка от меньшего к большему, однотипные значения
print(a)
#a = [1, 2, 3, 4, 6, 5, 7, [0, -1]]
#a.sort() #Выдаст ошибку так как в спике разные значения, цифры и список
#print(a)

a = [1, -1, 3, -4, -2, 5, 6, 0]
a.sort(key=abs) #Сортировка по обсолютному значению
print(a)

a = ['Пикачу', 'Лох', 'Паронормальный']
a.sort(key=len)
print(a) #Сортировка по длинне

a = [1, 2, 3, 4, 5, 6, 7]
a.reverse() #Переворачивает список
print(a)
a = ['Почему']
a.reverse()
print(a)

