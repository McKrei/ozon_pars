from bs4 import BeautifulSoup

from main import Parsing


def get_all_data_page(page_source: str) -> list:
    soup = BeautifulSoup(page_source, "lxml")
    all_data = []
    blocks = soup.find_all('div', {'class': 'im0 i0m'})
    print(len(blocks))
    for block in blocks:
        if not block:
            continue
        url = block.find('a', {'class': 'tile-hover-target ii8 i9i'})
        all_data.append((
            block.find('span', {'class': 'dt5 td5 dt6 dt8 tsBodyL ii8 i9i'}).text,
            url.get('href') if url else None,
        ))
    return all_data


def save_data_to_csv(data) -> list[list]:
    with open("obuv.csv", "a", encoding="utf-8") as file:
        for item in data:
            file.write('|'.join(map(str, item)) + '\n')


columns = [
    "Название",
    "ссылка на товар",
]


def main():
    save_data_to_csv([columns])
    url = "https://www.ozon.ru/brand/nike-18077713/category/obuv-17777?page="
    parsing = Parsing()
    for i in range(1, 279):
        print(i)
        page = parsing.get_page(f'{url}{i}')
        data = get_all_data_page(page)
        save_data_to_csv(data)
    parsing.driver.quit()

if __name__ == '__main__':
    main()
