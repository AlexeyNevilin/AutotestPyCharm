#Используя модуль datetime, написать функцию change_month,
#которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.
from datetime import datetime
def change_month(my_date, my_month): #change_month('21.06.17', -5)
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    if my_month > 0:
        new_date = (
            str(my_date.day).zfill(2)
            + '.' +
            (str(my_date.month + my_month) if (my_date.month + my_month) <= 12 else str((my_date.month + my_month) % 12)).zfill(2)
            + '.' +
            (str(my_date.year + 0) if (my_month + my_date.month) <= 12 else str(my_date.year + ((my_date.month + my_month) // 12)))
        )
        print(new_date)
    else:
        new_date = (
            str(my_date.day).zfill(2)
            + '.' +
            (str(my_date.month + my_month) if (my_date.month + my_month) > 0 else str((my_date.month + my_month) // 12)).zfill(2)
            + '.' +
            (str(my_date.year + 0) if (my_date.month + my_month) > 0 else str(my_date.year + ((my_date.month + my_month) // 12)))
        )
        print(new_date)


#Напишите декоратор func_time,
#который подсчитывает и выводит сколько времени выполняется функция,
#обернутая в него.
import time
from datetime import datetime
def simple_decor(func):
    def func_time():
        data_start = datetime.now()
        print('Функция начала работу')
        func()
        print('Конец работы функции', '\n', 'Функция работала:', datetime.now() - data_start, 'сек.')
    return func_time

@simple_decor
def ticket(): #ticket()
    quantity = 0
    for i in range(1000000):
        i = str(i).zfill(6)
        if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
            quantity += 1
    print(quantity)


#Опишите класс Name.
#Экземпляр класса создается одной строкой,
#состоящей из 2-3 слов (на это должна быть проверка).
