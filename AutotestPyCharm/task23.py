class Name:
    """Клас ФИО"""
    def __init__(self, fio):
        """Принимает ФИО одной строкой, 2-3 слова"""
        if 2 <= len(fio.split()) <= 3:
            self.fio = fio
            self.fio = self.fio.split()
        else:
            print('Введите ФИО состоящее из 2-3 слов')

    def brief_name(self):
        """Возвращается Фамилию и имя без отчества"""
        print(self.fio[0] + ' ' + self.fio[1])

    def initials(self):
        """Возвращает Фамилию и инициалы"""
        f_ini = ''
        for i in range(1, len(self.fio)):
            ini = self.fio[i]
            f_ini += (ini[0].upper() + '.')
        f_ini = self.fio[0].title() + ' ' + f_ini
        print(f_ini)

    @staticmethod
    def strfname(format):
        """Преобразует по переданному формату format строку"""



my_name = Name('Неволин Алексей Павлович')
my_name2 = Name('Неволин Алексей')