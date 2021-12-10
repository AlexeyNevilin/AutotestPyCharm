from selenium import webdriver

d = webdriver.Chrome()
d.set_window_size(1920,1080)
d.get('https://sbis.ru')
d.find_element_by_link_text('Поддержка').click()
d.find_element_by_css_selector('href="/download"').scrollintoview()
