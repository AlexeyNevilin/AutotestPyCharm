#Напишите функцию, которая проверяет является ли число палиндромом
def palindrome(number):
    number = str(number)
    if number == number[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')


'''a = input()
if a == a[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')'''