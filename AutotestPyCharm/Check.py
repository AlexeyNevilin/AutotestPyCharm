class Name:
    """Клас ФИО"""
    def __init__(self, fio):
        """Принимает ФИО одной строкой, 2-3 слова"""
        self.fio = fio
        self.fio = self.fio.split()
        if len(fio.split()) < 2 or len(fio.split()) > 3:
            raise ValueError('ФИО должно состоять из 2-3 слов')


