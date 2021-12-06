#Используя модуль datetime, написать функцию change_month,
#которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
def change_month(my_date, my_month): #Пример ввода: change_month('21.06.17', -5)
    my_date = datetime.strptime(my_date, '%d.%m.%y').date()
    change_date = my_date + relativedelta(months=+my_month)
    print(change_date.strftime('%d.%m.%y'))


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
def ticket(): #Пример ввода: ticket()
    quantity = 0
    for i in range(1000000):
        i = str(i).zfill(6)
        if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
            quantity += 1
    print(quantity)


#Опишите класс Name.
#Экземпляр класса создается одной строкой,
#состоящей из 2-3 слов (на это должна быть проверка).
class Name:
    """Клас ФИО"""
    def __init__(self, fio):
        """Принимает ФИО одной строкой, 2-3 слова"""
        if 2 <= len(fio.split()) <= 3:
            self.fio = fio
            self.fio = self.fio.split()
        else:
            print('Введите ФИО состоящее из 2-3 слов')

    def brief_name(self): #Пример ввода: my_name.brief_name()
        """Возвращается Фамилию и имя без отчества"""
        print(self.fio[0] + ' ' + self.fio[1])

    def initials(self): #Пример ввода: my_name.initials()
        """Возвращает Фамилию и инициалы"""
        f_ini = ''
        for i in range(1, len(self.fio)):
            ini = self.fio[i]
            f_ini += (ini[0].upper() + '.')
        f_ini = self.fio[0].title() + ' ' + f_ini
        print(f_ini)

    @staticmethod
    def strfname(format): #Пример ввода: Name.strfname('%Ф %и.%о.')
        """Преобразует по переданному формату format строку"""
        my_fio = 'Неволин Алексей Павлович'
        surname, name, patronymic = my_fio.split(' ')
        str_format = [
            ('%И', name.capitalize()),
            ('%и.', name[0].upper() + '.'),
            ('%Ф', surname.capitalize()),
            ('%ф.', surname[0].upper() + '.'),
            ('%О', patronymic.capitalize()),
            ('%о.', patronymic[0].upper() + '.')
        ]
        for old_format, new_format in str_format:
            format = format.replace(old_format, new_format)
        print(format)


my_name = Name('Неволин Алексей Павлович')
my_name2 = Name('Неволин Алексей')
my_name3 = Name('Неволин Алексей Павлович Неволин')