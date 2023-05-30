import time
import undetected_chromedriver.v2 as uc


class Parsing:
    '''Класс для сохранения состояния драйвера и получения html страницы'''
    def __init__(self):
        options = uc.ChromeOptions()
        # options.add_argument('--user-data-dir=c:\\temp\\profile2')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

        self.driver = uc.Chrome(options=options)

    def get_page(self, url):
        '''Получаем html страницы'''
        self.driver.get(url)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(4)
        page_source = self.driver.page_source
        return page_source
