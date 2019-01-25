import os, sys
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return 'File Not Found'
    with open(filepath, 'r', encoding='utf8') as f:
        return f.read().strip()


def get_most_frequent_words(list_of_words):
    words = words_counter(list_of_words)
    return sorted(words.keys(), reverse=True, key=words.get)


def words_counter(any_text: str):
    counter = Counter()
    words = any_text.strip().split()
    for word in words:
        counter[word] += 1
    return counter


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print('Укажите путь к файлу')
    text_as_str = load_data(file_path)
    for word in get_most_frequent_words(text_as_str)[:10]:
        print(word)
