import string
import re

white_punc = string.whitespace + string.punctuation + '’' + '”' + '“' + string.digits

remove_table = str.maketrans("", "", white_punc)

word_count_dict = {}

with open("C:/GitHub/python/thinkPython/Chapter_13/MobyDick.txt", encoding='utf-8') as file:

    for line in file:
        word_list = re.split(r'[ ,\-\—]', line)

        for word in word_list:
            new_str = word.translate(remove_table)
            if new_str != '':
                word_count_dict[new_str.lower()] = word_count_dict.get(new_str.lower(), 0) + 1

t = []
for key, value in word_count_dict.items():
    t.append((value, key))
t.sort(reverse=True)

print(len(t))

for num, word in t[0:100]:

    print(f"{word}:{num}")