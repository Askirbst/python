import math

def build_list_append():
    t = []
    with open("C:/GitHub/python/thinkPython/Chapter_10/words.txt") as file:
        for line in file:
            t.append(line.strip())
    return t


def in_bisect(t, value):
    is_word = False
    length = len(t)
    if length < 1:
        return False
    
    length = math.ceil(len(t) / 2)
    word = (t[length - 1])
    if value == word:
        return True
    elif value > word:
        is_word = in_bisect(t[length:], value)
    else:
        is_word = in_bisect(t[0:length], value)

    return is_word


target_word = input("Enter a target word:\n")

word_list = build_list_append()

print(in_bisect(word_list, target_word))