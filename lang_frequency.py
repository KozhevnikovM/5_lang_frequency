import os, sys
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf8') as file:
        return file.read().strip()


def get_most_frequent_words(any_text):
    words = any_text.split()
    return Counter(words).most_common()[:10]



if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
    except IndexError:
        print('Укажите путь к файлу')

    text_as_str = load_data(file_path)

    if text_as_str is None:
        exit('File not found')

    for word in get_most_frequent_words(text_as_str):
        print(word[0])
