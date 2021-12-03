a=int(input())
b=int(input())
if b != 0:
    print(a/b)
else:
    print('Деление невозможно')
    b= int(input('Введите ненулевое значение: '))
    if b == 0:
        print('Вы дебил!')
    else:
        print(a/b)



