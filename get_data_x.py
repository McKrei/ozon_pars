import os
import json
import re
from collections import defaultdict
from tqdm import tqdm
from bs4 import BeautifulSoup

def process_file(filename):
    """
    Обрабатывает отдельный файл HTML.

    Args:
        filename (str): Путь к файлу HTML.
    """
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    try:

        product_id = re.findall(r'\d+', filename)[0]
        soup = BeautifulSoup(html, "lxml")
        title = soup.find('h1', {'class': 'x8k'}).text
        kv = soup.find_all('dl', {'class': 'q1j'})
        dct = {}

        for item in kv:
            key = item.find('span', {'class': 'j1q'})
            value = item.find('dd', {'class': 'jq1'})

            if key and value:
                key = key.text.strip().replace('\n', '').replace('\t', '')
                value = value.text.strip().replace('\n', '').replace('\t', '')
                params.append(key)
                dct[key] = value

        if dct:
            result_dict[title].update({product_id: dct})
    except Exception as e:
        print(product_id, e)

def process_files_in_directory(directory):
    """
    Обрабатывает все файлы HTML в заданной директории.

    Args:
        directory (str): Путь к директории с файлами HTML.
    """
    for root, _, files in os.walk(directory):
        total_files = len(files)
        progress_bar = tqdm(total=total_files, desc='Processing files')
        for filename in files:
            file_path = os.path.join(root, filename)
            process_file(file_path)
            progress_bar.update(1)
        progress_bar.close()

if __name__ == "__main__":
    result_dict = defaultdict(dict)
    params = []
    process_files_in_directory("./pages")
    unique_keys = set(params)
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(dict(result_dict), f, ensure_ascii=False, indent=4)
