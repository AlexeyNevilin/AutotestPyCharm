#Используя модуль datetime, написать функцию change_month,
#которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.
from datetime import datetime
from datetime import timedelta
def change_month(input_date, input_month): # change_month('21.06.17', -5)
    date = datetime.strptime(input_date, '%d.%m.%y').date()
    if (date.month + input_month) % 12 == 0:
        modified_month = 12
    else:
        modified_month = (date.month + input_month) % 12
    modified_year = date.year

    month = date.month + input_month
    if month > 12:
        while month > 12:
            month -= 12
            modified_year += 1
    elif month <= 0:
        while month <= 0:
            month += 12
            modified_year -= 1
    else:
        modified_year = date.year

    modified_year_str = str(date.day).zfill(2) + '.' + str(modified_month).zfill(2) + '.' + str(modified_year).zfill(2)
    if 28 <= date.day <= 31 and modified_month != 12:
        max_day = datetime.strptime(('01' + '.' + str(modified_month + 1).zfill(2) + '.' + str(modified_year).zfill(2)), '%d.%m.%Y').date() - timedelta(days=1)
        max_day = str(max_day.day).zfill(2) + '.' + str(max_day.month).zfill(2) + '.' + str(max_day.year).zfill(2)
        if modified_year_str > max_day:
            max_day = datetime.strptime(max_day, '%d.%m.%Y').date()
            modified_day = max_day.day
        else:
            modified_day = date.day
    else:
        modified_day = date.day

    modified_date = str(modified_day).zfill(2) + '.' + str(modified_month).zfill(2) + '.' + str(modified_year).zfill(2)
    modified_date = datetime.strptime(modified_date, '%d.%m.%Y').date()
    print(modified_date)


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
    def __init__(self, fio): #Пример ввода: my_name3 = Name('Неволин') #my_name4 = Name('Неволин Алексей Павлович Неволин')
        """Принимает ФИО одной строкой, 2-3 слова"""
        self.fio = fio
        self.fio = self.fio.split()
        if len(fio.split()) < 2 or len(fio.split()) > 3:
            raise ValueError('ФИО должно состоять из 2-3 слов')

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