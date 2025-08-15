import string
import re

word_count_dict = {}
words_in_book = []

white_punc = string.whitespace + string.punctuation + '’' + '”' + '“' + string.digits
remove_table = str.maketrans("", "", white_punc)

def word_file_list():
    fin = open("C:/GitHub\python/thinkPython/words.txt")
    t = []
    for line in fin:
        t.append(line[:-1])
    return t


def count_words(t):
    for word in t:
        new_str = word.translate(remove_table).lower()
        if new_str != '':
            word_count_dict[new_str] = word_count_dict.get(new_str, 0) + 1


def fill_list():
    with open("C:/GitHub/python/thinkPython/Chapter_13/MobyDick.txt", encoding='utf-8') as file:
        for line in file:
            words = re.split(r'[ ,\-\—]', line)
            count_words(words)

    for key, _ in word_count_dict.items():
        words_in_book.append(key)


def compare_lists(book_list, file_list):
    for word in book_list:
        if word not in file_list:
            print(word)

t = word_file_list()

fill_list()

compare_lists(words_in_book, t)


