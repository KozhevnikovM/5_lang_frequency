import os, sys
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return 'File Not Found'
    with open(filepath, 'r', encoding='utf8') as f:
        return f.read().strip()


def get_most_frequent_words(text):
    words = calc_words(text)
    return sorted(words.keys(), reverse=True, key=words.get)


def calc_words(text):
    counter = Counter()
    words = text.strip().split()
    for word in words:
        counter[word] += 1
    return counter


if __name__ == '__main__':
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print('Укажите путь к файлу')
    text = load_data('text.txt')
    for i in get_most_frequent_words(text)[:10]:
        print(i)
