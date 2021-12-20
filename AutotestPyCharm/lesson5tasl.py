from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

d = wd.Chrome()
d.maximize_window()
d.get('https://sbis.ru')
d.find_element(By.LINK_TEXT, 'Поддержка').click()
scrollTo_block = d.find_element(By.CLASS_NAME, 'sbis_ru-Support-block2__section-mob')
d.execute_script('return arguments[0].scrollIntoView(true);', scrollTo_block)
d.find_element(By.CSS_SELECTOR, '[href="/download"]').click()

response = requests.get(d.current_url)
soup = BeautifulSoup(response.content, 'html.parser')

results = []
link_list = soup.find('div', {'data-for': "ereport25"})
load_blocks = link_list.find_all('div', {'class': 'sbis_ru-DownloadNew-loadLink'})
for link in load_blocks:
    download_links = link.find('a').get('href')
    download_links_name = link.find('a').text
    results.append(f'{download_links_name}: {download_links}')

file = open('links.txt', 'w', encoding="windows-1251")
file.writelines('\n'.join(results))
file.close()
