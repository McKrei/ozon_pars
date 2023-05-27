import multiprocessing
import re
import time

from main import Parsing


def save_page(page_data, name):
    with open(f'pages/{name}.html', 'w', encoding='utf-8') as f:
        f.write(page_data)


def get_url():
    with open('unique_phones.csv', 'r', encoding='utf-8') as f:
        result = [el.split('|')[0] for el in f.read().strip().split('\n')]
    return result


def search_and_save_data(urls):
    for url in urls:
        parsing = Parsing()
        page = parsing.get_page('https://www.ozon.ru' + url)
        name = re.findall(r'\d+', url)[-1]
        save_page(page, name)
        time.sleep(1)
        parsing.driver.quit()


def main(process=10):
    all_url = get_url()
    chunk_size = len(all_url) // process
    chunks = [all_url[i:i+chunk_size] for i in range(0, len(all_url), chunk_size)]
    pool = multiprocessing.Pool(processes=process)
    pool.map(search_and_save_data, chunks)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
