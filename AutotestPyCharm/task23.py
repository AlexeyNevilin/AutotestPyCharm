class Name:
    """Клас ФИО"""
    def __init__(self, fio):
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
    def strfname(format): #Пример ввода: Name.strfname('%и. %о. %Ф')
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
#my_name3 = Name('Неволин')
#my_name4 = Name('Неволин Алексей Павлович Неволин')