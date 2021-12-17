from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

d = wd.Chrome()
d.set_window_size(1920,1080)
d.get('https://sbis.ru')
d.find_element(By.LINK_TEXT, 'Поддержка').click()
scrollTo_block = d.find_element(By.CLASS_NAME, 'sbis_ru-Support-block2__section-mob')
d.execute_script('return arguments[0].scrollIntoView(true);', scrollTo_block)
d.find_element(By.CSS_SELECTOR, '[href="/download"]').click()

def read_file(filelinks):
    with open(filelinks) as input_file:
        text = input_file.read()
    return text

def parse_download_link(filelinks):
    results = []
    text = read_file(filelinks)

    soup = BeautifulSoup(text)
    link_list = soup.find('div', {'data-for': "ereport25"})
    loadLinks = link_list.find_all('div', {'class': "sbis_ru-DownloadNew-flex__child"})

    for link in loadLinks:
        download_links = link.find('div', {'class': "sbis_ru-DownloadNew-loadLink"}).find('a').get('href')
        results.append({'download_link': download_links})
        with open('links.txt', 'w') as links:
            for key, val in results:
                links.write('{}:{}\n'.format(key, val))
                links.close()
    return
