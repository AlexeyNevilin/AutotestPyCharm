print('Hello world')

a = 63
print(id(a))

b = 10
print(type(b) )

fio = 'Nevolin Alexey Pavlivych'
print(fio.split())
print(type(fio.split()))


a = 'Привет папа как дела что делаешь'
b = len(a.split())
print(b)

s = 'Я ненавижу много работат! Я ненавижу много работать'
print(s.replace('ненавижу', 'люблю'))

s = '     Привет папа как дела что делаешь     '
print(s.strip())

s = '     Привет папа как дела что делаешь     '
print(s.rstrip())

s = '     Привет папа как дела что делаешь     '
print(s.lstrip())

file_name = 'pic.jpg'
print(file_name.endswith('.jpg'))
print(file_name.endswith('.xml'))
print(file_name.startswith('pic'))
print(file_name.startswith('doc'))

strocka = 'ТутТолькоБуквы'
print(strocka.isalpha())
strocka = 'Тут не только буквы'
print(strocka.isalpha())
strocka = '89997771111'
print(strocka.isdigit())
strocka = '8-999-777-1111'
print(strocka.isdigit())

s = ' ООО Тензор'
print(s.upper())
print(s.lower())