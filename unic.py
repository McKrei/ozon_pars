

def main():
    with open('kappa.csv', 'r', encoding='utf-8') as f:
        all_phone = [el.split('|')[::-1] for el in f.read().strip().split('\n') if len(el.split('|')) == 2 and '?' in el]
        dict_phone = {
            url[:url.index('?')]: name
            for url, name in all_phone
        }
    print(len(all_phone))
    print(len(dict_phone))
    with open('unique.csv', 'w', encoding='utf-8') as f:
        for item in dict_phone.items():
            f.write('|'.join(map(str, item)) + '\n')


if __name__ == '__main__':
    main()
