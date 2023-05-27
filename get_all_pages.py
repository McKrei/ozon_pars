import re
import time

from main import Parsing


def save_page(page_data, name):
    with open(f'pages/{name}.html', 'w', encoding='utf-8') as f:
        f.write(page_data)


def get_url():
    with open('unique.csv', 'r', encoding='utf-8') as f:
        result = [el.split('|')[0] for el in f.read().strip().split('\n')]
    return result


def search_and_save_data(urls):
    parsing = Parsing()
    for url in urls:
        page = parsing.get_page('https://www.ozon.ru' + url)
        name = re.findall(r'\d+', url)[-1]
        save_page(page, name)
    parsing.driver.quit()


def main():
    all_url = get_url()
    # chunks = [all_url[i:i+chunk_size] for i in range(0, len(all_url), chunk_size)]
    search_and_save_data(all_url[:50])

if __name__ == '__main__':
    main()
