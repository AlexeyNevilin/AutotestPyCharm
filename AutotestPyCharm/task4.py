#Пришлось подумать
a = input('Введите текст содержащий бувы "а": ')
b = len(a)
a = a.replace('а', '')
c = len(a)
print(a, ':', 'Удалено', b-c)
#Готово