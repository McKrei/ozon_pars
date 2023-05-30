from bs4 import BeautifulSoup

import sys
from main import Parsing


def get_all_data_page(page_source: str) -> list:
    soup = BeautifulSoup(page_source, "lxml")
    all_data = []
    blocks = soup.find_all('div', {'class': 'i2m mi2'})
    print(len(blocks))
    for block in blocks:
        if not block:
            continue
        url = block.find('a', {'class': 'tile-hover-target j0i ji1'})
        all_data.append((
            block.find('span', {'class': 'd7t t7d d8t ud tsBodyL j0i ji1'}).text,
            url.get('href') if url else None,
        ))
    return all_data


def save_data_to_csv(data) -> list[list]:
    with open("kappa.csv", "a", encoding="utf-8") as file:
        for item in data:
            file.write('|'.join(map(str, item)) + '\n')


columns = [
    "Название",
    "ссылка на товар",
]


def main(start, end):
    save_data_to_csv([columns])
    url = "https://www.ozon.ru/brand/kappa-146870879/category/odezhda-obuv-i-aksessuary-7500/?page="
    parsing = Parsing()
    for i in range(start, end):
        print(i)
        page = parsing.get_page(f'{url}{i}')
        data = get_all_data_page(page)
        save_data_to_csv(data)
    parsing.driver.quit()

if __name__ == '__main__':
    start, end = map(int, sys.argv[1:])
    main(start, end)
