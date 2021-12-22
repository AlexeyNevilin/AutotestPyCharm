from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os

def get_links():

    #Открыть браузер и перейти на сайт
    d = wd.Chrome()
    d.maximize_window()
    d.get('https://sbis.ru')

    #Кликнуть по кнопке Поддержка
    d.find_element(By.LINK_TEXT, 'Поддержка').click()

    #Доскролить до нужного объекта
    scrollTo_block = d.find_element(By.CLASS_NAME, 'sbis_ru-Support-block2__section-mob')
    d.execute_script('return arguments[0].scrollIntoView(true);', scrollTo_block)

    #Кликнуть по кнопке Скачать
    d.find_element(By.CSS_SELECTOR, '[href="/download"]').click()

    #Парсинг HTML-файл
    response = requests.get(d.current_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Находим все нужные ссылки
    results = []
    link_list = soup.find('div', {'data-for': "ereport25"})
    load_blocks = link_list.find_all('div', {'class': 'sbis_ru-DownloadNew-loadLink'})
    for link in load_blocks:
        download_links = link.find('a').get('href')
        download_links_name = link.find('a').text
        results.append(f'{download_links_name}: {download_links}')

    #Записываем ссылки в файл
    file = open('links.txt', mode='w')
    file.write('\n'.join(results))
    file.close()

    #Закрываем браузер
    d.quit()


def volune_catalog():
    volume_dirs = 0
    volume_file = 0
    volume_file_py = 0
    volume_file_exe = 0
    path = 'C:\\Users\\lesha\\AppData\\Local\\Programs\\Python\\Python39'

    # Ищем по дереву каталога все папки и файлы
    for root, dirs, files in os.walk(path):

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