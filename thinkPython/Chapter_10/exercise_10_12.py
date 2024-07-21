import math


def is_length(word):
    if len(word) >= 6:
        return False
    else:
        return True


def build_list():
    t = []
    with open("F:/Programming/Git_Python/python/thinkPython/Chapter_10/words.txt") as file:
        for line in file:
            t.append(line.strip())
    return t


def word_search(t, value):
    length = len(t)

    if length <= 1:
        return False
    
    length = math.ceil(len(t) / 2)
    word = (t[length - 1])

    if value == word:
        return True
    elif value > word:
        return word_search(t[length:], value)
    else:
        return word_search(t[0:length], value)


def interlock(word1, word2):
    new_word = ''
    for i in range(len(word1)):
        new_word = new_word + word1[i] + word2[i]
    return new_word


def print_interlock(t, word1, word2):
    if len(word1) == len(word2) and is_length(word1):
        interlocked_word = interlock(word1, word2)
        if word_search(t, interlocked_word):
            print(f"{word1} + {word2} = {interlocked_word}")


def find_interlock(t):
    length = len(t) - 1
    for i in range(length - 1):
        j = i + 1
        while j <= length:
            word1, word2 = t[i], t[j]

            print_interlock(t, word1, word2)
            j += 1

lis = build_list()
find_interlock(lis)