import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver.v2 as uc


class Parsing:
    '''Класс для сохранения состояния драйвера и получения html страницы'''
    def __init__(self):
        options = Options()
        options.add_argument('--user-data-dir=/tmp/profile2')  # Изменяем путь к профилю на Linux-совместимый
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

        self.driver = uc.Chrome(options=options)

    def get_page(self, url):
        '''Получаем html страницы'''
        self.driver.get(url)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        page_source = self.driver.page_source
        return page_source
