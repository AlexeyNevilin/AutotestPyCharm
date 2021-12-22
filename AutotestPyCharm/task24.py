import os

def volune_catalog():
    volume_dirs = 0
    volume_file = 0
    volume_file_py = 0
    volume_file_exe = 0

    # Ищем по дереву каталога все папки и файлы
    for root, dirs, files in os.walk('C:\\Users\\lesha\\AppData\\Local\\Programs\\Python\\Python39'):

        # Считает количество всех папок и файлов
        volume_dirs += 1
        volume_file += len(files)

        # Считаем количество всех файлов с расширение .py и .exe
        for file in files:
            expansion = os.path.splitext(file)[1]

            if expansion == '.py':
                volume_file_py += 1

            if expansion == '.exe':
                volume_file_exe += 1

    # Объединяем для записи в файл
    results = (f'Количество папок: {volume_dirs} \n'
               f'Количество файлов: {volume_file}\n'
               f'Количество файлов с расширением ".py": {volume_file_py}\n'
               f'Количество файлов с расширением ".exe": {volume_file_exe}')

    # Записываем ссылки в файл
    file_catalog = open('volume.txt', mode='w')
    file_catalog.write(results)
    file_catalog.close()













"""path = 'C:\\Users\\lesha\\AppData\\Local\\Programs\\Python\\Python39'
volume_dirs = 0
volume_file = 0
volume_file_py = 0
volume_file_exe = 0

#Ищем по дереву каталога все папки и файлы
for root, dirs, files in os.walk(path):
    #Считает количество всех папок и файлов
    volume_dirs += 1
    volume_file += len(files)

    #Считаем количество всех файлов с расширение .py и .exe
    for file in files:
        expansion = os.path.splitext(file)[1]

        if expansion == '.py':
            volume_file_py += 1

        if expansion == '.exe':
            volume_file_exe += 1

#Объединяем для записи в файл
results = (f'Количество папок: {volume_dirs} \n'
           f'Количество файлов: {volume_file}\n'
           f'Количество файлов с расширением ".py": {volume_file_py}\n'
           f'Количество файлов с расширением ".exe": {volume_file_exe}')

#Записываем ссылки в файл
file = open('volume.txt', mode='w')
file.write(results)
file.close()"""